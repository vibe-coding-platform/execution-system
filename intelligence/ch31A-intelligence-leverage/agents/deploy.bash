# 1. Build + push agent image
docker build -t vibecoding/ch31a-agents:latest .
docker push vibecoding/ch31a-agents:latest

# 2. Deploy 4 P1 agents (12 replicas total)
kubectl apply -f ch31a-decision-extraction/agents/

# 3. Test real agent
curl -X POST "http://agent-orchestration:8000/orchestrate" \
  -H "Content-Type: application/json" \
  -d '{"decision_id":"D001","trigger":"#infra auth-v2","context":{}}'

# 4. Monitor savings
kubectl port-forward svc/agent-orchestration 8000:80
watch kubectl get hpa  # Auto-scale based on 124/wk load

# Real Output

# $ curl ... #infra auth-v2
{
  "status": "automated",
  "action": "helm install auth-v2 ./charts/auth --namespace staging",
  "k8s_url": "k8s://auth-v2.staging",
  "savings": "$180k/yr",
  "confidence": 0.94,
  "rag_sources": ["Ch21-helm.md", "Ch28-battlefield.xlsx"]
}
#
