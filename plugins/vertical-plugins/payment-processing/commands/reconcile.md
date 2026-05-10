---
description: Reconcile internal transaction records against processor or bank statements
argument-hint: "[processor] [date_range]"
---

# Reconciliation Command

## Workflow

### Step 1: Load Data Sources
1. Fetch internal transaction records for the specified date range
2. Pull processor settlement files (Stripe payouts, Adyen settlements, etc.)
3. Optionally pull bank statement data via Plaid or direct feed

### Step 2: Match Transactions
For each processor record:
1. Match by transaction ID or network reference number
2. Verify amounts match (within tolerance for FX conversions)
3. Verify settlement dates align
4. Flag unmatched records on either side

### Step 3: Identify Breaks
Categorize discrepancies:
- **Missing internal**: processor settled but no internal record (possible lost webhook)
- **Missing external**: internal record captured but not in processor settlement
- **Amount mismatch**: records exist on both sides but amounts differ
- **Date mismatch**: settlement date differs beyond tolerance
- **FX variance**: amount differs due to exchange rate timing

### Step 4: Generate Report
1. Summary statistics (match rate, total breaks, break amount)
2. Detail listing of each break with recommended action
3. Auto-resolve trivial breaks (rounding, FX within tolerance)
4. Escalate material breaks for investigation

## Output Format
```
Reconciliation Report: [Processor] [Date Range]
Total Internal Records: XXX
Total Processor Records: XXX
Matched: XXX (XX.X%)
Breaks: XX ($X,XXX.XX total)

Break Details:
  #1  txn_xxx  Missing external  $XXX.XX  Action: investigate webhook
  #2  txn_xxx  Amount mismatch   $X.XX    Action: FX adjustment
```
