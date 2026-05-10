---
name: merchant-portfolio
description: |
  Ongoing merchant portfolio monitoring, risk management, and performance analysis.
  Perfect for: merchant health monitoring, chargeback management, limit adjustments, portfolio risk.
  Not ideal for: initial merchant onboarding (use merchant-onboarding).
---

# Merchant Portfolio Management

## Core Philosophy
**"A healthy portfolio is a watched portfolio — catch problems early, reward good merchants, and act decisively on bad actors."**

## Monitoring Framework

### Daily Metrics Per Merchant
| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Chargeback rate | <0.65% | 0.65-0.90% | >0.90% |
| Refund rate | <5% | 5-15% | >15% |
| Decline rate | <15% | 15-30% | >30% |
| Authorization amount | Within 2σ | 2-3σ deviation | >3σ deviation |
| Average ticket | Within 2σ | 2-3σ deviation | >3σ deviation |

### Visa/MC Monitoring Programs
**Visa Dispute Monitoring Program (VDMP)**:
- Standard: >0.65% dispute rate AND >75 disputes/month
- Excessive: >0.90% dispute rate AND >100 disputes/month
- Fines: $10K-$100K/month, escalating

**Mastercard Excessive Chargeback Program (ECP)**:
- Excessive: >1.5% chargeback rate AND >100 chargebacks/month
- High Excessive: >3.0% chargeback rate AND >300 chargebacks/month

### Actions by Alert Level
| Level | Action |
|-------|--------|
| Warning | Email merchant, add to watch list, weekly review |
| Critical | Call merchant, reduce limits, increase reserve, 30-day remediation plan |
| Violation | Suspend processing, freeze funds, initiate termination review |
| Termination | Close account, report to MATCH, settle reserves |

## Portfolio Analytics
- Total processing volume by month, quarter, year
- Revenue per merchant (fees collected)
- Portfolio attrition rate
- Average merchant lifecycle
- Revenue concentration risk (top 10 merchants as % of total)
- Industry distribution and risk heat map
