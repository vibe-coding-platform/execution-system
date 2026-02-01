# Ch18 Boundary Map

**Monolith → Microservices extraction order:**

Monolith (2M LOC)
├── ✅ User Service (12%) → Q2 Strangler
├── ✅ Payment Service (8%) → Q3 Replatform
├── Order Service (22%) → Q4
├── Inventory (18%) → Retire
└── Reporting (15%) → Q1 2027

**Extraction Priority:** Low coupling → High business value


