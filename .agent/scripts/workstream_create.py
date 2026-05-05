#!/usr/bin/env python3
"""
workstream_create.py — Create a new workstream in this project (SOP-001 automated).

Usage:
    python3 .agent/scripts/workstream_create.py --id WS-002 --name "auth-flow" --title "User Authentication"
    python3 .agent/scripts/workstream_create.py --id WS-002 --name "auth-flow" --title "User Authentication" --owner "Nick Thompson"
"""

import argparse
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AGENT_DIR = PROJECT_ROOT / ".agent"
TEMPLATE = AGENT_DIR / "workstreams" / "_template" / "WORKSTREAM.md"
WORKSTREAMS_DIR = AGENT_DIR / "workstreams"
INDEX_PATH = WORKSTREAMS_DIR / "INDEX.md"


def update_placeholder(path: Path, replacements: dict):
    text = path.read_text()
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description="Create a new workstream")
    parser.add_argument("--id", required=True, help="Workstream ID e.g. WS-002")
    parser.add_argument("--name", required=True, help="Short slug e.g. auth-flow")
    parser.add_argument("--title", required=True, help="Human-readable title")
    parser.add_argument("--owner", default="", help="Owner name")
    parser.add_argument("--spec-section", default="", help="Related PROJECT_SPEC section")
    args = parser.parse_args()

    ws_id = args.id.upper()
    ws_dir = WORKSTREAMS_DIR / f"{ws_id}-{args.name}"
    branch_name = f"ws/{ws_id.replace('WS-', '').zfill(3)}-{args.name}"
    today = date.today().isoformat()

    if ws_dir.exists():
        print(f"❌  Workstream folder already exists: {ws_dir}")
        sys.exit(1)

    # Create folder structure
    (ws_dir / "tasks").mkdir(parents=True)
    (ws_dir / "decisions").mkdir(parents=True)
    (ws_dir / "docs").mkdir(parents=True)

    # Copy and fill template
    dest = ws_dir / "WORKSTREAM.md"
    shutil.copy(TEMPLATE, dest)
    update_placeholder(dest, {
        "WS-XXX": ws_id,
        "[Workstream Name]": args.title,
        "ws/XXX-short-name": branch_name,
        'owner: ""': f'owner: "{args.owner}"',
        'parent_spec_section: ""': f'parent_spec_section: "{args.spec_section}"',
        "YYYY-MM-DD": today,
    })

    # Keep empty dirs tracked in git
    for subdir in ["tasks", "decisions", "docs"]:
        (ws_dir / subdir / ".gitkeep").touch()

    print(f"✅  Workstream created: {ws_dir}")
    print(f"\n⚠️   Manual steps remaining:")
    print(f"    1. Add WS to workstreams/INDEX.md")
    print(f"    2. Add WS to PROJECT_SPEC.md workstreams table")
    print(f"    3. Add WS to CONTEXT.md active workstreams table")
    print(f"    4. Create branch:  git checkout -b {branch_name}")
    print(f"    5. Post to Discord with WS ID and purpose\n")


if __name__ == "__main__":
    main()
