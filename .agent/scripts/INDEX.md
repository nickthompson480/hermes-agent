---
type: index
title: "Scripts Index"
project: hermes-fork
updated: 2026-05-04
---

# Scripts

Automation scripts for project CRUD operations. All scripts are run from the project root.

---

## Per-Project Scripts (`.agent/scripts/`)

| Script | Purpose | Usage |
|--------|---------|-------|
| `workstream_create.py` | Create a new workstream (SOP-001 automated) | `python3 .agent/scripts/workstream_create.py --id WS-002 --name "feature" --title "Feature Name"` |
| `session_init.py` | Two-phase session scaffold + finalize. Phase 1: creates timestamped session file with git context. Phase 2 (`--finalize`): commits `.agent/` and verifies clean repo. | `python3 .agent/scripts/session_init.py --description "what you're doing" --workstreams WS-001` |
| `mission_create.py` | Create a new mission file (SOP-004 step 1 automated) | `python3 .agent/scripts/mission_create.py --id MISSION-001 --name "slug" --title "Title"` |

## Meta Scripts (`~/agent/scripts/`)

| Script | Purpose | Usage |
|--------|---------|-------|
| `project_create.py` | Create a new project from template | `python3 ~/agent/scripts/project_create.py --name "My Project" --description "..."` |
| `project_list.py` | List all registered projects | `python3 ~/agent/scripts/project_list.py` |
| `project_status.py` | Cross-project status dashboard | `python3 ~/agent/scripts/project_status.py` |

---

## Dependencies
Scripts require Python 3.8+ and PyYAML. A venv is pre-configured at `~/agent/.venv`:
```bash
# Run meta scripts with the venv python
~/agent/.venv/bin/python3 ~/agent/scripts/project_list.py

# Or activate the venv first
source ~/agent/.venv/bin/activate
python3 ~/agent/scripts/project_list.py

# Per-project scripts can use the same venv
~/agent/.venv/bin/python3 .agent/scripts/session_init.py --description "..."
```
