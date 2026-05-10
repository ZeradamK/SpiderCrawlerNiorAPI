---
description: Initiate merchant onboarding application workflow
argument-hint: "[business_name]"
---

# Merchant Onboarding Command

## Workflow

### Step 1: Application Intake
Collect merchant application data:
- Legal business name and DBA
- Business type (sole proprietor, LLC, corporation)
- EIN/SSN, incorporation date and state
- Business address and phone
- Beneficial owners (25%+ ownership)
- Website URL and business description
- Expected monthly volume and average ticket size

### Step 2: Business Verification
1. Verify business registration (Secretary of State)
2. Verify EIN with IRS TIN matching
3. Check business credit (D&B, Experian Business)
4. Website review (products, pricing, terms, refund policy)
5. MATCH/TMF check (terminated merchant databases)

### Step 3: Underwriting Decision
Score based on:
- Business age and financial health
- Industry risk (MCC classification)
- Processing history (if available)
- Owner credit history
- Chargeback/fraud history

### Step 4: Provisioning
If approved:
- Assign MCC code
- Set processing limits (daily, monthly, single transaction)
- Configure fee schedule (interchange-plus, flat rate, tiered)
- Set settlement schedule and reserve requirements
- Provision payment gateway credentials
- Configure webhook endpoints

## Output Format
```
Merchant Application: [business_name]
Status: approved | declined | pending_review
MID: mch_xxx
MCC: XXXX
Monthly Limit: $XXX,XXX
Settlement: T+1 | T+2
Fee Schedule: interchange + X.XX% + $0.XX
```
