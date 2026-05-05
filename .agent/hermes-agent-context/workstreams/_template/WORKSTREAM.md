---
type: workstream
id: WS-XXX
title: "[Workstream Name]"
project: hermes-fork
status: planning           # planning | active | paused | blocked | complete | cancelled
owner: "Nick Thompson"
created: 2026-05-04
updated: 2026-05-04
branch: ws/XXX-short-name  # git branch for this workstream
parent_spec_section: ""    # which section of PROJECT_SPEC this maps to
missions: []               # MISSION-XXX IDs that target this workstream
---

# WS-XXX — [Workstream Name]

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
| T-001 | | 🔵 Todo | | |

### Status Key
- 🔵 Todo · 🟡 In Progress · 🟠 Blocked · ✅ Done · ❌ Cancelled

---

## Work Log
<!-- Chronological history of every session touching this domain.
     Most recent at top. This grows indefinitely — it's the domain's full history. -->

### YYYY-MM-DD
- **Session:** [brief description — link: `sessions/YYYY-MM-DD_HHMMSS-desc.md`]
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
git log --oneline --grep="WS-XXX"

# Full diff of all workstream changes
git log -p --grep="WS-XXX"

# Files this workstream has touched
git log --name-only --pretty=format:"" --grep="WS-XXX" | sort -u | grep -v '^$'
```
