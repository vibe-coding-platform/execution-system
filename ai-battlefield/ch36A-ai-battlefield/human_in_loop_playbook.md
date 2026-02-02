# Ch36A Human-in-Loop Playbook (95% Auto + 5% Human → Production)

**95% automated → 5% human review → 20x leverage maintained**

## 🎯 HITL ESCALATION MATRIX
Confidence <80%: IMMEDIATE human review
Confidence 80-95%: Async human approval (Slack)
Confidence >95%: Fully autonomous

Escalation: Workflow → Slack #ai-review → Architect → Done

text

## 🛡️ SAFETY GATES (Production)
Ch24 Pre-commit: 100% pass required

Ch20 SLOs: 7-day history green

Ch28 Battlefield: Green/Yellow zone apps only

Ch29 Architects: Own final approval <5%

Ch34 Intelligence: All logged → P&L tracking

text

## 📋 HITL WORKFLOW (5min cycle)
Agent executes → confidence_score

<80% → Slack #ai-review → Architect 2min SLA

80-95% → Async 👍👎 → Ch34 feedback loop

95% → Ch22 GitOps → Production deploy

text

## 📈 HITL METRICS TARGETS
Human review rate: 5% max
Architect touch: <30min/wk
Escalation SLA: 2min p95
Feedback loop: 95%→97% weekly