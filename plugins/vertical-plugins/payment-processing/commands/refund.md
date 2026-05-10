---
description: Issue a full or partial refund on a captured transaction
argument-hint: "[transaction_id] [amount]"
---

# Refund Command

## Workflow

### Step 1: Validate Original Transaction
1. Look up the original transaction by ID
2. Verify status is `captured` or `settled`
3. Calculate total already-refunded amount
4. Confirm requested refund does not exceed remaining refundable amount

### Step 2: Determine Refund Type
- **Void** — if transaction is captured but not yet settled, issue a void instead (saves interchange fees)
- **Full refund** — if amount equals original capture amount minus prior refunds
- **Partial refund** — if amount is less than remaining refundable amount
- **Credit** — if original transaction is older than the network's refund window (typically 120 days)

### Step 3: Process Refund
1. Route to the original processor with original transaction reference
2. For card refunds: submit as a credit to the original card
3. For ACH refunds: initiate a return credit via the originating bank
4. For wallet refunds: credit the original wallet balance

### Step 4: Update Records
1. Create a child transaction linked to the original (type: `refund`)
2. Update original transaction's refunded amount
3. Adjust merchant's settlement batch if pre-settlement
4. Trigger refund notification to merchant webhook
5. Return refund confirmation

## Output Format
```
Refund ID: txn_xxx
Original Transaction: txn_xxx
Status: refunded
Refund Amount: $XX.XX USD
Remaining Refundable: $XX.XX USD
Method: void | credit | return
```
