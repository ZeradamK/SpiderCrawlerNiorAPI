---
name: case-management
description: |
  Fraud case management workflows — investigation, evidence, resolution, and reporting.
  Perfect for: fraud analyst workflows, case assignment, SLA tracking, investigation reports.
  Not ideal for: automated real-time scoring (use fraud-scoring).
---

# Fraud Case Management

## Core Philosophy
**"Every flagged transaction deserves a decision — manage the queue, not the other way around."**

## Case Lifecycle

```
CREATED → ASSIGNED → INVESTIGATING → DECISION → CLOSED
                          │
                          ├──▶ ESCALATED → SENIOR_REVIEW → DECISION → CLOSED
                          │
                          └──▶ INFO_REQUESTED → INVESTIGATING (loop)
```

## Queue Management

### Priority Scoring
```
priority = base_priority + amount_factor + time_factor + pattern_factor

base_priority:
  - High-value (>$5K): 100
  - Account takeover: 90
  - BIN attack: 85
  - First-party fraud: 70
  - General review: 50

amount_factor: log10(amount_cents) × 5
time_factor: minutes_until_deadline × -0.5
pattern_factor: linked_cases × 10
```

### SLA Targets
| Priority | Response Time | Resolution Time |
|----------|--------------|-----------------|
| Critical (>90) | 15 minutes | 2 hours |
| High (70-89) | 1 hour | 8 hours |
| Medium (50-69) | 4 hours | 24 hours |
| Low (<50) | 8 hours | 48 hours |

### Auto-Assignment
- Round-robin within skill-matched analyst pool
- Workload balancing (max 15 active cases per analyst)
- Skill routing (BIN attacks → specialized analysts)
- Language matching (customer contact cases)

## Investigation Workflow

### Step 1: Initial Assessment (5 min)
1. Review transaction details and fraud score factors
2. Check customer history (prior disputes, account age)
3. Check device and IP history
4. Assess: quick decision possible or deeper investigation needed?

### Step 2: Deep Investigation (if needed)
1. Pull full entity graph (linked cards, devices, IPs, accounts)
2. Review transaction timeline
3. Check external data sources (Sift, Sardine)
4. Cross-reference with known fraud patterns
5. Contact cardholder if needed (for non-fraud disputes)

### Step 3: Decision
- **Approve**: Release transaction, update model training data
- **Decline**: Block transaction, add entities to blocklist
- **Escalate**: Route to senior analyst or law enforcement
- **Pending**: Request additional information

### Step 4: Documentation
- Record decision rationale
- Tag fraud type (if confirmed)
- Update entity risk scores
- Feed back to ML model training pipeline

## Reporting

### Daily Report
- Cases opened vs closed
- Average resolution time
- Win rate on represented chargebacks
- Top fraud patterns detected
- Queue depth and SLA adherence

### Monthly Report
- Fraud rate trends
- Dollar amount prevented
- False positive rate
- Model performance metrics
- Rule effectiveness analysis
