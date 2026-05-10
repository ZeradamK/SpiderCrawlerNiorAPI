---
name: recurring-billing
description: |
  Subscription and recurring payment management — billing cycles, dunning, plan changes.
  Perfect for: SaaS billing, subscription management, installment payments, dunning workflows.
  Not ideal for: one-time payments, marketplace payouts.
---

# Recurring Billing

## Core Philosophy
**"A successful subscription business is built on invisible payments — the best billing is billing the customer never has to think about."**

## Subscription Lifecycle

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│  TRIAL   │───▶│  ACTIVE  │───▶│ CANCELED │
└──────────┘    └──────────┘    └──────────┘
                     │ ▲
                     ▼ │
                ┌──────────┐
                │PAST_DUE  │───▶ CANCELED (after dunning exhausted)
                └──────────┘
                     │
                     ▼
                ┌──────────┐
                │  PAUSED  │
                └──────────┘
```

## Billing Engine

### Cycle Management
1. **Fixed-date billing**: Bill on the same day each month (e.g., 1st)
2. **Anniversary billing**: Bill N days/months after subscription start
3. **Proration**: Calculate partial amounts for mid-cycle changes
4. **Grace period**: Configurable window after failed payment before status change

### Invoice Generation
For each billing cycle:
1. Calculate base subscription amount
2. Apply usage-based charges (metered billing)
3. Apply discounts and coupons
4. Calculate tax (integrate with tax engine)
5. Generate invoice with line items
6. Attempt payment against stored credential

### Dunning (Failed Payment Recovery)
```
Day 0:  Initial charge attempt
Day 1:  Retry #1 + email notification
Day 3:  Retry #2 + email notification
Day 5:  Retry #3 + email notification (card update prompt)
Day 7:  Retry #4 + SMS notification
Day 10: Retry #5 + final warning email
Day 14: Cancel subscription + final notification
```

**Smart retry timing:**
- Retry at different times of day (paycheck deposit patterns)
- Retry on different days (avoid weekends for some demographics)
- Update card details via network account updater before retry

### Plan Changes
- **Upgrade**: Prorate remaining current plan, charge difference immediately
- **Downgrade**: Apply at end of current billing cycle
- **Add-on**: Prorate and charge immediately
- **Quantity change**: Prorate based on new quantity

## Network Indicators for Recurring

When processing recurring transactions:
1. First transaction: `stored_credential = initial`, cardholder-initiated
2. Subsequent: `stored_credential = subsequent`, merchant-initiated
3. Include `network_transaction_id` from initial authorization
4. Set `recurring_indicator = recurring` (fixed) or `installment` (finite series)

## Metrics
- Monthly Recurring Revenue (MRR)
- Churn rate (voluntary + involuntary)
- Dunning recovery rate (target: >60%)
- Failed payment rate (target: <5%)
- Average revenue per user (ARPU)
