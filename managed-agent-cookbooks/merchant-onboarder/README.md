# Merchant Onboarder — Managed Agent Cookbook

## Security Tier: Standard

Processes merchant applications from intake through provisioning.

## Subagent Architecture

```
merchant-onboarder (orchestrator)
├── doc-reader (read-only)
├── underwriter (read-only)
└── provisioner (read + write)
```

## Deployment

```bash
export MIDDESK_MCP_URL=...
scripts/deploy-managed-agent.sh merchant-onboarder
```
