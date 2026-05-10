#!/usr/bin/env bash
set -euo pipefail

# Deploy a managed agent to the Anthropic Agents API.
#
# Usage:
#   export ANTHROPIC_API_KEY=sk-ant-...
#   scripts/deploy-managed-agent.sh <agent-slug> [--dry-run]
#
# Required environment:
#   ANTHROPIC_API_KEY — API key for the Anthropic Agents API
#   Plus any MCP server URLs referenced in the agent manifest (e.g., STRIPE_MCP_URL)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
COOKBOOKS_DIR="$ROOT_DIR/managed-agent-cookbooks"

SLUG="${1:?Usage: deploy-managed-agent.sh <agent-slug> [--dry-run]}"
DRY_RUN="${2:-}"

AGENT_DIR="$COOKBOOKS_DIR/$SLUG"
AGENT_YAML="$AGENT_DIR/agent.yaml"

if [[ ! -f "$AGENT_YAML" ]]; then
    echo "ERROR: agent.yaml not found at $AGENT_YAML" >&2
    exit 1
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" && "$DRY_RUN" != "--dry-run" ]]; then
    echo "ERROR: ANTHROPIC_API_KEY not set" >&2
    exit 1
fi

# Validate environment variables in the manifest don't contain unsafe characters
SAFE='^[A-Za-z0-9._/:@=-]*$'
validate_env_var() {
    local name="$1"
    local value="${!name:-}"
    if [[ -n "$value" && ! "$value" =~ $SAFE ]]; then
        echo "ERROR: Environment variable $name contains unsafe characters" >&2
        exit 1
    fi
}

echo "=== Eris Managed Agent Deployment ==="
echo "Agent:    $SLUG"
echo "Manifest: $AGENT_YAML"
echo "Mode:     ${DRY_RUN:-live}"
echo ""

# Parse the agent manifest
echo "Parsing agent manifest ..."
AGENT_JSON=$(python3 -c "
import yaml, json, sys
with open('$AGENT_YAML') as f:
    data = yaml.safe_load(f)
json.dump(data, sys.stdout, indent=2)
")

# Resolve system.file to inline text
SYSTEM_FILE=$(echo "$AGENT_JSON" | python3 -c "
import json, sys
data = json.load(sys.stdin)
s = data.get('system', {})
if isinstance(s, dict) and 'file' in s:
    print(s['file'])
" 2>/dev/null || true)

if [[ -n "$SYSTEM_FILE" ]]; then
    RESOLVED_PATH="$AGENT_DIR/$SYSTEM_FILE"
    if [[ ! -f "$RESOLVED_PATH" ]]; then
        echo "ERROR: system.file '$SYSTEM_FILE' resolves to non-existent path: $RESOLVED_PATH" >&2
        exit 1
    fi
    echo "  Resolved system prompt: $RESOLVED_PATH"
fi

# Resolve subagent manifests
echo "Resolving subagents ..."
SUBAGENTS=$(echo "$AGENT_JSON" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for agent in data.get('callable_agents', []):
    if 'manifest' in agent:
        print(agent['manifest'])
" 2>/dev/null || true)

for sub in $SUBAGENTS; do
    SUB_PATH="$AGENT_DIR/$sub"
    if [[ ! -f "$SUB_PATH" ]]; then
        echo "  ERROR: subagent manifest '$sub' not found at $SUB_PATH" >&2
        exit 1
    fi
    echo "  Found subagent: $sub"
done

# Validate MCP server environment variables
echo "Validating MCP server URLs ..."
MCP_VARS=$(echo "$AGENT_JSON" | python3 -c "
import json, sys, re
data = json.load(sys.stdin)
text = json.dumps(data)
for match in re.findall(r'\\\$\{(\w+)\}', text):
    print(match)
" 2>/dev/null || true)

for var in $MCP_VARS; do
    validate_env_var "$var"
    if [[ -n "${!var:-}" ]]; then
        echo "  $var = [set]"
    else
        echo "  WARNING: $var is not set"
    fi
done

if [[ "$DRY_RUN" == "--dry-run" ]]; then
    echo ""
    echo "=== DRY RUN — would deploy: ==="
    echo "$AGENT_JSON"
    echo ""
    echo "Dry run complete. No API calls made."
    exit 0
fi

echo ""
echo "=== Deploying to Anthropic Agents API ==="
echo "TODO: Implement actual API deployment"
echo "  POST /v1/agents with resolved manifest"
echo ""
echo "Deployment script ready for production integration."
