---
type: sop
id: SOP-002
title: "Running a Work Session with AI"
project: hermes-fork
status: stable
version: "1.1"
created: 2026-05-04
updated: 2026-05-04
trigger: "Any time you start a coding/planning session on this project"
applies_to: all
---

# SOP-002 — Running a Work Session with AI

**Trigger:** Any time you start a coding/planning session on this project.

---

## Before You Start

### 1. Load context
- Share `CONTEXT.md` with the AI — it reads this first
- Share the relevant workstream `WORKSTREAM.md`(s)
- State the session goal clearly: *"Today I want to accomplish X"*

### 2. Git orientation (agent runs these)
```bash
git status                          # confirm clean working tree
git log --oneline -10               # recent history
git log --oneline --grep="WS-XXX"  # history for this workstream
git log --oneline main..HEAD        # what's diverged from main
```

### 3. Note the starting commit SHA
```bash
git rev-parse HEAD   # record this — used in the session file later
```

---

## During the Session

- Decisions → into the workstream's **Decisions** table (never verbal-only)
- Bugs/surprises → into **Issues & Lessons Learned**
- Commit frequently — small, scoped commits referencing the WS ID
- `.agent/` changes committed **separately** from code changes
- Never commit `wip` to `main` — see `docs/GIT_CONVENTIONS.md`

---

## End of Session

### 1. Commit code changes
```bash
git add src/                   # code changes
git commit -m "feat(WS-XXX): description"
```
Keep code commits separate from context commits — see `docs/GIT_CONVENTIONS.md`.

### 2. Capture git summary
```bash
git log --oneline BEFORE_SHA..HEAD   # commits this session
git diff --stat BEFORE_SHA..HEAD     # files changed
```

### 3. Self-audit before wrapping

Before creating the session file, check:

| Question | |
|----------|-|
| Any WIP/TODO left in code or `.agent` files? | |
| Any workstream task statuses still In Progress that are actually done? | |
| Any verbal decisions this session that didn't land in a file? | |
| CONTEXT.md `workstreams:` frontmatter list still accurate? | |
| Any stray scratch files or temp branches to clean up? | |
| Mission file updated if a mission ran? | |

Resolve anything before proceeding. The same checklist lives in the session template.

### 4. Write a session file
Use `session_init.py` — it scaffolds the file with git context pre-populated and warns on dirty repo:
```bash
python3 .agent/scripts/session_init.py \
  --description "brief-description" \
  --workstreams WS-001
```
Fill in all sections: Goal, What Was Done, Outcomes, Decisions, Issues, Lessons, Next Actions, Git Summary.

Then finalize — commits `.agent/` and verifies the repo is clean:
```bash
python3 .agent/scripts/session_init.py \
  --description "brief-description" --finalize
```

### 5. Update workstreams
- Work Log entry (with branch + commit SHA reference)
- Decisions table
- Issues & Lessons Learned
- Task statuses
- Update `updated` frontmatter date

### 6. Route Next Actions from the session file
Before updating CONTEXT.md, route every item in the session's `## Next Actions`:
- **WS-specific** → add to the relevant workstream's `## Tasks` table
- **Project-level** → add to `CONTEXT.md ## Open Items`
- **Items routed** → mark the session table row resolved or remove it

### 7. Update CONTEXT.md
- Promote routed Next Actions into **Open Items** table (see step 6)
- Review existing Open Items — anything resolved this session? Remove from table AND `open_items:` frontmatter
- Keep all three frontmatter lists in sync with their body tables:
  - `workstreams:` — active WS IDs (drives portfolio dashboard)
  - `missions:` — running mission IDs
  - `open_items:` — list of `{id, description, priority}` structs (drives portfolio dashboard)
- Update the **Active Workstreams table** and **Active Missions table** if status changed
- Update known issues or key decisions if applicable

### 8. Post to Discord
- Session summary to the project channel

---

## Tips
- Load workstream context at session start, not mid-session
- One workstream per session when possible — cleaner context and cleaner git history
- If a mission drove the session, reference its ID in the session file frontmatter
- Always commit `.agent/` separately — makes the context history independently readable
