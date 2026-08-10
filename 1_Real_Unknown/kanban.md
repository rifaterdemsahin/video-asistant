# 📋 Project Kanban Board

> **Stage 1 of 7 (Real Unknown):** Track setup tasks, ongoing development, and pilot status.
> This file is a live Kanban board. AI agents and human developers must keep this updated as they do their work.

---

## 📖 How to Use This Kanban

1. **Move Tasks**: Move task items between sections (`Backlog 📥`, `Planned 📋`, `In Progress 🔄`, `In Review 👀`, `Done ✅`) as work progresses.
2. **Assignee**: Designate who is working on the task (e.g., `Claude`, `Gemini`, `Copilot`, `Kilo Code`, or `Human`).
3. **Traceability**: Link each task to its relevant stage documentation or source code (e.g., referencing a setup guide in `2_Environment` or a validation check in `7_Testing_Known`).
4. **Update Logs**: When an AI agent performs a task, they must update this kanban board in the same commit to ensure real-time status accuracy.

---

## 📥 Backlog
*Tasks that are defined but not yet scheduled.*

- [ ] **TSK-009: Define first concrete video-production task**
  - **Assignee:** Human / Claude
  - **Details:** Pick the first real workflow to automate (e.g. transcript → markdown note, thumbnail generation, upload metadata).
  - **Stage Reference:** [1_Real_Unknown/tasks.md](../1_Real_Unknown/tasks.md)

---

## 📋 Planned / To Do
*Tasks scheduled for implementation.*

- [ ] **TSK-005: Setup CI/CD Pipeline**
  - **Assignee:** Claude / DevOps
  - **Details:** Add GitHub Actions workflow to deploy static content to GitHub Pages, gated by smoke tests.
  - **Stage Reference:** [2_Environment/github_pages.md](../2_Environment/github_pages.md)

- [ ] **TSK-006: Wire up AI model + YouTube secrets from Key Vault**
  - **Assignee:** Claude / Security
  - **Details:** Pull `ANTHROPIC-API-KEY`, `YOUTUBE-API-KEY`, `GEMINI-API-KEY-PRIMARY`, `FAL-AI-KEY` from `dp-kv-deliverypilot` at runtime — never commit values.
  - **Stage Reference:** [2_Environment/setup_azure.md](../2_Environment/setup_azure.md)

---

## 🔄 In Progress
*Active tasks currently being worked on.*

*No active tasks in progress.*

---

## 👀 In Review
*Tasks completed and awaiting validation/review.*

*Nothing awaiting review yet.*

---

## ✅ Done
*Verified and completed tasks.*

- [x] **TSK-001: Bootstrap from delivery-pilot-template**
  - **Assignee:** Claude
  - **Details:** Copied the 7-stage template structure, agent files, and toolbox scripts into this repo.
  - **Stage Reference:** [README.md](../README.md)

- [x] **TSK-002: Replace template placeholders**
  - **Assignee:** Claude
  - **Details:** Replaced `{{PROJECT_NAME}}` and related placeholders with `video-asistant` values across `README.md`, `index.html`, `sitemap.xml`, `robots.txt`, and the Supabase config.
  - **Stage Reference:** [index.html](../index.html)

- [x] **TSK-003: Define project OKRs**
  - **Assignee:** Claude
  - **Details:** Documented the problem statement and OKRs — video production assistant, Chrome + AI models, markdown sources.
  - **Stage Reference:** [1_Real_Unknown/okrs.md](../1_Real_Unknown/okrs.md)

- [x] **TSK-004: Point secrets at existing Key Vault**
  - **Assignee:** Claude
  - **Details:** Updated secrets docs to reference the existing `dp-kv-deliverypilot` vault instead of creating a new one.
  - **Stage Reference:** [2_Environment/setup_azure.md](../2_Environment/setup_azure.md)

---

## ⚙️ Maintenance

- [ ] Go over git commits periodically, reread changed files, and create/update Kanban tasks to stay on track
- [ ] Update the environment folder > 1_Real_Unknown
- [ ] Update the environment folder > 2_Environment
- [ ] Add new features incoming as visuals folder > 3_Simulation
- [ ] Add new ways of doing the implementation  to formula folder > 4_Formula
- [ ] Update the Symbols and pay technical debt > 5_Symbols
- [ ] Add new errors in semblance  > 6_Semblance
- [ ] Update the tests folder > 7_Testing_Known
