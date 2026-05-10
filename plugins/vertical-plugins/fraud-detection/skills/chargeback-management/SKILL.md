---
name: chargeback-management
description: |
  End-to-end chargeback and dispute lifecycle management across card networks.
  Perfect for: dispute handling, representment, evidence compilation, win-rate optimization.
  Not ideal for: pre-authorization fraud prevention (use fraud-scoring).
---

# Chargeback Management

## Core Philosophy
**"Every chargeback is a learning opportunity — win it if you can, learn from it always."**

## Dispute Lifecycle

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ RECEIVED │───▶│ ANALYZED │───▶│REPRESENTED│───▶│ RESOLVED │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │               │               │               │
     │               ▼               ▼               ├─▶ WON
     │          ┌──────────┐   ┌──────────┐         ├─▶ LOST
     │          │ ACCEPTED │   │PRE-ARBIT │         └─▶ ACCEPTED
     │          └──────────┘   └──────────┘
     │                              │
     │                              ▼
     │                         ┌──────────┐
     │                         │ARBITRATION│
     │                         └──────────┘
```

## Reason Code Mapping

### Visa
| Code | Category | Description | Win Strategy |
|------|----------|-------------|--------------|
| 10.1 | Fraud | EMV liability shift | Provide 3DS proof |
| 10.4 | Fraud | Card-absent fraud | Provide AVS, CVV, delivery proof |
| 13.1 | Consumer | Merchandise not received | Provide tracking + delivery confirmation |
| 13.3 | Consumer | Not as described | Provide product description + terms |
| 12.6 | Processing | Duplicate processing | Show transactions are distinct |

### Mastercard
| Code | Category | Description | Win Strategy |
|------|----------|-------------|--------------|
| 4837 | Fraud | No cardholder authorization | Provide signed receipt or 3DS |
| 4853 | Consumer | Goods/services not provided | Provide delivery proof |
| 4860 | Processing | Credit not processed | Show refund already issued |

## Evidence Compilation

### Required Evidence by Category
**Fraud disputes:**
- 3DS authentication proof (CAVV, ECI)
- AVS match confirmation
- CVV verification result
- IP geolocation matching cardholder
- Device fingerprint history
- Prior non-disputed purchases from same card

**Non-receipt disputes:**
- Shipping carrier tracking number
- Delivery confirmation with signature
- GPS delivery confirmation
- Customer communication acknowledging receipt

**Not-as-described disputes:**
- Product listing/description at time of purchase
- Terms and conditions accepted by customer
- Return policy
- Customer service interaction logs
- Photos of product as shipped

## Representment Best Practices

1. **Respond within deadline** — Visa: 30 days, MC: 45 days
2. **Address the specific reason code** — Don't send generic evidence
3. **Include a compelling rebuttal letter** — Summarize evidence clearly
4. **Cite network rules** — Reference applicable Visa Core Rules or MC Standards
5. **Quality over quantity** — Curate the strongest evidence, don't dump everything

## Metrics
- Chargeback rate per merchant: Target <0.65% (Visa/MC monitoring threshold)
- Win rate: Industry average ~30%, target >45%
- Response rate: Target 100% of representable disputes
- Average response time: Target <5 business days
- Cost per dispute: Track and minimize
