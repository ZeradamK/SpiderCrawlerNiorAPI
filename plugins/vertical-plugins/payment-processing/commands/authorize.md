---
description: Authorize a payment transaction against a payment method
argument-hint: "[amount] [currency] [payment_method]"
---

# Authorize Payment Command

## Workflow

### Step 1: Gather Transaction Details
If amount, currency, and payment method are provided, use them. Otherwise, ask the user for:
- **Amount** (in smallest currency unit, e.g., cents)
- **Currency** (ISO 4217, e.g., USD, EUR, GBP)
- **Payment method** (card token, ACH details, or wallet ID)

### Step 2: Risk Assessment
Before submitting to the network:
1. Run velocity checks (hourly/daily transaction count and volume)
2. Check device fingerprint and IP geolocation
3. Evaluate fraud rules engine
4. If risk score > 75, flag for manual review and **STOP**

### Step 3: 3-D Secure Check
For card transactions over the configured threshold:
1. Determine if 3DS is required (SCA mandate, issuer preference)
2. If required, initiate 3DS challenge flow
3. Record ECI and authentication status

### Step 4: Network Authorization
1. Route to the optimal processor based on card brand, region, and cost
2. Submit authorization request with AVS and CVV data
3. Parse network response (auth code, AVS result, CVV result)

### Step 5: Record Result
1. Create transaction record with status `authorized` or `declined`
2. Store network response details for settlement reference
3. Set authorization expiry (typically 7 days for cards)
4. Return transaction ID and authorization details to user

## Output Format
```
Transaction ID: txn_xxx
Status: authorized | declined
Auth Code: XXXXXX
Amount: $XX.XX USD
Risk Score: XX/100
AVS: Y | N | U
CVV: M | N | U
```
