---
description: Capture a previously authorized payment transaction
argument-hint: "[transaction_id] [amount]"
---

# Capture Payment Command

## Workflow

### Step 1: Validate Authorization
1. Look up the transaction by ID
2. Verify status is `authorized` (not expired, voided, or already captured)
3. Confirm capture amount does not exceed authorized amount
4. Check authorization expiry — if expired, advise re-authorization

### Step 2: Partial vs Full Capture
- If capture amount equals authorized amount → full capture
- If capture amount is less → partial capture; remaining auth amount is released
- If no amount specified → default to full capture
- **Multiple partial captures** are supported for split-shipment scenarios

### Step 3: Submit Capture
1. Route capture request to the original processor
2. Include original auth code and transaction reference
3. Process network response

### Step 4: Update Records
1. Update transaction status to `captured`
2. Queue transaction for next settlement batch
3. Update merchant's daily capture volume
4. Return capture confirmation

## Output Format
```
Transaction ID: txn_xxx
Status: captured
Captured Amount: $XX.XX USD
Original Auth Amount: $XX.XX USD
Settlement Batch: stl_xxx (next cycle)
```
