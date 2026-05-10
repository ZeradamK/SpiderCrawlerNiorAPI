#!/usr/bin/env python3
"""Reference orchestrator for cross-agent handoff events.

This script demonstrates how to manage handoff_request events between
managed agents in the Eris platform. It parses agent output for structured
handoff requests and routes them to the appropriate target agent.

Usage:
    python3 scripts/orchestrate.py

This is a reference implementation — adapt for your production event loop.
"""

import json
import re
import sys
from typing import Any

# Allowlisted agent targets for handoff routing
ALLOWED_TARGETS = {
    "transaction-processor",
    "fraud-analyzer",
    "chargeback-handler",
    "merchant-onboarder",
    "compliance-screener",
    "settlement-agent",
    "reconciliation-agent",
    "risk-assessor",
    "payment-router",
    "dispute-resolver",
}

# Schema for validating handoff payloads
HANDOFF_PAYLOAD_SCHEMA = {
    "type": "object",
    "required": ["event"],
    "properties": {
        "event": {"type": "string", "maxLength": 10000},
        "context": {"type": "object"},
        "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
    },
}

# Compile pattern for extracting handoff requests from agent output
# Use non-greedy match with length cap to prevent ReDoS on adversarial input
HANDOFF_RE = re.compile(
    r'\{"type":\s*"handoff_request"[^}]{0,5000}\}',
    re.DOTALL,
)


def extract_handoff(text: str) -> dict[str, Any] | None:
    """Extract and validate a handoff request from agent output text.

    Returns sanitized handoff dict or None if no valid handoff found.
    """
    if len(text) > 100_000:
        # Cap input length to prevent excessive regex scanning
        text = text[:100_000]

    match = HANDOFF_RE.search(text)
    if not match:
        return None

    try:
        blob = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

    if blob.get("type") != "handoff_request":
        return None

    target = blob.get("target_agent")
    if target not in ALLOWED_TARGETS:
        print(f"WARNING: Handoff to unknown target '{target}' — blocked", file=sys.stderr)
        return None

    payload = blob.get("payload", {})
    if not isinstance(payload, dict):
        return None
    if "event" not in payload:
        return None
    if len(str(payload.get("event", ""))) > 10000:
        print("WARNING: Handoff payload event exceeds max length — truncating", file=sys.stderr)
        payload["event"] = str(payload["event"])[:10000]

    return {
        "type": "handoff_request",
        "target_agent": target,
        "payload": payload,
    }


def route_handoff(handoff: dict[str, Any]) -> None:
    """Route a validated handoff to the target agent.

    In production, this would call:
        client.beta.agents.sessions.steer(
            agent_id=resolve_agent_id(handoff["target_agent"]),
            input=handoff["payload"]["event"],
        )
    """
    target = handoff["target_agent"]
    event = handoff["payload"]["event"]
    priority = handoff["payload"].get("priority", "medium")

    print(f"Routing handoff to {target} (priority: {priority})")
    print(f"  Event: {event[:200]}{'...' if len(event) > 200 else ''}")


def main() -> None:
    """Reference event loop — reads from stdin in production."""
    print("Eris Orchestrator — reference implementation")
    print(f"Allowed targets: {', '.join(sorted(ALLOWED_TARGETS))}")
    print()

    # Example: process a sample handoff
    sample_output = '''
    Based on my analysis, this transaction shows signs of account takeover.
    {"type": "handoff_request", "target_agent": "fraud-analyzer", "payload": {"event": "Investigate potential ATO on customer cust_12345. New device, password changed 10 minutes before $3,200 purchase.", "priority": "high"}}
    '''

    handoff = extract_handoff(sample_output)
    if handoff:
        route_handoff(handoff)
    else:
        print("No valid handoff found in sample output")


if __name__ == "__main__":
    main()
