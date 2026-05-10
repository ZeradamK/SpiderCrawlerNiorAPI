# Eris — Payment as a Service

> A modular, plugin-based payment processing platform built on Claude's agent architecture. Eris provides end-to-end payment workflows through composable agents, vertical plugins, and managed agent cookbooks.

## Architecture

Eris follows a "write once, deploy two ways" pattern — the same system prompts and skills ship both as **Cowork plugins** (interactive UI) and **Claude Managed Agents** (headless API-driven deployment).

## Repository Structure

```
├── plugins/
│   ├── agent-plugins/               # Named agents — one self-contained plugin each
│   │   └── <slug>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── agents/<slug>.md     # Canonical system prompt
│   │       └── skills/              # Bundled copies, synced from vertical-plugins/
│   ├── vertical-plugins/            # Payment verticals — skill sources, commands, MCPs
│   │   └── <vertical>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── commands/
│   │       ├── skills/
│   │       └── .mcp.json
│   └── partner-built/               # Partner integrations (Stripe, Adyen, Plaid)
├── managed-agent-cookbooks/         # CMA cookbooks (one dir per named agent)
│   └── <slug>/
│       ├── agent.yaml               # System + skills references
│       ├── subagents/*.yaml         # Depth-1 leaf workers
│       ├── steering-examples.json
│       └── README.md
├── sdk/                             # Eris SDK — client libraries and API wrappers
├── schemas/                         # JSON schemas for payment objects
└── scripts/                         # Deployment, validation, and sync tooling
```

## Payment Verticals

| Vertical | Description |
|----------|-------------|
| **payment-processing** | Core transaction lifecycle — authorization, capture, settlement, refunds |
| **fraud-detection** | Real-time scoring, rule engines, ML model integration, case management |
| **compliance-aml** | KYC/AML screening, sanctions checks, SAR filing, regulatory reporting |
| **merchant-services** | Onboarding, underwriting, MCC classification, fee management |
| **treasury-management** | Cash positioning, FX hedging, liquidity forecasting, bank connectivity |
| **settlement-clearing** | Batch settlement, interchange optimization, network reconciliation |
| **digital-wallets** | Tokenization, wallet lifecycle, P2P transfers, stored value |

## Named Agents

| Agent | Purpose | Subagents |
|-------|---------|-----------|
| **transaction-processor** | End-to-end payment orchestration | authorizer, capturer, settler |
| **fraud-analyzer** | Real-time fraud scoring and case review | scorer, investigator, reporter |
| **chargeback-handler** | Dispute lifecycle management | intake-reader, evidence-builder, resolver |
| **merchant-onboarder** | Merchant application processing | doc-reader, underwriter, provisioner |
| **compliance-screener** | AML/KYC screening workflows | doc-parser, rules-engine, escalator |
| **settlement-agent** | Batch settlement orchestration | aggregator, netter, poster |
| **reconciliation-agent** | Cross-system reconciliation | matcher, break-finder, resolver |
| **risk-assessor** | Transaction and portfolio risk scoring | data-puller, modeler, reporter |
| **payment-router** | Intelligent payment routing | analyzer, optimizer, executor |
| **dispute-resolver** | End-to-end dispute resolution | intake, investigator, decision-maker |

## Development Workflow

1. Edit skills in `vertical-plugins/`, then run `python3 scripts/sync-agent-skills.py` to propagate
2. Run `python3 scripts/check.py` before committing — validates manifests, file references, skill drift
3. Test commands with `/plugin:command-name` syntax
4. Deploy managed agents with `scripts/deploy-managed-agent.sh <agent-slug>`

## Security

- All agent prompts embed guardrails: no external communications, cite every data point, surface for review at checkpoints
- Tool grants are segmented: only writer subagents get `Write`; readers get `Read` + `Grep`
- MCP servers require user consent on first connect
- Environment variables validated before API substitution

## License

Apache 2.0 — See [LICENSE](LICENSE) for details.
