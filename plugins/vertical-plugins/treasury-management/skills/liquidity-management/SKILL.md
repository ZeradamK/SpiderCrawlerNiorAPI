---
name: liquidity-management
description: |
  Cash flow forecasting, liquidity optimization, and working capital management.
  Perfect for: cash forecasting, sweep automation, buffer management, bank relationship.
  Not ideal for: transaction-level processing (use transaction-lifecycle).
---

# Liquidity Management

## Core Philosophy
**"Cash is oxygen — forecast it, optimize it, and never run out."**

## Cash Flow Forecasting

### Inflow Sources
| Source | Predictability | Timing |
|--------|---------------|--------|
| Card settlements | High | T+1 or T+2 |
| ACH receipts | Medium | T+1 to T+3 |
| Wire receipts | Low | Same day |
| Reserve releases | High | Scheduled |
| Interest income | High | Monthly |

### Outflow Sources
| Source | Predictability | Timing |
|--------|---------------|--------|
| Merchant payouts | High | T+1 or T+2 |
| Refund credits | Medium | Immediate to T+3 |
| Chargeback debits | Low | Event-driven |
| Operating expenses | High | Monthly |
| Network fees | High | Monthly |
| Reserve contributions | High | Daily |

### Forecasting Model
```
Projected_Balance(T+n) = Current_Balance
  + Σ Expected_Inflows(T+1 to T+n)
  - Σ Expected_Outflows(T+1 to T+n)
  ± Adjustment_Factor(seasonality, day_of_week, holidays)
```

## Sweep Automation
- **End-of-day sweep**: Move excess cash to interest-bearing account
- **Target balance sweep**: Maintain minimum in operating account
- **Threshold sweep**: Sweep when balance exceeds threshold
- **Cross-currency sweep**: Convert excess foreign currency to base currency

## Buffer Management
- Minimum operating buffer: 2x average daily settlement volume
- Reserve buffer: As required by processor/network agreements
- Contingency buffer: 1 week of operating expenses
- FX buffer: Sufficient to cover 3-day FX settlement mismatch

## Bank Relationship Management
- Maintain relationships with 2+ banks for redundancy
- Diversify deposits across banks (no more than 50% at one bank)
- Monitor bank health and credit ratings
- Negotiate fee structures based on volume
