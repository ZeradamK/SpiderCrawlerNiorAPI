---
description: View real-time cash position across all accounts and currencies
argument-hint: "[currency] [date]"
---

# Cash Position Command

## Workflow

### Step 1: Aggregate Balances
1. Pull real-time balances from all bank accounts
2. Pull processor float balances (Stripe, Adyen pending payouts)
3. Pull reserve account balances
4. Pull FX position balances

### Step 2: Calculate Positions
For each currency:
- Available cash = bank balance - pending outflows + pending inflows
- Committed cash = settlement obligations + reserve requirements
- Free cash = available - committed
- Projected cash (T+1, T+3, T+7) based on settlement schedule

### Step 3: Display Dashboard

## Output Format
```
Cash Position Report: [date]

Currency  | Available    | Committed    | Free         | T+1 Projected
USD       | $X,XXX,XXX  | $XXX,XXX    | $X,XXX,XXX  | $X,XXX,XXX
EUR       | €X,XXX,XXX  | €XXX,XXX    | €X,XXX,XXX  | €X,XXX,XXX
GBP       | £X,XXX,XXX  | £XXX,XXX    | £X,XXX,XXX  | £X,XXX,XXX

Total (USD equiv): $XX,XXX,XXX
```
