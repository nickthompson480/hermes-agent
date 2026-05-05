#!/usr/bin/env python3
"""
mission_create.py — Create a new mission file from the template.

Usage:
    python3 .agent/scripts/mission_create.py --id MISSION-001 --name "scaffold-api" --title "Scaffold REST API"
    python3 .agent/scripts/mission_create.py --id MISSION-001 --name "scaffold-api" --title "Scaffold REST API" --workstreams WS-001 WS-002
"""

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AGENT_DIR = PROJECT_ROOT / ".agent"
TEMPLATE = AGENT_DIR / "missions" / "_template" / "MISSION.md"
MISSIONS_DIR = AGENT_DIR / "missions"
INDEX_PATH = MISSIONS_DIR / "INDEX.md"


def update_placeholder(path: Path, replacements: dict):
    text = path.read_text()
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description="Create a new mission file")
    parser.add_argument("--id", required=True, help="Mission ID e.g. MISSION-001")
    parser.add_argument("--name", required=True, help="Short slug e.g. scaffold-api")
    parser.add_argument("--title", required=True, help="Human-readable title")
    parser.add_argument("--workstreams", nargs="*", default=[], help="Target WS IDs")
    parser.add_argument("--base-branch", default="main", help="Branch to fork from (default: main)")
    args = parser.parse_args()

    mission_id = args.id.upper()
    num = mission_id.replace("MISSION-", "").zfill(3)
    branch_name = f"mission/{num}-{args.name}"
    today = date.today().isoformat()
    filename = f"{mission_id}-{args.name}.md"
    dest = MISSIONS_DIR / filename

    if dest.exists():
        print(f"❌  Mission file already exists: {dest}")
        sys.exit(1)

    shutil.copy(TEMPLATE, dest)

    ws_yaml = "\n".join(f"  - {ws}" for ws in args.workstreams) if args.workstreams else "  - WS-001"

    update_placeholder(dest, {
        "MISSION-001": mission_id,
        "[Mission Title]": args.title,
        "mission/001-short-name": branch_name,
        "workstreams:\n  - WS-001": f"workstreams:\n{ws_yaml}",
        "base_branch: main": f"base_branch: {args.base_branch}",
        "YYYY-MM-DD": today,
        "> **Status:** Draft | **Workstreams:** WS-001 | **Branch:** `mission/001-name`":
            f"> **Status:** Draft | **Workstreams:** {', '.join(args.workstreams) or 'WS-001'} | **Branch:** `{branch_name}`",
    })

    print(f"✅  Mission file created: {dest.relative_to(PROJECT_ROOT)}")
    print(f"   Branch (when approved): git checkout -b {branch_name}")
    print(f"\n⚠️   Next steps:")
    print(f"    1. Fill in Objective, Scope, Pre-conditions, Task Breakdown")
    print(f"    2. Add to missions/INDEX.md")
    print(f"    3. Add mission ID to relevant workstream frontmatter (missions: field)")
    print(f"    4. Submit to Opus for review (SOP-004 Phase 2)\n")


if __name__ == "__main__":
    main()
