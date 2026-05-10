---
name: merchant-onboarding
description: |
  End-to-end merchant onboarding workflow from application to provisioning.
  Perfect for: new merchant setup, application processing, MCC assignment, limit configuration.
  Not ideal for: ongoing merchant monitoring (use merchant-portfolio).
---

# Merchant Onboarding

## Core Philosophy
**"Fast onboarding with smart risk controls — get merchants processing quickly without compromising safety."**

## Application Processing

### Required Documentation
**Sole Proprietor**: Government ID, SSN, business license (if required), bank statement
**LLC/Corporation**: Articles of incorporation, EIN letter, operating agreement, beneficial ownership form
**All**: Voided check or bank letter for settlement account, 3 months bank statements (for high-volume)

### MCC Assignment
Assign the correct Merchant Category Code based on primary business activity:
- Review business description and website
- Map to ISO 18245 MCC code
- Consider sub-categories for better interchange qualification
- Common high-risk MCCs: 5962 (direct marketing), 5966 (outbound telemarketing), 7995 (gambling)

### MATCH/TMF Check
Before approving, check terminated merchant databases:
- **MATCH** (Mastercard Alert to Control High-risk Merchants)
- **TMF** (Terminated Merchant File)
- If listed: decline or require detailed explanation + senior approval

### Reserve Requirements
| Risk Tier | Reserve Type | Amount | Duration |
|-----------|-------------|--------|----------|
| Low | None | $0 | N/A |
| Medium | Rolling | 5% of volume | 6 months |
| High | Fixed + Rolling | $10K + 10% | 12 months |
| Very High | Up-front + Rolling | $25K + 15% | 18 months |

## Provisioning Workflow
1. Generate Merchant ID (mch_xxx)
2. Create processor account (Stripe Connect, Adyen sub-merchant, etc.)
3. Configure payment methods accepted
4. Set processing limits
5. Configure settlement schedule and bank account
6. Generate API keys and webhook secret
7. Send welcome email with integration documentation
