# Ch25 Kill Criteria Checklist

**Kill if ANY 3+ criteria match. Save $2M/year per 10 apps.**

## 🚨 IMMEDIATE KILL (4+ criteria)
| App | Criteria | Status |
|-----|----------|--------|
| [ ] | <100 users/month | Usage |
| [ ] | No API/analytics | Integration |
| [ ] | >5 years no changes | Maintenance |
| [ ] | <$10k business value | Revenue |
| [ ] | Manual deploy | Toil |
| [ ] | >3 part-time owners | Team |

## 🟡 CONSIDER KILL (3 criteria)
| App | Criteria | Status |
|-----|----------|--------|
| [ ] | <1k users/month | Usage |
| [ ] | No tests | Reliability |
| [ ] | Duplicate function | Redundancy |
| [ ] | EOL dependencies | Security |

## EXECUTE KILL
Notify owners → 30 days deprecation

Redirect traffic → API gateway

Archive code → cold storage

Celebrate $200k/year savings/app