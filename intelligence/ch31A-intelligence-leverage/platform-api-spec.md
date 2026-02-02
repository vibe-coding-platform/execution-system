# Ch31A Platform API Specification (Agent Ready)

**REST + GraphQL → 4 P1 agents autonomous. Ch14-30 platform = agent backend.**

## 🔌 API ENDPOINTS (P1 Agents)

### **Infra Agent (D001)**
POST /api/v1/infra/provision
{
"service": "auth-v2",
"template": "ch21-helm-k8s",
"env": "staging"
}
→ Returns: K8s URL + credentials (90s)

text

### **SRE Agent (D002)**
POST /api/v1/incident/triage
{
"alert": "payment-api-5xx",
"pod_count": 3,
"slo_target": "99.9%"
}
→ Returns: Auto-scale executed


### **Code Agent (D003)**
POST /api/v1/review/hotfix
{
"pr_url": "gh/pr/123",
"lines_changed": 45,
"lint_pass": true
}
→ Returns: /approve + merge


### **Roster Agent (D004)**
POST /api/v1/oncall/schedule
{
"week": "2026-W6",
"team": "sre-team1",
"rotation": "primary"
}
→ Returns: PagerDuty updated


## 🏗️ PLATFORM PREREQS (Ch17-30)
✅ Ch14 Self-service → API facade
✅ Ch21 K8s → Golden templates
✅ Ch20 Observability → Alert context
✅ Ch22 Pipelines → Agent auth
