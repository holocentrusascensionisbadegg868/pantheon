#!/usr/bin/env python3
"""Generates PBNJ.md — full PB&J test outputs, one section per gem, no truncation."""
import sys
import re
from pathlib import Path

REPO_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "tests" / "pbnj-outputs"
PBNJ_FILE = REPO_ROOT / "PBNJ.md"

def summarize(output_text, max_words=140):
    """Strip markdown noise, return first max_words as a single prose paragraph."""
    # Remove markdown headers, horizontal rules, bold markers, blockquotes
    text = re.sub(r'^#{1,6}\s+', '', output_text, flags=re.MULTILINE)
    text = re.sub(r'^---+\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.MULTILINE)
    # Collapse whitespace and newlines into single spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Trim to max_words
    words = text.split()
    if len(words) > max_words:
        text = ' '.join(words[:max_words]) + '…'
    return text

outputs = sorted(OUTPUT_DIR.glob("*.md"))
if not outputs:
    print("No PB&J outputs yet. Run: bash tests/pbnj-test.sh <pattern-name>")
    sys.exit(0)

rows = []
for output_file in outputs:
    pattern = output_file.stem
    pattern_file = REPO_ROOT / "patterns" / pattern / "pattern.md"
    if not pattern_file.exists():
        continue

    frontmatter = pattern_file.read_text()

    # Extract trigger
    trigger_match = re.search(r'^trigger:\s*\[([^\]]+)\]', frontmatter, re.MULTILINE)
    trigger = trigger_match.group(1).split(',')[0].strip().strip('"') if trigger_match else "—"

    # Extract origin-type
    origin_match = re.search(r'^origin-type:\s*(\S+)', frontmatter, re.MULTILINE)
    origin = origin_match.group(1) if origin_match else "historian"
    badge = " ✦" if origin == "authored" else ""

    # Extract output section and summarize to 140 words
    raw = output_file.read_text()
    output_match = re.split(r'\*\*Output:\*\*\s*\n', raw, maxsplit=1)
    raw_output = output_match[1].strip() if len(output_match) > 1 else raw.strip()
    summary = summarize(raw_output)

    rows.append((pattern, badge, trigger, summary))

lines = [
    "# PB&J Test Results\n\n",
    "> **Input:** *Construct a Peanut Butter and Jelly Sandwich*\n\n",
    f"Same input. Every gem. Output summarized to 140 words — enough to grasp the concept. "
    f"Full test logs in [`tests/pbnj-outputs/`](tests/pbnj-outputs/).\n\n",
    f"| Pattern | Trigger | PB&J Output (≤140 words) |\n",
    f"|---------|---------|---------------------------|\n",
]

for pattern, badge, trigger, summary in rows:
    link = f"[{pattern}{badge}](patterns/{pattern}/pattern.md)"
    lines.append(f"| {link} | {trigger} | {summary} |\n")

lines.append(f"\n_✦ = authored gem (written from live practice) · {len(rows)} gems tested_\n\n")
lines.append("_Full outputs: [`tests/pbnj-outputs/`](tests/pbnj-outputs/) · Refresh: `bash tests/pbnj-test.sh <pattern>`_\n")

PBNJ_FILE.write_text("".join(lines))
print(f"✓ PBNJ.md generated — {len(rows)} patterns")
