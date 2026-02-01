# Ch17 Path Calculator
apps = [
    {"name": "Legacy CRM", "score": 92, "path": "Strangler Q2"},
    {"name": "Payment API", "score": 87, "path": "Replatform Q3"}
]

print("QUICK WINS (Score >80):")
for app in apps:
    if app["score"] > 80:
        print(f"✅ {app['name']} → {app['path']}")
