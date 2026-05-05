#!/usr/bin/env python3
"""
session_init.py — Two-phase project session management.

Phase 1 — scaffold: creates a timestamped session file with git context pre-populated.
Phase 2 — finalize: commits .agent/ changes and verifies the repo is clean.

Usage:
    # Phase 1 — run at the start of a session (or just before wrapping)
    python3 .agent/scripts/session_init.py --description "implement auth middleware"
    python3 .agent/scripts/session_init.py --description "scaffold API" --workstreams WS-001 WS-002
    python3 .agent/scripts/session_init.py --description "run MISSION-001" --mission MISSION-001

    # Phase 2 — run after filling in the session file
    python3 .agent/scripts/session_init.py --description "implement auth middleware" --finalize
"""

import argparse
import subprocess
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AGENT_DIR = PROJECT_ROOT / ".agent"
TEMPLATE = AGENT_DIR / "sessions" / "_template" / "SESSION.md"
SESSIONS_DIR = AGENT_DIR / "sessions"
INDEX_PATH = SESSIONS_DIR / "INDEX.md"


def git(cmd: list, cwd=PROJECT_ROOT) -> str:
    try:
        return subprocess.check_output(cmd, cwd=cwd, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ""


def check_dirty() -> str:
    """Return porcelain status string, empty if clean."""
    return git(["git", "status", "--porcelain"])


def scaffold(description: str, workstreams: list, mission: str):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M%S")
    slug = description.lower().replace(" ", "-")[:50]
    filename = f"{timestamp}-{slug}.md"
    dest = SESSIONS_DIR / filename

    if dest.exists():
        print(f"⚠️  Session file already exists: {dest.name}")
        return

    # Warn about dirty repo before scaffolding
    dirty = check_dirty()
    if dirty:
        print(f"\n⚠️  Uncommitted changes detected:")
        for line in dirty.splitlines():
            print(f"   {line}")
        print()

    # Git context
    branch = git(["git", "branch", "--show-current"])
    start_sha = git(["git", "rev-parse", "HEAD"])
    short_sha = start_sha[:7] if start_sha else "?"

    # Read template and fill
    text = TEMPLATE.read_text()
    ws_yaml = "\n".join(f"  - {ws}" for ws in workstreams) if workstreams else "  - WS-XXX"
    ws_display = ", ".join(workstreams) if workstreams else "WS-XXX"
    today_str = now.strftime("%Y-%m-%d %H:%M")
    project_name = PROJECT_ROOT.name

    text = text.replace(
        "workstreams:\n  - WS-001\n  - WS-002",
        f"workstreams:\n{ws_yaml}"
    )
    text = text.replace("mission: null", f"mission: {mission}")
    text = text.replace("branch: ws/001-name", f"branch: {branch or 'main'}")
    text = text.replace("YYYY-MM-DD HH:MM", today_str)
    text = text.replace(
        "[Brief description of what was accomplished]",
        description
    )
    text = text.replace(
        '\"[project-slug or \'meta\']\"',
        f'"{project_name}"'
    )
    text = text.replace("scope: project", "scope: project")  # no-op, already correct
    text = text.replace(
        "> YYYY-MM-DD HH:MM | Workstreams: WS-001, WS-002 | Branch: `ws/001-name`",
        f"> {today_str} | Workstreams: {ws_display} | Branch: `{branch or 'main'}`"
    )
    text = text.replace(
        "# Session — [Brief Description]",
        f"# Session — {description.title()}"
    )

    # Pre-populate git summary with start SHA
    text = text.replace(
        "`ws/001-name` → `main` (merged / pending merge)",
        f"`{branch}` → `main` (pending)"
    )
    text = text.replace(
        "# Reproduce full diff for this session:\ngit diff BEFORE_SHA..AFTER_SHA",
        f"# Reproduce full diff for this session:\ngit diff {short_sha}..AFTER_SHA"
    )
    # Pre-populate the Repos Touched table
    text = text.replace(
        "| ~/agent | BEFORE | AFTER |",
        f"| {project_name} | {short_sha} | AFTER |"
    )

    dest.write_text(text)

    print(f"✅  Session file created: {dest.relative_to(PROJECT_ROOT)}")
    print(f"   Branch:    {branch}")
    print(f"   Start SHA: {start_sha}")
    print(f"\n🔍  Before you fill it in — self-audit:")
    print(f"    · Any WIP/TODO comments left in code or .agent files?")
    print(f"    · Any task statuses still showing In Progress that are actually done?")
    print(f"    · Any verbal decisions this session that didn't land in a file?")
    print(f"    · CONTEXT.md workstreams: frontmatter list still accurate?")
    print(f"    · Any stray scratch files or temp branches to clean up?")
    print(f"    · Mission file updated if a mission ran?")
    print(f"\n📝  Fill in the session file (including the Self-Audit table), then run:")
    print(f"    python3 .agent/scripts/session_init.py --description \"{description}\" --finalize\n")


def finalize(description: str):
    """
    Phase 2: find the session file, commit .agent/ changes, verify repo is clean.
    Mirrors session_wrap.py's finalize behavior for the project context.
    """
    slug = description.lower().replace(" ", "-")[:50]

    # Find matching session file
    matches = sorted(SESSIONS_DIR.glob(f"*-{slug}.md"))
    if not matches:
        # Try partial match on first 20 chars of slug
        matches = sorted(SESSIONS_DIR.glob("*.md"))
        matches = [m for m in matches if slug[:20] in m.name and m.name != "_template"]

    if not matches:
        print(f"❌  No session file found matching '{slug}'")
        print(f"    Check {SESSIONS_DIR}")
        return

    session_file = matches[-1]
    date_str = session_file.name[:10]

    print(f"\n📦  Committing .agent/ changes...")
    subprocess.run(["git", "add", ".agent/"], cwd=PROJECT_ROOT, capture_output=True)
    result = subprocess.run(
        ["git", "commit", "-m",
         f"docs(agent-context): session wrap {date_str} — {description}"],
        cwd=PROJECT_ROOT, capture_output=True, text=True
    )

    if result.returncode == 0:
        first_line = result.stdout.strip().splitlines()[0] if result.stdout.strip() else "committed"
        print(f"  ✅  {first_line}")
    else:
        msg = result.stderr.strip() or result.stdout.strip()
        if "nothing to commit" in msg:
            print(f"  ℹ️  Nothing new to commit in .agent/")
        else:
            print(f"  ⚠️  {msg}")

    # Final repo status
    print(f"\n📋  Final repo status:")
    sha = git(["git", "rev-parse", "--short", "HEAD"])
    dirty = check_dirty()
    if dirty:
        print(f"  ⚠️  {PROJECT_ROOT.name} — uncommitted changes @ {sha}:")
        for line in dirty.splitlines():
            print(f"       {line}")
        print(f"\n⚠️  Commit or stash remaining changes before closing.\n")
    else:
        print(f"  ✅  {PROJECT_ROOT.name} — clean @ {sha}")
        print(f"\n🏁  Session wrap complete. Post summary to Discord.\n")


def main():
    parser = argparse.ArgumentParser(description="Project session scaffold and finalize")
    parser.add_argument("--description", required=True,
                        help="Brief session description (used in filename)")
    parser.add_argument("--workstreams", nargs="*", default=[],
                        help="WS IDs involved e.g. WS-001 WS-002")
    parser.add_argument("--mission", default="null",
                        help="Mission ID if applicable")
    parser.add_argument("--finalize", action="store_true",
                        help="Commit .agent/ and verify repo is clean (phase 2)")
    args = parser.parse_args()

    if args.finalize:
        finalize(args.description)
    else:
        scaffold(args.description, args.workstreams, args.mission)


if __name__ == "__main__":
    main()
