# agents/p1-infra.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: infra-agent-d001
spec:
  replicas: 3  # 50/wk load
  template:
    spec:
      containers:
      - name: agent
        image: vibecoding/ch31a-agents:latest
        env:
        - name: DECISION_ID
          value: "D001"
        resources:
          requests:
            cpu: "100m"
            memory: "256Mi"
---
# Repeat for D002, D003, D004 (12 total replicas)
