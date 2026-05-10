---
description: Execute or analyze FX hedging strategies for cross-border payment exposure
argument-hint: "[currency_pair] [amount] [tenor]"
---

# FX Hedging Command

## Workflow

### Step 1: Assess FX Exposure
1. Calculate net exposure by currency pair
2. Identify settlement timing mismatches (receive EUR today, pay USD in T+2)
3. Quantify unhedged exposure
4. Model VaR (Value at Risk) at 95% confidence

### Step 2: Hedging Strategy
Based on exposure profile:
- **Spot**: Immediate conversion for same-day settlement needs
- **Forward**: Lock in rate for future settlement dates (T+2 to 12 months)
- **NDF (Non-Deliverable Forward)**: For restricted currencies
- **Options**: For uncertain exposure amounts (protective puts)

### Step 3: Execute or Recommend
- Below threshold ($10K): auto-execute spot conversion
- Medium ($10K-$500K): recommend strategy, execute on approval
- Large (>$500K): recommend strategy with multiple quotes, require treasury approval

### Step 4: Record and Monitor
1. Record trade details and hedging rationale
2. Monitor mark-to-market of open positions
3. Alert on significant rate movements (>1% intraday)

## Output Format
```
FX Hedging Analysis: [currency_pair]
Net Exposure: [amount] [currency]
Current Rate: X.XXXX
VaR (95%, 1d): $XX,XXX
Recommendation: spot | forward | option
Indicative Rate: X.XXXX
Cost: $X,XXX
```
