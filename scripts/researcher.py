#!/usr/bin/env python3
"""
Pantheon Researcher Agent.

Finds current news via free RSS feeds, matches to a Pantheon gem, digs historical precedent.
Uses local Ollama (qwen2.5:32b) — zero API cost.
Outputs a research brief as JSON to stdout.

Usage:
  python3 researcher.py --mode auto
  python3 researcher.py --mode gem --arg andon-cord
  python3 researcher.py --mode topic --arg "OpenAI talent exodus"
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

PANTHEON_ROOT = Path(__file__).parent.parent
PATTERNS_DIR  = PANTHEON_ROOT / "patterns"

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
OLLAMA_MODEL = "qwen2.5:32b-instruct-q4_K_M"

RSS_FEEDS = [
    "https://feeds.reuters.com/reuters/topNews",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
    "https://feeds.skynews.com/feeds/rss/world.xml",
]


def fetch_rss_headlines(limit: int = 20) -> list[str]:
    """Pull top headlines from free RSS feeds. Returns list of 'Title: Description' strings."""
    stories = []
    headers = {"User-Agent": "Mozilla/5.0 (compatible; Pantheon/1.0)"}
    for url in RSS_FEEDS:
        try:
            r = requests.get(url, timeout=8, headers=headers)
            r.raise_for_status()
            root = ET.fromstring(r.text)
            for item in root.findall(".//item")[:6]:
                title = item.findtext("title", "").strip()
                desc = item.findtext("description", "").strip()
                link = item.findtext("link", "").strip()
                if title:
                    snippet = f"{title}"
                    if desc:
                        # Strip HTML tags from description
                        import re
                        desc_clean = re.sub(r"<[^>]+>", "", desc)[:200]
                        snippet += f": {desc_clean}"
                    if link:
                        snippet += f" [{link}]"
                    stories.append(snippet)
        except Exception as e:
            print(f"⚠ RSS fetch failed for {url}: {e}", file=sys.stderr)
            continue
        if len(stories) >= limit:
            break
    return stories[:limit]


def ollama_chat(prompt: str) -> str:
    """Call local Ollama and return the text response."""
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.3},
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=180)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()


def load_gem_summaries(patterns_dir: Path) -> list[dict]:
    """Load name + 300-char summary for every gem."""
    summaries = []
    for gem_dir in sorted(patterns_dir.iterdir()):
        if not gem_dir.is_dir():
            continue
        pattern_file = gem_dir / "pattern.md"
        if not pattern_file.exists():
            continue
        text = pattern_file.read_text(encoding="utf-8")
        summaries.append({
            "name": gem_dir.name,
            "summary": text[:300],
        })
    return summaries


def load_full_gem(gem_name: str) -> str:
    """Return full pattern.md text for a gem. Exits if gem not found."""
    pattern_file = PATTERNS_DIR / gem_name / "pattern.md"
    if not pattern_file.exists():
        sys.exit(f"✗ Gem not found: '{gem_name}'. Check patterns/ directory.")
    return pattern_file.read_text(encoding="utf-8")


def run_research(mode: str, arg: str | None) -> dict:
    summaries = load_gem_summaries(PATTERNS_DIR)
    gem_list = "\n".join(f"- {s['name']}: {s['summary']}" for s in summaries)

    if mode == "auto":
        headlines = fetch_rss_headlines(limit=20)
        if not headlines:
            sys.exit("✗ Could not fetch any RSS headlines. Check network.")
        news_block = "\n".join(f"{i+1}. {h}" for i, h in enumerate(headlines))
        task_context = f"Here are today's top news headlines:\n\n{news_block}\n\nPick the single most compelling story that best illustrates one of the Pantheon gems."

    elif mode == "gem":
        full_gem = load_full_gem(arg)
        headlines = fetch_rss_headlines(limit=20)
        news_block = "\n".join(f"{i+1}. {h}" for i, h in enumerate(headlines))
        task_context = (
            f"The gem is '{arg}'. Full pattern:\n{full_gem}\n\n"
            f"Here are today's top headlines:\n\n{news_block}\n\n"
            f"Pick the headline that best illustrates this gem in action today."
        )

    else:  # topic
        headlines = fetch_rss_headlines(limit=20)
        news_block = "\n".join(f"{i+1}. {h}" for i, h in enumerate(headlines))
        task_context = (
            f"The requested topic is: {arg}\n\n"
            f"Here are today's top headlines:\n\n{news_block}\n\n"
            f"Find the most relevant story about this topic, then match it to the best Pantheon gem."
        )

    prompt = f"""{task_context}

Available Pantheon gems:
{gem_list}

Output a JSON research brief with this exact structure:
{{
  "current_event": "one sentence describing the current news story",
  "gem_name": "exact gem name from the list above",
  "gem_summary": "one sentence describing the gem's core insight",
  "historical_precedent": "2-3 sentences: who used this pattern before, when, context",
  "historical_outcome": "one sentence: what happened as a result",
  "open_loop": "one sentence: what the pattern revealed but did not resolve — the lesson history keeps surfacing",
  "source_urls": ["url from the headline if available, otherwise empty list"]
}}

Return ONLY valid JSON. No markdown fences. No commentary."""

    raw = ollama_chat(prompt)

    # Strip markdown fences if present
    if "```" in raw:
        parts = raw.split("```")
        for part in reversed(parts):
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            if part.startswith("{"):
                return json.loads(part)

    try:
        return json.loads(raw.strip())
    except json.JSONDecodeError as e:
        print(f"✗ Could not parse JSON from researcher response: {e}", file=sys.stderr)
        print(f"Raw response:\n{raw}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Pantheon Researcher Agent")
    parser.add_argument("--mode", choices=["auto", "gem", "topic"], default="auto")
    parser.add_argument("--arg", help="Gem name or topic text (required for gem/topic mode)")
    args = parser.parse_args()

    if args.mode in ("gem", "topic") and not args.arg:
        sys.exit(f"✗ --arg is required for --mode {args.mode}")

    arg = args.arg
    if arg:
        arg = arg.replace("`", "").replace("$", "").replace(";", "").replace("&", "").replace("|", "").replace(">", "").replace("<", "")

    brief = run_research(args.mode, arg)
    print(json.dumps(brief, ensure_ascii=False))


if __name__ == "__main__":
    main()
