---
description: Run KYC screening on a customer or business entity
argument-hint: "[customer_id or entity_name]"
---

# KYC Screening Command

## Workflow

### Step 1: Collect Identity Data
Gather required identity documents and data:
- **Individual**: Full legal name, DOB, SSN/TIN, address, government ID
- **Business**: Legal name, EIN/TIN, incorporation state, beneficial owners, registered agent

### Step 2: Identity Verification
1. Document verification (ID scan via Jumio/Onfido)
2. Biometric matching (selfie vs ID photo)
3. Database checks (SSN validation, address verification)
4. Phone/email verification

### Step 3: Sanctions & PEP Screening
Check against:
- OFAC SDN List (US sanctions)
- EU Consolidated Sanctions
- UN Sanctions List
- PEP databases (politically exposed persons)
- Adverse media screening

### Step 4: Risk Assessment
Score customer risk based on:
- Geographic risk (country of residence, nationality)
- Business type risk (MSB, crypto, gambling = higher risk)
- Transaction patterns (expected volume and frequency)
- Source of funds documentation

### Step 5: Decision & Documentation
- **Approved**: Clear for onboarding
- **Enhanced Due Diligence**: Additional documentation required
- **Declined**: Risk too high, document reasons
- **Pending**: Awaiting additional verification

## Output Format
```
KYC Screening: [entity_name]
Status: approved | edd_required | declined | pending
Risk Level: low | medium | high
Identity Verified: yes | no | partial
Sanctions Match: none | potential_match | confirmed_match
PEP Status: none | match
```
