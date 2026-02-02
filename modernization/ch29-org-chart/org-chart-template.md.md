# Ch29 Vibe Coding Organizational Structure


                      CTO (1)
                         |
            ┌────────────┼────────────┐
    Platform VP (1)   Engineering VP (40)  Product (15)
       |                    |              |
 ┌─────┴─────┐        ┌─────┴────────┐     │
Architects(2) Pipelines(3) Domain Teams(30) │
Self-Service(3) Run(2) │ │
│ │ │ │
Portal Eng(2) SRE(2) │ │
Product Owners(5)



**80 engineers → 12 platform (15%) → 40 domain → 28 app teams freed**

## 🏗️ PLATFORM TEAM SPEC (12 FTE)
| Role | Count | Reports To | Mission |
|------|-------|------------|---------|
| Platform VP | 1 | CTO | L3 golden paths Q2 |
| Platform PM | 1 | VP | Developer NPS >8 |
| Architects | 2 | VP | Golden templates |
| Pipeline Eng | 3 | Architect | 90s staging→prod |
| Portal Eng | 3 | Architect | Self-service UI |
| SRE | 2 | VP | 99.9% uptime |

## 🌐 DOMAIN ARCHITECT PLAYBOOK
Own 10 apps → Ch17 migration matrix

Kill 3 apps → Ch25 checklist

Extract 3 services → Ch18 strangler

Modernize 4 apps → Ch27 green zone
→ Q4 2026: 10 apps → L3 compliance
