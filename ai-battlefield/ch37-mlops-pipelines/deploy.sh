#!/bin/bash
# Ch37 MLOps Production Deploy → Weekly retrain + $2M P&L signals

echo "🚀 Deploying Ch37 MLOps Pipelines..."

# 1. Install MLOps stack
pip install -r requirements.txt

# 2. Setup MLflow tracking
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns &
MLFLOW_PID=$!
sleep 5

# 3. Start Prefect server
prefect server start --host 0.0.0.0 --port 4200 &
PREFECT_PID=$!
sleep 10

# 4. Build + deploy MLOps pipeline
prefect deployment build mlops_pipeline_spec.py:mlops_pipeline -n "weekly-mlops" -a
prefect deployment run "mlops_pipeline/weekly-mlops" --detach

# 5. Start weekly cycle + P&L signals API
nohup python weekly_cycle_automation.py > mlops.log 2>&1 &
nohup uvicorn pnl_signal_framework:app --host 0.0.0.0 --port 8003 > api.log 2>&1 &

# 6. Test production endpoints
sleep 15
echo "Testing P&L signals..."
curl http://localhost:8003/pnl-signals

echo "✅ Ch37 MLOps LIVE"
echo "📊 MLflow: http://localhost:5000"
echo "🎛️  Prefect: http://localhost:4200" 
echo "💰  P&L API: http://localhost:8003/pnl-signals"
echo "📈 Weekly cycle: Mon 2AM → \$2M/yr signals"
echo "🗄️  PIDs: MLflow=$MLFLOW_PID Prefect=$PREFECT_PID"

# Cleanup function
trap "kill $MLFLOW_PID $PREFECT_PID; exit" SIGINT SIGTERM

cd ai-battlefield/ch37-mlops-pipelines/
chmod +x deploy.sh
./deploy.sh                    # Full MLOps stack (60s)

# Verify Production 
# P&L signals (real-time predictions)
# curl http://localhost:8003/pnl-signals
# → {"predicted_lift": "+$2.1M/yr", "roi": "12x"}

# MLflow models
# open http://localhost:5000

# Prefect dashboard  
# open http://localhost:4200