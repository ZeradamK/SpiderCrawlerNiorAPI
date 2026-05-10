# Compliance Screener — Managed Agent Cookbook

## Security Tier: High

This agent handles sensitive KYC/AML screening. All operations are logged for regulatory audit.

## Subagent Architecture

```
compliance-screener (orchestrator)
├── doc-parser (read-only)
│   └── Skills: kyc-verification
├── rules-engine (read-only)
│   └── Skills: aml-screening
└── escalator (read + write)
    └── Skills: regulatory-reporting
```

## CRITICAL COMPLIANCE NOTES

- **NEVER disclose SAR filing status to subjects** — This is a federal crime under 31 USC 5318(g)(2)
- All screening results are retained for 5 years
- Enhanced due diligence applies to high-risk geographies and PEP matches
- Conservative matching: flag potential matches for human review

## Deployment

```bash
export COMPLYADVANTAGE_MCP_URL=...
export JUMIO_MCP_URL=...
scripts/deploy-managed-agent.sh compliance-screener
```
