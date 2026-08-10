# 🎬 DeliveryPilot Video Production Framework — Pipeline

> **Stage 3: Simulation** — This is the canonical, real-world video production pipeline this project assists with. Sourced from the author's own workflow index in Canva.

**Source of truth:** [Canva — "aug 9 - video 1 mvp animation"](https://www.canva.com/design/DAHRZe5KBoA/OJU0sL318CozUaTBpkdT2g/edit) (page 1 = index + infographic brief, 105 pages total). Update this file whenever that index changes. In Canva, open the **Pages** panel for a top-down grid view of all pages at once instead of scrolling the single-page editor.

---

## The 16-Step Index

| # | Title | Phase | Flow-Tool / Output |
|---|-------|-------|---------------------|
| 0 | 📂 INDEX | Meta Layer | Update workflow (this table) |
| 1 | 📐 ARCHITECTURE | Planning | Infographic — define structure & narrative flow |
| 2 | PLAN | Pre-Production | Script prompt and AI voiceover planning |
| 3 | 🎨 ASSETS | Asset Generation | Find and create with Google (Flow) / Postit batch AI |
| 4 | 👥 COHORT | Production | Record and do — screen/voiceover capture |
| 5 | GAPS | Review | Rewatch footage and find gaps before assembly |
| 6 | 🔧 ASSEMBLY | Timeline Composition | Place assets on the timeline (rough layout, Canva Video) |
| 7 | ✨ POLISH | Hand-Off | Take it to DaVinci (prepare for post-production) |
| 8 | 🧪 REFINEMENT | Editing | Do the cuts — trim clips, fix timing, remove gaps |
| 9 | 🔊 AUDIO | Audio Sync | Score them — waveform alignment, layering, mixing |
| 10 | 🎨 EDIT COLOR | Color & GFX | Graphics — color grading & overlays (DaVinci) |
| 11 | 🖼️ THUMBNAIL | Thumbnail Generation | Gemini create / Postit |
| 12 | 📤 EXPORT | Rendering | Extract — final export (1080p/4K) |
| 13 | 🏷️ METADATA | SEO Prep | Gemini create — marketing plan, analytics retention |
| 14 | WIG | Goal-Setting | DX 4 levels *(likely "Wildly Important Goal" per the 4 Disciplines of Execution — unconfirmed, ask before relying on this)* |
| 15 | TACTICS | Execution | Hands-on |

Steps 0–13 come with full phase/color/description detail from the original design brief (below). Steps 14–15 were added to the live index after the brief was written — their exact intent needs confirming with the author before automating around them.

---

## Phase Detail (from the design brief, steps 0–13)

| Step | Phase | Icon | Color | Description |
|------|-------|------|-------|--------------|
| 0 | Meta Layer | ⟳ | Gray | Workflow orchestration & version control |
| 1 | Planning | 📐 | Strategic Blue | Define structure & narrative flow |
| 2 | Pre-Production | 🎙️ | Soft Purple | Script prompt & AI voiceover planning |
| 3 | Asset Gen. | ✨ | Bright Teal | Find & create visual assets |
| 4–5 | Production | 🎬 | Red/Coral | Screen recording, voiceover capture, review (record & rewatch) |
| 6 | Timeline Comp. | 🧩 | Orange | Place assets on timeline (rough layout) |
| 8 | Editing | ✂️ | Deep Teal | Trim clips, fix timing, remove gaps |
| 7 | Hand-Off | → | Purple/Gold | Prepare for post-production |
| 9 | Audio Sync | 〰️ | Bright Green | Audio alignment, layering, mixing |
| 10 | Color & GFX | 🎨 | Magenta | Color grading & graphic overlays |
| 11 | Thumbnail Gen. | 🖼️ | Bright Yellow/Gold | AI-powered thumbnail creation |
| 12 | Rendering | ⬇️ | Deep Blue | Final export (1080p/4K) |
| 13 | SEO Prep | 🏷️ | Teal | AI-generated titles, descriptions, tags |
| 13 | Analytics | 📊 | Vibrant Cyan | Track engagement & retention metrics |

**Revision loop:** a bidirectional loop is designed between Step 6 (Refinement) and Step 9/10 (Color grading) — cuts and color grading iterate on each other, not strictly linear.

**Production trio:** Steps 4–5–6 (Cohort → Gaps → Assembly) are visually clustered — capture → review → rough-assemble happens as one tight loop before hand-off to DaVinci.

---

## How This Maps to the video-asistant Assistant

This is the workflow the assistant (this project) should eventually help with, step by step. Candidate skill mapping (see [`2_Environment/superskills.md`](../2_Environment/superskills.md)):

| Step | Candidate Skill(s) |
|------|---------------------|
| 2 PLAN | Claude drafting scripts/prompts directly |
| 3 ASSETS | `image-generation` (fal.ai), Google tools |
| 4–5 COHORT / GAPS | `video-transcribe`, `video-to-obsidian-note` (rewatch via transcript + screenshots) |
| 9 AUDIO / 10 EDIT COLOR / 7 POLISH | Chrome automation into DaVinci Resolve web/UI where applicable, or manual (outside Chrome+AI scope for now) |
| 11 THUMBNAIL | `image-generation`, Canva MCP |
| 13 METADATA | Claude-drafted titles/descriptions/tags, `claude-in-chrome` to publish via YouTube Studio |

Steps that require native desktop apps (DaVinci Resolve editing itself) are out of scope for the Chrome + AI models environment defined in [`1_Real_Unknown/problem_statement.md`](../1_Real_Unknown/problem_statement.md) — this assistant supports the steps around the edit, not the NLE itself.

---

## Next Step

See `1_Real_Unknown/tasks.md` TSK-009 — pick one step above (recommended: Step 13 METADATA, or Step 4–5 COHORT/GAPS via `video-transcribe`) and simulate + spec it before implementing.
