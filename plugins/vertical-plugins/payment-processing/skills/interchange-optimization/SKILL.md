---
name: interchange-optimization
description: |
  Optimize interchange fees through data enrichment, network token usage, and settlement timing.
  Perfect for: cost reduction analysis, B2B payment optimization, interchange qualification.
  Not ideal for: ACH/wire payments, cryptocurrency transactions.
---

# Interchange Optimization

## Core Philosophy
**"Interchange is the largest controllable cost in card processing — every basis point matters at scale."**

## Interchange Fundamentals

### Fee Components
```
Total Processing Cost = Interchange + Assessment + Processor Markup
                        (70-80%)      (5-10%)      (10-25%)
```

### Interchange Categories (Visa Example)

| Category | Rate | Trigger |
|----------|------|---------|
| CPS Retail | 1.51% + $0.10 | Card-present, swiped/dipped |
| CPS e-Commerce Basic | 1.80% + $0.10 | Card-not-present, basic AVS |
| CPS e-Commerce Preferred | 1.65% + $0.10 | CNP + AVS + CVV + 3DS |
| Commercial Standard | 2.70% + $0.10 | Corporate card, no Level 2 data |
| Commercial Level 2 | 2.10% + $0.10 | Corporate card + tax amount + PO |
| Commercial Level 3 | 1.90% + $0.10 | Corporate + line-item detail |
| Regulated Debit | 0.05% + $0.22 | Durbin-regulated debit (max cap) |

## Optimization Strategies

### Strategy 1: Data Enrichment
Send as much transaction data as possible to qualify for lower interchange:

**Level 1 (Basic)**:
- Merchant name, MCC, amount, currency
- Card number, expiry

**Level 2 (Enhanced)**:
- Everything in Level 1, plus:
- Tax amount (sales tax line)
- Customer code / PO number
- Merchant postal code
- **Savings**: 0.30-0.60% on commercial cards

**Level 3 (Full line-item)**:
- Everything in Level 2, plus:
- Line-item descriptions, quantities, unit costs
- Commodity codes, product codes
- Ship-to postal code, freight amount
- **Savings**: 0.50-0.80% on commercial cards

### Strategy 2: Network Tokens
Replace raw PANs with network-provisioned tokens:
- Visa Token Service: 0.10% interchange reduction
- Mastercard MDES: Similar program
- Higher approval rates (tokens update automatically on reissuance)
- Reduced PCI scope (tokens are non-sensitive)

### Strategy 3: 3-D Secure Authentication
3DS shifts liability from merchant to issuer AND reduces interchange:
- Visa: ECI 05 (fully authenticated) → CPS e-Commerce Preferred
- MC: UCAF with AAV → lower interchange category
- **Bonus**: Chargebacks for authenticated transactions are the issuer's liability

### Strategy 4: Settlement Timing
- Settle within 24 hours of authorization for best rates
- Delayed settlement (>48h) can trigger downgrades to higher categories
- Same-day capture + next-day settlement = optimal

### Strategy 5: Debit Routing (Durbin Amendment)
For regulated debit cards (issuers with >$10B assets):
- Route via lowest-cost debit network (not always Visa/MC)
- PIN debit networks: STAR, NYCE, Pulse, Accel
- Maximum fee: 0.05% + $0.22 (Durbin cap)
- Savings vs signature debit: 0.50-1.50%

## Downgrade Prevention

### Common Downgrade Triggers
| Trigger | Category Shift | Fix |
|---------|---------------|-----|
| Missing AVS data | Standard → EIRF | Always send billing address |
| Late settlement (>48h) | Preferred → Standard | Settle same-day |
| Missing CVV | e-Commerce Basic → Standard | Always collect CVV |
| No 3DS on SCA-required | e-Commerce → Standard | Implement 3DS 2.x |
| Missing tax amount | Commercial L2 → Standard | Parse invoices for tax |
| Missing line items | Commercial L3 → L2 | Enrich with product data |

### Monitoring
Track interchange qualification rate:
- **Target**: >95% of transactions at best available rate
- **Alert**: If downgrade rate exceeds 10% in any 24-hour period
- **Report**: Weekly interchange optimization report with savings opportunity

## ROI Calculator

```
Monthly card volume:        $10,000,000
Current blended rate:       2.35%
Optimized blended rate:     2.05%
Monthly savings:            $30,000
Annual savings:             $360,000
```
