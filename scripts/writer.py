#!/usr/bin/env python3
"""
Pantheon Writer Agent.

Reads a research brief from stdin, writes a 4-part cliffhanger thread series
for X and Threads using a three-pass generation loop:
  Pass 1 — narrative outline (what to say)
  Pass 2 — 4-part thread draft with cliffhangers
  Pass 3 — tension self-critique; rewrites if score < 7

Uses local Ollama (qwen2.5:32b) — zero API cost.
Outputs JSON to stdout.

Usage:
  echo '<research_brief_json>' | python3 writer.py
  python3 researcher.py --mode auto | python3 writer.py
"""

import json
import sys
from pathlib import Path

import requests

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
OLLAMA_MODEL = "qwen2.5:32b-instruct-q4_K_M"

SYSTEM_PROMPT = """You are a master of narrative tension writing for Pantheon — a project that surfaces the cognitive patterns of history's greatest problem-solvers.

Rules you never break:
- Every sentence earns the next. If a sentence doesn't create tension or advance the story, cut it.
- Drop into scenes mid-action. Never start with "Did you know", "Throughout history", or any orientation phrase.
- Specificity is everything. "Shockley watched his eight best engineers resign on a single Tuesday" beats "researchers left the company."
- The reader must feel like they discovered something the rest of the world missed.
- The loop never closes. The last post always leaves a question permanently open.
- No em-dashes. No "fascinating", "remarkable", "incredible". Show it — don't label it."""


def ollama_chat(system: str, user: str, temperature: float = 0.85) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "options": {"temperature": temperature},
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=240)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()


def _parse_json(raw: str) -> dict:
    if "```" in raw:
        for part in reversed(raw.split("```")):
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            if part.startswith("{"):
                return json.loads(part)
    return json.loads(raw.strip())


def _strip_dashes(text: str) -> str:
    return text.replace("\u2014", "-").replace("\u2013", "-")


def _enforce_constraints(content: dict) -> dict:
    content["x_thread"] = [_strip_dashes(p) for p in content["x_thread"]]
    content["threads_thread"] = [_strip_dashes(p) for p in content["threads_thread"]]
    return content


def _pass1_outline(brief: dict) -> dict:
    """Generate narrative outline from research brief."""
    prompt = f"""You are building the story architecture for a thread series.

Research brief:
Current event: {brief['current_event']}
Gem: {brief['gem_name']} — {brief['gem_summary']}
Historical precedent: {brief['historical_precedent']}
Historical outcome: {brief['historical_outcome']}
The open loop: {brief['open_loop']}

Extract the four narrative beats for a cliffhanger thread:
1. HOOK — the current tension, mid-scene, no preamble
2. MIRROR — the historical precedent that makes the parallel vivid
3. TWIST — one angle that subverts the obvious reading; what most people miss
4. PAYOFF — the outcome + the open question history never closed

Return ONLY valid JSON:
{{
  "hook": "one sentence: current tension, drop in mid-scene",
  "mirror": "2 sentences: who did this before, when, the vivid parallel",
  "twist": "1-2 sentences: the unexpected angle; what the mirror reveals that the obvious reading misses",
  "payoff": "1-2 sentences: what the pattern produced + the permanently open question",
  "gem_name": "{brief['gem_name']}"
}}"""

    raw = ollama_chat(SYSTEM_PROMPT, prompt, temperature=0.5)
    return _parse_json(raw)


def _pass2_thread(outline: dict, prior_score: int = None) -> dict:
    """Write 4-part cliffhanger thread from outline."""
    score_note = f"\nYour previous attempt scored {prior_score}/10 on tension. Push harder — every post must feel incomplete without the next.\n" if prior_score else ""

    prompt = f"""Write a 4-part cliffhanger thread series. Each post is raw social media text — no labels, no numbering, no "X 1/4:" prefixes. Just the post content itself.
{score_note}
Narrative beats:
Hook: {outline['hook']}
Mirror: {outline['mirror']}
Twist: {outline['twist']}
Payoff: {outline['payoff']}
Gem: {outline['gem_name']}

X thread rules (4 short posts):
- Post 1: drop into the hook mid-scene. End the post with exactly: 🧵 2/4 ↓
- Post 2: the historical mirror. End with exactly: 🧵 3/4 ↓
- Post 3: the twist. End with exactly: 🧵 4/4 ↓
- Post 4: outcome + open loop. End with: #PantheonGems
- Each X post under 240 characters. Tight. Punchy. No em-dashes.

Threads thread rules (4 longer posts):
- Post 1: hook, 2-3 sentences. End with exactly: 🧵 2/4 ↓
- Post 2: historical mirror, 2-3 sentences. End with exactly: 🧵 3/4 ↓
- Post 3: the twist, 2-3 sentences. End with exactly: 🧵 4/4 ↓
- Post 4: outcome + "This pattern lives in Pantheon as {outline['gem_name']} — and it's still open."
- Each Threads post under 450 characters. Flowing prose. No bullets. No em-dashes.

Return ONLY valid JSON. The array values are the post text itself — nothing else:
{{
  "x_thread": ["<post 1 text>", "<post 2 text>", "<post 3 text>", "<post 4 text>"],
  "threads_thread": ["<post 1 text>", "<post 2 text>", "<post 3 text>", "<post 4 text>"],
  "subject_line": "<one-line description for approval preview>"
}}"""

    raw = ollama_chat(SYSTEM_PROMPT, prompt, temperature=0.85)
    return _parse_json(raw)


def _pass3_critique(content: dict, outline: dict) -> tuple[dict, int]:
    """Score tension 1-10. Returns (content, score). If score < 7, retries Pass 2."""
    x_preview = "\n".join(f"Post {i+1}: {p}" for i, p in enumerate(content["x_thread"]))

    prompt = f"""Rate this 4-part thread series on cliffhanger tension. Return a single integer from 1 to 10.

{x_preview}

Score on:
- Hook drops mid-scene with no preamble (2 pts)
- Each post creates genuine need for the next (3 pts)
- Twist subverts the obvious read (2 pts)
- Payoff leaves the loop permanently open (3 pts)

Return ONLY valid JSON: {{"score": <integer 1-10>, "weakest_point": "<one sentence>"}}"""

    try:
        raw = ollama_chat(SYSTEM_PROMPT, prompt, temperature=0.3)
        result = _parse_json(raw)
        score = int(result.get("score", 7))
        weak = result.get("weakest_point", "")
        print(f"  Tension score: {score}/10 — {weak}", file=sys.stderr)
    except Exception as e:
        print(f"  ⚠ Pass 3 scoring failed ({e}) — skipping", file=sys.stderr)
        return content, 7

    if score < 7:
        print(f"  Score < 7 — rewriting with Pass 2...", file=sys.stderr)
        try:
            revised = _pass2_thread(outline, prior_score=score)
            revised = _enforce_constraints(revised)
            if _is_valid_thread(revised):
                return revised, score
        except Exception as e:
            print(f"  ⚠ Pass 2 retry failed ({e}) — keeping original", file=sys.stderr)

    return content, score


def _is_valid_thread(content: dict) -> bool:
    """Check that thread arrays have 4 real posts (not placeholder text)."""
    for key in ("x_thread", "threads_thread"):
        posts = content.get(key, [])
        if len(posts) != 4:
            return False
        if any(len(p) < 20 or p in ("post1", "post2", "post3", "post4") for p in posts):
            return False
    return True


def _validate(content: dict) -> list[str]:
    """Return list of constraint violations."""
    errors = []
    for i, post in enumerate(content["x_thread"]):
        if len(post) > 280:
            errors.append(f"x_thread[{i}] = {len(post)} chars (limit 280)")
    for i, post in enumerate(content["threads_thread"]):
        if len(post) > 500:
            errors.append(f"threads_thread[{i}] = {len(post)} chars (limit 500)")
    return errors


def generate_posts(brief: dict) -> dict:
    print("  Pass 1: building narrative outline...", file=sys.stderr)
    outline = _pass1_outline(brief)

    print("  Pass 2: writing 4-part thread...", file=sys.stderr)
    content = _pass2_thread(outline)
    content = _enforce_constraints(content)

    if not _is_valid_thread(content):
        print("  ⚠ Pass 2 returned invalid thread — retrying...", file=sys.stderr)
        content = _pass2_thread(outline)
        content = _enforce_constraints(content)

    print("  Pass 3: tension critique...", file=sys.stderr)
    content, _ = _pass3_critique(content, outline)
    content = _enforce_constraints(content)

    errors = _validate(content)
    if errors:
        print(f"  ⚠ Constraint warnings: {errors}", file=sys.stderr)

    content["gem_name"] = brief.get("gem_name", "")
    return content


def main():
    brief_raw = sys.stdin.read().strip()
    if not brief_raw:
        sys.exit("✗ No input on stdin. Pipe a research brief JSON.")

    try:
        brief = json.loads(brief_raw)
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON on stdin: {e}", file=sys.stderr)
        sys.exit(1)

    output = generate_posts(brief)
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
