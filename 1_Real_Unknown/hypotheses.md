# 🧪 Hypotheses

> **Stage 1: Real Unknown** — Document your initial assumptions and how they will be validated in Stage 7.

---

## 🔍 Core Hypotheses

### Hypothesis 1: Chrome + AI models + markdown sources are sufficient for a useful video production assistant
*No new hosting, database, or backend infrastructure is required to meaningfully help with video production tasks.*

- **Rationale:** Video production tasks (research, scripting, metadata, transcripts) are document- and browser-centric, not compute-heavy — existing Chrome automation and AI-model skills should cover most of the workflow.
- **Validation Method:** Run the first real workflow (TSK-009 in `tasks.md`) end-to-end using only Chrome automation, AI-model calls, and markdown files; note any point where new infrastructure becomes necessary.
- **Linked Test:** [7_Testing_Known/validation_report.md](../7_Testing_Known/validation_report.md)
- **Status:** ⏳ Pending Validation

---

### Hypothesis 2: Reusing the existing Azure Key Vault is sufficient for secrets
*The `dp-kv-deliverypilot` vault already holds the API keys this project needs (Anthropic, OpenAI, Gemini, YouTube, fal.ai, Google OAuth), so no new vault or secret store is required.*

- **Rationale:** A dedicated per-project vault adds operational overhead (RBAC, rotation, cost tracking) without a clear benefit for a single-operator project.
- **Validation Method:** Confirm every secret this project needs during real use resolves via `az keyvault secret show --vault-name dp-kv-deliverypilot`.
- **Linked Test:** [7_Testing_Known/validation_report.md](../7_Testing_Known/validation_report.md)
- **Status:** ⏳ Pending Validation
