---
name: kyc-verification
description: |
  Know Your Customer identity verification and due diligence workflows.
  Perfect for: customer onboarding, identity verification, beneficial ownership, risk rating.
  Not ideal for: ongoing transaction monitoring (use aml-screening).
---

# KYC Verification

## Core Philosophy
**"Know who you're doing business with — identity is the foundation of trust in payments."**

## CIP (Customer Identification Program)

### Individual Requirements
| Data Point | Required | Verification Method |
|-----------|----------|-------------------|
| Full legal name | Yes | Government ID |
| Date of birth | Yes | Government ID |
| Address | Yes | Utility bill, bank statement |
| SSN/TIN (US) | Yes | SSN validation service |
| Government ID | Yes | Document scan + biometric |
| Phone number | Recommended | OTP verification |
| Email address | Recommended | Email verification |

### Business Requirements
| Data Point | Required | Verification Method |
|-----------|----------|-------------------|
| Legal entity name | Yes | Secretary of State |
| EIN/TIN | Yes | IRS TIN matching |
| Incorporation state/country | Yes | Corporate registry |
| Business address | Yes | Utility bill, lease |
| Beneficial owners (25%+) | Yes | Individual KYC per owner |
| Control person | Yes | Individual KYC |
| Business license | Varies | State/local registry |
| Articles of incorporation | Varies | Corporate registry |

## Due Diligence Tiers

### Standard Due Diligence (SDD)
- Low-risk customers
- Basic CIP verification
- Annual review

### Enhanced Due Diligence (EDD)
Triggered by:
- High-risk geography (FATF list)
- High-risk business type (MSB, crypto, gambling)
- PEP status
- High transaction volume
- Adverse media hits

Additional requirements:
- Source of funds documentation
- Source of wealth documentation
- Purpose of account/relationship
- Expected transaction patterns
- Senior management approval
- Quarterly or semi-annual review

### Simplified Due Diligence
For low-risk scenarios:
- Publicly listed companies
- Government entities
- Regulated financial institutions
- Low-value prepaid cards (<$1,000)

## Risk Rating

### Customer Risk Factors
| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Geography | Domestic, low-risk | Non-FATF, moderate | FATF high-risk, sanctioned |
| Business Type | Retail, professional | Wholesale, import/export | MSB, crypto, gambling |
| Entity Type | Individual, public co | Private company | Trust, shell company, NPO |
| Volume | <$50K/month | $50K-$500K/month | >$500K/month |
| PEP Status | None | Related to PEP | Direct PEP |
| Adverse Media | None | Historical | Current/recent |

### Composite Score
```
risk_score = max(geo_risk, business_risk, entity_risk, volume_risk, pep_risk, media_risk)
```
Conservative approach: highest individual factor determines overall risk.

## Ongoing Monitoring

### Trigger Events
- Name change or legal entity restructuring
- Change in beneficial ownership
- Significant change in transaction patterns
- New sanctions list publication
- Adverse media alert
- Regular periodic review (annual for standard, quarterly for high-risk)

## Document Management
- Store all KYC documents in encrypted vault
- Maintain audit trail of all verification steps
- Retain for 5 years after relationship ends
- Support regulatory requests for document production
