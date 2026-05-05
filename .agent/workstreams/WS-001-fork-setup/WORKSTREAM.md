---
type: workstream
id: WS-001
title: "Fork Setup & Upstream Remote"
project: hermes-fork
status: paused           # planning | active | paused | blocked | complete | cancelled
owner: "Nick Thompson"
created: 2026-05-04
updated: 2026-05-04
branch: ws/001-fork-setup  # git branch for this workstream
parent_spec_section: ""    # which section of PROJECT_SPEC this maps to
missions: []               # MISSION-XXX IDs that target this workstream
---

# WS-001 — Fork Setup & Upstream Remote

---

## Purpose
Establish the hermes-fork repository: fork from NousResearch/hermes-agent, configure upstream remote, record baseline SHA for future diff tracking, and put agent context scaffolding in place.

## Scope
Everything needed to get the fork into a clean, trackable state: GitHub fork, clone, upstream remote, baseline SHA recording, and upstream diff tooling. Does NOT include ongoing cherry-pick or China strip work (those are WS-003 and WS-002 respectively).

## Features / Deliverables
- Fork repo on GitHub under Nick's account ✅
- Clone into ~/code/projects/hermes-fork ✅
- Upstream remote `NousResearch/hermes-agent` configured ✅
- Baseline upstream SHA recorded in CONTEXT.md ✅
- Upstream diff script (`upstream-diff.sh`) written ✅

---

## Tasks

| ID | Task | Status | Assigned | Notes |
|----|------|--------|----------|-------|
| T-001 | Fork repo on GitHub under Nick's account | ✅ Done | | Done 2026-05-04 |
| T-002 | Clone fork into ~/code/projects/hermes-fork (replace template scaffold) | ✅ Done | | Done 2026-05-04 |
| T-003 | Add upstream remote pointing to NousResearch/hermes-agent | ✅ Done | | Done 2026-05-04 |
| T-004 | Verify baseline runs cleanly | ✅ Done | | Done 2026-05-04 |
| T-005 | Record starting upstream commit SHA as the fork baseline | ✅ Done | | Recorded in CONTEXT.md; diff script written |

### Status Key
- 🔵 Todo · 🟡 In Progress · 🟠 Blocked · ✅ Done · ❌ Cancelled

---

## Work Log
<!-- Chronological history of every session touching this domain.
     Most recent at top. This grows indefinitely — it's the domain's full history. -->

### 2026-05-04
- **Session:** Fork setup & upstream tracking scaffolding
- **Branch:** `main` @ `7ba4883`
- **Completed:**
  - T-001: Forked NousResearch/hermes-agent on GitHub under Nick's account
  - T-002: Cloned fork into ~/code/projects/hermes-fork
  - T-003: Added upstream remote (`NousResearch/hermes-agent`)
  - T-004: Verified baseline clone is intact
  - T-005: Recorded baseline upstream SHA in CONTEXT.md; wrote upstream-diff.sh script
- **Commits:**
  - `d26308c` — feat(agent-context): add project management context — WS-001/002/003, upstream-tracking skill
  - `7ba4883` — feat(WS-001): record upstream remotes, baseline SHA, cleanup nested .agent dir
- **Decisions made:**
  - Use `.agent/` directory for all agent context files
  - Track upstream via SHA in CONTEXT.md, diff with upstream-diff.sh script
- **Blockers / Issues:**
  - None
- **Next:**
  - Domain is complete for now. Monitoring handled by WS-003 cron job.

---

## Decisions
| Date | Decision | Rationale | Alternatives Considered |
|------|----------|-----------|------------------------|
| 2026-05-04 | Use `.agent/` dir for context | Keeps agent files separate from code | Inline comments |
| 2026-05-04 | Track upstream via SHA in CONTEXT.md | Simple, human-readable baseline | Git submodule, branch tracking |

## Issues & Lessons Learned
| Date | Issue | Resolution | Lesson |
|------|-------|------------|--------|
| 2026-05-04 | Nested `.agent/` dir existed inside fork | Removed during cleanup (7ba4883) | Always check for nested scaffolding dirs after clone |

## Docs & References
- [CONTEXT.md](../../CONTEXT.md) — project-level context including upstream baseline SHA
- [upstream-diff.sh](../../scripts/upstream-diff.sh) — script to diff against upstream

## Git Reference
```bash
# All commits for this workstream
git log --oneline --grep="WS-001"

# Full diff of all workstream changes
git log -p --grep="WS-001"

# Files this workstream has touched
git log --name-only --pretty=format:"" --grep="WS-001" | sort -u | grep -v '^$'
```
