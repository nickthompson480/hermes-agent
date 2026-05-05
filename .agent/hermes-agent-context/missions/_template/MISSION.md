---
type: mission
id: MISSION-001
title: "[Mission Title]"
project: hermes-fork
status: draft              # draft | reviewed | approved | running | complete | failed | rejected
created: 2026-05-04
updated: 2026-05-04
branch: mission/001-short-name   # git branch for this mission — always isolated
base_branch: main                # branch mission forks from
workstreams:
  - WS-001
scope: "One-sentence description of what this mission accomplishes"
reviewer: opus
reviewed_date: null
executor: sonnet
estimated_tasks: 0
---

# MISSION-XXX — [Mission Title]

> **Status:** Draft | **Workstreams:** WS-001 | **Branch:** `mission/001-name`
> **Review:** Opus | **Execution:** Sonnet

---

## Objective
<!-- What does this mission accomplish? What is the end state when complete?
     Be specific enough that success is unambiguous. -->

## Scope
### In Scope
-

### Out of Scope
-

## Pre-conditions
<!-- What must be true before this mission runs? Dependencies, env state, required files. -->

- [ ]

## Workstream Mapping
| Task Group | Workstream | Notes |
|------------|------------|-------|
| | WS-001 | |

---

## Task Breakdown
<!-- Tasks must be specific, atomic, and independently executable where possible.
     Group by phase. Flag parallelizable tasks. Reference WS ID in every task. -->

### Phase 1 — [Phase Name]
> Parallel execution: Yes / No

| ID | Task | Workstream | Parallelizable | Depends On | Notes |
|----|------|------------|----------------|------------|-------|
| T-001 | | WS-001 | ✅ Yes | — | |
| T-002 | | WS-001 | ❌ No | T-001 | |

### Phase 2 — [Phase Name]
> Parallel execution: Yes / No

| ID | Task | Workstream | Parallelizable | Depends On | Notes |
|----|------|------------|----------------|------------|-------|
| T-003 | | WS-001 | ✅ Yes | — | |

---

## Agent Instructions
<!-- Specific guidance for the executing agent(s). Read this before starting. -->

- Branch: `git checkout -b mission/XXX-name` from `main` (or specified base branch)
- Follow all SOPs in `.agent/SOPs/` — especially SOP-002 and SOP-004
- Commit message format: `type(MISSION-XXX/T-XXX): description` — see `docs/GIT_CONVENTIONS.md`
- Commit `.agent/` context changes separately from code changes
- Log all work to the relevant workstream Work Logs
- Write a session file on completion referencing this mission
- **If blocked: halt and report — do not improvise outside mission scope**
- **Never merge to main without human or Opus review of the mission diff**

## Swarm Configuration (if applicable)
<!-- Only fill this out if sub-agents will run in parallel -->

| Sub-agent | Assigned Tasks | Workstream(s) | Branch |
|-----------|----------------|---------------|--------|
| Agent A | T-001, T-003 | WS-001 | mission/XXX-agent-a |
| Agent B | T-002 | WS-001 | mission/XXX-agent-b |

> ⚠️ Swarm agents must operate on isolated files/modules to avoid merge conflicts.
> Coordinate merge order after all agents complete.

---

## Opus Review

### Review Checklist
- [ ] Objective is specific — success state is unambiguous
- [ ] Tasks are atomic and independently executable
- [ ] Dependencies between tasks are clearly marked
- [ ] Pre-conditions are realistic and verified
- [ ] Scope is appropriately sized for a single mission run
- [ ] Swarm configuration is conflict-safe (no overlapping writes)
- [ ] Agent instructions are sufficient for autonomous execution
- [ ] Branch strategy is correct — mission branch isolated from main
- [ ] All referenced workstreams exist and are active
- [ ] Commit convention is specified and clear

### Review Notes
**Reviewer:** Opus | **Date:** YYYY-MM-DD

```
[Opus review notes, gaps identified, risks flagged, revisions requested]
```

### Decision
- [ ] ✅ Approved — proceed to execution on `mission/XXX-name`
- [ ] 🔄 Revise and resubmit — see notes above
- [ ] ❌ Rejected — see notes above

---

## Execution Log
<!-- Executor fills this in during the run -->

| Task | Status | Commit | Agent | Notes |
|------|--------|--------|-------|-------|
| T-001 | | | | |

## Git Summary (filled on completion)
```bash
# Mission diff — review before merging to main:
git diff main...mission/XXX-name

# All mission commits:
git log --oneline --grep="MISSION-XXX"
```

## Outcome
**Completed:** YYYY-MM-DD
**Session File:** `sessions/YYYY-MM-DD_HHMMSS-mission-XXX.md`
**Merged to:** `main` @ `SHA`
**Result:**

### Follow-on Work
<!-- Anything discovered during execution that was out of scope for this mission.
     Do not let these die here — route before closing:
     - WS-specific → add to the workstream's Tasks table
     - Project-level → promote to CONTEXT.md Open Items
     Leave blank if nothing surfaced. -->

| Item | Route To | Notes |
|------|----------|-------|
| | | |
