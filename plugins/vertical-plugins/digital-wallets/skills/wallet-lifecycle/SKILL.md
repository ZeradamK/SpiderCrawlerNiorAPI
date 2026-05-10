---
name: wallet-lifecycle
description: |
  Digital wallet creation, management, and lifecycle operations.
  Perfect for: wallet provisioning, balance management, tier upgrades, account closure.
  Not ideal for: card tokenization for PCI (use tokenization skill).
---

# Wallet Lifecycle Management

## Core Philosophy
**"A wallet is a trust relationship — earn it gradually, protect it always."**

## Wallet States

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ CREATED  │───▶│  ACTIVE  │───▶│ SUSPENDED│
└──────────┘    └──────────┘    └──────────┘
                     │ ▲              │
                     │ │              ▼
                     ▼ │         ┌──────────┐
                ┌──────────┐    │  CLOSED  │
                │ UPGRADED │    └──────────┘
                └──────────┘
```

## Tier System

### Tier Levels
| Tier | KYC Level | Balance Max | Daily Transfer | Features |
|------|-----------|-------------|----------------|----------|
| Basic | Email + phone | $1,000 | $500 | P2P, store purchases |
| Standard | Full KYC (ID + SSN) | $10,000 | $5,000 | + Bill pay, ACH transfers |
| Premium | Enhanced KYC | $100,000 | $50,000 | + Wire, international, crypto |
| Business | Business KYC | $500,000 | $250,000 | + Payroll, multi-user, API |

### Upgrade Path
1. User requests upgrade
2. Additional KYC verification required
3. Review and approval (auto for Standard, manual for Premium/Business)
4. Limits updated immediately on approval

## Balance Operations

### Funding (Money In)
- **Bank transfer (ACH)**: T+1 to T+3, free
- **Debit card**: Instant, 1.5% fee
- **Direct deposit**: Free, requires employer setup
- **Cash load**: Via retail partner network

### Withdrawal (Money Out)
- **Bank transfer (ACH)**: T+1, free (Standard+)
- **Instant transfer**: Minutes, $0.25-$1.00 fee
- **ATM withdrawal**: Via partner network, fee varies
- **Check**: Mail, $5.00 fee

### Auto-Reload
- Set threshold balance
- Auto-fund from default source when balance drops below threshold
- Configurable reload amount
- Daily reload limit to prevent runaway charges

## Security Features
- PIN for in-person transactions
- Biometric authentication (Face ID, Touch ID)
- Device binding (trusted devices)
- Transaction notifications (real-time push)
- Spending controls (category locks, geographic limits)
- Freeze/unfreeze instant toggle
- Two-factor for high-value transfers

## Regulatory Compliance
- FinCEN MSB registration (for P2P and stored value)
- State money transmitter licenses
- Prepaid access rule compliance
- E-Sign Act consent for electronic statements
- Regulation E (error resolution, unauthorized transfers)
