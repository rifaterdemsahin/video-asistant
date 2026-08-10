#  Tasks & Phases

> **Stage 1: Real Unknown** — Project phases and task breakdown managed by the **Real Agent**. Each task is assigned to a specific agent. Complex tasks are coordinated by the Real Agent across multiple agents.

## Phase 1: Bootstrap (Completed)

| ID | Task | Agent | Done |
|----|------|-------|------|
| TSK-001 | Bootstrap project from `delivery-pilot-template` (7-stage folders, agent files, toolbox) | Real Agent | [x] |
| TSK-002 | Replace template placeholders with `video-asistant` project values | Symbols Agent | [x] |
| TSK-003 | Define project OKRs and problem statement (video production assistant) | Real Agent | [x] |
| TSK-004 | Point secrets docs at existing Azure Key Vault `dp-kv-deliverypilot` (no new vault) | Environment Agent | [x] |
| TSK-005 | Rebuild navigation menus and pass smoke tests | Environment Agent | [x] |

## Phase 2: Skills & Environment (In Progress)

| ID | Task | Agent | Done |
|----|------|-------|------|
| TSK-006 | Catalog video-production skills sourced from popular GitHub repos in `2_Environment/superskills.md` | Environment Agent | [ ] |
| TSK-007 | Document Chrome + AI-model environment setup for video production workflows | Environment Agent | [ ] |
| TSK-008 | Deploy to GitHub Pages and verify | Symbols Agent | [ ] |

## Phase 3: Video Production Workflows (In Progress)

| ID | Task | Agent | Done |
|----|------|-------|------|
| TSK-009 | Document the real 16-step video production pipeline (sourced from the author's Canva index) | Simulation Agent | [x] |
| TSK-010 | Pick the first step to automate (candidate: Step 13 METADATA, or Step 4–5 COHORT/GAPS via `video-transcribe`) | Real Agent | [ ] |
| TSK-011 | Spec and implement the first workflow step | Formula / Symbols Agent | [ ] |

## Task Management Rules

1. **Real Agent owns this file** — breaks the project into phases and tasks, assigns agents, coordinates complex tasks
2. **Every task names its agent** — the Agent column identifies which stage agent is responsible for execution
3. **Status tracking**: `[ ]` Pending, `[x]` Completed, `[~]` In Progress, `[!]` Blocked
4. **Link to specs** — tasks that implement a spec should reference the SPEC-XXX number
5. **Task granularity** — a task should be completable in a single coding session
