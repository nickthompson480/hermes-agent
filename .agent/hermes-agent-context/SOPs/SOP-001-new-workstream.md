---
type: sop
id: SOP-001
title: "Create a New Workstream"
project: hermes-fork
status: stable             # draft | stable | deprecated
version: "1.1"
created: 2026-05-04
updated: 2026-05-04
trigger: "When a new feature, module, or domain of work needs its own tracking"
applies_to: all
---

# SOP-001 — Create a New Workstream

**Trigger:** When a new feature, module, or domain of work needs its own tracking.

---

## Automated Path (preferred)

Use the script — it handles folder creation, template copy, placeholder substitution,
`.gitkeep` files for git-tracked empty dirs, and prints the manual steps remaining:

```bash
python3 .agent/scripts/workstream_create.py \
  --id WS-002 \
  --name "short-slug" \
  --title "Human Readable Title" \
  --owner "Nick Thompson" \
  --spec-section "Section from PROJECT_SPEC"
```

The script will confirm what it created and print the manual steps below that still need
to be done. Skip to step 5.

---

## Manual Path (reference / fallback)

1. **Assign an ID** — Check `workstreams/INDEX.md` for the next available `WS-XXX` number.
2. **Create the folder structure**
   ```bash
   mkdir -p .agent/workstreams/WS-XXX-name/{tasks,decisions,docs}
   touch .agent/workstreams/WS-XXX-name/tasks/.gitkeep
   touch .agent/workstreams/WS-XXX-name/decisions/.gitkeep
   touch .agent/workstreams/WS-XXX-name/docs/.gitkeep
   ```
3. **Copy the template**
   ```bash
   cp .agent/workstreams/_template/WORKSTREAM.md .agent/workstreams/WS-XXX-name/WORKSTREAM.md
   ```
4. **Fill in the frontmatter** — id, title, status, owner, branch (`ws/XXX-short-name`), created date, parent_spec_section.

---

## Steps after creation (both paths)

5. **Add to `workstreams/INDEX.md`** — Append a row in the Active Workstreams table.
6. **Link from `PROJECT_SPEC.md`** — Add a row in the Workstreams table.
7. **Update `CONTEXT.md`** — Add to Active Workstreams table; add the WS ID to the `workstreams:` frontmatter list.
8. **Create the branch**
   ```bash
   git checkout -b ws/XXX-short-name
   ```
9. **Commit the new workstream files**
   ```bash
   git add .agent/workstreams/WS-XXX-name/ .agent/workstreams/INDEX.md .agent/CONTEXT.md .agent/PROJECT_SPEC.md
   git commit -m "docs(agent-context): create WS-XXX — [title]"
   ```
10. **Announce in Discord** — Post a note in the project channel with WS ID and purpose.
