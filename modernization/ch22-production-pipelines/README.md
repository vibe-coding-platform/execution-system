# 🚀 Ch22 Production Pipelines LIVE

**GitOps templates + Self-service UI + Pipeline compliance dashboard.**

## 📦 GitOps Templates

| File | Purpose |
|------|---------|
| [argo-cd-app-of-apps.yaml](gitops/argo-cd-app-of-apps.yaml) | **Argo CD master sync** |
| [.github/workflows/gitops-pipeline.yml](.github/workflows/gitops-pipeline.yml) | **90s Staging→Prod** |
| [compliance-dashboard/grafana-pipeline.json](compliance-dashboard/grafana-pipeline.json) | **DORA metrics LIVE** |
| [self-service-ui/argocd-app-create.yaml](self-service-ui/argocd-app-create.yaml) | **1-click service deploy** |

## 🎯 Pipeline Flow (90 seconds)
PR → pre-commit → test → build → staging → compliance ✅ → prod
GitHub Actions → Argo CD → Cluster


## 📊 DORA Metrics Tracked
- **Deploy Frequency**: >2/day  
- **Lead Time**: <15min  
- **Success Rate**: >95%  
- **MTTR**: <1hr

## 🚀 Self-Service Deploy
```bash
# Developers fork platform-starter → PR → AUTO staging → approve → prod
git push origin main  # Pipeline triggered automatically

