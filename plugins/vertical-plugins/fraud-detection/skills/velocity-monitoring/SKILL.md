---
name: velocity-monitoring
description: |
  Real-time velocity checks and rate limiting for payment fraud prevention.
  Perfect for: card testing detection, BIN attacks, account takeover, rapid-fire fraud.
  Not ideal for: sophisticated fraud patterns (use fraud-scoring), AML (use aml-screening).
---

# Velocity Monitoring

## Core Philosophy
**"Speed kills — in fraud, velocity is the strongest single signal."**

## Velocity Dimensions

### Per-Card Velocity
| Check | Window | Threshold | Action |
|-------|--------|-----------|--------|
| Transaction count | 1 hour | 5 | Flag for review |
| Transaction count | 24 hours | 20 | Flag for review |
| Transaction amount | 24 hours | $5,000 | Flag for review |
| Decline count | 1 hour | 3 | Soft block |
| Distinct merchants | 1 hour | 3 | Flag for review |
| Distinct countries | 24 hours | 2 | Flag for review |

### Per-IP Velocity
| Check | Window | Threshold | Action |
|-------|--------|-----------|--------|
| Transaction count | 5 minutes | 10 | Hard block |
| Distinct cards | 1 hour | 5 | Hard block (BIN attack) |
| Decline rate | 1 hour | >50% | Hard block |
| Account creations | 1 hour | 3 | Flag for review |

### Per-Device Velocity
| Check | Window | Threshold | Action |
|-------|--------|-----------|--------|
| Transaction count | 1 hour | 10 | Flag for review |
| Distinct cards | 24 hours | 3 | Hard block |
| Distinct accounts | 24 hours | 2 | Flag for review |

### Per-Merchant Velocity
| Check | Window | Threshold | Action |
|-------|--------|-----------|--------|
| Decline rate | 1 hour | >30% | Alert merchant |
| Chargeback count | 24 hours | 10 | Alert + review |
| Refund rate | 24 hours | >20% | Alert merchant |

## Implementation

### Sliding Window Counter
Use Redis sorted sets for real-time counting:
```
Key: velocity:{dimension}:{entity_id}:{check_name}
Members: transaction_id (score = timestamp)

On each transaction:
1. ZADD key timestamp txn_id
2. ZREMRANGEBYSCORE key 0 (now - window)
3. ZCARD key → current count
4. Compare against threshold
```

### Burst Detection
Beyond simple thresholds, detect acceleration:
- Calculate rate-of-change in velocity
- If velocity doubles within 10 minutes → elevated alert
- If 3+ cards from same BIN range in 5 minutes → BIN attack alert

## Monitoring
- Velocity check latency: Target <5ms p99
- Block rate by velocity rule: Track for tuning
- False positive rate: Review blocked legitimate transactions
- BIN attack detection rate: Target >95% within 2 minutes
