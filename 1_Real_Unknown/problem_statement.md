# 🎯 Problem Statement

> **Stage 1: Real Unknown** — Clearly define the pain point, gap, or opportunity before starting.

---

## 🔍 Core Problem / Pain Point
*Describe the primary problem you are trying to solve. What is broken, inefficient, or missing?*

- **Current State:** Video production tasks (research, scripting, thumbnails, uploads, metadata, transcripts) are handled manually and scattered across tools with no single assistant tying them together.
- **Ideal State:** An AI assistant that operates in Chrome and via AI models, working from plain markdown sources, that can be asked to help with any part of the video production workflow.
- **The Gap:** No structured project exists yet to define, plan, and automate this workflow end-to-end.

## 👥 Target Audience & Stakeholders
*Who is experiencing this pain point? Who will benefit from the solution?*

- **Primary User:** The project owner (rifaterdemsahin) producing videos for their YouTube channel.
- **Secondary Stakeholders:** None — single-operator project.

## 💡 Proposed Value Proposition
*How does solving this problem add value? What are the high-level benefits?*

- Faster turnaround on video production tasks by delegating repetitive work to an AI assistant.
- A single, markdown-driven source of truth for every stage of production (research → script → assets → publish).
- Reuses existing Chrome automation and AI-model tooling instead of building new infrastructure.

## 🚀 Constraints & Scope Boundaries
*What is explicitly out of scope or a known constraint for this problem definition?*

- No new Azure Key Vault — secrets are read from the existing `dp-kv-deliverypilot` vault only.
- Environment is limited to Chrome + AI models; no new hosting/runtime infrastructure is assumed by default.
- Sources of truth are markdown files, not a database, at this stage.
