---
description: Look up transaction details by ID, reference, or merchant
argument-hint: "[transaction_id or reference_id]"
---

# Transaction Lookup Command

## Workflow

### Step 1: Parse Search Input
- If `txn_xxx` format → direct transaction ID lookup
- If `ref_xxx` or external ID → search by reference_id
- If `mch_xxx` → list recent transactions for that merchant
- Otherwise → search by amount + date range + payment method last-four

### Step 2: Retrieve Transaction
1. Fetch full transaction record including all child transactions (refunds, chargebacks)
2. Include network response details
3. Include risk assessment data
4. Include settlement batch information if settled

### Step 3: Display Results
Present a comprehensive view of the transaction lifecycle.

## Output Format
```
Transaction ID: txn_xxx
Type: authorization → capture → settlement
Status: settled
Amount: $XX.XX USD
Merchant: Example Corp (mch_xxx)
Payment Method: Visa ****1234 (credit)
Risk Score: XX/100

Timeline:
  Authorized:  YYYY-MM-DD HH:MM:SS  Auth Code: XXXXXX
  Captured:    YYYY-MM-DD HH:MM:SS  Amount: $XX.XX
  Settled:     YYYY-MM-DD HH:MM:SS  Batch: stl_xxx

Network Response:
  AVS: Y (full match)
  CVV: M (match)
  3DS: 2.2 authenticated (ECI: 05)
```
