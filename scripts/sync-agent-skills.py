#!/usr/bin/env python3
"""Sync bundled skills from vertical-plugins into agent-plugins.

Usage:
    python3 scripts/sync-agent-skills.py

Skills are authored in vertical-plugins/ and vendored (copied) into each
agent-plugin's skills/ directory. This script propagates changes from the
canonical vertical source into all agent bundles.
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERTICALS = ROOT / "plugins" / "vertical-plugins"
AGENTS = ROOT / "plugins" / "agent-plugins"


def index_vertical_skills() -> dict[str, Path]:
    """Build name→path index of all vertical skills."""
    skills: dict[str, Path] = {}
    if not VERTICALS.exists():
        return skills
    for skill_dir in VERTICALS.rglob("skills/*"):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            skills[skill_dir.name] = skill_dir
    return skills


def sync() -> int:
    """Sync all bundled skills from their vertical sources."""
    vertical_skills = index_vertical_skills()
    print(f"Indexed {len(vertical_skills)} vertical skills\n")

    synced = 0
    errors = 0

    if not AGENTS.exists():
        print("No agent-plugins directory found")
        return 0

    for agent_dir in sorted(AGENTS.iterdir()):
        if not agent_dir.is_dir():
            continue
        skills_dir = agent_dir / "skills"
        if not skills_dir.exists():
            continue

        for bundled_skill in sorted(skills_dir.iterdir()):
            if not bundled_skill.is_dir():
                continue
            name = bundled_skill.name
            if name not in vertical_skills:
                print(f"  WARNING: {bundled_skill} has no vertical source")
                errors += 1
                continue

            source = vertical_skills[name]
            # Delete and re-copy from source
            shutil.rmtree(bundled_skill)
            shutil.copytree(source, bundled_skill)
            synced += 1
            print(f"  Synced: {agent_dir.name}/skills/{name} ← {source.relative_to(ROOT)}")

    print(f"\nSynced {synced} skill(s), {errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(sync())
