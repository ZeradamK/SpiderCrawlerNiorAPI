---
description: Prepare and file a Suspicious Activity Report (SAR) with FinCEN
argument-hint: "[case_id]"
---

# SAR Filing Command

## Workflow

### Step 1: Gather Case Information
1. Pull investigation case details
2. Compile all suspicious transactions
3. Identify all subjects (individuals and entities)
4. Document the suspicious activity narrative

### Step 2: Complete SAR Form
FinCEN Form 111 fields:
- **Part I**: Subject information (name, SSN/EIN, DOB, address, phone)
- **Part II**: Suspicious activity information
  - Date range of activity
  - Total amount involved
  - Type of suspicious activity (money laundering, structuring, fraud, etc.)
- **Part III**: Financial institution information
- **Part IV**: Activity narrative (free-text description)

### Step 3: Narrative Drafting
The narrative must include:
1. **Who** — subjects and their roles
2. **What** — the suspicious activity
3. **When** — date range and key dates
4. **Where** — locations and accounts involved
5. **Why** — why the activity is suspicious
6. **How** — the method/technique used

### Step 4: Review & Submit
1. Compliance officer review and approval
2. Submit via FinCEN BSA E-Filing
3. Retain copy for 5 years
4. **NEVER notify the subject of the SAR filing**

## Output Format
```
SAR Draft: [case_id]
Subjects: [count]
Activity Type: [category]
Date Range: [start] to [end]
Total Amount: $XXX,XXX.XX
Status: draft | under_review | filed
FinCEN Tracking: [if filed]
```
