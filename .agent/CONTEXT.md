---
type: context
title: "Hermes Fork — Context"
project: hermes-fork
status: active
created: 2026-05-04
P26-05-04
owner: "Nick Thompson"
folder: ~/code/projects/hermes-fork
discord_channel: "https://discord.com/channels/1484773475423092807/1501057788741161140"
discord_channel_id: "1501057788741161140"
main_branch: main
workstreams: [WS-001, WS-002, WS-003]
missions: []               # MISSION IDs currently running e.g. [MISSION-001]
open_items:
  []                       # each entry: {id: OI-001, description: "...", priority: high|medium|low}
---

# Project Context — Hermes Fork

> **This is the AI's entry point. Load this file first, every session.**
> Then load the relevant workstream(s) and check the git context below.

---

## Upstream Tracking
- **Upstream:** `git@github.com:NousResearch/hermes-agent.git` (remote: `upstream`)
- **Fork:** `git@github.com:nickthompson480/hermes-agent.git` (remote: `origin`)
- **Fork Baseline SHA:** `a1bed18194ff1ee8de1bf3e81007ddba06b61042` (2026-05-04)
- **upstream_last_reviewed:** `a1bed18194ff1ee8de1bf3e81007ddba06b61042`
- **Upstream Diff Script:** `.agent/scripts/upstream-diff.sh`
- **Triage Skill:** `.agent/skills/upstream-tracking.md`

---

## Quick Links
- [**→ Agent Quick Start**](./docs/AGENT_QUICKSTART.md) ← new agents read this first
- [Project Spec](./PROJECT_SPEC.md)
- [Git Conventions](./docs/GIT_CONVENTIONS.md) ← read before any commits
- [Workstreams Index](./workstreams/INDEX.md)
- [Missions Index](./missions/INDEX.md)
- [Sessions Index](./sessions/INDEX.md)
- [SOPs](./SOPs/INDEX.md)
- [Skills & Knowledge](./skills/INDEX.md)

---

## Active Workstreams
| WS | Name | Branch | Status |
|----|------|--------|--------|
| WS-001 | Fork Setup & Upstream Remote | `ws/001-fork-setup` | ⏸ Paused |
| WS-002 | Strip China Platform Integrations | `ws/002-china-strip` | ✅ Complete |
| WS-003 | Upstream Tracking Process & Skill | `ws/003-upstream-tracking` | ⏸ Paused |

## Active Missions
| Mission | Title | Branch | Status |
|---------|-------|--------|--------|
| _(none)_ | | | |

---

## Open Items
<!-- Forward work not yet assigned to a workstream task or mission.
     Sources: session Next Actions (project-level), mission Follow-on Work.
     WS-specific work goes directly into the workstream's Tasks table instead.
     At each session open: review this list — resolve, assign, or promote items.
     At each session close: add anything new; keep open_items: frontmatter in sync.
     ID format: OI-001, OI-002, ... -->

| ID | Item | Source | Priority | Added |
|----|------|--------|----------|-------|
| _(none)_ | | | | |

## Known Issues / Blockers
<!-- Current problems blocking progress — not forward work.
     Resolved issues move to the relevant workstream's Issues & Lessons Learned. -->
| Issue | Status | Notes |
|-------|--------|-------|
| | | |

## Key Decisions (project-wide)
| Date | Decision | Rationale |
|------|----------|-----------| 
| 2026-05-04 | Strip all 6 China platforms in one mission pass | Cleaner history; single diff to review before merge |
| 2026-05-04 | Merged mission/001-china-strip to main | Human review approved; merged with --no-ff |

---

## Git Context
<!-- Run these at the start of every session to orient quickly -->

```bash
# What branch am I on? What's recent?
git status
git log --oneline -10

# What's happened on the active workstream?
git log --oneline --grep="WS-001"

# What's changed since main?
git log --oneline main..HEAD
```

---

## AI Instructions for This Project

### Every Session — Open
1. Load this file first
2. Review **Open Items** above — any resolved since last session? Remove from table and frontmatter list.
3. Load the relevant workstream `WORKSTREAM.md`(s)
4. Run the git context commands above to orient
5. Follow **SOP-002** for session protocol

### Every Session — Close
- Write a timestamped session file in `sessions/`
- Update all touched workstreams (work log, decisions, issues, task statuses)
- Route Next Actions from session file:
  - Project-level → **Open Items** table + `open_items:` frontmatter list
  - WS-specific → workstream `## Tasks` table
- Update `workstreams:`, `missions:`, and `open_items:` frontmatter lists to match tables
- Post summary to Discord channel

### Commits
- Every commit references a WS or MISSION ID — see `docs/GIT_CONVENTIONS.md`
- `.agent/` context changes committed separately from code changes
- Mission execution always runs on an isolated `mission/XXX` branch
