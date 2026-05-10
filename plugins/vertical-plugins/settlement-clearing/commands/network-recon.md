---
description: Reconcile settlement records against card network clearing files
argument-hint: "[network] [date]"
---

# Network Reconciliation Command

## Workflow

### Step 1: Fetch Network Files
1. Download TC33 (Visa) or IPM (Mastercard) clearing files
2. Parse transaction-level detail records
3. Map network transaction IDs to internal transaction IDs

### Step 2: Three-Way Match
Match across three sources:
1. **Internal records**: Our captured transactions
2. **Processor records**: Processor settlement files
3. **Network records**: TC33/IPM clearing files

### Step 3: Identify Discrepancies
- Unmatched internal transactions (we captured, network didn't clear)
- Unmatched network transactions (network cleared, we don't have record)
- Amount mismatches (interchange rate discrepancies)
- Fee discrepancies (calculated vs charged interchange)

### Step 4: Resolve
- Auto-resolve: Timing differences (T+1 vs T+2 clearing)
- Manual review: Amount mismatches, unmatched records
- Escalate: Systematic discrepancies indicating configuration issues

## Output Format
```
Network Reconciliation: [network] [date]
Internal Records: XXX
Network Records: XXX
Matched: XXX (XX.X%)
Breaks: XX ($X,XXX.XX)
Auto-Resolved: XX
Pending Review: XX
```
