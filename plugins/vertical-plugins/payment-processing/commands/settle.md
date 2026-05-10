---
description: Initiate settlement for a batch of captured transactions
argument-hint: "[merchant_id] [date]"
---

# Settlement Command

## Workflow

### Step 1: Identify Settlement Candidates
1. Query all transactions with status `captured` for the specified merchant
2. Filter by settlement date (default: today's cutoff)
3. Exclude transactions with pending disputes or holds
4. Group by currency

### Step 2: Calculate Settlement Amounts
For each currency group:
1. Sum all capture amounts
2. Subtract refunds processed since last settlement
3. Subtract chargeback debits
4. Calculate and deduct processing fees (interchange + markup + per-txn)
5. Compute net settlement amount

### Step 3: Create Settlement Batch
1. Generate settlement batch record with all included transactions
2. Validate net amount is positive (if negative, roll into next cycle)
3. Lock included transactions (prevent further refunds until settled)

### Step 4: Execute Payout
1. Initiate ACH credit or wire to merchant's bank account
2. Apply settlement delay (T+1, T+2, etc. per merchant config)
3. Record expected arrival date

### Step 5: Confirm and Report
1. Update all included transactions to status `settled`
2. Update batch status to `processing`
3. Generate settlement report with line-item breakdown
4. Send settlement notification to merchant webhook

## Output Format
```
Settlement Batch: stl_xxx
Merchant: mch_xxx
Transactions: XX
Gross Amount: $XX,XXX.XX USD
Fees: -$XXX.XX
Net Payout: $XX,XXX.XX USD
Expected Arrival: YYYY-MM-DD
```
