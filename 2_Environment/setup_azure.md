# ☁️ Azure Key Vault & Credentials Setup Guide

> **Stage 2: Environment** — Configuration and onboarding instructions for secrets management.

---

## 🔒 Azure Key Vault Setup

All environment variables and secrets must be loaded dynamically from Azure Key Vault at runtime.

**This project uses the existing vault `dp-kv-deliverypilot` — do not create a new Key Vault.**

### 1. Azure Authentication
```bash
# Log in to Azure account
az login

# Set active subscription (subscription owning dp-kv-deliverypilot)
az account set --subscription "Azure subscription 1"
```

### 2. Verify Access to the Existing Vault
```bash
# Confirm the vault is reachable (resource group: deliverypilot-rg)
az keyvault show --name dp-kv-deliverypilot

# List available secret names (no values)
az keyvault secret list --vault-name dp-kv-deliverypilot -o table
```

### 3. Reading Secrets at Runtime
```bash
# Fetch a secret value when needed (never print/log it, never commit it)
az keyvault secret show --vault-name dp-kv-deliverypilot --name "ANTHROPIC-API-KEY" --query value -o tsv
```

### 4. Registering a New Secret (only if the project needs one that doesn't exist yet)
```bash
az keyvault secret set --vault-name dp-kv-deliverypilot --name "NEW-SECRET-NAME" --value "..."
```

---

## 🔑 Secrets Used by This Project

Existing secrets in `dp-kv-deliverypilot` relevant to a video production / AI assistant workflow:

| Secret Name | Purpose |
|-------------|---------|
| `ANTHROPIC-API-KEY` | Claude API access |
| `OPENAI-API-KEY` | OpenAI API access (e.g. Whisper transcription) |
| `GEMINI-API-KEY-PRIMARY` / `GEMINI-API-KEY-SECONDARY` | Google Gemini API access |
| `GOOGLE-IMAGEN-API-KEY` | Google Imagen image generation |
| `FAL-AI-KEY` | fal.ai image generation |
| `YOUTUBE-API-KEY` | YouTube Data API (metadata, uploads, search) |
| `google-oauth-client-id` / `google-oauth-client-secret` / `google-oauth-refresh-token` | Google OAuth (Drive, Calendar, etc.) |
| `canva-mcp-CANVA-CLIENT-ID` / `canva-mcp-CANVA-CLIENT-SECRET` | Canva MCP integration |
| `AXIOM-TOKEN` | Server-side logging, if this project ever needs it |

See [`.env.example`](../.env.example) for the local placeholder mapping and [`.kilo/skills/secrets.md`](../.kilo/skills/secrets.md) for the full rules.

## 🔑 GitHub Actions Integration
To pull secrets into GitHub workflows, the repository needs Azure Service Principal credentials scoped to `dp-kv-deliverypilot`:

1. Create a Service Principal (if one doesn't already exist for this purpose):
   ```bash
   az ad sp create-for-rbac --name "video-asistant-github-sp" --role contributor \
       --scopes /subscriptions/b85b029d-9f7c-4c5a-8939-819480780c5d/resourceGroups/deliverypilot-rg \
       --sdk-auth
   ```
2. Store the JSON output as a GitHub Repository Secret named `AZURE_CREDENTIALS`.
3. In workflows, use the action:
   ```yaml
   - name: Azure Login
     uses: azure/login@v1
     with:
       creds: ${{ secrets.AZURE_CREDENTIALS }}
   - name: Get Key Vault Secrets
     uses: Azure/get-keyvault-secrets@v1
     with:
       keyvault: "dp-kv-deliverypilot"
       secrets: "ANTHROPIC-API-KEY, YOUTUBE-API-KEY"
   ```

---

## 🧪 Verification Checklist
- [ ] Azure CLI successfully authenticated (`az account show`)
- [ ] Active subscription is verified
- [ ] `dp-kv-deliverypilot` is reachable and no new vault was created
- [ ] Zero secret configurations committed to source files
