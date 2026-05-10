# Transaction Processor — Managed Agent Cookbook

## Security Tier: Standard

This agent processes payment transactions end-to-end. It has read access to transaction data and delegates write operations to specialized subagents.

## Subagent Architecture

```
transaction-processor (orchestrator)
├── authorizer (read-only)
│   └── Skills: transaction-lifecycle, payment-routing, fraud-scoring
├── capturer (read + write)
│   └── Skills: transaction-lifecycle
└── settler (read + write)
    └── Skills: batch-processing, interchange-optimization
```

## Tool Grant Breakdown

| Subagent | Read | Write | Edit | Grep | Bash |
|----------|------|-------|------|------|------|
| authorizer | yes | no | no | yes | no |
| capturer | yes | yes | yes | no | no |
| settler | yes | yes | yes | no | no |

## MCP Servers Required

| Server | Environment Variable | Purpose |
|--------|---------------------|---------|
| Stripe | `STRIPE_MCP_URL` | Card processing |
| Adyen | `ADYEN_MCP_URL` | Alternative processor |
| Visa Direct | `VISA_MCP_URL` | Direct push payments |

## Handoff Patterns

- **Inbound**: Receives transaction requests from external systems
- **Outbound**: Hands off to `fraud-analyzer` (risk), `chargeback-handler` (disputes), `settlement-agent` (FX)

## Deployment

```bash
export STRIPE_MCP_URL=...
export ADYEN_MCP_URL=...
export VISA_MCP_URL=...
scripts/deploy-managed-agent.sh transaction-processor
```
