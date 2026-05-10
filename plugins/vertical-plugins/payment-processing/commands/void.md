---
description: Void an authorized or captured transaction before settlement
argument-hint: "[transaction_id]"
---

# Void Transaction Command

## Workflow

### Step 1: Validate Transaction
1. Look up transaction by ID
2. Verify status is `authorized` or `captured` (not yet settled)
3. If already settled, advise using `/refund` instead
4. If already voided, return current void status

### Step 2: Process Void
1. Submit void/reversal to the original processor
2. Release the authorization hold on the cardholder's account
3. No interchange fees are charged for voided transactions

### Step 3: Update Records
1. Update transaction status to `voided`
2. Remove from pending settlement batch
3. Release merchant's processing volume allocation
4. Log void reason for audit trail

## Output Format
```
Transaction ID: txn_xxx
Status: voided
Original Amount: $XX.XX USD
Interchange Saved: $X.XX
Voided At: YYYY-MM-DD HH:MM:SS UTC
```
