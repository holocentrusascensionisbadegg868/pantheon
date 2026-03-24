#!/usr/bin/env python3
"""
Pantheon Pipeline API
Runs on Mac host (port 8401). Called by n8n (Docker) via host.docker.internal.
Handles: content generation, draft storage, social posting, Telegram outbound + inbound.

Telegram inbound (approve/skip buttons, on-demand commands) is handled via long polling —
NOT n8n webhook. This avoids the n8n credential/setWebhook complexity entirely.
n8n is only used for the daily schedule trigger.

See: documentation/guides/pantheon-architecture.md
"""

import importlib.util
import json
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Optional

import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

PANTHEON_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PANTHEON_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
from shared import get_secret

# Fetch secrets once at startup
TG_TOKEN = get_secret("PANTHEON_TG_BOT_TOKEN")
TG_CHAT_ID = get_secret("PANTHEON_TG_CHAT_ID")

app = FastAPI()

# In-memory draft store: message_id -> {x_post, threads_post}
_drafts: dict[int, dict] = {}


# ── Generation ────────────────────────────────────────────────────────────────

@app.get("/generate")
def generate(mode: str = "auto", arg: str = ""):
    """Run researcher | writer pipeline. Returns {x_post, threads_post, subject_line}."""
    researcher_cmd = [sys.executable, str(SCRIPTS_DIR / "researcher.py"), "--mode", mode]
    if arg:
        researcher_cmd += ["--arg", arg]

    researcher = subprocess.run(
        researcher_cmd, capture_output=True, text=True, cwd=str(PANTHEON_ROOT)
    )
    if researcher.returncode != 0:
        raise HTTPException(500, detail=f"Researcher failed: {researcher.stderr}")

    writer = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "writer.py")],
        input=researcher.stdout, capture_output=True, text=True, cwd=str(PANTHEON_ROOT)
    )
    if writer.returncode != 0:
        raise HTTPException(500, detail=f"Writer failed: {writer.stderr}")

    draft = json.loads(writer.stdout.strip())
    draft["x_char_count"] = len(draft["x_post"])
    return draft


# ── Draft storage ─────────────────────────────────────────────────────────────

class DraftIn(BaseModel):
    x_post: str
    threads_post: str


@app.post("/draft/{message_id}")
def store_draft(message_id: int, draft: DraftIn):
    _drafts[message_id] = draft.model_dump()
    return {"ok": True}


@app.get("/draft/{message_id}")
def get_draft(message_id: int):
    draft = _drafts.get(message_id)
    if not draft:
        raise HTTPException(404, detail=f"Draft {message_id} not found")
    return draft


# ── Posting ───────────────────────────────────────────────────────────────────

def _do_post(draft: dict) -> dict:
    """Load pantheon-post.py and post to X and Threads. Returns {x_id, t_id}."""
    spec = importlib.util.spec_from_file_location(
        "pp", str(SCRIPTS_DIR / "pantheon-post.py")
    )
    pp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pp)
    x_id = pp.post_to_x(draft["x_post"])
    t_id = pp.post_to_threads(
        draft["threads_post"] + "\n\nhttps://pantheon-lilac.vercel.app/"
    )
    return {"x_id": str(x_id), "t_id": str(t_id)}


@app.post("/post/{message_id}")
def post_draft(message_id: int):
    """Post stored draft to X and Threads. Returns {x_id, t_id}."""
    draft = _drafts.get(message_id)
    if not draft:
        raise HTTPException(404, detail=f"Draft {message_id} not found")
    return _do_post(draft)


# ── Telegram outbound ─────────────────────────────────────────────────────────

class SendDraftIn(BaseModel):
    x_post: str
    threads_post: str
    subject_line: str
    x_char_count: int
    chat_id: Optional[str] = None  # defaults to vault PANTHEON_TG_CHAT_ID


@app.post("/telegram/send-draft")
def send_draft(body: SendDraftIn):
    """Send draft preview to Telegram with Post/Skip inline keyboard. Returns {message_id}."""
    chat_id = body.chat_id or TG_CHAT_ID
    text = (
        f"*Pantheon draft - {body.subject_line}*\n\n"
        f"*X ({body.x_char_count} chars):*\n{body.x_post}\n\n"
        f"*Threads:*\n{body.threads_post}"
    )
    keyboard = {"inline_keyboard": [[
        {"text": "✅ Post to social", "callback_data": "post"},
        {"text": "❌ Skip", "callback_data": "skip"},
    ]]}
    r = requests.post(
        f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown",
              "reply_markup": keyboard},
    )
    r.raise_for_status()
    msg_id = r.json()["result"]["message_id"]
    return {"message_id": msg_id}


# ── Telegram inbound — long polling ───────────────────────────────────────────
# Handles approve/skip callbacks and on-demand commands (topic:, gem:, explore:).
# No webhook registration. No n8n Telegram Trigger. No credential management.
# Runs as a background daemon thread inside this process.

def _tg(method: str, **kwargs):
    """Fire-and-forget Telegram API call."""
    try:
        requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/{method}", json=kwargs, timeout=10)
    except Exception as e:
        print(f"[TG] {method} failed: {e}", flush=True)


def _handle_callback(cb: dict):
    """User clicked Post or Skip on a draft message."""
    chat_id = str(cb["message"]["chat"]["id"])
    message_id = cb["message"]["message_id"]
    callback_query_id = str(cb["id"])
    action = cb.get("data", "")

    # Always ack the button press so the spinner goes away
    _tg("answerCallbackQuery", callback_query_id=callback_query_id)

    draft = _drafts.get(message_id)
    if not draft:
        _tg("sendMessage", chat_id=chat_id, text="⚠️ Draft expired (server restarted). Run a new generate.")
        return

    if action == "post":
        try:
            result = _do_post(draft)
            _tg("sendMessage", chat_id=chat_id,
                text=f"✅ Posted!\n\nX: {result['x_id']}\nThreads: {result['t_id']}")
        except Exception as e:
            _tg("sendMessage", chat_id=chat_id, text=f"❌ Post failed: {e}")
    elif action == "skip":
        _tg("sendMessage", chat_id=chat_id, text="❌ Skipped.")


def _handle_message(msg: dict):
    """User sent a command: topic:, gem:, or explore:"""
    text = msg.get("text", "").strip()
    chat_id = str(msg["chat"]["id"])
    lower = text.lower()

    if lower.startswith("gem:"):
        mode, arg = "gem", text[4:].strip()
    elif lower.startswith("topic:"):
        mode, arg = "topic", text[6:].strip()
    elif lower.startswith("explore:"):
        mode, arg = "topic", text[8:].strip()
    else:
        return  # ignore unrecognised messages

    if not arg:
        return

    _tg("sendMessage", chat_id=chat_id, text=f"🔍 Researching {arg}...")

    try:
        # Reuse the generate endpoint logic via subprocess (same as n8n would call it)
        researcher_cmd = [sys.executable, str(SCRIPTS_DIR / "researcher.py"), "--mode", mode, "--arg", arg]
        researcher = subprocess.run(researcher_cmd, capture_output=True, text=True, cwd=str(PANTHEON_ROOT))
        if researcher.returncode != 0:
            raise RuntimeError(researcher.stderr[:300])

        writer = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "writer.py")],
            input=researcher.stdout, capture_output=True, text=True, cwd=str(PANTHEON_ROOT)
        )
        if writer.returncode != 0:
            raise RuntimeError(writer.stderr[:300])

        draft = json.loads(writer.stdout.strip())
        draft["x_char_count"] = len(draft["x_post"])

        # Send draft with buttons
        r = send_draft(SendDraftIn(
            x_post=draft["x_post"],
            threads_post=draft["threads_post"],
            subject_line=draft["subject_line"],
            x_char_count=draft["x_char_count"],
            chat_id=chat_id,
        ))
        _drafts[r["message_id"]] = {"x_post": draft["x_post"], "threads_post": draft["threads_post"]}

    except Exception as e:
        _tg("sendMessage", chat_id=chat_id, text=f"❌ Error: {e}")


def _polling_loop():
    """Long-poll Telegram for updates. Runs forever as a daemon thread."""
    print("[Pantheon] Telegram polling started.", flush=True)
    offset = 0
    while True:
        try:
            r = requests.get(
                f"https://api.telegram.org/bot{TG_TOKEN}/getUpdates",
                params={"offset": offset, "timeout": 30,
                        "allowed_updates": ["message", "callback_query"]},
                timeout=35,
            )
            for update in r.json().get("result", []):
                offset = update["update_id"] + 1
                if "callback_query" in update:
                    _handle_callback(update["callback_query"])
                elif "message" in update:
                    _handle_message(update["message"])
        except Exception as e:
            print(f"[Pantheon] Poll error: {e}", flush=True)
            time.sleep(5)


def _start_polling():
    """Clear any existing webhook and start the polling thread."""
    try:
        requests.post(
            f"https://api.telegram.org/bot{TG_TOKEN}/deleteWebhook",
            json={"drop_pending_updates": False},
            timeout=10,
        )
    except Exception as e:
        print(f"[Pantheon] deleteWebhook failed: {e}", flush=True)
    threading.Thread(target=_polling_loop, daemon=True).start()


# Start polling when the server boots
_start_polling()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8401, log_level="info")
