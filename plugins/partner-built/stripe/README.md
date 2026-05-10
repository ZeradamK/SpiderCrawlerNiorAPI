# Stripe Connector

Partner-built integration for Stripe's payment processing platform.

## Capabilities

- **Charges**: Create, capture, refund card payments
- **Subscriptions**: Manage recurring billing with Stripe Billing
- **Payouts**: Initiate payouts to connected accounts
- **Connect**: Multi-party payments, marketplace payouts
- **Disputes**: Manage chargebacks and evidence submission
- **Balance**: Real-time balance and transaction reporting

## MCP Server

Connects to Stripe's MCP endpoint for tool-based access to the Stripe API.

## Authentication

Requires `STRIPE_API_KEY` environment variable set to a valid Stripe secret key.

## Skills

- `stripe-payments`: Core payment operations via Stripe API
- `stripe-connect`: Marketplace and platform payment workflows
- `stripe-billing`: Subscription and invoice management
