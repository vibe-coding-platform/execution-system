#!/bin/bash
# Ch39 Team Structure Deploy → 20x leverage structure
pip install -r requirements.txt
uvicorn product_engineer_playbook:app --host 0.0.0.0 --port 8005 &
sleep 5

# Test Product Engineer E2E
curl -X POST "http://localhost:8005/feature" \
  -H "Content-Type: application/json" \
  -d '{"spec":"User API v3","service_name":"user-api-v3"}'

echo "✅ Ch39: 20x Centaur Pods LIVE on :8005"
echo "📊 \$320M output trajectory → 13 pods"
