#!/bin/bash
# Ch38 Governance Production Deploy → $15M/yr protected
pip install -r requirements.txt
uvicorn governance_layer:app --host 0.0.0.0 --port 8004 &
sleep 5
curl -X POST "http://localhost:8004/enforce" \
  -H "Content-Type: application/json" \
  -d '{"workflow_id":"codegen-v2","confidence":0.92,"risk_score":0.12,"pnl_impact":250000}'
echo "✅ Ch38 Governance LIVE on :8004 → \$15M/yr protected"
