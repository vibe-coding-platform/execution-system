# Ch27 P&L Tracker - Modernization ROI
portfolio = [
    {"name": "Auth Service", "before": 8000, "after": 6000, "timeline": "Q1"},
    {"name": "User Portal", "before": 18000, "after": 8000, "timeline": "Q2"},
    {"name": "Batch Jobs", "before": 6800, "after": 0, "timeline": "Q1"},
]

total_before = sum(app["before"] for app in portfolio)
total_after = sum(app["after"] for app in portfolio)
annual_savings = (total_before - total_after) * 12

print(f"📊 Modernization P&L")
print(f"Monthly Before: ${total_before:,}")
print(f"Monthly After:  ${total_after:,}")
print(f"Annual Savings: ${annual_savings:,.0f}")
print("\nBy Quarter:")
for app in portfolio:
    savings = (app["before"] - app["after"]) * 12
    print(f"  {app['timeline']}: {app['name']} → ${savings:,.0f}/yr")
