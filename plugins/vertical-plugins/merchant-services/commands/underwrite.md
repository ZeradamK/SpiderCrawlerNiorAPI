---
description: Run underwriting analysis on a merchant application
argument-hint: "[merchant_id or application_id]"
---

# Underwriting Analysis Command

## Workflow

### Step 1: Financial Analysis
1. Review business financial statements (if available)
2. Check business credit report (D&B PAYDEX, Experian Intelliscore)
3. Review owner personal credit
4. Analyze cash flow patterns

### Step 2: Risk Assessment
| Factor | Weight | Low Risk | High Risk |
|--------|--------|----------|-----------|
| Business age | 15% | >5 years | <1 year |
| Industry (MCC) | 20% | Retail, grocery | Travel, digital goods |
| Monthly volume | 15% | <$50K | >$500K |
| Average ticket | 10% | <$50 | >$500 |
| Chargeback history | 20% | <0.5% | >1.0% |
| Owner credit | 10% | >700 | <600 |
| Website quality | 10% | Clear terms | No refund policy |

### Step 3: Determine Terms
Based on risk tier:
- **Low risk**: Standard fees, T+1 settlement, no reserve
- **Medium risk**: Higher fees, T+2 settlement, 5% rolling reserve
- **High risk**: Premium fees, T+3 settlement, 10% rolling reserve
- **Prohibited**: Decline application (illegal products, MATCH list)

### Step 4: Decision Documentation
Document underwriting rationale for compliance audit trail.

## Output Format
```
Underwriting Analysis: [merchant_name]
Risk Tier: low | medium | high
Decision: approved | conditional | declined
Conditions: [if conditional]
Reserve: X% rolling | $X,XXX fixed
Processing Limit: $XXX,XXX/month
```
