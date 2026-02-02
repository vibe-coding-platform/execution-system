#!/bin/bash
# deploy.sh - Production deploy
docker-compose up -d neo4j pinecone-proxy
sleep 30
python ch32/extract_kg.py  # Populate KG
docker-compose up -d supervisor
kubectl port-forward svc/supervisor 8000:80 &
echo "✅ Ch33: 5 agents + supervisor LIVE on :8000"
echo "Test: curl -X POST http://localhost:8000/orchestrate -d '{\"message\":\"#infra auth-v2\"}'"
