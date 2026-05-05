---
type: workstream
id: WS-002
title: "Strip China Platform Integrations"
project: hermes-fork
status: complete
owner: "Nick Thompson"
created: 2026-05-04
updated: 2026-05-04
branch: ws/002-china-strip
parent_spec_section: ""
missions: [MISSION-001]
---

# WS-002 — Strip China Platform Integrations

---

## Purpose

Remove all China-specific platform integrations from the hermes-fork to produce a clean Western-focused fork of NousResearch/hermes-agent. Platforms removed: Yuanbao (Tencent AI), WeChat personal (Weixin), WeCom (enterprise WeChat), QQ Bot, DingTalk (Alibaba), Feishu/Lark (ByteDance).

## Scope

- All gateway platform adapter files in `gateway/platforms/`
- All China-specific tool files in `tools/`
- All China-specific test files in `tests/`
- Provider entries in `hermes_cli/providers.py`
- Optional dependency groups in `pyproject.toml`
- Platform enum entries and config blocks in `gateway/config.py`
- Adapter startup blocks in `gateway/run.py`
- Display tier entries in `gateway/display_config.py`
- Target hints in `gateway/session.py`
- Import/reference cleanup in `gateway/platforms/__init__.py`, `webhook.py`, `tools/send_message_tool.py`

## Features / Deliverables
- ✅ All 6 China gateway adapters removed (13 files + qqbot/ dir)
- ✅ China tool files removed (3 files)
- ✅ China test files removed (19 files)
- ✅ Tencent TokenHub removed from providers.py
- ✅ China optional deps removed from pyproject.toml
- ✅ gateway/config.py scrubbed (enum entries + config loading blocks)
- ✅ gateway/run.py scrubbed (adapter startup blocks)
- ✅ display_config.py + session.py scrubbed
- ✅ Import references cleaned up — zero broken imports remain

---

## Tasks

| ID | Task | Status | Assigned | Notes |
|----|------|--------|----------|-------|
| T-001 | Audit all China-specific files | ✅ Done | | Done during MISSION-001 planning — 6 adapters, 3 tools, 19 tests, 4 code files identified |
| T-002 | Remove gateway platform adapters | ✅ Done | | `25b81d7` — 13 files + qqbot/ dir |
| T-003 | Remove tools/yuanbao_tools.py and feishu tool files | ✅ Done | | `dd5fab2` |
| T-004 | Remove Tencent TokenHub from hermes_cli/providers.py | ✅ Done | | `6acdb47` |
| T-005 | Remove optional deps from pyproject.toml | ✅ Done | | `cc87a5b` — dingtalk + feishu extras |
| T-006 | Remove China-platform test files | ✅ Done | | `2e7730e` — 19 files |
| T-007 | Scrub gateway/config.py, run.py, display_config.py, session.py | ✅ Done | | `c969abe`, `88179aa`, `22acd79` |
| T-008 | Verify no broken imports remain | ✅ Done | | `7d13f1c` — cleaned __init__.py, webhook.py, config.py, send_message_tool.py |

### Status Key
- 🔵 Todo · 🟡 In Progress · 🟠 Blocked · ✅ Done · ❌ Cancelled

---

## Work Log

### 2026-05-04 — MISSION-001
- **Branch:** `mission/001-china-strip`
- **Completed:** All 8 tasks — full China integration strip
- **Commits:**
  - `25b81d7` — remove China gateway platform adapters (T-002)
  - `dd5fab2` — remove China platform tool files (T-003)
  - `6acdb47` — remove Tencent TokenHub provider (T-004)
  - `cc87a5b` — remove China platform optional deps from pyproject.toml (T-005)
  - `2e7730e` — remove China platform test files (T-006)
  - `c969abe` — remove China platform entries from gateway config (T-007a)
  - `88179aa` — remove China platform adapter startup from gateway/run.py (T-007b)
  - `22acd79` — remove China platform entries from display_config and session (T-007c)
  - `7d13f1c` — fix remaining China platform references (T-008)
- **Decisions made:**
  - Strip all integrations in one mission pass (cleaner than incremental)
  - Delete China tests without replacement (no value in maintaining tests for deleted code)

---

## Decisions
| Date | Decision | Rationale | Alternatives Considered |
|------|----------|-----------|------------------------|
| 2026-05-04 | Remove all 6 China platforms in one mission | Cleaner history, easier to review in one diff | Incremental per-platform removal |
| 2026-05-04 | Delete tests without replacement | No value maintaining tests for deleted code | Keep as documentation, convert to tombstone stubs |
| 2026-05-04 | Keep hermes_cli/gateway.py setup wizard entries | Setup wizard references are config UX, not broken imports; low-risk to leave | Remove them too (deferred to future cleanup) |

## Issues & Lessons Learned
| Date | Issue | Resolution | Lesson |
|------|-------|------------|--------|
| 2026-05-04 | gateway/config.py had deep QQ Bot and Yuanbao credential blocks in _apply_env_overrides beyond obvious enum entries | Thorough grep after initial pass found them; removed in T-011 | Always grep the full file, not just the obvious sections |
| 2026-05-04 | tools/send_message_tool.py had 6 China _send_* helper functions (~279 lines) missed in initial scrub | Identified via broad grep, deleted as one block | send_message_tool.py has a large dispatch layer — check all send_* helpers when removing a platform |

## Docs & References
- Mission: [MISSION-001](../missions/MISSION-001-china-strip-and-ws-cleanup.md)

## Git Reference
```bash
git log --oneline --grep="MISSION-001"
```
