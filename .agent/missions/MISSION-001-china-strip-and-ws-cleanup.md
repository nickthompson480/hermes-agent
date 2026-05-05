---
type: mission
id: MISSION-001
title: "China Strip & Workstream Cleanup"
project: hermes-fork
status: complete
created: 2026-05-04
updated: 2026-05-04
branch: mission/001-china-strip
base_branch: main
workstreams:
  - WS-001
  - WS-002
  - WS-003
scope: "Retroactively document WS-001 completion, strip all China platform integrations (WS-002), finalize WS-003 upstream tooling, and wrap session context."
reviewer: self
reviewed_date: 2026-05-04
executor: sonnet
estimated_tasks: 16
---

# MISSION-001 — China Strip & Workstream Cleanup

> **Status:** Approved | **Workstreams:** WS-001, WS-002, WS-003 | **Branch:** `mission/001-china-strip`
> **Review:** Self-approved (Nick authorized execution) | **Execution:** Sonnet

---

## Objective

1. **WS-001 context fix:** Mark all WS-001 tasks as done (they were completed in the prior session but the workstream file was never updated).
2. **WS-002 execution:** Remove every China platform integration from the fork — gateway adapters, tools, tests, pyproject.toml extras, provider entries, and all cross-cutting references in config/run/display/session files.
3. **WS-003 context fix + cron:** Mark already-completed WS-003 tasks as done; set up the upstream monitoring cron job (T-004).
4. **Session wrap:** Write session file, update all workstreams, update CONTEXT.md, post changelog to #hermes-docs Discord channel.

End state: the fork has zero China platform code, all workstream files accurately reflect reality, and a cron job monitors upstream for new commits.

## Scope

### In Scope
- Removing all files in `gateway/platforms/` belonging to: yuanbao, weixin, wecom (+ wecom_callback + wecom_crypto), qqbot/, dingtalk, feishu (+ feishu_comment + feishu_comment_rules)
- Removing `tools/yuanbao_tools.py`, `tools/feishu_doc_tool.py`, `tools/feishu_drive_tool.py`
- Removing Tencent TokenHub from `hermes_cli/providers.py`
- Removing dingtalk + feishu optional extras from `pyproject.toml`
- Removing all China platform test files (see task list)
- Removing China platform enum values + config blocks from `gateway/config.py`
- Removing China adapter loading from `gateway/run.py`
- Removing China platform display entries from `gateway/display_config.py`
- Removing yuanbao-specific text from `gateway/session.py`
- Setting up upstream-diff cron job (WS-003 T-004)
- Updating all three workstream WORKSTREAM.md files
- Writing session file + updating CONTEXT.md + missions/INDEX.md

### Out of Scope
- Removing Feishu *skills* from the Hermes skills library (that's a global Hermes concern, not this fork)
- Modifying any non-China platform adapters
- Changing any config schema for Western platforms
- Merging to main (human reviews diff first)

## Pre-conditions

- [x] Repo exists at `~/code/projects/hermes-fork` with upstream remote configured
- [x] `origin` = `git@github.com:nickthompson480/hermes-agent.git`
- [x] `upstream` = `git@github.com:NousResearch/hermes-agent.git`
- [x] Starting branch: `main`, HEAD = `7ba4883`
- [x] `.agent/scripts/upstream-diff.sh` exists (for cron reference)
- [x] `.agent/skills/upstream-tracking.md` exists

## Workstream Mapping

| Task Group | Workstream | Notes |
|------------|------------|-------|
| T-001: Context fix | WS-001 | Retroactive — tasks already done |
| T-002 to T-011: China strip | WS-002 | Core mission work |
| T-012 to T-013: WS-003 wrap | WS-003 | Retroactive + cron |
| T-014 to T-016: Wrap | All | Session file + Discord post |

---

## Task Breakdown

### Phase 1 — WS-001 Context Retroactive Update
> Parallel execution: No — write context only, no code changes

| ID | Task | Workstream | Parallelizable | Depends On | Notes |
|----|------|------------|----------------|------------|-------|
| T-001 | Update WS-001 WORKSTREAM.md: mark T-001 through T-005 ✅ Done, fill in Work Log with prior session activity (fork created, upstream remote added, baseline SHA recorded, diff script written, skill written) | WS-001 | ❌ No | — | Don't fabricate commit SHAs — use `git log --oneline --grep=WS-001` to get real ones |

### Phase 2 — WS-002: China Platform Strip
> Parallel execution: No — sequential to avoid import errors slipping through

| ID | Task | Workstream | Parallelizable | Depends On | Notes |
|----|------|------------|----------------|------------|-------|
| T-002 | Create mission branch: `git checkout -b mission/001-china-strip` from main | WS-002 | ❌ No | T-001 | All subsequent work happens on this branch |
| T-003 | Remove gateway platform files: `yuanbao.py`, `yuanbao_media.py`, `yuanbao_proto.py`, `yuanbao_sticker.py`, `weixin.py`, `wecom.py`, `wecom_callback.py`, `wecom_crypto.py`, entire `qqbot/` directory, `dingtalk.py`, `feishu.py`, `feishu_comment.py`, `feishu_comment_rules.py` — commit as `chore(MISSION-001/T-003): remove China gateway platform adapters` | WS-002 | ❌ No | T-002 | 13 files + 1 dir |
| T-004 | Remove China tools: `tools/yuanbao_tools.py`, `tools/feishu_doc_tool.py`, `tools/feishu_drive_tool.py` — commit as `chore(MISSION-001/T-004): remove China platform tool files` | WS-002 | ❌ No | T-003 | |
| T-005 | Remove Tencent TokenHub from `hermes_cli/providers.py`: delete the `"tencent-tokenhub"` HermesOverlay entry (lines ~173-176), delete the `"tencent"/"tokenhub"/"tencent-cloud"/"tencentmaas"` alias entries (~316-319), delete the `"tencent-tokenhub": "Tencent TokenHub"` display name entry (~359). Commit as `chore(MISSION-001/T-005): remove Tencent TokenHub provider` | WS-002 | ❌ No | T-004 | Read file first, use exact line context for patch |
| T-006 | Remove China extras from `pyproject.toml`: delete the `dingtalk = [...]` and `feishu = [...]` lines in `[project.optional-dependencies]` section; also remove `"hermes-agent[dingtalk]"` and `"hermes-agent[feishu]"` from any groups that reference them. Commit as `chore(MISSION-001/T-006): remove China platform optional deps from pyproject.toml` | WS-002 | ❌ No | T-005 | |
| T-007 | Remove China test files — delete all of these: `tests/test_yuanbao_pipeline.py`, `tests/test_yuanbao_markdown.py`, `tests/test_yuanbao_proto.py`, `tests/test_yuanbao_integration.py`, `tests/tools/test_feishu_tools.py`, `tests/hermes_cli/test_dingtalk_auth.py`, `tests/gateway/test_feishu_bot_auth_bypass.py`, `tests/gateway/test_feishu_bot_admission.py`, `tests/gateway/test_feishu.py`, `tests/gateway/test_feishu_approval_buttons.py`, `tests/gateway/test_weixin.py`, `tests/gateway/test_wecom.py`, `tests/gateway/test_dingtalk.py`, `tests/gateway/test_qqbot.py`, `tests/gateway/test_setup_feishu.py`, `tests/gateway/test_feishu_onboard.py`, `tests/gateway/test_wecom_callback.py`, `tests/gateway/test_feishu_comment_rules.py`, `tests/gateway/test_feishu_comment.py`. Commit as `chore(MISSION-001/T-007): remove China platform test files` | WS-002 | ❌ No | T-006 | 19 files |
| T-008 | Scrub `gateway/config.py`: (a) Remove the `DINGTALK`, `FEISHU`, `WECOM`, `WECOM_CALLBACK`, `WEIXIN`, `QQBOT`, `YUANBAO` entries from the Platform enum; (b) Remove the dingtalk and feishu config-loading blocks (~lines 937-949 and 970-980 area). Commit as `chore(MISSION-001/T-008): remove China platform entries from gateway config` | WS-002 | ❌ No | T-007 | Read full context around each section before patching |
| T-009 | Scrub `gateway/run.py`: Remove the import+startup blocks for `DingTalkAdapter`, `FeishuAdapter`, `WeComAdapter` (callback + main), `WeixinAdapter`, `QQAdapter`, `YuanbaoAdapter` (~lines 4470-4555). Commit as `chore(MISSION-001/T-009): remove China platform adapter startup from gateway/run.py` | WS-002 | ❌ No | T-008 | Read surrounding context carefully — keep the structure for other adapters intact |
| T-010 | Scrub `gateway/display_config.py`: Remove the `"feishu"`, `"weixin"`, `"wecom"`, `"wecom_callback"`, `"dingtalk"` entries from the display tier dict (~lines 87-96). Scrub `gateway/session.py`: Remove the yuanbao-specific target hint string (~lines 373-374). Commit as `chore(MISSION-001/T-010): remove China platform entries from display_config and session` | WS-002 | ❌ No | T-009 | |
| T-011 | Verify no broken imports remain: run `python -c "from gateway import config; from gateway import run; from gateway import display_config; from gateway import session; print('OK')"` — fix any import errors before proceeding. Also run `grep -rn "yuanbao\|weixin\|wecom\|qqbot\|dingtalk\|feishu" gateway/ tools/ tests/ hermes_cli/ --include="*.py" \| grep -v "__pycache__"` and resolve any remaining references. Commit fixes if needed. | WS-002 | ❌ No | T-010 | Do NOT proceed to T-012 if import errors exist |

### Phase 3 — WS-003 Context Update + Cron
> Parallel execution: No

| ID | Task | Workstream | Parallelizable | Depends On | Notes |
|----|------|------------|----------------|------------|-------|
| T-012 | Update WS-003 WORKSTREAM.md: mark T-001, T-002, T-003, T-005 as ✅ Done (completed in prior session). Fill in Work Log. Leave T-004 (cron job) as the one remaining deliverable. | WS-003 | ❌ No | T-011 | |
| T-013 | Set up upstream monitoring cron job using Hermes cron system: schedule `.agent/scripts/upstream-diff.sh` to run weekly, delivering output to the hermes-fork Discord channel (ID: 1501057788741161140). Mark WS-003 T-004 ✅ Done in WORKSTREAM.md. | WS-003 | ❌ No | T-012 | Use `mcp_cronjob` with `action='create'`, schedule `every 7d`, deliver to `discord:1501057788741161140` |

### Phase 4 — Session Wrap + Post Changelog
> Parallel execution: No

| ID | Task | Workstream | Parallelizable | Depends On | Notes |
|----|------|------------|----------------|------------|-------|
| T-014 | Update WS-002 WORKSTREAM.md: mark T-001 through T-008 ✅ Done, fill in Work Log with all T-002 through T-011 commit SHAs (get from `git log --oneline --grep=MISSION-001`). Set status to `complete`. | WS-002 | ❌ No | T-013 | |
| T-015 | Write session file `sessions/2026-05-04_HHMMSS-mission-001-china-strip.md` (use `python3 .agent/scripts/session_init.py --description "mission-001-china-strip" --mission MISSION-001 --workstreams WS-001 WS-002 WS-003`). Fill in all sections. Update `sessions/INDEX.md`. Update `missions/INDEX.md` (status → complete). Update `CONTEXT.md` frontmatter (`missions: []`, `workstreams:` accurate). Commit `.agent/` changes as `docs(agent-context): session wrap — MISSION-001 china strip complete` | All | ❌ No | T-014 | |
| T-016 | Post changelog to Discord channel #hermes-docs (ID: 1501005248205164687) and push mission branch to origin. The changelog should be a clean bullet-point list of all changes made, organized by category (Files Removed, Providers, Config, Tests, Cron). Also push: `git push origin mission/001-china-strip` | All | ❌ No | T-015 | Use `mcp_send_message` with target `discord:1501005248205164687` |

---

## Agent Instructions

- **Start on main:** `git checkout main && git pull origin main` — verify HEAD = `7ba4883`
- **Create branch first (T-002):** `git checkout -b mission/001-china-strip` — all code work happens here
- **Context work (T-001) happens on main before branch:** WS-001 WORKSTREAM.md update commits to main, then create the mission branch
- **Read files before patching** — always read the section you're editing before using patch tool
- **Commit after each task group** — don't accumulate 10 changes before committing
- **Commit format:** `type(MISSION-001/T-XXX): description`
- **Separate .agent/ commits from code commits**
- **If import errors appear at T-011 that can't be fixed in 2 attempts — halt and report**
- **Do NOT merge to main** — push branch only, human reviews the diff

## Execution Log

| Task | Status | Commit | Agent | Notes |
|------|--------|--------|-------|-------|
| T-001 | ✅ Done | 9ba25d6 (main) | sonnet | WS-001 context update |
| T-002 | ✅ Done | mission branch created | sonnet | |
| T-003 | ✅ Done | 25b81d7 | sonnet | 13 adapter files removed |
| T-004 | ✅ Done | dd5fab2 | sonnet | 3 tool files removed |
| T-005 | ✅ Done | 6acdb47 | sonnet | TokenHub + 4 aliases removed |
| T-006 | ✅ Done | cc87a5b | sonnet | dingtalk + feishu deps removed |
| T-007 | ✅ Done | 2e7730e | sonnet | 19 test files removed |
| T-008 | ✅ Done | c969abe | sonnet | config.py scrubbed |
| T-009 | ✅ Done | 88179aa | sonnet | run.py scrubbed |
| T-010 | ✅ Done | 22acd79 | sonnet | display_config + session scrubbed |
| T-011 | ✅ Done | 7d13f1c | sonnet | __init__, webhook, send_message_tool cleaned |
| T-012 | ✅ Done | 1f1fe07 | sonnet | WS-003 WORKSTREAM.md updated |
| T-013 | ✅ Done | n/a (cron) | sonnet | Weekly cron job 2a98d31293a9 created |
| T-014 | ✅ Done | d41be7a | sonnet | WS-002 WORKSTREAM.md updated |
| T-015 | ✅ Done | (session commit) | sonnet | Session file + indexes + CONTEXT.md |
| T-016 | ✅ Done | (push + Discord) | sonnet | Branch pushed, changelog posted |

## Git Summary (filled on completion)
```bash
git diff main...mission/001-china-strip
git log --oneline --grep="MISSION-001"
```

## Outcome
**Completed:** 2026-05-04
**Session File:** `sessions/2026-05-04_200000-mission-001-china-strip.md`
**Merged to:** pending human review of `git diff main...mission/001-china-strip`
**Result:** Full success — all 16 tasks completed. Zero China platform code remains in the fork.

### Follow-on Work
| Item | Route To | Notes |
|------|----------|-------|
| | | |
