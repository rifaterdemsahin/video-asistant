# 🧰 Superskills Requirements

> **Stage 2: Environment** — The superskills catalog defining every loadable skill required for this project's agents to operate. Skills are loaded on-demand via the `skill` tool to avoid loading full project context.

## What are Superskills?

Superskills are focused, self-contained instruction files that agents load on-demand. Instead of reading the entire project context every time, an agent loads only the skills relevant to the current task. Each skill encapsulates a specific workflow, the files it needs, and the rules that apply.

Skills are defined as `.md` files in `.kilo/skills/` and are loaded via the `skill` tool.

## Required Superskills (Project-Specific)

These skills are defined in `.kilo/skills/` and are essential for the delivery-pilot-template workflow:

| Skill | File | Purpose | Load When |
|-------|------|---------|-----------|
| **navigation** | `.kilo/skills/navigation.md` | Two-menu architecture sync, debug menu config | Adding/modifying markdown files in any stage |
| **planning** | `.kilo/skills/planning.md` | Thinking gate, specs system, approval cascade | Before writing any code or specs |
| **simulation** | `.kilo/skills/simulation.md` | Design-first workflow: create images before code | Creating UI mockups or visual designs |
| **deploy** | `.kilo/skills/deploy.md` | Git commit-push-deploy workflow, smoke test gate | Committing, pushing, or deploying changes |
| **secrets** | `.kilo/skills/secrets.md` | Azure Key Vault integration, secrets management | Handling credentials or environment variables |
| **error-fix** | `.kilo/skills/error-fix.md` | Automated error scanning, GitHub Issue creation, fix application | Running smoke tests or fixing detected errors |

## Required Superskills (Claude/System)

These skills are referenced in `4_Formula/.claude/skills.md` and are required for the full self-learning loop:

| Skill | Purpose | Stage |
|-------|---------|-------|
| `code-review` | Review diffs for bugs before commits | 5, 7 |
| `verify` | Confirm features work in browser | 7 |
| `security-review` | Audit for secrets exposure, XSS, misconfig | 5, 7 |
| `run` | Launch static site and observe navigation | 3, 7 |
| `image-generation` | Generate diagrams, visuals, mockups | 3 |
| `github-blog-post` | Publish retrospectives and milestone reports | 6, 7 |

## Video Production Skills (Project-Specific)

This project's objective is to act as a **video production assistant** (Chrome + AI models, markdown sources). The following user-level skills are already installed (`~/.claude/skills/`) and available to any agent working in this repo — no vendoring needed, they load the same way as project skills:

| Skill | Purpose | Load When |
|-------|---------|-----------|
| `video-transcribe` | Download a video (e.g. YouTube) and transcribe it with Whisper | Turning a video into text/subtitles |
| `video-to-obsidian-note` | Download, transcribe, screenshot every 10s, and assemble a self-contained markdown note | Producing a markdown source doc from a video |
| `image-generation` | Generate images via fal.ai (thumbnails, diagrams, visuals) | Creating thumbnails or `3_Simulation/` visuals |
| `gdrive-search` / `gdrive-scan` | Search / summarize the Second Brain Google Drive | Pulling reference material or prior art |
| `github-blog-post` | Publish a post to rifaterdemsahin.com | Publishing a write-up derived from a video |
| `claude-in-chrome` | Automate Chrome — click, fill forms, screenshot, read console | Any browser-driven step (YouTube Studio, Canva, etc.) |

### Sourced From Popular GitHub Repos

Reviewed for future adoption — not vendored into this repo yet (third-party skill code should be read before being trusted with file/shell access):

| Repo | What it adds | Notes |
|------|--------------|-------|
| [anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic Agent Skills (docs, pdf, pptx, xlsx handling) | Canonical source; check here first before adding a new skill |
| [wilwaldon/Claude-Code-Video-Toolkit](https://github.com/wilwaldon/Claude-Code-Video-Toolkit) | FFmpeg post-processing, YouTube clipping, screen recording, Remotion/Manim programmatic video | Closest match to this project's editing needs |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | `/watch` — download, extract frames, transcribe any video in one command | Overlaps with `video-transcribe`; useful for frame-level analysis |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | Curated index of 50+ verified skills | Browse here when a new capability is needed |

**Rule:** before adding a skill from an external repo, read its source, confirm it doesn't exfiltrate data or run unreviewed remote code, then vendor it under `.claude/skills/<name>/` in this repo and add it to the tables above.

## Skill Dependencies

Some skills depend on each other or on specific MCP servers:

| Skill | Depends On | MCP Servers Needed |
|-------|-----------|-------------------|
| error-fix | secrets, deploy | GitHub, Azure Key Vault, Browser |
| secrets | — | Azure Key Vault |
| deploy | — | GitHub, File System |
| planning | — | File System |
| simulation | — | File System |
| navigation | — | File System |

## Skill → Stage Mapping

```
1_Real_Unknown  →  planning (scan & map OKRs)
2_Environment   →  navigation (sync menus), secrets (setup)
3_Simulation    →  simulation (design images), image-generation
4_Formula       →  planning (specs + thinking log)
5_Symbols       →  deploy (commit/push), code-review, security-review, video-transcribe, video-to-obsidian-note, claude-in-chrome
6_Semblance     →  error-fix (log errors/fixes), github-blog-post
7_Testing_Known →  deploy (smoke test gate), verify, run
```

## Skill Loading Workflow

When an agent needs to perform a task:

```
1. Identify the task type (e.g., "commit and push changes")
2. Load the relevant skill (e.g., deploy skill)
3. Skill provides focused instructions and context
4. Agent executes the task following skill workflow
5. Skill context is unloaded — minimal memory footprint
```

## Creating a New Superskill

1. Determine the workflow that needs encapsulation
2. Create `.kilo/skills/<skill-name>.md` with:
   - **Purpose**: What the skill does
   - **Key Files**: Files the skill needs to reference
   - **Workflow**: Step-by-step instructions
   - **Rules**: Guardrails and policies specific to this skill
3. Register in `kilo.json` under the `skills` array
4. Add to the Required Superskills table above
5. Update this file's Skill → Stage Mapping
6. Commit and push the new skill file

## Rules

- **Skills are self-contained** — each skill is loadable independently
- **No duplication** — if a workflow exists in a skill, reference it; don't repeat
- **Keep skills updated** — when project rules change, update the corresponding skill
- **Skills inherit coordinator rules** — all skills follow `agents.md` coordinator rules
- **Minimum context** — load only the skills needed for the current task
