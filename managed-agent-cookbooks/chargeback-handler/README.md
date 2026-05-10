# Chargeback Handler — Managed Agent Cookbook

## Security Tier: Standard

Manages the complete chargeback lifecycle from intake through resolution.

## Subagent Architecture

```
chargeback-handler (orchestrator)
├── intake-reader (read-only)
├── evidence-builder (read + write)
└── resolver (read + write)
```

## Deployment

```bash
export STRIPE_MCP_URL=...
scripts/deploy-managed-agent.sh chargeback-handler
```
