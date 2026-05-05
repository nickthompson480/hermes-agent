---
name: upstream-tracking
title: "Upstream Hermes Tracking Process"
type: skill
status: stable
scope: project
project: hermes-fork
created: 2026-05-04
updated: 2026-05-04
tags: [upstream, git, triage, fork-maintenance]
---

# Upstream Tracking — NousResearch/hermes-agent

This skill governs how the hermes-fork project monitors upstream changes and decides what to pull.

**Upstream remote:** `upstream` → `https://github.com/NousResearch/hermes-agent`
**Our fork:** `origin` → Nick's GitHub fork
**Baseline SHA:** recorded in `.agent/CONTEXT.md` after WS-001 completes

---

## Triage Categories

Every upstream commit or PR falls into one of four buckets:

| Category | Label | Action |
|----------|-------|--------|
| 🇨🇳 China integration | `strip` | Already removed — skip. Reject if re-introduced. |
| 🧹 Cleanup / refactor | `review` | Evaluate — likely want if it touches files we kept |
| 🐛 Bug fix | `pull` | Cherry-pick unless it touches stripped files |
| ✨ New feature | `evaluate` | Read the diff, decide based on relevance and scope |
| 📦 Dep / build | `review` | Check if it affects stripped extras or our kept ones |
| 🔒 Security patch | `pull` | Always pull — highest priority |

---

## Upstream Review Workflow

### Step 1 — Fetch upstream changes
```bash
cd ~/code/projects/hermes-fork
git fetch upstream
git log upstream/main --oneline --since="2 weeks ago" --not main
```

Or since last recorded review SHA (stored in CONTEXT.md `upstream_last_reviewed`):
```bash
git log upstream/main --oneline ^<LAST_REVIEW_SHA>
```

### Step 2 — Summarize and triage
For each commit, assign a category label (see table above). Key signals:
- Mentions `yuanbao`, `weixin`, `wecom`, `qqbot`, `dingtalk`, `feishu` → `strip`, skip
- Touches `gateway/platforms/`, `tools/`, `agent/`, `hermes_cli/` → likely relevant
- `pyproject.toml` changes → check if they affect our kept deps

Quick scan script (see `scripts/upstream-diff.sh`):
```bash
bash .agent/scripts/upstream-diff.sh
```

### Step 3 — Cherry-pick decision checklist

Before cherry-picking any commit, answer:
- [ ] Does it touch any stripped file? (if yes → skip or manually adapt)
- [ ] Does it introduce a new China platform dependency? (if yes → reject)
- [ ] Does it conflict with our strip commits? (if yes → resolve manually)
- [ ] Is it a security patch? (if yes → always pull)
- [ ] Does it change the skill system, tool registry, or cron core? (if yes → high value, pull)

### Step 4 — Apply changes
```bash
# Single commit
git cherry-pick <sha>

# Range
git cherry-pick <oldest_sha>^..<newest_sha>

# On conflict
git cherry-pick --continue   # after resolving
git cherry-pick --abort      # to bail out
```

Commit format for cherry-picks:
```
chore(upstream): cherry-pick <short-sha> — <original message>

Upstream: NousResearch/hermes-agent@<full-sha>
Original author: <name>
```

### Step 5 — Record review
After reviewing a batch, update `CONTEXT.md`:
```yaml
upstream_last_reviewed: <SHA of last upstream commit reviewed>
upstream_last_reviewed_date: YYYY-MM-DD
```

Then log in WS-003 work log with summary of what was pulled/skipped.

---

## Automated Monitoring (Cron)

A cron job runs weekly to fetch upstream and report new commits. See the cron job named `hermes-upstream-monitor` in Hermes cron config.

Output delivered to #hermes-fork with:
- Count of new upstream commits since last review
- Categorized summary (how many bug fixes, features, China-specific, etc.)
- Any security-relevant commits flagged immediately

---

## China Integration Blocklist

These files/directories are stripped. If an upstream commit modifies them, it is auto-categorized as `strip` and skipped:

```
gateway/platforms/yuanbao.py
gateway/platforms/yuanbao_media.py
gateway/platforms/yuanbao_proto.py
gateway/platforms/yuanbao_sticker.py
gateway/platforms/weixin.py
gateway/platforms/wecom.py
gateway/platforms/wecom_callback.py
gateway/platforms/wecom_crypto.py
gateway/platforms/qqbot/
gateway/platforms/dingtalk.py
gateway/platforms/feishu.py
gateway/platforms/feishu_comment.py
gateway/platforms/feishu_comment_rules.py
tools/yuanbao_tools.py
tools/feishu_doc_tool.py
tools/feishu_drive_tool.py
skills/yuanbao/
skills/feishu*/
tests/test_yuanbao*.py
tests/test_feishu*.py
```

Also blocklist in `pyproject.toml` optional extras:
- `dingtalk` extra (`dingtalk-stream`, `alibabacloud-dingtalk`)
- `feishu` extra (`lark-oapi`)
- Tencent TokenHub provider in `hermes_cli/providers.py`

---

## Pitfalls

- **Cherry-pick order matters** — apply oldest→newest. Reversing order causes cascading conflicts.
- **Test after every batch** — run `pytest tests/` after pulling a batch before committing.
- **Our strip commits must stay on top** — if upstream reverts a China integration removal, our strip commits will conflict. Resolve by keeping our version (`git checkout --ours <file>`).
- **New China integrations in upstream** — upstream may add new CN platforms. Always `grep` for new gateway adapters in upstream diffs before pulling pyproject.toml changes.
- **Dep changes** — upstream may bump a dep version in a commit that also touches a stripped file. Split the cherry-pick manually: apply only the non-China hunk.
