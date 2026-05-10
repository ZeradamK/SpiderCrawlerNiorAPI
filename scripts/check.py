#!/usr/bin/env python3
"""Validate Eris manifests, file references, and skill drift.

Run before committing:
    python3 scripts/check.py

Exit 0 if clean, 1 if errors found.
"""

import json
import os
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []


def error(msg: str) -> None:
    ERRORS.append(msg)
    print(f"  ERROR: {msg}", file=sys.stderr)


def check_json(path: Path) -> dict | None:
    try:
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        error(f"{path}: invalid JSON — {e}")
        return None


def check_yaml(path: Path) -> dict | None:
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        error(f"{path}: invalid YAML — {e}")
        return None


def check_frontmatter(path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    text = path.read_text()
    if not text.startswith("---"):
        error(f"{path}: missing YAML frontmatter")
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        error(f"{path}: malformed YAML frontmatter")
        return None
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        error(f"{path}: invalid frontmatter YAML — {e}")
        return None
    if not isinstance(fm, dict):
        error(f"{path}: frontmatter is not a mapping")
        return None
    if "name" not in fm:
        error(f"{path}: frontmatter missing 'name'")
    if "description" not in fm:
        error(f"{path}: frontmatter missing 'description'")
    return fm


def check_marketplace() -> None:
    """Validate marketplace.json and source paths."""
    print("Checking marketplace.json ...")
    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp_path.exists():
        error("marketplace.json not found")
        return
    mp = check_json(mp_path)
    if mp is None:
        return
    for plugin in mp.get("plugins", []):
        src = plugin.get("source", "")
        resolved = (ROOT / src).resolve()
        if not resolved.exists():
            error(f"marketplace.json: source path '{src}' does not exist")


def check_plugin_jsons() -> None:
    """Validate all plugin.json files."""
    print("Checking plugin.json files ...")
    for pj in ROOT.rglob("plugin.json"):
        if ".claude-plugin" not in str(pj):
            continue
        data = check_json(pj)
        if data and "name" not in data:
            error(f"{pj}: missing 'name'")


def check_agent_markdowns() -> None:
    """Validate agent system prompt frontmatter."""
    print("Checking agent markdown frontmatter ...")
    agents_dir = ROOT / "plugins" / "agent-plugins"
    if not agents_dir.exists():
        return
    for md in agents_dir.rglob("*.md"):
        if md.parent.name == "agents":
            check_frontmatter(md)


def check_skill_markdowns() -> None:
    """Validate skill SKILL.md frontmatter."""
    print("Checking skill SKILL.md frontmatter ...")
    for skill_md in ROOT.rglob("SKILL.md"):
        check_frontmatter(skill_md)


def check_cookbook_yamls() -> None:
    """Validate managed-agent-cookbook YAML files and their references."""
    print("Checking cookbook YAML files ...")
    cookbooks = ROOT / "managed-agent-cookbooks"
    if not cookbooks.exists():
        return
    for yf in cookbooks.rglob("*.yaml"):
        data = check_yaml(yf)
        if data is None:
            continue

        # Check system.file references
        system = data.get("system", {})
        if isinstance(system, dict) and "file" in system:
            ref = system["file"]
            resolved = (yf.parent / ref).resolve()
            if not resolved.exists():
                error(f"{yf}: system.file '{ref}' does not exist")

        # Check skills.path references
        for skill in data.get("skills", []):
            if isinstance(skill, dict) and "path" in skill:
                ref = skill["path"]
                resolved = (yf.parent / ref).resolve()
                if not resolved.exists():
                    error(f"{yf}: skills.path '{ref}' does not exist")

        # Check callable_agents.manifest references
        for agent in data.get("callable_agents", []):
            if isinstance(agent, dict) and "manifest" in agent:
                ref = agent["manifest"]
                resolved = (yf.parent / ref).resolve()
                if not resolved.exists():
                    error(f"{yf}: callable_agents.manifest '{ref}' does not exist")


def check_steering_examples() -> None:
    """Validate steering-examples.json files."""
    print("Checking steering-examples.json files ...")
    for se in ROOT.rglob("steering-examples.json"):
        data = check_json(se)
        if data is not None and not isinstance(data, list):
            error(f"{se}: expected a JSON array")


def check_skill_drift() -> None:
    """Check that bundled skills in agent-plugins match vertical-plugins sources."""
    print("Checking for skill drift ...")
    vertical_skills: dict[str, Path] = {}

    # Index all vertical skills
    verticals = ROOT / "plugins" / "vertical-plugins"
    if verticals.exists():
        for skill_dir in verticals.rglob("skills/*"):
            if skill_dir.is_dir():
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    vertical_skills[skill_dir.name] = skill_md

    # Check bundled skills match
    agents = ROOT / "plugins" / "agent-plugins"
    if not agents.exists():
        return
    for skill_dir in agents.rglob("skills/*"):
        if not skill_dir.is_dir():
            continue
        bundled_md = skill_dir / "SKILL.md"
        if not bundled_md.exists():
            continue
        if skill_dir.name in vertical_skills:
            source = vertical_skills[skill_dir.name]
            if bundled_md.read_text() != source.read_text():
                error(
                    f"Skill drift: {skill_dir} differs from {source}. "
                    f"Run: python3 scripts/sync-agent-skills.py"
                )


def main() -> int:
    print(f"Eris check.py — validating from {ROOT}\n")

    check_marketplace()
    check_plugin_jsons()
    check_agent_markdowns()
    check_skill_markdowns()
    check_cookbook_yamls()
    check_steering_examples()
    check_skill_drift()

    print()
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} error(s) found", file=sys.stderr)
        return 1
    else:
        print("PASSED: all checks clean")
        return 0


if __name__ == "__main__":
    sys.exit(main())
