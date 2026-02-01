# Ch19 Service Communication 🚦

**Gateway configs + event schemas + outbox pattern. Sync without tight coupling.**

## 1. API Gateway (Edge)

- `gateway/api-gateway.nginx.conf`  
  - Single entry point `/api/*`  
  - Routes to `user-service`, `order-service`  
  - Adds `X-Request-Id` for tracing

## 2. Event Schemas (Async Backbone)

- `events/user-registered.json`  
- `events/order-created.json`  

Use these as **canonical contracts** between services.

## 3. Outbox Pattern (Reliability)

- `outbox/outbox-table.sql` → per-service outbox table  
- `outbox/example-insert.sql` → write events in same TX as business change  
- `outbox/outbox-worker.ts` → polls DB → publishes to broker

**Flow:**
1. Request hits API Gateway → service  
2. Service writes to DB + outbox (same transaction)  
3. Outbox worker publishes events → other services consume

This is the **minimum set** to avoid “RPC hell” and lost messages.



