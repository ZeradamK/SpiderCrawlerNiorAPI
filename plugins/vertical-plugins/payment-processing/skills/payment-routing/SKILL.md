---
name: payment-routing
description: |
  Intelligent payment routing and processor selection for optimal approval rates and cost.
  Perfect for: multi-processor environments, cost optimization, failover routing.
  Not ideal for: single-processor setups, non-card payment methods.
---

# Payment Routing

## Core Philosophy
**"Route every transaction to maximize approval probability while minimizing cost — but never sacrifice security for either."**

## Routing Decision Matrix

### Primary Factors (weighted)

| Factor | Weight | Description |
|--------|--------|-------------|
| Approval Rate | 35% | Historical approval rate for this BIN range + processor combo |
| Cost | 25% | Total cost (interchange + assessment + markup) |
| Latency | 15% | Current p95 response time of the processor |
| Availability | 15% | Processor uptime and error rate in last 15 minutes |
| Network Rules | 10% | Mandated routing (Durbin amendment, regional requirements) |

### Routing Algorithm

```
1. INPUT: transaction (amount, currency, card_bin, mcc, merchant_id)
2. FILTER: Remove processors that cannot handle this:
   - Currency not supported
   - Card network not supported
   - Merchant not provisioned on processor
   - Processor in degraded/down state
3. SCORE each remaining processor:
   score = (approval_rate × 0.35) + (cost_inverse × 0.25) +
           (latency_inverse × 0.15) + (availability × 0.15) +
           (network_compliance × 0.10)
4. SELECT: Highest scoring processor
5. FALLBACK: If primary fails, try next-highest scorer
```

### BIN-Level Routing Intelligence

Maintain a rolling 30-day lookup table:
- Key: `{bin_range}:{processor}:{mcc}`
- Value: `{approval_rate, avg_latency, decline_reasons}`
- Update: Every authorization response feeds back into the table
- Minimum sample size: 50 transactions before using BIN-level data

### Cost Optimization

#### Interchange Categories
- **Qualified**: Standard consumer card, swiped/dipped → lowest rate
- **Mid-Qualified**: Keyed-in, rewards card → higher rate
- **Non-Qualified**: Corporate card, missing data → highest rate

#### Cost Reduction Strategies
1. **Send Level 2/3 data** for B2B transactions (reduces interchange by 0.5-1.0%)
2. **Use network tokens** instead of PANs (Visa: 0.10% discount)
3. **Batch settlement timing**: Same-day settlement for lower interchange
4. **Durbin routing**: Route debit cards via lowest-cost network (PIN debit vs signature)

### Failover Strategy

```
Primary processor fails/times out
  ├── Retry same processor (1x, after 2s delay)
  │     └── Still fails
  │           ├── Route to secondary processor
  │           │     └── Submit with same transaction data
  │           │           ├── Approved → record processor affinity
  │           │           └── Declined → check if retriable
  │           └── If no secondary available
  │                 └── Return decline with reason
  └── If timeout
        ├── Send reversal to primary
        └── Route to secondary
```

### Geographic Routing

| Card Issuer Region | Preferred Processor | Reason |
|--------------------|--------------------|--------|
| US Domestic | Local acquirer | Lowest interchange, fastest settlement |
| EU/EEA | EU-based acquirer | SCA compliance, SEPA settlement |
| UK | UK acquirer | Post-Brexit specific rules |
| APAC | Regional acquirer | Local scheme support (JCB, UnionPay) |
| LATAM | Local acquirer | Currency controls, local scheme support |

### Real-Time Health Monitoring

Track per processor every 60 seconds:
- Error rate (5xx responses)
- Timeout rate
- P50/P95/P99 latency
- Approval rate deviation from baseline

**Circuit breaker**: If error rate > 10% or timeout rate > 5% over 5 minutes:
1. Mark processor as `degraded`
2. Reduce traffic to 10% (canary)
3. If canary traffic recovers, gradually restore
4. If canary fails, mark `down` and route 100% to failover

## Reporting

### Daily Routing Report
- Transaction count and volume per processor
- Approval rate per processor per card network
- Average cost per transaction per processor
- Failover events and success rates
- Cost savings from intelligent routing vs round-robin baseline
