---
name: aml-screening
description: |
  Anti-money laundering transaction monitoring and pattern detection.
  Perfect for: transaction monitoring, structuring detection, SAR preparation, typology analysis.
  Not ideal for: real-time transaction authorization (use fraud-scoring).
---

# AML Screening

## Core Philosophy
**"Follow the money — every suspicious pattern is a story waiting to be told."**

## AML Typologies

### 1. Structuring (Smurfing)
- Multiple deposits just below $10,000 CTR threshold
- Same individual or linked accounts
- Detection: aggregate same-entity transactions in 24-48h windows
- Alert: Total >$10,000 across 3+ transactions in 48 hours

### 2. Layering
- Rapid movement of funds through multiple accounts
- Shell companies, round-tripping, back-to-back transactions
- Detection: graph analysis of fund flows, circular patterns
- Alert: Funds return to origin within 72 hours via 3+ intermediaries

### 3. Trade-Based Money Laundering
- Over/under-invoicing of goods
- Phantom shipments
- Detection: compare invoice amounts with market prices
- Alert: Price deviation >30% from market for commodity

### 4. Funnel Accounts
- Many-to-one or one-to-many fund flows
- Individual account receiving from >10 unrelated senders
- Detection: fan-in/fan-out analysis
- Alert: >10 unique senders in 30 days to personal account

### 5. Rapid Movement
- Funds deposited and withdrawn within 24-48 hours
- No economic purpose for the account
- Detection: measure funds-in vs funds-out velocity
- Alert: >80% of deposits withdrawn within 48 hours

## Transaction Monitoring Rules

### Rule Categories
| Category | Example Rule | Threshold |
|----------|-------------|-----------|
| CTR | Cash transaction | = $10,000 |
| Structuring | Aggregate cash | >$10,000 / 48h window |
| Wire | International wire | >$3,000 (travel rule) |
| Velocity | Rapid fund movement | >80% withdrawn in 48h |
| Geographic | High-risk country | Any transaction |
| Behavior | Account anomaly | >3σ from baseline |

### Scoring Model
```
aml_risk_score = Σ(rule_weight × rule_triggered) + behavior_score + entity_score

Thresholds:
  0-30:   Normal activity
  31-60:  Enhanced monitoring (increase review frequency)
  61-80:  Investigation required (open case within 48 hours)
  81-100: Immediate escalation (compliance officer review within 4 hours)
```

## Regulatory Requirements

### Bank Secrecy Act (BSA)
- Currency Transaction Report (CTR): >$10,000 cash transactions
- Suspicious Activity Report (SAR): Any suspicious activity >$5,000
- Customer Identification Program (CIP): Verify identity at onboarding
- Customer Due Diligence (CDD): Ongoing monitoring
- Beneficial Ownership: Identify 25%+ owners

### Travel Rule (FATF Recommendation 16)
For wire transfers >$3,000:
- Originator: name, account, address
- Beneficiary: name, account
- Must travel with the wire through all intermediary banks

### Record Retention
- SAR filings: 5 years from filing date
- CTR filings: 5 years from filing date
- KYC records: 5 years after account closure
- Transaction records: 5 years from date of transaction

## Monitoring
- Alert-to-SAR conversion rate: Track effectiveness
- False positive rate: Target <80% (industry average ~95%)
- SAR filing timeliness: Within 30 days of detection
- Regulatory exam readiness: Continuous audit trail
