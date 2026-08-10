# Secrets & Key Vault Skill

Load this skill when handling credentials, environment variables, or Azure Key Vault integration.

## Purpose
Manage secrets securely through the existing Azure Key Vault `dp-kv-deliverypilot` — never expose credentials in code, config, or git history, and never create a new vault for this project.

## Key Files
- `.env.example` — Template for required environment variables (placeholders only, no real secrets)
- `2_Environment/setup_azure.md` — Azure Key Vault setup guide

## Secrets Map
| Secret | Vault | Purpose |
|--------|-------|---------|
| `ANTHROPIC-API-KEY` | `dp-kv-deliverypilot` | Claude API access |
| `OPENAI-API-KEY` | `dp-kv-deliverypilot` | OpenAI API access (e.g. Whisper) |
| `GEMINI-API-KEY-PRIMARY` / `-SECONDARY` | `dp-kv-deliverypilot` | Google Gemini API access |
| `GOOGLE-IMAGEN-API-KEY` | `dp-kv-deliverypilot` | Google Imagen image generation |
| `FAL-AI-KEY` | `dp-kv-deliverypilot` | fal.ai image generation |
| `YOUTUBE-API-KEY` | `dp-kv-deliverypilot` | YouTube Data API |
| `google-oauth-client-id` / `-client-secret` / `-refresh-token` | `dp-kv-deliverypilot` | Google OAuth (Drive, Calendar) |
| `canva-mcp-CANVA-CLIENT-ID` / `-SECRET` | `dp-kv-deliverypilot` | Canva MCP integration |
| `AXIOM-TOKEN` | `dp-kv-deliverypilot` | Logging API token (if ever needed) |

## Rules
- Never store secrets in code, config files, or git history
- **Use the existing vault `dp-kv-deliverypilot` only — do not create a new Key Vault for this or any environment (dev/staging/prod all share it).**
- Load secrets at runtime via `az keyvault secret show --vault-name dp-kv-deliverypilot --name <NAME>`, the Azure SDK, or GitHub Actions `Azure/get-keyvault-secrets`
- When a new secret is needed, check `az keyvault secret list --vault-name dp-kv-deliverypilot` first — it may already exist
- When adding a genuinely new secret, update `.env.example` with the placeholder variable name (no value), then run `az keyvault secret set --vault-name dp-kv-deliverypilot --name "..." --value "..."`
