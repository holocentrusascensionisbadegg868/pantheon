#!/usr/bin/env python3
"""
Pantheon content pipeline.

Generates compelling social content from a gem or free topic,
sends to Telegram for approval, then posts to X and Threads.

Usage:
  python3 pantheon-post.py                        # pick random gem
  python3 pantheon-post.py --gem andon-cord       # specific gem
  python3 pantheon-post.py --topic "Hannibal at Cannae"  # free topic
  python3 pantheon-post.py --dry-run              # generate only, no post
"""

import argparse
import json
import random
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shared import get_secret

import requests
import tweepy

# ── Paths ──────────────────────────────────────────────────────────────────
PANTHEON_ROOT = Path(__file__).parent.parent
PATTERNS_DIR  = PANTHEON_ROOT / "patterns"

# ── Content generation ─────────────────────────────────────────────────────
def generate_content(gem_name: str = "", subject: str = "") -> dict:
    """Run researcher + writer pipeline and return content dict."""
    if gem_name:
        researcher_cmd = [sys.executable, str(Path(__file__).parent / "researcher.py"),
                          "--mode", "gem", "--arg", gem_name]
    else:
        researcher_cmd = [sys.executable, str(Path(__file__).parent / "researcher.py"),
                          "--mode", "topic", "--arg", subject]

    researcher = subprocess.run(researcher_cmd, capture_output=True, text=True,
                                cwd=Path(__file__).parent.parent)
    if researcher.returncode != 0:
        sys.exit(f"✗ Researcher failed:\n{researcher.stderr}")

    writer = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "writer.py")],
        input=researcher.stdout, capture_output=True, text=True,
        cwd=Path(__file__).parent.parent
    )
    if writer.returncode != 0:
        sys.exit(f"✗ Writer failed:\n{writer.stderr}")

    return json.loads(writer.stdout.strip())

def random_gem() -> str:
    gems = [d.name for d in PATTERNS_DIR.iterdir()
            if d.is_dir() and (d / "pattern.md").exists()]
    return random.choice(gems)

# ── Telegram ───────────────────────────────────────────────────────────────
def tg_send(token: str, chat_id: str, text: str, reply_markup=None) -> int:
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json=payload)
    r.raise_for_status()
    return r.json()["result"]["message_id"]

def tg_get_updates(token: str, offset: int = 0, timeout: int = 30) -> list:
    try:
        r = requests.get(
            f"https://api.telegram.org/bot{token}/getUpdates",
            params={
                "offset": offset,
                "timeout": timeout,
                "allowed_updates": json.dumps(["callback_query", "message"]),
            },
            timeout=timeout + 5,
        )
        if r.status_code == 409:
            # Another poller (e.g. n8n) is active — wait and retry
            time.sleep(3)
            return []
        r.raise_for_status()
        return r.json().get("result", [])
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        return []

def tg_answer_callback(token: str, callback_id: str):
    requests.post(f"https://api.telegram.org/bot{token}/answerCallbackQuery",
                  json={"callback_query_id": callback_id})

def await_approval(token: str, chat_id: str, content: dict) -> str:
    """Send draft to Telegram, return 'post', 'skip', or edited text."""

    x_preview = "\n".join(
        f"*[{i+1}/4]* {p}" for i, p in enumerate(content["x_thread"])
    )
    t_preview = "\n\n".join(
        f"*[{i+1}/4]* {p}" for i, p in enumerate(content["threads_thread"])
    )
    preview = (
        f"*Pantheon draft — {content['subject_line']}*\n\n"
        f"*X Thread (4 posts):*\n{x_preview}\n\n"
        f"*Threads Thread (4 posts):*\n{t_preview}"
    )

    keyboard = {
        "inline_keyboard": [[
            {"text": "✅ Post to social",  "callback_data": "post"},
            {"text": "❌ Skip",       "callback_data": "skip"},
        ]]
    }

    tg_send(token, chat_id, preview, reply_markup=keyboard)
    print("Waiting for Telegram approval...")

    # Get current update offset to ignore old messages (non-blocking)
    updates = tg_get_updates(token, timeout=0)
    offset = (updates[-1]["update_id"] + 1) if updates else 0

    while True:
        updates = tg_get_updates(token, offset=offset)
        for update in updates:
            offset = update["update_id"] + 1

            # Inline button press
            if "callback_query" in update:
                cb = update["callback_query"]
                if str(cb["message"]["chat"]["id"]) == str(chat_id):
                    tg_answer_callback(token, cb["id"])
                    return cb["data"]  # "post" or "skip"

            # Text reply (manual edit)
            if "message" in update:
                msg = update["message"]
                if str(msg["chat"]["id"]) == str(chat_id) and "text" in msg:
                    return msg["text"]

        time.sleep(1)

# ── Posting ────────────────────────────────────────────────────────────────
def post_to_x_thread(posts: list) -> str:
    client = tweepy.Client(
        consumer_key=get_secret("PANTHEON_X_API_KEY"),
        consumer_secret=get_secret("PANTHEON_X_API_SECRET"),
        access_token=get_secret("PANTHEON_X_ACCESS_TOKEN"),
        access_token_secret=get_secret("PANTHEON_X_ACCESS_SECRET"),
    )
    last_id = None
    first_id = None
    for i, text in enumerate(posts):
        kwargs = {"text": text[:280]}
        if last_id:
            kwargs["in_reply_to_tweet_id"] = last_id
        resp = client.create_tweet(**kwargs)
        last_id = resp.data["id"]
        if first_id is None:
            first_id = last_id
        if i < len(posts) - 1:
            time.sleep(1)
    return first_id

def _safe_truncate(text: str, limit: int = 490) -> str:
    if len(text) <= limit:
        return text
    candidate = text[:limit]
    for marker in (". ", "! ", "? "):
        pos = candidate.rfind(marker)
        if pos > limit // 2:
            return candidate[:pos + 1]
    return candidate

def _post_threads_single(token: str, text: str, reply_to_id: str = None) -> str:
    params = {"media_type": "TEXT", "text": _safe_truncate(text, 490), "access_token": token}
    if reply_to_id:
        params["reply_to_id"] = reply_to_id
    r = requests.post("https://graph.threads.net/v1.0/me/threads", data=params)
    if not r.ok:
        print(f"  Threads container error: {r.status_code} {r.text}", file=sys.stderr)
    r.raise_for_status()
    creation_id = r.json()["id"]
    time.sleep(2)  # let container finalize before publishing
    r2 = requests.post(
        "https://graph.threads.net/v1.0/me/threads_publish",
        data={"creation_id": creation_id, "access_token": token}
    )
    if not r2.ok:
        print(f"  Threads publish error: {r2.status_code} {r2.text}", file=sys.stderr)
    r2.raise_for_status()
    return r2.json()["id"]

def post_to_threads_thread(posts: list) -> str:
    token = get_secret("PANTHEON_THREADS_ACCESS_TOKEN")
    last_id = None
    first_id = None
    try:
        for i, text in enumerate(posts):
            post_id = _post_threads_single(token, text, reply_to_id=last_id)
            last_id = post_id
            if first_id is None:
                first_id = post_id
            if i < len(posts) - 1:
                time.sleep(3)
        return first_id
    except Exception as e:
        print(f"  ⚠ Reply thread failed ({e}) — falling back to single post", file=sys.stderr)
        # Strip cliffhanger markers and join as one flowing post
        combined = " ".join(
            p.replace("🧵 2/4 ↓", "").replace("🧵 3/4 ↓", "").replace("🧵 4/4 ↓", "").strip()
            for p in posts
        )
        return _post_threads_single(token, _safe_truncate(combined, 490))

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Pantheon content pipeline")
    parser.add_argument("--gem",     help="Gem name (e.g. andon-cord)")
    parser.add_argument("--topic",   help="Free-form topic")
    parser.add_argument("--dry-run", action="store_true", help="Generate only, don't post")
    args = parser.parse_args()

    # Determine subject
    if args.topic:
        subject = args.topic
        gem_name = ""
    else:
        gem_name = args.gem or random_gem()
        print(f"Gem: {gem_name}")
        subject = ""

    # Generate content
    print("Generating content via Claude (research + write)...")
    content = generate_content(gem_name=gem_name, subject=subject)

    # Append gem-specific URL to last Threads post
    if not content.get("threads_thread"):
        sys.exit("✗ Writer returned empty threads_thread")
    gem_name = content.get("gem_name", "")
    site_url = f"https://pantheon-lilac.vercel.app/?gem={gem_name}" if gem_name else "https://pantheon-lilac.vercel.app/"
    content["threads_thread"][-1] += f"\n\n{site_url}"

    print(f"\n── X Thread ({len(content['x_thread'])} posts) ──")
    for i, p in enumerate(content["x_thread"]):
        print(f"  [{i+1}/4] ({len(p)} chars) {p}")
    print(f"\n── Threads Thread ({len(content['threads_thread'])} posts) ──")
    for i, p in enumerate(content["threads_thread"]):
        print(f"  [{i+1}/4] ({len(p)} chars) {p}")

    if args.dry_run:
        print("\n[dry-run] Done.")
        return

    # Telegram approval gate
    tg_token  = get_secret("PANTHEON_TG_BOT_TOKEN")
    tg_chat   = get_secret("PANTHEON_TG_CHAT_ID")

    decision = await_approval(tg_token, tg_chat, content)

    if decision == "skip":
        print("Skipped.")
        tg_send(tg_token, tg_chat, "❌ Skipped — nothing posted.")
        return

    # Post
    x_id = None
    t_id = None
    errors = []

    try:
        print("Posting to X...")
        x_id = post_to_x_thread(content["x_thread"])
        print(f"✓ X thread: {x_id}")
    except Exception as e:
        print(f"✗ X failed: {e}", file=sys.stderr)
        errors.append(f"X failed: {e}")

    try:
        print("Posting to Threads...")
        t_id = post_to_threads_thread(content["threads_thread"])
        print(f"✓ Threads thread: {t_id}")
    except Exception as e:
        print(f"✗ Threads failed: {e}", file=sys.stderr)
        errors.append(f"Threads failed: {e}")

    status = "✅ Posted!"
    details = "\n".join(filter(None, [
        f"X: `{x_id}`" if x_id else None,
        f"Threads: `{t_id}`" if t_id else None,
        *[f"⚠ {err}" for err in errors],
    ]))
    tg_send(tg_token, tg_chat, f"{status}\n\n{details}")

if __name__ == "__main__":
    main()
