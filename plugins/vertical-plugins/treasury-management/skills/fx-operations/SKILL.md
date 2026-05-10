---
name: fx-operations
description: |
  Foreign exchange operations for multi-currency payment processing.
  Perfect for: FX conversion, hedging, exposure management, cross-border payments.
  Not ideal for: domestic single-currency payments.
---

# FX Operations

## Core Philosophy
**"Every basis point in FX spread is margin — manage it like the P&L item it is."**

## Multi-Currency Architecture

### Currency Accounts
Maintain nostro accounts in major settlement currencies:
- USD, EUR, GBP, CAD, AUD, JPY, CHF, SGD, HKD

### FX Conversion Points
1. **At authorization**: Lock rate for the customer (display currency → settlement currency)
2. **At settlement**: Convert merchant settlement to their preferred currency
3. **At payout**: Convert from Eris operating currency to merchant bank currency
4. **At repatriation**: Convert foreign currency balances back to base currency

### Rate Sources
| Source | Use Case | Refresh Frequency |
|--------|----------|-------------------|
| ECB Reference | Benchmark | Daily |
| Bloomberg | Institutional | Real-time |
| CurrencyCloud API | Execution | Real-time |
| Bank rates | Large conversions | On request |

### Markup Structure
| Conversion Type | Markup | Rationale |
|----------------|--------|-----------|
| Consumer DCC | 2.5-3.5% | Dynamic currency conversion at POS |
| Merchant settlement | 0.5-1.0% | Standard cross-border settlement |
| Treasury sweep | 0.1-0.3% | Internal balance optimization |
| Institutional | Negotiated | High-volume client rate |

## Risk Management
- Daily VaR calculation by currency pair
- Stop-loss limits on unhedged exposure
- Regular hedge ratio review (target: 70-90% of known exposure)
- Weekly FX P&L reporting
- Monthly hedge effectiveness assessment
