---
name: batch-processing
description: |
  Settlement batch assembly, netting, and payout execution.
  Perfect for: daily settlement processing, batch management, payout scheduling.
  Not ideal for: real-time authorization (use transaction-lifecycle).
---

# Batch Processing

## Core Philosophy
**"Settlement is where promises become money — every cent must be accounted for."**

## Settlement Architecture

```
Captured Transactions
       │
       ▼
┌─────────────────┐
│ Batch Assembly   │  Cutoff time → group by merchant + currency
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Netting       │  Captures - Refunds - Chargebacks - Fees
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Fee Calculation │  Interchange + Assessment + Markup
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Payout Execution │  ACH/Wire to merchant bank
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Confirmation   │  Settlement report + webhook
└─────────────────┘
```

## Batch Assembly Rules

### Cutoff Times
- **Daily settlement**: 11:59 PM merchant local time
- **Real-time settlement**: Continuous (Visa Real-Time Payments)
- **Weekly settlement**: Friday 5:00 PM merchant local time

### Exclusions
Do NOT include in settlement batch:
- Transactions with status `disputed` (pending chargeback resolution)
- Transactions under fraud investigation hold
- Transactions from suspended merchants
- Transactions where capture amount was subsequently voided

### Netting Rules
```
Net Amount = Σ(captures) - Σ(refunds) - Σ(chargebacks) - Σ(fees)

If Net Amount > 0: Pay merchant
If Net Amount < 0: Debit merchant reserve or carry forward
If Net Amount = 0: No payout, generate zero-balance report
```

## Fee Structure

### Interchange (Network-Mandated)
- Set by Visa/MC/Amex, varies by card type, MCC, entry mode
- Published semi-annually (April and October for Visa/MC)
- Not negotiable — applies to all acquirers equally

### Assessment (Network Fees)
- Visa: 0.14% (credit), 0.13% (debit)
- Mastercard: 0.13% (credit and debit)
- Amex: Set by merchant agreement

### Processor Markup (Negotiable)
- Interchange-plus: interchange + fixed % + per-transaction fee
- Flat rate: Single blended rate (e.g., 2.9% + $0.30)
- Tiered: Qualified/Mid-Qualified/Non-Qualified rates

## Payout Methods

### ACH (Standard)
- Timing: Next business day (T+1) or custom delay
- Cost: ~$0.25 per transaction
- Limit: $25M per transaction (NACHA limit)
- Returns: R01-R99 codes, monitor for 60 days

### Wire (Large Amounts)
- Timing: Same-day
- Cost: $15-$30 per wire
- Use for: Settlements >$100K or urgent payouts

### Push-to-Card (Instant)
- Timing: Minutes
- Cost: $0.50-$1.00 per push
- Use for: On-demand payouts, gig economy merchants

## Monitoring
- Settlement success rate: Target >99.5%
- Payout timing SLA adherence
- Fee calculation accuracy: Compare to network clearing files
- ACH return rate: Target <1%
