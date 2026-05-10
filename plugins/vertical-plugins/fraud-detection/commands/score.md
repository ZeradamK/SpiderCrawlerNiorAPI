---
description: Score a transaction for fraud risk in real-time
argument-hint: "[transaction_id or transaction_data]"
---

# Fraud Score Command

## Workflow

### Step 1: Collect Transaction Signals
Gather all available data points:
- Transaction amount, currency, MCC, merchant risk tier
- Payment method details (card BIN, funding type, country)
- Device fingerprint (browser, OS, screen resolution, timezone)
- IP address and geolocation
- Email address and phone number
- Shipping vs billing address comparison
- Customer account age and history

### Step 2: Run Scoring Models
Execute in parallel:
1. **Rules engine**: Apply deterministic rules (velocity, blocklists, geo-fencing)
2. **ML model**: Run through trained fraud classification model
3. **Network signals**: Check consortium data (shared fraud signals across merchants)
4. **Third-party enrichment**: Query Sift, Sardine, or Socure for additional signals

### Step 3: Combine Scores
Weighted ensemble:
- Rules engine: 30% weight (hard rules can override)
- ML model: 40% weight
- Network signals: 15% weight
- Third-party: 15% weight

### Step 4: Decision
| Score Range | Decision | Action |
|-------------|----------|--------|
| 0-30 | Approve | Proceed with authorization |
| 31-60 | Review | Queue for manual review |
| 61-85 | Challenge | Trigger 3DS or step-up auth |
| 86-100 | Decline | Block transaction, log reason |

### Step 5: Return Result

## Output Format
```
Transaction: txn_xxx
Risk Score: XX/100
Decision: approve | review | challenge | decline
Confidence: XX%

Top Factors:
  1. [factor_name]: [value] (contribution: +XX)
  2. [factor_name]: [value] (contribution: +XX)
  3. [factor_name]: [value] (contribution: -XX)

Rules Triggered: [rule_ids]
Model Version: v2.4.1
Latency: XXms
```
