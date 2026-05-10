# Reconciliation Agent — Managed Agent Cookbook

## Security Tier: Standard

Cross-system reconciliation between internal records, processor data, and bank statements.

## Subagent Architecture

```
reconciliation-agent (orchestrator)
├── matcher (read-only)
├── break-finder (read-only)
└── resolver (read + write)
```

## Deployment

```bash
export STRIPE_MCP_URL=...
export PLAID_MCP_URL=...
scripts/deploy-managed-agent.sh reconciliation-agent
```
