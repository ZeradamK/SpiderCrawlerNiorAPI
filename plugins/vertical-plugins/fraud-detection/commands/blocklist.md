---
description: Manage fraud blocklists — add or remove cards, IPs, emails, devices
argument-hint: "[add|remove] [type] [value]"
---

# Blocklist Management Command

## Workflow

### Step 1: Parse Input
- **Action**: `add` or `remove`
- **Type**: `card`, `bin`, `ip`, `email`, `device`, `address`, `phone`
- **Value**: The entity to block/unblock
- **Reason**: Required for audit trail

### Step 2: Validate Entry
1. Verify format matches type (e.g., valid BIN range, valid IP/CIDR)
2. Check for conflicts (blocking a BIN range that covers legitimate high-volume merchants)
3. For IP blocks: warn if CIDR range is too broad (>/24 requires confirmation)
4. For email blocks: support wildcard patterns (e.g., `*@disposable-email.com`)

### Step 3: Apply
1. Add/remove from blocklist database
2. Set expiry if specified (default: no expiry)
3. Log change with operator, timestamp, and reason
4. If adding: retroactively flag recent transactions matching the blocked entity

### Step 4: Confirm

## Output Format
```
Blocklist Updated:
  Action: added | removed
  Type: [entity_type]
  Value: [entity_value]
  Reason: [reason]
  Expires: [date] | never
  Recent matches: XX transactions flagged
```
