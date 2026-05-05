---
type: workstream
id: WS-002
title: "Strip China Platform Integrations"
project: hermes-fork
status: planning           # planning | active | paused | blocked | complete | cancelled
owner: "Nick Thompson"
created: 2026-05-04
updated: 2026-05-04
branch: ws/002-china-strip  # git branch for this workstream
parent_spec_section: ""    # which section of PROJECT_SPEC this maps to
missions: []               # MISSION-XXX IDs that target this workstream
---

# WS-002 — Strip China Platform Integrations

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
| T-001 | Audit all China-specific files (gateway/platforms/, tools/, skills/, tests/, pyproject.toml extras) | 🔵 Todo | | |
| T-002 | {'Remove gateway platform adapters': 'yuanbao, weixin, wecom, qqbot, dingtalk, feishu'} | 🔵 Todo | | |
| T-003 | Remove tools/yuanbao_tools.py and feishu tool files | 🔵 Todo | | |
| T-004 | Remove Tencent TokenHub from hermes_cli/providers.py | 🔵 Todo | | |
| T-005 | Remove optional deps from pyproject.toml (dingtalk, feishu extras) | 🔵 Todo | | |
| T-006 | Remove China-platform test files | 🔵 Todo | | |
| T-007 | Verify no broken imports remain | 🔵 Todo | | |
| T-008 | Run test suite to confirm no regressions | 🔵 Todo | | |

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
git log --oneline --grep="WS-002"

# Full diff of all workstream changes
git log -p --grep="WS-002"

# Files this workstream has touched
git log --name-only --pretty=format:"" --grep="WS-002" | sort -u | grep -v '^$'
```
