---
description: Process settlement batch for captured transactions
argument-hint: "[merchant_id] [date]"
---

# Batch Settlement Command

## Workflow

### Step 1: Batch Assembly
1. Query all captured, unsettled transactions for the merchant
2. Apply settlement cutoff time (default: 11:59 PM merchant local time)
3. Exclude transactions with pending disputes or holds
4. Group by currency and payment method type

### Step 2: Netting
For each group:
- Sum captures (gross credits)
- Subtract refunds (debits)
- Subtract chargebacks (debits)
- Calculate net settlement amount

### Step 3: Fee Calculation
Deduct from net settlement:
- Interchange fees (per-transaction, varies by card type)
- Network assessment fees (Visa: 0.14%, MC: 0.13%)
- Processor markup (per agreement)
- Per-transaction fees
- Monthly minimum fee adjustment (if applicable)

### Step 4: Execute Payout
1. Submit ACH credit to merchant bank account
2. Record batch with full transaction detail
3. Generate settlement report

## Output Format
```
Settlement Batch: stl_xxx
Merchant: [name] (mch_xxx)
Period: [start_date] to [end_date]
Transactions: XX captures, XX refunds, XX chargebacks
Gross: $XX,XXX.XX
Fees: -$X,XXX.XX (interchange: $XXX, assessment: $XX, markup: $XXX)
Net Payout: $XX,XXX.XX
Expected Arrival: YYYY-MM-DD
```
