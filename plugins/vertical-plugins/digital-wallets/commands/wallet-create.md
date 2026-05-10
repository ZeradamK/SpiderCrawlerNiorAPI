---
description: Create a new digital wallet for a customer
argument-hint: "[customer_id]"
---

# Wallet Creation Command

## Workflow

### Step 1: Customer Verification
1. Verify customer identity (KYC status must be approved)
2. Check for existing wallets (prevent duplicates)
3. Determine wallet tier based on KYC level

### Step 2: Wallet Provisioning
1. Generate wallet ID (wal_xxx)
2. Set wallet limits based on tier:
   - **Basic** (KYC lite): $1,000 balance, $500/day transfer
   - **Standard** (full KYC): $10,000 balance, $5,000/day transfer
   - **Premium** (enhanced KYC): $100,000 balance, $50,000/day transfer
3. Create multi-currency sub-wallets (USD, EUR, GBP)

### Step 3: Payment Method Linking
1. Link funding source (bank account, debit card)
2. Verify funding source (micro-deposits or instant verification)
3. Set as default funding source

### Step 4: Enable Features
- P2P transfers
- Bill payments
- Merchant payments (NFC, QR, online)
- Auto-reload from funding source

## Output Format
```
Wallet Created: wal_xxx
Customer: [customer_id]
Tier: basic | standard | premium
Balance Limit: $XX,XXX
Daily Transfer Limit: $XX,XXX
Currencies: USD, EUR, GBP
Status: active
```
