---
type: sop
id: SOP-005
title: "Using Git as Project Context"
project: hermes-fork
status: stable
version: "1.0"
created: 2026-05-04
updated: 2026-05-04
trigger: "At session start, when orienting to a project, or when reconstructing what happened on a workstream or mission"
applies_to: all
---

# SOP-005 — Using Git as Project Context

**Trigger:** At the start of any session, when orienting to a project, or when you need to
reconstruct what happened on a workstream or mission without reading every prose file.

> Git history is project context. A well-structured commit log is queryable,
> diffable, and chronologically precise in ways that prose files cannot match.
> Use it proactively — not just for version control.

---

## Session Start Orientation

Run these before loading workstream files. They give you the current state fast.

```bash
# Where am I? Is the tree clean?
git status
git branch --show-current

# What's recent?
git log --oneline -15

# What's diverged from main?
git log --oneline main..HEAD

# What workstreams/missions are active? (scan recent commit scopes)
git log --oneline -30 | grep -oP '\(.*?\)' | sort -u
```

---

## Workstream Context Queries

```bash
# All commits for a workstream
git log --oneline --grep="WS-001"

# Full narrative diff — everything done on WS-001
git log -p --grep="WS-001"

# Files WS-001 has touched
git log --name-only --pretty=format:"" --grep="WS-001" | sort -u | grep -v '^$'

# When was a specific file last changed, and by which WS?
git log --oneline -- src/path/to/file.py

# What changed in WS-001 since it was created (on its branch)?
git diff main...ws/001-name
```

---

## Mission Context Queries

```bash
# All commits for a mission
git log --oneline --grep="MISSION-002"

# Full mission diff (review before merging)
git diff main...mission/002-name

# Execution log — what tasks completed and when?
git log --oneline --grep="MISSION-002/T-"

# Who ran the mission? (agent-type commits)
git log --oneline --grep="agent" --grep="MISSION-002" --all-match
```

---

## Session Reconstruction

When you need to understand what a past session did:

```bash
# Find the session's before/after SHAs (from the session file's Git Summary)
# Then:
git log --oneline BEFORE_SHA..AFTER_SHA
git diff BEFORE_SHA..AFTER_SHA
git diff --stat BEFORE_SHA..AFTER_SHA

# What .agent files were updated in that session?
git diff --name-only BEFORE_SHA..AFTER_SHA -- .agent/
```

---

## Diff a Specific File Over Time

```bash
# Full history of a file
git log --follow -p -- src/module.py

# What it looked like at a specific commit
git show SHA:src/module.py

# Compare a file between two commits
git diff SHA1..SHA2 -- src/module.py
```

---

## Recovering Context After a Long Gap

When returning to a project after time away:

```bash
# 1. Skim recent history
git log --oneline -20

# 2. Check all active branches
git branch -a

# 3. What's unmerged to main?
git log --oneline main..HEAD

# 4. Any WIP commits to be aware of?
git log --oneline --grep="wip"

# 5. Load CONTEXT.md, then query git for each active workstream
```

---

## Searching History by Content

```bash
# Find commits that changed a specific string (e.g. a function name)
git log -S "functionName" --oneline

# Find commits whose message contains a keyword
git log --oneline --grep="auth"

# Commits between two dates
git log --oneline --after="2024-01-01" --before="2024-03-01"
```

---

## Rules for Agents

1. **Always run session start orientation before loading prose context** — git is faster and more precise
2. **Note the starting SHA** before any work: `git rev-parse HEAD` — you'll need it for the session file
3. **Never treat git log as supplementary** — treat it as the primary timeline, prose files as the narrative layer
4. **If prose and git disagree** — git wins; update the prose file to match
5. **Reference the full GIT_CONVENTIONS doc** before making any commits: `docs/GIT_CONVENTIONS.md`
