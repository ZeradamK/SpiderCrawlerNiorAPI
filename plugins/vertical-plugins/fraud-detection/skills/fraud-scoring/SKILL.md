---
name: fraud-scoring
description: |
  Real-time fraud risk scoring using ML models, rule engines, and network signals.
  Perfect for: transaction-level fraud decisions, risk scoring, model evaluation.
  Not ideal for: AML/sanctions screening (use aml-screening), merchant underwriting.
---

# Fraud Scoring

## Core Philosophy
**"Score fast, decide faster — every millisecond of latency is a customer waiting and a fraudster probing."**

## Scoring Architecture

```
Transaction Input
       │
       ├──▶ Feature Extraction (5ms)
       │       ├── Transaction features (amount, MCC, currency)
       │       ├── Card features (BIN, funding, country, age)
       │       ├── Device features (fingerprint, OS, browser)
       │       ├── Behavioral features (velocity, patterns)
       │       └── Derived features (distance, time-of-day)
       │
       ├──▶ Model Inference (10ms)
       │       ├── Primary: XGBoost ensemble
       │       ├── Secondary: Neural network (deep features)
       │       └── Calibration: Platt scaling → probability
       │
       ├──▶ Rules Engine (2ms)
       │       ├── Hard rules (blocklist, velocity limits)
       │       ├── Soft rules (scoring adjustments)
       │       └── Override rules (allowlist, VIP)
       │
       └──▶ Ensemble + Decision (1ms)
               ├── Weighted combination
               ├── Threshold application
               └── Decision output
```

**Total latency budget: <50ms p95**

## Feature Engineering

### Transaction Features
| Feature | Type | Description |
|---------|------|-------------|
| `amount_cents` | int | Transaction amount in cents |
| `amount_zscore` | float | Amount z-score vs merchant average |
| `mcc` | categorical | Merchant category code |
| `currency` | categorical | Transaction currency |
| `is_international` | bool | Card country ≠ merchant country |
| `is_card_present` | bool | POS vs e-commerce |
| `has_3ds` | bool | 3DS authentication attempted |
| `entry_mode` | categorical | chip/swipe/keyed/token |

### Velocity Features
| Feature | Window | Description |
|---------|--------|-------------|
| `txn_count_1h` | 1 hour | Transactions on this card in last hour |
| `txn_count_24h` | 24 hours | Transactions on this card in last day |
| `txn_amount_24h` | 24 hours | Total amount on this card in last day |
| `distinct_merchants_24h` | 24 hours | Unique merchants in last day |
| `distinct_countries_24h` | 24 hours | Unique countries in last day |
| `distinct_devices_7d` | 7 days | Unique devices in last week |

### Device & Network Features
| Feature | Type | Description |
|---------|------|-------------|
| `device_fingerprint` | hash | Browser/device fingerprint |
| `device_age_days` | int | Days since first seen this device |
| `ip_country` | categorical | IP geolocation country |
| `ip_risk_score` | float | IP reputation score |
| `ip_is_proxy` | bool | Detected proxy/VPN/Tor |
| `email_age_days` | int | Email address age |
| `email_domain_risk` | categorical | Disposable/free/corporate domain |

## Model Training

### Training Data
- Labeled fraud/non-fraud transactions (minimum 12 months history)
- Fraud labels from chargebacks, confirmed fraud reports, SAR filings
- Label delay: chargebacks arrive 30-120 days after transaction
- Handle class imbalance: ~0.1% fraud rate → SMOTE + class weights

### Model Evaluation
| Metric | Target | Description |
|--------|--------|-------------|
| AUC-ROC | >0.95 | Overall discriminative power |
| Precision @1% FPR | >60% | Catch rate at low false positive |
| Recall @50% precision | >80% | Coverage at acceptable precision |
| Latency p95 | <20ms | Model inference time |

### Model Deployment
- A/B testing: shadow mode for 2 weeks before promoting
- Champion/challenger: current production vs new candidate
- Rollback: instant rollback to previous model version
- Monitoring: drift detection on feature distributions and score distributions

## Rules Engine

### Rule Types
1. **Hard block**: Immediate decline, no override
   - Card on confirmed fraud blocklist
   - IP from sanctioned country
   - Device on blocklist
2. **Soft flag**: Add to risk score, may trigger review
   - First-time card on merchant (add +15)
   - International transaction (add +10)
   - High-risk MCC (add +20)
3. **Override**: Bypass model score
   - VIP customer allowlist (set score to 0)
   - Test transactions (set score to 0)

### Rule Lifecycle
1. **Draft** → rule created, not active
2. **Shadow** → evaluates on live traffic, no action taken
3. **Active** → evaluates and acts on live traffic
4. **Deprecated** → disabled, retained for audit

## Case Management

### Queue Priority
1. High-value review queue (>$5,000)
2. First-party fraud queue (repeat disputants)
3. Account takeover queue (credential change + purchase)
4. General review queue (score 31-60)

### Investigator Actions
- **Approve**: Release transaction, update model feedback
- **Decline**: Block transaction, add to blocklist optionally
- **Escalate**: Route to senior analyst or law enforcement
- **Request info**: Contact cardholder for verification

## Monitoring & Alerts

### Real-Time Dashboards
- Fraud rate by hour, merchant, BIN range, country
- Model score distribution (detect calibration drift)
- Rule hit rates (detect rule staleness)
- False positive rate by merchant
- Review queue depth and SLA adherence

### Alerting
- Fraud rate spike >2x baseline → P1 alert
- Model score distribution shift >2σ → P2 alert
- Review queue depth >100 → P2 alert
- New BIN attack detected (>50 sequential BINs in 1 hour) → P1 alert
