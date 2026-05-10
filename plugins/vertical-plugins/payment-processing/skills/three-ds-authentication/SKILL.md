---
name: three-ds-authentication
description: |
  3-D Secure authentication for card-not-present transactions. SCA compliance and liability shift.
  Perfect for: e-commerce payment security, SCA compliance, chargeback liability management.
  Not ideal for: card-present transactions, recurring payments after initial auth.
---

# 3-D Secure Authentication

## Core Philosophy
**"Authenticate the cardholder, not just the card — frictionless when possible, challenged when necessary."**

## 3DS Version Comparison

| Feature | 3DS 1.0 (Legacy) | 3DS 2.x (Current) |
|---------|-------------------|---------------------|
| User Experience | Full-page redirect | Inline iframe / app SDK |
| Data Points | ~15 fields | ~150 fields (risk-based) |
| Frictionless Flow | No | Yes (up to 95% of transactions) |
| Mobile Support | Poor | Native SDK support |
| SCA Compliance | Partial | Full PSD2 compliance |

## Authentication Flow

### 3DS 2.x Flow

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Merchant│───▶│  3DS    │───▶│ Issuer  │───▶│  ACS    │
│ Server  │    │ Server  │    │  DS     │    │(Issuer) │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │
     │  AReq ──────▶│              │              │
     │              │  AReq ──────▶│              │
     │              │              │  AReq ──────▶│
     │              │              │              │
     │              │              │  ARes ◀──────│
     │              │  ARes ◀──────│              │
     │  ARes ◀──────│              │              │
     │              │              │              │
     │  [If challenge required]    │              │
     │  CReq ──────────────────────────────────▶ │
     │  CRes ◀──────────────────────────────────│
     │              │              │              │
     │  RReq ──────▶│              │              │
     │  RRes ◀──────│              │              │
```

### ECI Values (Electronic Commerce Indicator)

| ECI | Meaning | Liability |
|-----|---------|-----------|
| 05 (Visa) / 02 (MC) | Fully authenticated | Issuer |
| 06 (Visa) / 01 (MC) | Attempted (issuer not enrolled) | Issuer |
| 07 (Visa) / 00 (MC) | Not authenticated / failed | Merchant |

## SCA (Strong Customer Authentication) Rules

### When SCA is Required (PSD2/EU)
- All electronic payments in the EEA
- One-leg-out transactions (one party in EEA)
- Initial transaction for recurring/subscription

### SCA Exemptions
| Exemption | Condition | Max Amount |
|-----------|-----------|------------|
| Low Value | Transaction below threshold | EUR 30 |
| Low Risk (TRA) | Acquirer's fraud rate below threshold | EUR 500 |
| Recurring | Subsequent recurring with same amount | Unlimited |
| Merchant-Initiated | MIT with prior cardholder agreement | Unlimited |
| Corporate | B2B with corporate card (lodged) | Unlimited |
| Allowlisting | Cardholder has allowlisted merchant | Unlimited |

### TRA (Transaction Risk Analysis) Thresholds

| Acquirer Fraud Rate | Max Exempt Amount |
|--------------------|--------------------|
| < 0.13% | EUR 100 |
| < 0.06% | EUR 250 |
| < 0.01% | EUR 500 |

## Implementation Checklist

1. **Integrate 3DS Server** — EMVCo-certified provider
2. **Collect browser/device data** — User-Agent, screen size, timezone, language
3. **Send rich data** — Shipping address, email, phone, purchase history
4. **Handle frictionless** — Most transactions should complete without challenge
5. **Handle challenge** — Inline iframe for web, SDK for mobile
6. **Process result** — Map ECI to authorization request
7. **Store CAVV/AAV** — Required for chargeback defense

## Monitoring

- Frictionless rate: Target >85%
- Authentication success rate: Target >90%
- Challenge completion rate: Target >70%
- Cart abandonment due to 3DS: Track and minimize
