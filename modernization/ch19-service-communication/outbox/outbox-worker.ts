// Ch19 Outbox worker - polls DB → pushes to broker
import { Client } from "pg";
import { v4 as uuid } from "uuid";

const POLL_INTERVAL_MS = 1000;

async function run() {
  const db = new Client({ connectionString: process.env.DATABASE_URL });
  await db.connect();

  while (true) {
    const { rows } = await db.query(
      `SELECT id, event_type, payload
       FROM outbox_events
       WHERE processed_at IS NULL
       ORDER BY occurred_at
       LIMIT 100`
    );

    for (const row of rows) {
      // TODO: publish to Kafka/Redis/etc.
      console.log("Publishing event", row.event_type, row.id);

      await db.query(
        `UPDATE outbox_events
         SET processed_at = now()
         WHERE id = $1`,
        [row.id]
      );
    }

    await new Promise((r) => setTimeout(r, POLL_INTERVAL_MS));
  }
}

run().catch((err) => {
  console.error("Outbox worker failed", err);
  process.exit(1);
});
