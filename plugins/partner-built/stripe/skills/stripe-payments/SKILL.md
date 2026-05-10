---
name: stripe-payments
description: |
  Core Stripe payment operations — PaymentIntents, charges, refunds, and payment methods.
  Perfect for: Stripe-specific payment workflows, migration guidance, API usage.
---

# Stripe Payments

## Payment Flow

### PaymentIntent Lifecycle
```
create → requires_payment_method → requires_confirmation → requires_action → processing → succeeded
                                                                                          │
                                                                                     requires_capture
                                                                                          │
                                                                                       captured
```

### Key Operations

**Create PaymentIntent**:
- Amount (cents), currency, payment method types
- Capture method: `automatic` (default) or `manual` (auth-only)
- Metadata for your reference

**Confirm PaymentIntent**:
- Attach payment method and confirm in one step
- Handle `requires_action` for 3DS/SCA

**Capture**:
- For `capture_method: manual` — capture within 7 days
- Partial capture supported

**Refund**:
- Full or partial refund via Refund object
- Reason: `duplicate`, `fraudulent`, `requested_by_customer`

## Best Practices
- Use PaymentIntents (not Charges API) for all new integrations
- Always handle `requires_action` for SCA compliance
- Use idempotency keys for all create/update operations
- Store PaymentIntent ID (not charge ID) as your reference
- Use webhooks for async status updates (don't poll)
