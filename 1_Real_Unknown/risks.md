#  Project Risks

> **Stage 1: Real Unknown** — Track active risks, solved risks, and the risk update log. Add new risks with every project update and mention those that are solved.

## Risk Matrix

| Severity | Symbol | Meaning |
|----------|--------|---------|
| Critical | 🔴 | Blocks delivery — must resolve immediately |
| High | 🟠 | Significantly impacts quality or timeline |
| Medium | 🟡 | Should be addressed in current milestone |
| Low | 🟢 | Monitor — address when convenient |

---

## ⚠️ Active Risks

### R-001: Azure Key Vault Unavailability
- **Status:** 🟡 Active
- **Severity:** Medium
- **Likelihood:** Low (Azure SLA is high, but network/auth issues can occur)
- **Impact:** Agents cannot retrieve `ANTHROPIC-API-KEY`, `YOUTUBE-API-KEY`, or other secrets from `dp-kv-deliverypilot` — automated workflows fail.
- **Trigger:** Azure outage, expired credentials, network partition, missing `az login` session
- **Mitigation:** Verify `az account show` / `az keyvault secret list --vault-name dp-kv-deliverypilot` before relying on a secret at runtime.
- **Last Updated:** 2026-08-10

### R-002: CDN Dependency — Frontend Degradation
- **Status:** 🟡 Active
- **Severity:** Medium
- **Likelihood:** Low (CDN uptime is high, but outages happen)
- **Impact:** If the CDN goes down, FontAwesome icons, PrismJS highlighting, and Google Fonts break in `index.html` / `markdown_renderer.html`.
- **Trigger:** CDN outage affecting `cdnjs.cloudflare.com` or `fonts.googleapis.com`
- **Mitigation:** Track CDN status; consider local fallback assets if this becomes a recurring issue.
- **Last Updated:** 2026-08-10

---

## ✅ Solved Risks

### R-S01: No GitHub Actions Workflow
- **Status:** ✅ Solved (2026-08-10)
- **Severity:** Was 🟠 High
- **Risk:** GitHub Pages would not deploy via CI, and smoke tests would not gate deploys.
- **Resolution:** `.github/workflows/static.yml` carried over from the template — `smoke` job runs the SPEC-008 runner, `deploy` job requires it (`needs: smoke`).
- **Verification:** Workflow file present at bootstrap time; `smoke_test.py` passes 10/10 locally.

### R-S02: GitHub Pages Not Enabled (was R-004)
- **Status:** ✅ Solved (2026-08-10)
- **Severity:** Was 🟡 Medium
- **Risk:** `.github/workflows/static.yml` existed and gated on smoke tests, but Pages was not yet enabled, so the site was not actually live.
- **Resolution:** Enabled Pages via `gh api repos/rifaterdemsahin/video-asistant/pages -X POST -f build_type=workflow` (Source: GitHub Actions), then re-ran the deploy workflow (run `31427477900`) — both `smoke` and `deploy` jobs succeeded.
- **Verification:** `python3 5_Symbols/toolbox/smoke_test.py --base-url https://rifaterdemsahin.github.io/video-asistant/` → 11/11 passed, including "Deployed Site Reachable" (HTTP 200). Root page and `5_Symbols/markdown_renderer.html` both confirmed live via `curl`.

---

## 📋 Risk Update Log

| Date | Update | Risk ID | Change |
|------|--------|---------|--------|
| 2026-08-10 | Project bootstrapped from delivery-pilot-template | R-001 → R-003 | Initial risk assessment carried forward from template + new CI/CD gap identified |
| 2026-08-10 | GitHub Pages enabled and deploy verified live | R-004 | Solved → R-S02: Pages enabled (build via Actions), workflow re-run green, cloud smoke test 11/11 |

---

## Risk Review Cadence

- **Every project update** — Add new risks, update existing ones, move solved risks to the Solved section
- **Every milestone completion** — Review all active risks, re-evaluate severity/likelihood
- **Smoke test failures** — If a smoke test catches a new class of error, create a risk entry
- **Tool changes** — When adding or removing a tool, evaluate and log new risks
