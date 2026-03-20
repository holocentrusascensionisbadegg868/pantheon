#!/usr/bin/env python3
"""Generates commands/pantheon.md — the /pantheon dispatch table, auto-built from all patterns."""
import sys
import re
import yaml
from pathlib import Path

REPO_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent
OUTPUT_FILE = REPO_ROOT / "commands" / "pantheon.md"

def extract_frontmatter(text):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}

rows = []
for pattern_file in sorted((REPO_ROOT / "patterns").glob("*/pattern.md")):
    pattern = pattern_file.parent.name
    # Only include patterns that have a claude adapter
    adapter = pattern_file.parent / "adapters" / "claude.md"
    if not adapter.exists():
        continue

    fm = extract_frontmatter(pattern_file.read_text())

    # First trigger
    triggers = fm.get("trigger", [])
    if isinstance(triggers, list):
        trigger = triggers[0].strip().strip('"') if triggers else "—"
    else:
        trigger = str(triggers).strip().strip('"')

    # First practitioner name
    practitioners = fm.get("practitioners", [])
    if practitioners and isinstance(practitioners, list):
        genius = practitioners[0].get("name", "—")
    else:
        genius = "—"

    origin_type = fm.get("origin-type", "historian")
    badge = " ✦" if origin_type == "authored" else ""

    rows.append((pattern, badge, genius, trigger))

lines = [
    "---\n",
    "description: List all available Pantheon patterns with trigger conditions and invoke instructions\n",
    "---\n\n",
    "# Pantheon — Cognitive Pattern Library\n\n",
    "Executable mental models from history's greatest problem solvers. Drop them into any AI session.\n\n",
    "---\n\n",
    "## Available Patterns\n\n",
    f"| Command | Pattern | Genius | Trigger |\n",
    f"|---------|---------|--------|--------|\n",
]

for pattern, badge, genius, trigger in rows:
    cmd = f"`/pantheon-{pattern}`"
    lines.append(f"| {cmd} | {pattern}{badge} | {genius} | {trigger} |\n")

lines += [
    "\n_✦ = authored gem (written from live practice)_\n\n",
    "---\n\n",
    "## Usage\n\n",
    "Invoke any pattern by name:\n",
    "```\n",
    "/pantheon-musk-filter\n",
    "/pantheon-andon-cord\n",
    "/pantheon-feynman-clarity\n",
    "```\n\n",
    "Patterns also auto-trigger when Claude detects the right context (if skills are installed).\n\n",
    "---\n\n",
    "## Install\n\n",
    "```bash\n",
    "curl -fsSL https://raw.githubusercontent.com/dkschrei/pantheon/main/install.sh | bash\n",
    "```\n\n",
    "Restart Claude Code to activate.\n\n",
    "---\n\n",
    f"*github.com/dkschrei/pantheon — {len(rows)} patterns*\n",
]

OUTPUT_FILE.write_text("".join(lines))
print(f"✓ commands/pantheon.md generated — {len(rows)} patterns")
