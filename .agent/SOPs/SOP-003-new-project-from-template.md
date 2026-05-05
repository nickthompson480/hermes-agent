---
type: sop
id: SOP-003
title: "Spin Up a New Project from Template"
project: hermes-fork
status: stable
version: "1.0"
created: 2026-05-04
updated: 2026-05-04
trigger: "Starting a new proof of concept or project"
applies_to: all
---

# SOP-003 — Spin Up a New Project from Template

**Trigger:** Starting a new proof of concept or project.

---

## Steps

### 0. Verify git identity (first-time setup only)
```bash
git config --global user.name   # should return your name
git config --global user.email  # should return your email
```
If blank, set them before any commits:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 1. Copy the template
```bash
cp -r ~/code/projects/project-template ~/code/projects/[new-project-name]
cd ~/code/projects/[new-project-name]
```

### 2. Initialize git
```bash
git init
git add .
git commit -m "init: project scaffold from template"
```

### 3. Update `CONTEXT.md` frontmatter
- Set: title, project slug, status (`planning`), created date, owner, folder path

### 4. Update `PROJECT_SPEC.md` frontmatter + body
- Set: title, project slug, created date, owner
- Fill in: Overview, Goals, Tech Stack

### 5. Create a Discord channel
- Right-click your server → **Add Channel** → name it `[project-name]`
- Enable Developer Mode → right-click channel → Copy ID
- Add channel URL + ID to `CONTEXT.md` frontmatter

### 6. Create the first workstream
- Follow **SOP-001** to create WS-001 for the initial scope

### 7. Tell the AI
- Share the project folder path and the Discord channel link
- The AI will maintain context and log sessions to the right place
