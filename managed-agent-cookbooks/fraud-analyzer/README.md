# Fraud Analyzer — Managed Agent Cookbook

## Security Tier: Elevated

This agent scores transactions for fraud risk and investigates flagged activity. It has read access to transaction and customer data, with write access restricted to the reporter subagent for generating reports.

## Subagent Architecture

```
fraud-analyzer (orchestrator)
├── scorer (read-only)
│   └── Skills: fraud-scoring, velocity-monitoring
├── investigator (read-only)
│   └── Skills: fraud-scoring, device-fingerprinting, case-management
└── reporter (read + write)
    └── Skills: case-management
```

## Tool Grant Breakdown

| Subagent | Read | Write | Edit | Grep | Bash |
|----------|------|-------|------|------|------|
| scorer | yes | no | no | yes | no |
| investigator | yes | no | no | yes | no |
| reporter | yes | yes | yes | no | no |

## MCP Servers Required

| Server | Environment Variable | Purpose |
|--------|---------------------|---------|
| Sift | `SIFT_MCP_URL` | Third-party fraud signals |
| Sardine | `SARDINE_MCP_URL` | Device intelligence |

## Deployment

```bash
export SIFT_MCP_URL=...
export SARDINE_MCP_URL=...
scripts/deploy-managed-agent.sh fraud-analyzer
```
