---
name: webhook-management
description: |
  Payment event webhook delivery, retry logic, and signature verification.
  Perfect for: event-driven payment notifications, processor webhook handling, event replay.
  Not ideal for: synchronous API responses, polling-based integrations.
---

# Webhook Management

## Core Philosophy
**"Webhooks are the nervous system of payment processing — every event must be delivered, verified, and acknowledged."**

## Event Types

| Category | Events |
|----------|--------|
| Transaction | `transaction.authorized`, `transaction.captured`, `transaction.settled`, `transaction.declined`, `transaction.voided` |
| Refund | `refund.created`, `refund.completed`, `refund.failed` |
| Dispute | `dispute.opened`, `dispute.evidence_due`, `dispute.won`, `dispute.lost` |
| Settlement | `settlement.batch_created`, `settlement.completed`, `settlement.failed` |
| Merchant | `merchant.activated`, `merchant.suspended`, `merchant.limit_reached` |
| Payout | `payout.initiated`, `payout.completed`, `payout.failed`, `payout.returned` |

## Delivery

### Signature Verification
Every webhook payload is signed:
```
Eris-Signature: t=1234567890,v1=sha256_hmac_hex
```

Verification:
1. Extract timestamp `t` and signature `v1` from header
2. Construct signed payload: `{timestamp}.{raw_body}`
3. Compute HMAC-SHA256 with webhook secret
4. Compare computed signature to `v1`
5. Reject if timestamp is older than 5 minutes (replay protection)

### Retry Policy
```
Attempt 1: Immediate
Attempt 2: 5 minutes
Attempt 3: 30 minutes
Attempt 4: 2 hours
Attempt 5: 8 hours
Attempt 6: 24 hours
Attempt 7: 48 hours (final)
```

- Expect HTTP 2xx within 30 seconds
- Any non-2xx or timeout → schedule retry
- After all retries exhausted → mark as `failed`, alert merchant
- Merchant can replay failed webhooks via API

### Idempotency
- Every event has a unique `event_id`
- Merchants should deduplicate by `event_id`
- Events may be delivered more than once (at-least-once delivery)
- Include `delivery_attempt` count in headers

## Monitoring
- Delivery success rate per merchant endpoint
- Average delivery latency
- Retry rate (high retry rate = unhealthy endpoint)
- Failed delivery alerts
