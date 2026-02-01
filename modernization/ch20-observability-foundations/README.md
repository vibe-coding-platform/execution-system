# 🚀 Ch20 Observability Foundations LIVE

**OpenTelemetry templates + SLO dashboards + Platform configs. Zero logs-only apps.**

## 📦 Copy-Paste Templates

| File | Purpose |
|------|---------|
| [otel-collector-config.yaml](otel-collector-config.yaml) | **Production collector** |
| [slo-dashboard.json](slo-dashboard.json) | **Grafana SLOs** (import 3000) |
| [docker-compose.observability.yml](docker-compose.observability.yml) | **1-command stack** |
| [service-instrumentation/node.js](service-instrumentation/node.js) | **Node.js auto-instrumentation** |

## 🎯 5-Minute Setup
```bash
docker-compose -f docker-compose.observability.yml up -d
# Grafana: http://localhost:3000
# Import slo-dashboard.json




