# 💀 Ch25 Killing Dumb Apps LIVE

**Kill list + checklist + $2M/year savings calculator.**

## 📊 Kill Candidates (Copy to Excel)
| File | Purpose |
|------|---------|
| [kill-candidates.xlsx](kill-candidates.xlsx) | **Score + prioritize 50 apps** |
| [migration-mapping.json](migration-mapping.json) | **API redirects post-kill** |

## 🎯 Kill Criteria (3+ = Kill)
🚨 IMMEDIATE: <100 users + >5yr old + no owner → KILL NOW
🟡 CONSIDER: <1k users + duplicate + no tests → Q3

text

## 💰 Expected Savings (10 apps)
Monthly: $82k → Annual: $984k
Team freed: 25 FTE → $1.5M velocity gain
Total: $2.5M/year

text

## 🚀 Execute Kill
```bash
# 1. Update nginx/api-gateway redirects
cat migration-mapping.json | jq -r '.killRedirects | to_entries[] | "\(.key) → \(.value)"'

# 2. Archive repo
git clone old-app && git remote set-url origin git@github.com:vibe-coding-platform/archive/old-app

# 3. Celebrate in Ch23 platform dashboard
90% CTOs fear killing → stay L1 technical debt hell.