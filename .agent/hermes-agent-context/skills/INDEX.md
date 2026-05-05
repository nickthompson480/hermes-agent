---
type: index
title: "Skills Index"
project: hermes-fork
updated: 2026-05-04
---

# Skills & Knowledge Base

Project-level skills, patterns, and reusable knowledge specific to this project.

---

| Skill | Description | Workstream |
|-------|-------------|------------|
| [upstream-tracking](./upstream-tracking.md) | Workflow for monitoring upstream NousResearch/hermes-agent commits, triage categories, cherry-pick process, and China blocklist | WS-003 |

---

## How to Add a Skill

**Project skills are the default.** When a repeatable pattern or approach emerges,
capture it here first. Only escalate to a global Hermes skill if:
- A global skill already exists and needs updating based on what you learned, OR
- The skill is clearly generic enough to benefit other unrelated projects

### Steps
1. Copy `_template/SKILL.md` → `skills/skill-name.md`
2. Fill in frontmatter: title, tags, scope, originating workstream
3. Add it to the index table above
4. Reference it from the relevant workstream's `## Docs & References` section
