# Settlement Agent — Managed Agent Cookbook

## Security Tier: High

Handles batch settlement with write access for payout execution.

## Subagent Architecture

```
settlement-agent (orchestrator)
├── aggregator (read-only)
├── netter (read-only)
└── poster (read + write)
```

## Deployment

```bash
export MODERN_TREASURY_MCP_URL=...
scripts/deploy-managed-agent.sh settlement-agent
```
