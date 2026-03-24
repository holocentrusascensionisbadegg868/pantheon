# Pantheon Architecture

## How it works

```
┌─────────────────────────────────────────────────────────────┐
│  n8n (Docker, port 5678)                                    │
│                                                             │
│  "Pantheon: Daily Auto Draft"  ← schedule trigger only     │
│   7am → GET /generate → POST /telegram/send-draft          │
│        → POST /draft/{message_id}                          │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP to host.docker.internal:8401
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  pantheon_api.py (Mac host, port 8401, launchd managed)     │
│                                                             │
│  GET  /generate          → researcher.py | writer.py        │
│  POST /telegram/send-draft → sends Telegram message         │
│  POST /draft/{id}        → stores draft in memory           │
│  POST /post/{id}         → posts to X + Threads             │
│                                                             │
│  Background thread: long-polls Telegram getUpdates          │
│    callback_query "post"  → _do_post() → ack               │
│    callback_query "skip"  → ack                             │
│    message "topic: X"     → generate → send-draft           │
└─────────────────────────────────────────────────────────────┘
```

## Why long polling instead of n8n Telegram Trigger

The n8n Telegram Trigger node requires:
1. A credential saved in n8n's DB with the bot token
2. n8n calling Telegram's `setWebhook` on workflow activation
3. A public webhook URL (ngrok) pointing to n8n
4. All three to stay in sync across restarts

When any of these break, inbound Telegram messages silently stop working
with no obvious error. Debugging requires querying n8n's SQLite DB directly.

Long polling in `pantheon_api.py` requires none of this:
- No webhook registration
- No n8n credential management
- No ngrok for inbound traffic
- Works immediately on server restart

The tradeoff is ~1 second response latency on button clicks. Acceptable for a 1-post/day pipeline.

## File locations

| File | Purpose |
|------|---------|
| `scripts/pantheon_api.py` | FastAPI server + Telegram polling loop |
| `scripts/researcher.py` | Fetches RSS headlines, Ollama analysis |
| `scripts/writer.py` | Ollama content generation |
| `scripts/pantheon-post.py` | Posts to X (tweepy) and Threads |
| `scripts/shared.py` | Vault secret fetching |
| `start-api.sh` | Wrapper script for launchd |
| `~/Library/LaunchAgents/com.nexus.pantheon-api.plist` | launchd service (auto-restart) |

## n8n workflows

| Workflow | ID | Purpose | Keep? |
|----------|----|---------|-------|
| Pantheon: Daily Auto Draft | RFMoof7UIKvhccAB | Schedule 7am → generate → send to TG | ✅ Yes |
| Pantheon: Telegram Handler | ix7DO4IoxSBW6XXO | Inbound TG handling | ❌ Deactivated — replaced by polling |

## Secrets (Infisical vault)

All secrets accessed via `nexus-secrets get KEY` or the `with-secrets` wrapper.

| Key | Purpose |
|-----|---------|
| `PANTHEON_TG_BOT_TOKEN` | @pantheon_publisher_bot token |
| `PANTHEON_TG_CHAT_ID` | Your Telegram chat ID |
| `ANTHROPIC_API_KEY` | Not used by pipeline (Ollama is free) |

## Cost

**$0/month** for the AI pipeline. Ollama runs locally (qwen2.5:32b).
The only costs are X API and Threads API (both free at this volume).

## Ops

```bash
# Restart API server
bash ~/Dev-Projects/pantheon/reload-svc.sh

# Check logs
tail -f ~/Dev-Projects/pantheon/logs/pantheon-api.log
tail -f ~/Dev-Projects/pantheon/logs/pantheon-api.err

# Manually trigger a post cycle (bypasses 7am schedule)
# → go to n8n UI, open Daily Auto Draft, click Execute workflow

# On-demand from Telegram
# Send to @pantheon_publisher_bot:
#   topic: AI regulation crackdown
#   gem: andon-cord
#   explore: NVIDIA supply chain
```

## Agent rules (DO NOT violate)

1. **Never add a Telegram Trigger node to any Pantheon n8n workflow.** Inbound Telegram is handled by `pantheon_api.py` polling. Adding a Telegram Trigger will conflict with the polling loop and break everything.

2. **Never add API credentials to n8n for Pantheon bot.** The bot token lives in Infisical and is loaded by `pantheon_api.py` at startup.

3. **Never replace Ollama models with Anthropic API calls** in researcher.py or writer.py. The pipeline runs at $0/month on Ollama intentionally.

4. **n8n is only a scheduler** for Pantheon. It makes HTTP calls to `host.docker.internal:8401`. It does not own any Telegram logic.
