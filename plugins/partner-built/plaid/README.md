# Plaid Connector

Partner-built integration for Plaid's financial data platform.

## Capabilities

- **Account Linking**: Connect bank accounts via Plaid Link
- **Identity Verification**: IDV with document and selfie verification
- **Transactions**: Categorized transaction history
- **Balance**: Real-time account balance checks
- **Income**: Income and employment verification
- **Assets**: Asset reports for underwriting
- **Transfer**: ACH transfers via Plaid Transfer

## MCP Server

Connects to Plaid's MCP endpoint for tool-based access to the Plaid API.

## Authentication

Requires `PLAID_CLIENT_ID` and `PLAID_SECRET` environment variables.

## Skills

- `plaid-link`: Account connection and verification workflows
- `plaid-data`: Transaction, balance, and identity data retrieval
