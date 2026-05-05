---
type: sop
id: SOP-004
title: "Write and Execute a Mission"
project: hermes-fork
status: stable
version: "1.1"
created: 2026-05-04
updated: 2026-05-04
trigger: "When a large, discrete scope of work is ready to be executed autonomously by an agent or swarm"
applies_to: all
---

# SOP-004 — Write and Execute a Mission

**Trigger:** When a large, discrete scope of work is ready to be executed autonomously by an agent or swarm.

---

## Phase 1 — Draft the Mission

1. **Assign an ID** — Check `missions/INDEX.md` for the next `MISSION-XXX` number
2. **Create the file**
   ```bash
   cp .agent/missions/_template/MISSION.md .agent/missions/MISSION-XXX-description.md
   ```
3. **Fill in the mission**
   - Objective — specific, unambiguous end state
   - Scope — in/out
   - Pre-conditions — what must be true before execution
   - Task breakdown — atomic, ordered/parallelized, WS-mapped, dependency-aware
   - Branch name — `mission/XXX-short-name`, base branch (usually `main`)
   - Swarm config — if parallel sub-agents are appropriate
   - Set `status: draft`
4. **Add to `missions/INDEX.md`**
5. **Link mission ID in relevant workstream frontmatter** (`missions:` field)

---

## Phase 2 — Opus Review

1. Load the mission file + relevant workstream(s) into an **Opus** session
2. Opus works through the **Review Checklist** in the mission file
3. Opus fills in **Review Notes** with gaps, risks, or revisions
4. Opus sets the **Decision**: Approved / Revise / Rejected + date
5. If **Revise** → return to Phase 1, update, resubmit
6. If **Approved** → update frontmatter: `status: approved`, `reviewed_date: YYYY-MM-DD`
7. Commit the approved mission file:
   ```bash
   git add .agent/missions/MISSION-XXX-description.md
   git commit -m "docs(agent-context): MISSION-XXX approved by Opus"
   ```

---

## Phase 3 — Execution (Sonnet or smaller)

1. **Create the mission branch**
   ```bash
   git checkout main              # or specified base_branch
   git checkout -b mission/XXX-short-name
   ```
2. Update mission frontmatter: `status: running`
3. Load the approved mission + relevant workstream(s)
4. Execute tasks in defined order, respecting dependencies
5. **Commit conventions** — see `docs/GIT_CONVENTIONS.md`:
   ```bash
   # Code changes
   git commit -m "feat(MISSION-XXX/T-001): description"
   # Context changes
   git commit -m "docs(agent-context): MISSION-XXX T-001 complete, update WS-XXX"
   ```
6. For swarms — spawn sub-agents per the Swarm Configuration table, each on its own branch; merge sub-agent branches together before final merge to main
7. Update the **Execution Log** table after each task
8. **If blocked — halt and report; do not improvise outside mission scope**

---

## Phase 4 — Review & Merge

1. **Generate the mission diff** for human or Opus review:
   ```bash
   git diff main...mission/XXX-name
   git log --oneline --grep="MISSION-XXX"
   ```
2. Review confirms correctness and no scope creep
3. **Merge with no-fast-forward**:
   ```bash
   git checkout main
   git merge --no-ff mission/XXX-name -m "merge(MISSION-XXX): [title] complete"
   git branch -d mission/XXX-name
   ```
4. Update mission frontmatter: `status: complete`, fill in **Outcome** section + merge SHA

---

## Phase 5 — Close Out

1. **Route Follow-on Work** from the mission's `## Follow-on Work` table:
   - WS-specific → add to the workstream's `## Tasks` table
   - Project-level → promote to `CONTEXT.md ## Open Items`
   Do this before writing the session file so the session reflects final state.
2. **Write a session file** — reference `mission: MISSION-XXX` in frontmatter
   - Include the full **Git Summary** block (commits, diff stat, before/after SHA)
3. **Update all touched workstreams** — work log, decisions, issues, task statuses
4. **Update `CONTEXT.md`** — remove mission from `missions:` frontmatter list; add any Open Items promoted in step 1; update Active Missions table
5. **Update `missions/INDEX.md`** — move to Completed table
6. **Commit context updates**:
   ```bash
   git add .agent/
   git commit -m "docs(agent-context): close MISSION-XXX, write session, update workstreams"
   ```
7. **Post summary to Discord**
