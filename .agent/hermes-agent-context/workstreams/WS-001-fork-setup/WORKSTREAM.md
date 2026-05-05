---
type: workstream
id: WS-001
title: "Fork Setup & Upstream Remote"
project: hermes-fork
status: active           # planning | active | paused | blocked | complete | cancelled
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
<!-- Workstreams are persistent domains, not tickets. This workstream is the permanent
     home for everything related to this area — across the entire life of the project.
     You will return here multiple times as the domain evolves.
     Describe the domain: what area of the project does this own? -->

## Scope
<!-- What belongs in this workstream and what doesn't?
     Helps disambiguate when a task could fit multiple workstreams. -->

## Features / Deliverables
<!-- Current known deliverables. This list grows over time as new work is identified. -->

---

## Tasks

| ID | Task | Status | Assigned | Notes |
|----|------|--------|----------|-------|
| T-001 | Fork repo on GitHub under Nick's account | 🔵 Todo | | |
| T-002 | Clone fork into ~/code/projects/hermes-fork (replace template scaffold) | 🔵 Todo | | |
| T-003 | Add upstream remote pointing to NousResearch/hermes-agent | 🔵 Todo | | |
| T-004 | Verify baseline runs cleanly | 🔵 Todo | | |
| T-005 | Record starting upstream commit SHA as the fork baseline | 🔵 Todo | | |

### Status Key
- 🔵 Todo · 🟡 In Progress · 🟠 Blocked · ✅ Done · ❌ Cancelled

---

## Work Log
<!-- Chronological history of every session touching this domain.
     Most recent at top. This grows indefinitely — it's the domain's full history. -->

### 2026-05-04
- **Session:** [brief description — link: `sessions/2026-05-04_HHMMSS-desc.md`]
- **Branch:** `ws/XXX-name` @ `abc1234`
- **Completed:**
  -
- **Decisions made:**
  -
- **Blockers / Issues:**
  -
- **Next:**
  -

---

## Decisions
| Date | Decision | Rationale | Alternatives Considered |
|------|----------|-----------|------------------------|
| | | | |

## Issues & Lessons Learned
| Date | Issue | Resolution | Lesson |
|------|-------|------------|--------|
| | | | |

## Docs & References
- [Doc Title](./docs/filename.md)

## Git Reference
```bash
# All commits for this workstream
git log --oneline --grep="WS-001"

# Full diff of all workstream changes
git log -p --grep="WS-001"

# Files this workstream has touched
git log --name-only --pretty=format:"" --grep="WS-001" | sort -u | grep -v '^$'
```
