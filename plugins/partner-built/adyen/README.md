# Adyen Connector

Partner-built integration for Adyen's omnichannel payment platform.

## Capabilities

- **Online Payments**: Web and mobile checkout via Drop-in or Components
- **Point of Sale**: In-person terminal payments
- **Platforms**: Marketplace and platform payments (Adyen for Platforms)
- **Issuing**: Card issuing and management
- **Revenue optimization**: Dynamic 3DS, account updater, network tokens

## MCP Server

Connects to Adyen's MCP endpoint for tool-based access to the Adyen API.

## Authentication

Requires `ADYEN_API_KEY` and `ADYEN_MERCHANT_ACCOUNT` environment variables.

## Skills

- `adyen-checkout`: Online payment flow management
- `adyen-platforms`: Marketplace split payments and payouts
