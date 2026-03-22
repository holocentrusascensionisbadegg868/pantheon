#!/usr/bin/env bash
# Historian targeted research — research any person, event, or era on demand.
# Usage: bash historian/target.sh "Florence Nightingale"
#        bash historian/target.sh "The Berlin Airlift"
#        bash historian/target.sh "Bell Labs 1947-1967"
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
PROMPT_TPL="${SCRIPT_DIR}/target-prompt.md"

TARGET="${*}"

if [[ -z "$TARGET" ]]; then
  echo "Usage: bash historian/target.sh \"<person, event, or era>\""
  echo ""
  echo "Examples:"
  echo "  bash historian/target.sh \"Florence Nightingale\""
  echo "  bash historian/target.sh \"The Berlin Airlift\""
  echo "  bash historian/target.sh \"Bell Labs 1947-1967\""
  exit 1
fi

if ! command -v claude &>/dev/null; then
  echo "ERROR: claude CLI not found. Install: npm install -g @anthropic-ai/claude-code"
  exit 1
fi

echo ""
echo "=== Researching: $TARGET ==="
echo ""

PROMPT=$(sed "s/{TARGET}/$TARGET/g" "$PROMPT_TPL")

cd "$REPO_ROOT"
if ! claude --dangerously-skip-permissions -p "$PROMPT"; then
  echo "ERROR: Claude failed on '$TARGET'"
  exit 1
fi

bash scripts/generate-patterns.sh
bash scripts/generate-pbnj.sh
bash scripts/generate-practitioners.sh
python3 scripts/generate-commands.py "$REPO_ROOT"

if ! git diff --quiet || ! git diff --staged --quiet; then
  git add patterns/ commands/ PATTERNS.md PBNJ.md PRACTITIONERS.md tests/pbnj-outputs/
  git commit -m "feat(patterns): $TARGET gem added (targeted research)"
  git push
  echo ""
  echo "✓ Committed + pushed: $TARGET"
else
  echo "WARNING: No new files detected — may have been merged into an existing gem."
  echo "Check the output above to see which gem was updated."
fi
