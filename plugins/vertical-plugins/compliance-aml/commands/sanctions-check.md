---
description: Run sanctions screening against global watchlists
argument-hint: "[entity_name or transaction_id]"
---

# Sanctions Check Command

## Workflow

### Step 1: Parse Entity
Extract screening targets:
- Originator name and country
- Beneficiary name and country
- Intermediary banks (SWIFT codes)
- Associated entities and aliases

### Step 2: Screen Against Lists
Check all targets against:
1. **OFAC SDN** — US Treasury Specially Designated Nationals
2. **OFAC Consolidated** — Non-SDN lists (SSI, FSE, NS-MBS)
3. **EU Consolidated** — European sanctions
4. **UN Sanctions** — UN Security Council consolidated list
5. **FATF High-Risk** — FATF-identified jurisdictions
6. **Local lists** — Country-specific sanctions and PEP lists

### Step 3: Fuzzy Matching
- Exact match check
- Phonetic matching (Soundex, Metaphone)
- Transliteration variants (Arabic, Cyrillic, Chinese)
- Alias and AKA matching
- Threshold: >85% match score triggers review

### Step 4: Decision
- **Clear**: No matches found
- **Potential Match**: Fuzzy match found, manual review required
- **True Match**: Confirmed match — BLOCK transaction immediately
- **False Positive**: Match investigated and cleared

## Output Format
```
Sanctions Screening: [entity_name]
Result: clear | potential_match | true_match
Lists Checked: OFAC, EU, UN, FATF
Matches Found: X
Highest Score: XX% against [list_name] entry [entry_id]
Action: proceed | block | review
```
