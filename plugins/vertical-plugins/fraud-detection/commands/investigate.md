---
description: Investigate a flagged transaction or customer for fraud patterns
argument-hint: "[transaction_id or customer_id]"
---

# Fraud Investigation Command

## Workflow

### Step 1: Build Investigation Profile
1. Pull all transactions for the entity (customer, card, device, IP)
2. Timeline view of activity over last 90 days
3. Map all linked entities (shared devices, IPs, emails, phones)
4. Check for known fraud indicators

### Step 2: Pattern Analysis
Evaluate against known fraud patterns:
- **Account takeover**: New device + password change + high-value purchase
- **Card testing**: Multiple small authorizations in rapid succession
- **Triangulation fraud**: Legitimate purchases followed by chargebacks
- **Synthetic identity**: Mix of real and fabricated identity elements
- **Friendly fraud**: Legitimate cardholder disputing valid charges
- **BIN attack**: Sequential card numbers from same BIN range

### Step 3: Link Analysis
Map connections between entities:
- Shared device fingerprints across different accounts
- Shared IP addresses or IP ranges
- Shared email patterns (e.g., firstname+N@domain.com)
- Shared shipping addresses
- Shared phone numbers

### Step 4: Generate Report
Compile findings with evidence and recommended action.

## Output Format
```
Investigation Report: [entity_type] [entity_id]

Risk Assessment: HIGH
Pattern Match: [pattern_name] (XX% confidence)

Entity Network:
  Accounts linked: XX
  Devices linked: XX
  IPs linked: XX

Timeline: [chronological event list]

Recommended Action: block | monitor | clear
Evidence: [supporting data points]
```
