#!/usr/bin/env bash
# PB&J Test — unit test for a single Pantheon gem
# Usage: bash tests/pbnj-test.sh <pattern-name>
# Output: tests/pbnj-outputs/<pattern-name>.md
#
# The PB&J test applies every gem to the same static problem:
#   "Construct a Peanut Butter and Jelly Sandwich"
# This produces a comparable, human-readable sample of what the gem actually does.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="${SCRIPT_DIR}/pbnj-outputs"
mkdir -p "$OUTPUT_DIR"

PATTERN="${1:-}"
if [ -z "$PATTERN" ]; then
  echo "Usage: bash tests/pbnj-test.sh <pattern-name>"
  exit 1
fi

ADAPTER="${REPO_ROOT}/patterns/${PATTERN}/adapters/claude.md"
if [ ! -f "$ADAPTER" ]; then
  echo "ERROR: adapter not found at $ADAPTER"
  exit 1
fi

ADAPTER_CONTENT=$(cat "$ADAPTER")

PROMPT="You are demonstrating a cognitive pattern from the Pantheon library.

Apply the following pattern to this exact task: **Construct a Peanut Butter and Jelly Sandwich**

Show the pattern in action step by step. Be concrete and specific to the PB&J task — do not describe the pattern abstractly. The output should make it immediately obvious what this pattern does differently.

Keep your response under 200 words.

--- PATTERN ---
${ADAPTER_CONTENT}
--- END PATTERN ---

Now apply it to: Construct a Peanut Butter and Jelly Sandwich"

echo "Running PB&J test for: $PATTERN"
OUTPUT=$(claude --dangerously-skip-permissions -p "$PROMPT" 2>/dev/null)

# Write output file
cat > "${OUTPUT_DIR}/${PATTERN}.md" << EOF
# PB&J Test — ${PATTERN}

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

${OUTPUT}
EOF

echo "✓ Saved: tests/pbnj-outputs/${PATTERN}.md"
echo "$OUTPUT"
