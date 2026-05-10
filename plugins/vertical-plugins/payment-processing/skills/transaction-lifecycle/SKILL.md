---
name: transaction-lifecycle
description: |
  Manage the full payment transaction lifecycle from authorization through settlement.
  Perfect for: end-to-end transaction processing, status management, lifecycle tracking.
  Not ideal for: fraud analysis (use fraud-scoring), compliance checks (use aml-screening).
---

# Transaction Lifecycle Management

## CRITICAL: Data Source Priority

**ALWAYS follow this data source hierarchy:**
1. FIRST: Check for MCP data sources (Stripe, Adyen, processor APIs)
2. DO NOT use web search if MCPs are available
3. ONLY if MCPs are unavailable: Use direct API calls or manual data entry

## Core Philosophy
**"Every payment tells a story — authorization is the promise, capture is the commitment, settlement is the delivery."**

## Transaction States

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ PENDING  │───▶│AUTHORIZED│───▶│ CAPTURED │───▶│ SETTLED  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                     │               │               │
                     ▼               ▼               ▼
                ┌──────────┐   ┌──────────┐    ┌──────────┐
                │  VOIDED  │   │ REFUNDED │    │ DISPUTED │
                └──────────┘   └──────────┘    └──────────┘
                                                     │
                                                     ▼
                                               ┌──────────┐
                                               │ RESOLVED │
                                               └──────────┘
```

## Authorization Flow

### Step 1: Pre-Authorization Checks
1. **Payment method validation**: Verify token is active, not expired, not flagged
2. **Merchant validation**: Confirm merchant is active, within processing limits
3. **Amount validation**: Check against single-transaction and daily volume limits
4. **Currency validation**: Verify merchant accepts this currency
5. **Duplicate detection**: Check for identical amount + card + merchant within 5 minutes

### Step 2: Risk Assessment
1. Run real-time fraud scoring (see `fraud-scoring` skill)
2. Apply merchant-specific rules
3. Check velocity limits (transactions per hour, per day, per card)
4. Evaluate device fingerprint and IP geolocation
5. **Decision gate**: If risk score > threshold, route to manual review queue

### Step 3: Network Routing
1. Identify card network (Visa, MC, Amex, Discover)
2. Select optimal processor based on:
   - **Cost**: Interchange category, processor markup
   - **Approval rate**: Historical approval rate for this BIN range
   - **Latency**: Current processor response times
   - **Availability**: Processor health check status
3. Apply network-specific formatting (ISO 8583 field mapping)

### Step 4: Authorization Request
1. Submit to selected processor with:
   - PAN/token, expiry, CVV (if present)
   - Amount, currency, MCC
   - AVS data (billing address)
   - 3DS authentication data (if applicable)
2. Parse response:
   - **Approved**: Store auth code, set expiry timer
   - **Declined**: Map network decline code to standard reason
   - **Referral**: Flag for voice authorization

## Capture Flow

### Timing Considerations
- **Same-day capture**: Common for digital goods, services
- **Delayed capture**: Physical goods (capture at shipment)
- **Auto-capture**: Configurable per merchant (capture after N hours)
- **Auth expiry**: Visa 7 days, MC 7 days, Amex 7 days (varies by MCC)

### Partial Captures
- Supported for split-shipment scenarios
- Each partial capture creates a child transaction
- Remaining auth amount is auto-released after final capture
- Track `captured_amount` vs `authorized_amount`

## Settlement Flow

### Batch Assembly
1. Collect all captured transactions since last settlement
2. Net refunds and chargebacks against captures
3. Calculate fees:
   - **Interchange**: Network-mandated, varies by card type and MCC
   - **Assessment**: Network fee (Visa: 0.14%, MC: 0.13%)
   - **Processor markup**: Per-transaction + percentage
4. Generate net settlement amount per currency

### Payout Execution
1. Submit ACH credit to merchant's bank account
2. Apply settlement delay (T+1 default, configurable)
3. Monitor ACH return codes (R01-R99)
4. Handle NSF or account-closed scenarios

## Refund Processing

### Refund Windows
- **Pre-settlement void**: No interchange cost, instant
- **Post-settlement refund**: Interchange not refunded by networks (except Visa)
- **Late refund / credit**: Beyond 120 days, processed as a new credit transaction
- **Partial refund**: Multiple partial refunds allowed up to original amount

### Refund Routing
1. Check if original transaction is pre-settlement → void instead
2. Route refund to original processor
3. Credit original payment method
4. For closed accounts: check with issuer for forwarding

## Error Handling

### Network Timeouts
1. If no response within 30 seconds, mark as `pending`
2. Send reversal/void to prevent duplicate charges
3. Re-query processor for definitive status
4. **Never** assume approval on timeout

### Decline Recovery
1. Map decline code to actionable category:
   - `insufficient_funds` → suggest retry with lower amount
   - `do_not_honor` → suggest alternate payment method
   - `card_expired` → prompt for updated card
   - `fraud_suspected` → do NOT retry, flag for review
2. Apply smart retry logic (not for fraud declines)

## Compliance Requirements

### PCI DSS
- Never log full PAN, CVV, or track data
- Use tokenization for all stored payment methods
- Encrypt cardholder data in transit (TLS 1.2+) and at rest (AES-256)

### Network Rules
- Visa: Must attempt auth reversal for voided auths within 24 hours
- MC: Must provide auth code with every capture
- Amex: OptBlue vs direct — different settlement flows

## Monitoring & Alerts

### Key Metrics
- Authorization approval rate (target: >85% for cards)
- Average authorization latency (<500ms)
- Settlement success rate (target: >99.5%)
- Refund processing time (<24 hours)
- Chargeback ratio per merchant (alert at >0.65%, critical at >0.9%)

### Alerting Thresholds
- Approval rate drop >5% in 1 hour → P1 alert
- Settlement failure → P1 alert
- Processor timeout rate >2% → P2 alert
- Single merchant chargeback spike → P2 alert
