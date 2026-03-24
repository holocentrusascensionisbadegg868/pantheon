# Pantheon Social Pipeline — Scaled Architecture
**Date:** 2026-03-24
**Status:** Approved for implementation

---

## Overview

Scale the Pantheon social content pipeline from a manual Python script into an automated, timely, research-driven system that connects current news to historical patterns via Pantheon gems. One post per day, always human-approved before publishing.

**Design principle:** Fewer services, fewer keys, fewer things to forget. Everything runs on infrastructure already in place.

---

## Services Used

| What | Service | Vault Key |
|---|---|---|
| Intelligence + web search | Anthropic API (direct) | `ANTHROPIC_API_KEY` |
| Orchestration + scheduling | n8n (already running) | `N8N_API_KEY` |
| Trigger + approval gate | Telegram bot | `PANTHEON_TG_BOT_TOKEN` |
| Publishing | X API + Threads API | `PANTHEON_X_*` / `PANTHEON_THREADS_*` |

No new accounts. No OpenRouter. No Serper.

---

## Architecture

```
TRIGGERS
├── Cron (7am daily, auto mode)
├── Telegram message → n8n webhook (on the go)
└── CLI: pantheon-post.py --gem X / --topic X (at desk)
         │
         ▼
RESEARCHER AGENT (researcher.py)
  Claude + native web_search tool
  • Scans news in monitored domains (AI, geopolitics, markets, tech)
  • Matches news story to strongest Pantheon gem
  • Digs historical precedent: who used this pattern, when, outcome
  • Identifies the open loop: what wasn't resolved, what's cycling again
  • Output: structured research brief (JSON) written to stdout
         │  (piped via stdin)
         ▼
WRITER AGENT (writer.py)
  Claude, no tools, pure generation
  • Receives research brief via stdin
  • Writes X post (hook + open loop, ≤280 chars)
  • Writes Threads post (full 5-part arc, ≤500 chars)
  • Output: x_post, threads_post, subject_line (JSON) written to stdout
         │
         ▼
HUMAN GATE (Telegram HITM)
  n8n sends draft preview with ✅ Post / ❌ Skip buttons
  User can also reply with edited text to override
         │
         ▼
PUBLISHER
  Post to X + Threads → confirm in Telegram
```

---

## Researcher Agent

**File:** `scripts/researcher.py`

**Interface:** CLI tool. Called by n8n Execute Command and by `pantheon-post.py` via subprocess. Outputs JSON to stdout.

**Inputs (CLI args):**
```
--mode auto|gem|topic
--arg  <gem-name> | <free-form topic>   # omit for auto
```

**Gem library strategy:** Load all `patterns/*/pattern.md` files, extract gem name + first 300 characters (name, tagline, core pattern) as a summary list. Pass all summaries to Claude for matching. Once Claude identifies the best match, load that gem's full `pattern.md` for the historical research phase. This keeps the matching prompt manageable (~18K chars for 54 gems at 300 chars each) while giving the researcher full context for the gem it selects.

**Process:**
1. If `auto`: use `web_search` to scan monitored domains for top current stories
2. Load gem summaries (name + 300-char extract per gem)
3. Claude matches the news story to the strongest gem
4. Load full `pattern.md` for the matched gem
5. Web search for historical precedents of that gem in action
6. Identify the open loop — what the pattern revealed but didn't resolve

**Model:** `claude-sonnet-4-6` with `web_search_20250305` tool enabled. This tool requires the `anthropic-beta: web-search-2025-03-05` header in the API call.

**Output (stdout JSON):**
```json
{
  "current_event": "...",
  "gem_name": "andon-cord",
  "gem_summary": "...",
  "historical_precedent": "...",
  "historical_outcome": "...",
  "open_loop": "...",
  "monitored_domains": ["AI", "tech industry"]
}
```

**Monitored domains (auto mode):** AI/ML industry, geopolitics, markets/finance, tech industry, science/medicine

---

## Writer Agent

**File:** `scripts/writer.py`

**Interface:** CLI tool. Reads research brief JSON from **stdin**. Outputs JSON to stdout. Called by n8n Execute Command (piped from researcher output) and by `pantheon-post.py` via subprocess pipe.

**Do not pass the research brief as a shell argument** — JSON with quotes and newlines will break shell escaping. Always pipe via stdin:
```bash
python3 researcher.py --mode auto | python3 writer.py
```

**Process:** Single Claude call, no tools. Receives research brief, generates both posts.

**Content arc:**
1. **HOOK** — drop the reader mid-scene. Something's happening NOW. No dates, no "Did you know."
2. **HISTORICAL MIRROR** — same pattern, different century. Who faced this before.
3. **THE GEM** — name the pattern. This is what it's called in Pantheon.
4. **THE OUTCOME** — what happened last time. What the pattern produced.
5. **THE OPEN LOOP** — the challenge. History handed us the answer. The loop didn't close. This is where the reader leans forward.

**X post:** Hook + open loop only. One punch. ≤280 chars. `#Pantheon` at end.

**Threads post:** Full arc, 5-7 sentences, flowing prose. ≤500 chars (Threads API limit). Ends with pointer: *"This pattern lives in Pantheon as [gem-name] — and it's still open."*

**Rules (hard constraints):**
- No em-dashes
- No "fascinating" or "remarkable" as adjectives
- No bullet points — flowing prose only
- No clean resolution — the loop stays open
- Sound like a smart friend who just discovered something, not a history professor

**Model:** `claude-sonnet-4-6`, no tools

**Output (stdout JSON):**
```json
{
  "x_post": "...",
  "threads_post": "...",
  "subject_line": "one-line description"
}
```

---

## n8n Workflows

**n8n owns the Telegram bot entirely.** No polling conflicts. Python scripts are pure CLI tools — pipe researcher stdout into writer stdin, parse final JSON output.

### Callback-wait mechanism

n8n does not natively suspend mid-execution to wait for a Telegram button press. The solution: use the **n8n Wait node** configured with a webhook resume URL. When the Wait node is reached, n8n suspends the execution and stores a resume webhook URL. The Telegram inline keyboard buttons are configured to POST to that resume URL when pressed. n8n then continues execution from the Wait node with the callback data.

This requires the n8n instance to be reachable from Telegram's servers (already true via ngrok or public IP in this setup).

### Execute Command strategy

n8n's Execute Command node runs a single shell command — it does not natively pipe one node's stdout as another node's stdin. The researcher and writer are chained in a **single Execute Command node** as a shell pipe:

```bash
python3 scripts/researcher.py --mode auto | python3 scripts/writer.py
```

For on-demand mode, n8n passes `--mode` and `--arg` to researcher. The `--arg` value comes from untrusted Telegram input — `researcher.py` must use `argparse` (which handles this safely) and must not shell-interpolate the value. n8n should pass the command as a parameterized array (not a concatenated string) where available, or the script itself must strip any shell-special characters before use.

### Workflow 1: Daily Auto
```
Schedule Trigger (7am daily)
  → Execute Command (single node):
      python3 scripts/researcher.py --mode auto | python3 scripts/writer.py
  → Parse JSON output (n8n JSON Parse node)
  → Telegram: send draft preview with ✅ Post / ❌ Skip inline buttons
              (buttons POST to n8n Wait node resume URL)
  → Wait node (suspends execution, resumes on button press)
  → Branch on callback data:
      "post"  → HTTP: post to X API → HTTP: post to Threads API
              → Telegram: "✅ Posted!" confirmation
      "skip"  → Telegram: "❌ Skipped." confirmation
```

### Workflow 2: On-Demand (Telegram trigger)
```
Telegram Trigger (message received on PANTHEON_TG_BOT_TOKEN)
  → Parse message prefix:
      "gem: <name>"    → --mode gem --arg "<name>"
      "topic: <text>"  → --mode topic --arg "<text>"
      "explore: <text>"→ --mode topic --arg "<text>"   (alias for topic)
  → Telegram: "Researching [topic]..." (acknowledgment)
  → Execute Command (single node):
      python3 scripts/researcher.py --mode <mode> --arg "<sanitized-arg>" | python3 scripts/writer.py
  → Parse JSON output
  → Telegram: send draft preview with inline buttons (same Wait node pattern)
  → Branch: post or skip (same as Workflow 1)
```

### Telegram trigger format (on the go)
```
gem: domain-cartographer
topic: OpenAI talent exodus
explore: what's happening with Nvidia and knowledge hoarding
```

`gem:` → researcher loads that specific gem and finds a current news match for it.
`topic:` / `explore:` → both map to `--mode topic`, researcher finds the best gem for the given topic.

---

## CLI Path

`pantheon-post.py` is updated to call `researcher.py` and `writer.py` via **subprocess pipe** (not Python module imports — the scripts are CLI tools). The HITM approval loop and publisher remain in `pantheon-post.py` and are unchanged.

```bash
python3 scripts/pantheon-post.py                          # auto mode
python3 scripts/pantheon-post.py --gem andon-cord        # specific gem
python3 scripts/pantheon-post.py --topic "free topic"    # free topic
python3 scripts/pantheon-post.py --dry-run               # preview only
```

---

## Failure Modes

| Failure | Behavior |
|---|---|
| Researcher returns malformed JSON | `pantheon-post.py` / n8n catches parse error, sends Telegram alert: "Research failed — try again or use --dry-run" |
| Web search returns no results | Claude falls back to gem-only content (no current news hook). Research brief includes `"current_event": null`. Writer handles gracefully. |
| X or Threads API fails after approval | Log the error. Send Telegram alert with the post text so it can be manually posted. Never silently drop an approved post. |
| Telegram bot unreachable at approval time | n8n Wait node times out after 24 hours. Execution is logged as expired. |
| Vault unreachable (Docker down) | Script exits with clear error: "Secret '[key]' not found in vault". No silent failures. |

---

## Files to Create / Modify

| File | Action |
|---|---|
| `scripts/researcher.py` | Create — researcher agent (CLI tool, stdout JSON) |
| `scripts/writer.py` | Create — writer agent (CLI tool, stdin → stdout JSON) |
| `scripts/pantheon-post.py` | Modify — call researcher + writer via subprocess pipe |
| n8n Workflow 1 | Create — daily scheduler with Wait node |
| n8n Workflow 2 | Create — Telegram trigger with Wait node |

---

## Cost Estimate

| Scenario | Cost per run | Monthly (30 days) |
|---|---|---|
| Writer only (current) | ~$0.02 | ~$0.60 |
| Researcher + Writer | ~$0.05 | ~$1.50 |
| Event-driven extras | ~$0.05/trigger | Negligible |

Note: Anthropic's `web_search_20250305` tool has per-search pricing on top of token costs. Estimate assumes 3-5 searches per researcher run. Actual cost may be slightly higher but remains well within the $25/month cap.

Monthly spend cap: $25. Alert at $5 and $10. No risk.
