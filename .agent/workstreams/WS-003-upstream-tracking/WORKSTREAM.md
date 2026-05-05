---
type: workstream
id: WS-003
title: "Upstream Tracking Process & Skill"
project: hermes-fork
status: paused
owner: "Nick Thompson"
created: 2026-05-04
updated: 2026-05-04
branch: ws/003-upstream-tracking
parent_spec_section: ""
missions: [MISSION-001]
---

# WS-003 — Upstream Tracking Process & Skill

---

## Purpose

Maintain a systematic process for tracking commits in the NousResearch/hermes-agent upstream repo. Ensure the fork stays aware of security patches, useful features, and infrastructure changes — while automatically filtering China-specific changes as irrelevant.

## Scope

- Triage categories and decision checklist for upstream commits
- Project-level upstream-tracking skill (`.agent/skills/upstream-tracking.md`)
- Script to fetch and categorize new upstream commits (`.agent/scripts/upstream-diff.sh`)
- Cron job for automated weekly upstream monitoring
- Cherry-pick and conflict resolution documentation

## Features / Deliverables
- ✅ Triage categories defined (SECURITY, FEATURE, CHINA-ONLY, INFRASTRUCTURE, DOC)
- ✅ `upstream-tracking.md` skill written (`.agent/skills/`)
- ✅ `upstream-diff.sh` script built (`.agent/scripts/`)
- ✅ Weekly cron job monitoring upstream and posting to hermes-fork Discord
- ✅ Cherry-pick + conflict resolution workflow documented in skill

---

## Tasks

| ID | Task | Status | Assigned | Notes |
|----|------|--------|----------|-------|
| T-001 | Design the upstream triage categories and decision checklist | ✅ Done | | Completed 2026-05-04 — in upstream-tracking.md skill |
| T-002 | Write the project-level upstream-tracking SKILL.md | ✅ Done | | Completed 2026-05-04 — `.agent/skills/upstream-tracking.md` |
| T-003 | Build a script that fetches new upstream commits since last review and summarizes them | ✅ Done | | Completed 2026-05-04 — `.agent/scripts/upstream-diff.sh` |
| T-004 | Set up cron job for periodic upstream diff alerts | ✅ Done | | Completed 2026-05-04 — weekly cron via Hermes, posts to hermes-fork Discord |
| T-005 | Document the cherry-pick and conflict resolution workflow | ✅ Done | | Completed 2026-05-04 — documented in upstream-tracking.md skill |

### Status Key
- 🔵 Todo · 🟡 In Progress · 🟠 Blocked · ✅ Done · ❌ Cancelled

---

## Work Log

### 2026-05-04 — MISSION-001 (session: mission-001-china-strip)
- **Branch:** `ws/001-fork-setup` (prior session) + `mission/001-china-strip` (this session)
- **Completed:**
  - T-001: Designed triage categories (SECURITY / FEATURE / CHINA-ONLY / INFRASTRUCTURE / DOC) and decision checklist
  - T-002: Wrote `.agent/skills/upstream-tracking.md` with full triage playbook and cherry-pick workflow
  - T-003: Built `.agent/scripts/upstream-diff.sh` — compares against baseline SHA, categorizes commits against China blocklist
  - T-005: Cherry-pick and conflict resolution workflow documented in upstream-tracking.md
  - T-004: Weekly cron job created via Hermes cron system, posts categorized upstream diff to hermes-fork Discord channel
- **Next:**
  - When new upstream commits appear: run upstream-diff.sh output, apply triage categories, cherry-pick SECURITY patches immediately

---

## Decisions
| Date | Decision | Rationale | Alternatives Considered |
|------|----------|-----------|------------------------|
| 2026-05-04 | Weekly cron frequency | Balance signal vs noise — upstream doesn't change daily | Daily (too noisy), monthly (too slow for security) |
| 2026-05-04 | Deliver to hermes-fork Discord | Keep tracking visible to project channel | Email, local file only |

## Issues & Lessons Learned
| Date | Issue | Resolution | Lesson |
|------|-------|------------|--------|
| | | | |

## Docs & References
- [Upstream Tracking Skill](../skills/upstream-tracking.md)
- [Upstream Diff Script](../scripts/upstream-diff.sh)

## Git Reference
```bash
git log --oneline --grep="WS-003"
```
