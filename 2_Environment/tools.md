# 🧰 Tools Overview — Delivery Pilot Template

> **Stage 2 of 7 (Environment):** A single reference covering **every tool** used in this project — what it does, why it was chosen, and where its secrets live. When a tool is added, changed, or removed, update this document and `architecture.md` together.

---

## 🗺️ The Stack at a Glance

| Layer | Tool | Role | Detail Doc |
|-------|------|------|------------|
| **Frontend hosting** | GitHub Pages | Static site (`index.html`, docs, mockups) | [`github_pages.md`](./github_pages.md) |
| **Edge compute** | Cloudflare Workers | Auth, routing, caching, rate limiting | [`cloudflare_workers.md`](./cloudflare_workers.md) |
| **Backend deployments** | Fly.io | Container-based Python API hosting (Docker) | [`fly_io.md`](./fly_io.md) |
| **Database & data layer** | Supabase | Managed Postgres, auth, realtime, storage, pgvector | [`supabase.md`](./supabase.md) |
| **Server-side logs** | Axiom | Centralized logging, tracing, alerting, dashboards | [`axiom.md`](./axiom.md) |
| **Secrets** | Azure Key Vault | Stores all API keys & credentials | [`setup_azure.md`](./setup_azure.md) |
| **CI/CD** | GitHub Actions | Build, test, deploy pipeline | [`github_pages.md`](./github_pages.md) |
| **AI / Vector** | Kilo Code (local) / Qdrant (big repos) | Semantic search: Kilo Code built-in nomic text indexing for small projects, Qdrant vector DB for large repos | [`setup_ai.md`](./setup_ai.md) |
| **Auto-Fix Agent** | Error-Fix Agent (GitHub Token) | Automated error discovery: visits pages, finds errors, opens GitHub Issues, applies fixes, reports to `6_Semblance/`. Uses GitHub PAT from Azure Key Vault. | [`github_agent.md`](./github_agent.md) |
| **MCP Servers** | GitHub, Azure KV, Browser, Supabase, Axiom, Fly.io, Qdrant | Model Context Protocol servers connecting agents to external tools | [`mcp.md`](./mcp.md) |
| **Superskills** | 6 project skills + system skills | On-demand skill loading: navigation, planning, simulation, deploy, secrets, error-fix | [`superskills.md`](./superskills.md) |
| **AI Chat Links** | Gemini, Claude, Grok | Consumer AI chat web apps — opened in Chrome on request | See [AI Chat Links](#-ai-chat-links-open-in-chrome-on-request) below |
| **Production Web Tools** | Flow Music | Browser-based tools used in the production pipeline — opened in Chrome on request | See [Production Web Tools](#-production-web-tools-open-in-chrome-on-request) below |

---

## 💬 AI Chat Links (open in Chrome on request)

Consumer AI chat web apps used directly in the browser as part of the video production workflow (e.g. cross-checking a script or thumbnail idea across models). Per the **Open Links in Chrome** rule in `agents.md`/`claude.md`/`gemini.md`, when asked to open one of these, always use `open -a "Google Chrome" <url>` — never the OS default browser.

| AI | URL |
|----|-----|
| Google Gemini | https://gemini.google.com/app/ |
| Claude | https://claude.ai/ |
| Grok | https://grok.com/ |

---

## 🎵 Production Web Tools (open in Chrome on request)

Browser-based tools used for specific steps of [`3_Simulation/video_production_pipeline.md`](../3_Simulation/video_production_pipeline.md). Same rule applies — opened via `open -a "Google Chrome" <url>` when asked.

| Tool | URL | Pipeline Step |
|------|-----|---------------|
| Flow Music | https://www.flowmusic.app/ | Step 9 — 🔊 AUDIO (score/waveform) |

---

## 📦 Tool-by-Tool

### 1. GitHub Pages — Frontend Hosting
Serves the static site directly from the repo root. `index.html` **must** stay at the root. Deployed via GitHub Actions. → [`github_pages.md`](./github_pages.md)

### 2. Cloudflare Workers — Edge Compute (optional)
Lightweight edge logic for auth, routing, caching, and rate limiting in front of the backend. → [`cloudflare_workers.md`](./cloudflare_workers.md)

### 3. Fly.io — Container-Based Deployments
Runs the backend as **Docker containers** deployed globally close to users. Hosts Python APIs (FastAPI/Flask), background jobs, and WebSocket servers with persistent processes. This is where backend application code is deployed. → [`fly_io.md`](./fly_io.md)

### 4. Supabase — Database & Backend Features
The **primary database**: managed Postgres plus auth, auto-generated APIs, realtime, storage, and `pgvector`. Backend connects via `DATABASE_URL` / `supabase-py`; the frontend may use the anon key under Row Level Security. → [`supabase.md`](./supabase.md)

### 5. Axiom — Server-Side Logs
The **single source of truth for server-side logs**. Fly.io services and CI ship structured (JSON) events to Axiom for querying (APL), dashboards, and alerting. → [`axiom.md`](./axiom.md)

### 6. Azure Key Vault — Secrets
All credentials for every tool above are stored here and injected as env vars at deploy time. Never commit secrets to git. → [`setup_azure.md`](./setup_azure.md)

### 7. AI Stack — Semantic Search
Two-tier approach for semantic search and embeddings:

- **Kilo Code Local Nomic Text Indexing (default for small projects):** Built-in, zero-setup semantic search using nomic text indexing. The recommended default when using the delivery-pilot-template for smaller repos. No Docker, no external services.
- **Qdrant Vector Database (big repos only):** Full vector database via Docker for large codebases and multi-team projects. Only deploy Qdrant when the project outgrows Kilo Code local indexing.

---

## 🔐 Secrets Map

Every secret below lives in **Azure Key Vault** (one vault per environment: dev/staging/prod) and is referenced by name. See [`.env.example`](../.env.example).

| Tool | Secret(s) | Scope |
|------|-----------|-------|
| Supabase | `SUPABASE_URL`, `SUPABASE_ANON_KEY` | Frontend-safe (anon, with RLS) |
| Supabase | `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL` | Backend only |
| Axiom | `AXIOM_TOKEN`, `AXIOM_DATASET` | Backend / CI only |
| Fly.io | `FLY_API_TOKEN` | CI / deploy only |
| Azure | `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` | CI / runtime |
| AI | `AI_PROVIDER_API_KEY` | Backend only |

---

## 🔄 How Data Flows

```
Browser
  → GitHub Pages (static UI)
  → Cloudflare Workers (edge auth/routing)
      → Fly.io (Python API, in Docker)
          → Supabase  (read/write data, auth)
          → Axiom     (emit structured logs)
          → Azure Key Vault (pull secrets at runtime)
```

---

## ✅ Keeping This Doc Honest

1. Adding a tool? Create its `2_Environment/<tool>.md`, add a row to the tables above, and update [`architecture.md`](./architecture.md).
2. Adding a secret? Add it to the **Secrets Map** and [`.env.example`](../.env.example) (placeholder only).
3. Update the debug-menu config (`navigation_config.json` + HTML fallbacks) so the doc is reachable.
4. Cover it in the `/init-project` setup questionnaire so new projects choose it consciously.
