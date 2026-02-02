# Ch31 Agent Flywheel Templates (P1 Priority)

**304 decisions/wk → 4 agents → 90% automation → $990k/yr**

## 🤖 AGENT 1: INFRA PROVISIONING (50/wk)
Trigger: "#infra" in Slack
RAG Context: Ch14 portal + Ch21 Helm
Action: "helm install $service ./golden-paths/"
Success: 90s deploy → $180k/yr



## 🚨 AGENT 2: INCIDENT TRIAGE (20/wk)  
Trigger: PagerDuty alert
RAG Context: Ch20 observability + Ch19 events
Action: "Scale Payment API → 10 pods"
Success: 2min MTTR → $240k/yr



## 🔍 AGENT 3: ONCALL SCHEDULING (4/wk)
Trigger: "Monday rotation"
RAG Context: Ch29 SRE roster + Ch22 pipelines
Action: "Update PagerDuty → @sre-team1"
Success: Zero touch → $90k/yr



## ⚡ AGENT 4: CODE REVIEW LITE (50/wk subset)
Trigger: "hotfix PR < 100 LOC"
RAG Context: Ch24 pre-commit + Ch27 green zone
Action: "/approve → GitHub API"
Success: 30s PRs → $90k/yr Phase 1



**Flywheel: Agents improve RAG → Better agents → More automation**