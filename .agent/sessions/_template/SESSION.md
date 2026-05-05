---
type: session
title: "[Brief description of what was accomplished]"
project: hermes-fork
status: complete
created: 2026-05-04
workstreams:
  - WS-001
  - WS-002
mission: null          # MISSION-XXX if this session was mission-driven, else null
agent: sonnet          # model that did the work
duration: ~Xh Ym
branch: ws/001-name    # git branch session ran on
commits: []            # filled in at end — list of commit SHAs from this session
outcome: "One-liner summary of what was delivered"
---

# Session — [Brief Description]
> YYYY-MM-DD HH:MM | Workstreams: WS-001, WS-002 | Branch: `ws/001-name`

---

## Goal
<!-- What was the intent going in? -->

## What Was Done
<!-- Narrative of the work. Enough detail that someone (or an AI) reading this later
     understands what happened and why. -->

-

## Outcomes & Deliverables
<!-- Concrete things that exist now that didn't before: files, features, fixes. -->

- [ ]

## Workstream Updates Made
<!-- Enumerate what was updated so this session is traceable -->

| Workstream | What Changed |
|------------|-------------|
| WS-001 | |

## Decisions Made
<!-- Mirror these into the relevant workstreams. -->

| Decision | Rationale | Workstream |
|----------|-----------|------------|
| | | |

## Issues Encountered
<!-- Mirror into workstreams. -->

| Issue | Resolution | Workstream |
|-------|------------|------------|
| | | |

## Lessons Learned
-

## Before You Close — Self-Audit
<!--
Ask yourself before running session_init.py --finalize:
  - Any TODO or WIP comments left in code or .agent files?
  - Any workstream task statuses still showing In Progress that are actually done?
  - Any decisions made verbally this session that didn't land in a file?
  - Any issues encountered that aren't logged in the relevant workstream?
  - Is CONTEXT.md's workstreams: frontmatter list still accurate?
  - Any stray scratch files, test outputs, or temp branches to clean up?
  - Is the sessions/INDEX.md updated with this file?
  - If a mission ran: is the mission file status updated and missions/INDEX.md current?
-->

| Check | Status | Notes |
|-------|--------|-------|
| No WIP/TODO left in code or .agent files | | |
| All task statuses current in workstream(s) | | |
| Verbal decisions captured in writing | | |
| Issues logged in workstream | | |
| CONTEXT.md workstreams: frontmatter accurate | | |
| Stray files / temp branches cleaned up | | |
| sessions/INDEX.md updated | | |
| Mission file + index updated (if applicable) | | |

## Next Actions
<!-- Route before finalizing:
     - WS-specific → add to the workstream's Tasks table
     - Project-level → promote to CONTEXT.md Open Items
     - Cross-project or meta → promote to ~/agent/.agent/CONTEXT.md Open Items -->

| Action | Route To | Owner |
|--------|----------|-------|
| | | |

---

## Git Summary

### Branch
`ws/001-name` → `main` (merged / pending merge)

### Commits This Session
<!-- Run: git log --oneline SHA_before..HEAD and paste output -->
```
abc1234 feat(WS-001): description
def5678 docs(agent-context): update WS-001 work log
```

### Files Changed
<!-- Run: git diff --stat SHA_before..HEAD -->
```
src/module.py    | 42 +++++++++
.agent/workstreams/WS-001/WORKSTREAM.md | 18 +++++
```

### Diff Reference
```bash
# Reproduce full diff for this session:
git diff BEFORE_SHA..AFTER_SHA
```
