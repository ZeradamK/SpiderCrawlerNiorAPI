---
description: Transfer funds between wallets or to external accounts
argument-hint: "[from_wallet] [to_wallet] [amount] [currency]"
---

# Wallet Transfer Command

## Workflow

### Step 1: Validate Transfer
1. Verify source wallet has sufficient balance
2. Verify destination wallet or account exists
3. Check transfer limits (daily, per-transaction)
4. Run sanctions screening on both parties
5. Run AML transaction monitoring rules

### Step 2: Determine Transfer Type
- **Internal P2P**: Wallet-to-wallet (instant, no fees)
- **External push**: Wallet to bank account (ACH T+1, fee applies)
- **External pull**: Bank account to wallet (ACH T+1-3)
- **Cross-currency**: FX conversion required (markup applies)

### Step 3: Execute
1. Debit source wallet (atomic)
2. Credit destination wallet or initiate external transfer
3. For cross-currency: apply FX rate with markup
4. Generate transfer receipt for both parties

### Step 4: Confirm
1. Send confirmation to sender and recipient
2. Update transaction history for both wallets
3. Update velocity tracking counters

## Output Format
```
Transfer: tfr_xxx
From: wal_xxx ($XX.XX debited)
To: wal_xxx ($XX.XX credited)
Amount: $XX.XX USD
Fee: $X.XX
Status: completed | pending | failed
```
