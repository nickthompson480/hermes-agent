---
type: doc
title: "Agent Quick Start — .agent System"
project: hermes-fork
status: stable
version: "1.0"
created: 2026-05-04
updated: 2026-05-04
---

# Agent Quick Start — The `.agent` System

> **Read this first if you are an agent dropped into this project.**
> This document gives you a complete mental model of the system and the exact
> sequence to follow before doing any work.

---

## What Is `.agent`?

`.agent` is the project's context layer — everything an AI or human needs to
understand, navigate, and contribute to the project. It lives alongside the
code, is version-controlled in git, and is maintained continuously as work happens.

Think of it in three layers:

```
WHAT the project is      →  PROJECT_SPEC.md
HOW the work is tracked  →  workstreams/
HOW the work gets done   →  sessions/ + missions/ + SOPs + skills + git
```

---

## File Types at a Glance

| File | `type` | Role |
|------|--------|------|
| `CONTEXT.md` | `context` | Your entry point. Loaded first, every session. Points to everything. |
| `PROJECT_SPEC.md` | `spec` | What the project is — goals, scope, tech stack, timeline. |
| `workstreams/WS-XXX/WORKSTREAM.md` | `workstream` | Living record of a feature/domain. Tasks, work log, decisions, issues. |
| `sessions/YYYY-MM-DD_HHMMSS-*.md` | `session` | Post-work debrief. Written after substantial work. May span multiple workstreams. |
| `missions/MISSION-XXX.md` | `mission` | Large approved task batch. Opus reviews → Sonnet executes on isolated branch. |
| `SOPs/SOP-XXX.md` | `sop` | How recurring processes work. Read before doing that process. |
| `skills/*.md` | `skill` | Reusable patterns and knowledge that emerged from this project. |
| `docs/*.md` | `doc` | Reference documentation. |
| `*/INDEX.md` | `index` | Navigation index for each folder. |

Every file has YAML frontmatter. The `type`, `status`, `id`, and `updated` fields
are the most important for quick orientation.

---

## Load Sequence — Every Session

Follow this exact sequence before doing any work:

### Step 1 — Git orientation (30 seconds)
```bash
git status                          # clean tree? what branch?
git log --oneline -10               # what's recent?
git log --oneline main..HEAD        # what's diverged from main?
```

### Step 2 — Load CONTEXT.md
Read it fully. Note:
- Active workstreams and their branches
- Active missions and their status
- Project-level decisions and blockers
- The Discord channel (where session summaries are posted)

### Step 3 — Load the relevant workstream(s)
Read `WORKSTREAM.md` for every workstream you'll touch. Note:
- Current task statuses
- Recent work log entries
- Open decisions and blockers

### Step 4 — Git workstream context
```bash
git log --oneline --grep="WS-XXX"   # full history of this workstream
git diff main...ws/XXX-name         # everything not yet merged to main
```

### Step 5 — Note your starting SHA
```bash
git rev-parse HEAD   # record this — you'll need it for the session file
```

### Step 6 — Confirm session goal
Make sure you have a clear stated goal before writing a single line of code.

---

## The Commit Contract

Every commit you make must follow this contract. Read `docs/GIT_CONVENTIONS.md`
for the full reference. The short version:

```
type(SCOPE): short description

Refs: WS-XXX
```

| Rule | Detail |
|------|--------|
| Every commit references a WS or MISSION ID | No orphan commits |
| `.agent/` changes committed separately from code | Keeps context history clean |
| Mission execution always on `mission/XXX` branch | Never directly on main |
| `wip` commits never land on `main` | Squash before merging |
| Always `--no-ff` when merging branches | Preserve branch seams in history |

---

## The Workstream Loop

This is the core work cycle for any session:

```
load workstream → do work → commit (WS-scoped) → update workstream → write session file
```

More specifically, at the end of every substantial session:

1. Commit code: `git commit -m "feat(WS-XXX): description"`
2. Commit context separately: `git commit -m "docs(agent-context): update WS-XXX work log"`
3. Write a session file in `sessions/` using `session_init.py`
4. Update all touched workstreams — work log, decisions, issues, task statuses
5. **Route Next Actions** from the session file:
   - WS-specific → workstream `## Tasks` table
   - Project-level → `CONTEXT.md ## Open Items`
6. Update `CONTEXT.md` — Open Items (add new, remove resolved), Active Workstreams table, `workstreams:`/`missions:` frontmatter lists
7. Run `session_init.py --finalize` — commits `.agent/`, verifies clean
8. Post summary to Discord (channel ID in `CONTEXT.md` frontmatter)

---

## Missions — When and How

Missions are **not required** for all work. Use them when:
- The scope is large enough to need upfront planning and review
- Autonomous or parallel (swarm) execution is appropriate
- A clean isolated branch + diff review before merge is valuable

**The lifecycle:**
```
draft → [Opus reviews] → approved → [Sonnet executes on mission/XXX branch]
     → [diff reviewed] → merged --no-ff to main → session file written
```

Never execute a mission that hasn't been approved. Never merge a mission branch
without a diff review. See `SOPs/SOP-004-write-and-execute-mission.md`.

---

## Key Rules for Agents

1. **Git history is authoritative** — if prose files and git disagree, git wins; update the prose
2. **Never improvise outside mission scope** — if blocked, halt and report
3. **Always document decisions** — verbal decisions that don't land in a file don't exist
4. **`.agent/` commits are real commits** — treat them with the same discipline as code
5. **Skills default to project-level** — create in `.agent/skills/` first; only escalate to a global skill if one already exists and needs updating, or the skill clearly benefits other unrelated projects
6. **Session files are mandatory after substantial work** — not optional
7. **One branch per workstream, one branch per mission** — never mix concerns on a branch

---

## SOP Reference

| Situation | SOP to follow |
|-----------|--------------|
| Starting any session | SOP-002 + SOP-005 |
| Creating a new workstream | SOP-001 |
| Starting a new project from scratch | SOP-003 |
| Writing and running a mission | SOP-004 |
| Reconstructing context from git | SOP-005 |
