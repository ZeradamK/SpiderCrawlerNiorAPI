---
name: network-clearing
description: |
  Card network clearing file processing and reconciliation.
  Perfect for: TC33/IPM file processing, interchange validation, network reconciliation.
  Not ideal for: merchant-level settlement (use batch-processing).
---

# Network Clearing

## Core Philosophy
**"The network is the source of truth for clearing — reconcile early, reconcile often."**

## Clearing File Formats

### Visa TC33 (Transaction Clearing)
- Format: Fixed-width text records
- Delivery: Daily via VisaNet
- Key records:
  - TCR0: Financial transaction
  - TCR1: Addendum (Level 2/3 data)
  - TCR4: Fee collection
  - TCR5: Currency conversion

### Mastercard IPM (Integrated Processing Message)
- Format: ISO 8583 / fixed-width
- Delivery: Daily via MasterCard Network
- Key messages:
  - First presentment (original transaction)
  - Second presentment (represented chargeback)
  - Fee collection
  - Retrieval request

## Clearing Cycle

```
Day 0: Authorization (real-time)
Day 0: Capture/batch close
Day 1: First presentment to network
Day 1: Network clearing (TC33/IPM generation)
Day 2: Issuer receives clearing record
Day 2: Settlement funding between banks
Day 3: Merchant receives payout
```

## Reconciliation Process

### Daily Reconciliation Steps
1. **Download** clearing files from network
2. **Parse** transaction records
3. **Match** against internal transaction database
4. **Validate** interchange category assignments
5. **Identify** mismatches and exceptions
6. **Report** reconciliation results

### Match Key
Primary: Network reference number (ARN for Visa, DE63 for MC)
Secondary: Amount + date + card last-four + merchant ID
Fuzzy: Amount within tolerance + date ±1 day

### Exception Categories
| Category | Description | Action |
|----------|-------------|--------|
| Missing internal | Network has record, we don't | Investigate lost capture |
| Missing external | We have record, network doesn't | Re-submit or investigate |
| Amount mismatch | Amounts differ | Check FX, partial capture |
| Fee variance | Interchange rate differs | Verify qualification |
| Timing | Record in different date's file | Auto-resolve, monitor |

## Interchange Validation
- Compare actual interchange charged vs expected category
- Flag downgrades (higher rate than expected)
- Calculate potential savings from data enrichment
- Monthly interchange optimization report
