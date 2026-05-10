# Risk Assessor — Managed Agent Cookbook

## Security Tier: Standard

Transaction and portfolio risk scoring with limit recommendations.

## Subagent Architecture

```
risk-assessor (orchestrator)
├── data-puller (read-only)
├── modeler (read-only)
└── reporter (read + write)
```

## Deployment

```bash
export SIFT_MCP_URL=...
export MIDDESK_MCP_URL=...
scripts/deploy-managed-agent.sh risk-assessor
```
