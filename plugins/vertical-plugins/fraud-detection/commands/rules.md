---
description: Manage fraud detection rules — create, test, enable, disable
argument-hint: "[action] [rule_id]"
---

# Fraud Rules Management Command

## Workflow

### Step 1: Parse Action
- `create` — define a new fraud rule
- `test` — dry-run a rule against historical data
- `enable` / `disable` — toggle rule status
- `list` — show all active rules with hit rates
- `analyze` — show rule performance metrics

### Step 2: Rule Definition (for create)
Define rule using condition-action format:
```yaml
rule:
  name: "high-value-new-card"
  conditions:
    - field: amount
      operator: greater_than
      value: 50000  # $500.00
    - field: payment_method.first_seen_days
      operator: less_than
      value: 7
    - field: merchant.risk_tier
      operator: in
      value: ["elevated", "high"]
  action: review
  priority: 100
  enabled: true
```

### Step 3: Rule Testing (for test)
1. Run rule against last 30 days of transactions
2. Report: true positives, false positives, hit rate
3. Show impact on approval rate if enabled
4. Compare against existing rule overlap

### Step 4: Rule Performance (for analyze)
Display per-rule metrics:
- Hit rate (% of transactions triggering the rule)
- Precision (% of flagged transactions that were actually fraud)
- False positive rate
- Revenue impact (approved transactions that would have been blocked)

## Output Format
```
Rule: [rule_name] (ID: [rule_id])
Status: enabled | disabled
Hit Rate: X.XX%
Precision: XX.X%
False Positive Rate: X.XX%
Last 30 Days: XXX hits, XX confirmed fraud
```
