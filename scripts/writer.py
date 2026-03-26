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

SYSTEM_PROMPT = """You write like a journalist who never lets the reader feel satisfied. Every sentence earns the next. You work for Pantheon — a project that surfaces the cognitive patterns of history's greatest problem-solvers.

Your job: connect a current event to a historical pattern in a way that makes the reader feel like they just discovered something everyone else missed. The loop always stays open — no tidy resolution."""


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


def _pass2_thread(outline: dict) -> dict:
    """Write 4-part cliffhanger thread from outline."""
    prompt = f"""Write a 4-part thread series from this narrative outline.

Outline:
Hook: {outline['hook']}
Mirror: {outline['mirror']}
Twist: {outline['twist']}
Payoff: {outline['payoff']}
Gem: {outline['gem_name']}

Rules:
- Posts 1-3 must end with a cliffhanger that makes the next post feel necessary
- Use these exact endings: post 1 ends "🧵 2/4 ↓", post 2 ends "🧵 3/4 ↓", post 3 ends "🧵 4/4 ↓"
- Post 4 ends with: "This pattern lives in Pantheon as {outline['gem_name']} — and it's still open."
- X posts: punchy, under 240 chars each, end with #PantheonGems on post 4 only
- Threads posts: richer prose, under 450 chars each
- No em-dashes. No bullet points. No "fascinating" or "remarkable".
- The loop never closes.

Return ONLY valid JSON:
{{
  "x_thread": ["post1", "post2", "post3", "post4"],
  "threads_thread": ["post1", "post2", "post3", "post4"],
  "subject_line": "one-line description for approval preview"
}}"""

    raw = ollama_chat(SYSTEM_PROMPT, prompt, temperature=0.85)
    return _parse_json(raw)


def _pass3_critique(content: dict) -> dict:
    """Self-critique tension score. Rewrites if score < 7."""
    x_preview = "\n".join(f"X {i+1}/4: {p}" for i, p in enumerate(content["x_thread"]))
    threads_preview = "\n".join(f"T {i+1}/4: {p}" for i, p in enumerate(content["threads_thread"]))

    prompt = f"""Rate this 4-part thread series on cliffhanger tension from 1 to 10.

{x_preview}

Scoring criteria:
- Does each post make the reader need the next? (3 pts)
- Is the hook irresistible — does it drop mid-scene without explanation? (2 pts)
- Is the twist genuinely surprising, not the obvious read? (2 pts)
- Does the payoff leave something permanently unresolved? (3 pts)

If score >= 7: return the original thread unchanged.
If score < 7: rewrite the entire thread to raise the tension.

Return ONLY valid JSON:
{{
  "score": <integer 1-10>,
  "x_thread": ["post1", "post2", "post3", "post4"],
  "threads_thread": ["post1", "post2", "post3", "post4"],
  "subject_line": "{content['subject_line']}"
}}

The thread posts in your response must be the final version (original if score >= 7, rewritten if < 7)."""

    raw = ollama_chat(SYSTEM_PROMPT, prompt, temperature=0.3)
    result = _parse_json(raw)

    score = result.get("score", 0)
    print(f"  Tension score: {score}/10", file=sys.stderr)

    return {
        "x_thread": result["x_thread"],
        "threads_thread": result["threads_thread"],
        "subject_line": result.get("subject_line", content["subject_line"]),
    }


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

    print("  Pass 3: tension critique...", file=sys.stderr)
    content = _pass3_critique(content)
    content = _enforce_constraints(content)

    errors = _validate(content)
    if errors:
        print(f"  ⚠ Constraint warnings: {errors}", file=sys.stderr)

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
