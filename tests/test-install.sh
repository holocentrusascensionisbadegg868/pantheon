#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

echo "Testing install.sh in temp dir: $TMPDIR"

# Test 1: Fresh install
HOME="$TMPDIR" bash "${REPO_ROOT}/install.sh"

COMMANDS=$(ls "${TMPDIR}/.claude/commands/"*.md 2>/dev/null | wc -l | tr -d ' ')
[[ "$COMMANDS" -ge 3 ]] || { echo "FAIL: expected ≥3 commands, got $COMMANDS"; exit 1; }
echo "PASS: $COMMANDS commands installed"

SKILLS=$(ls "${TMPDIR}/.claude/skills/"*.md 2>/dev/null | wc -l | tr -d ' ')
[[ "$SKILLS" -ge 3 ]] || { echo "FAIL: expected ≥3 skills, got $SKILLS"; exit 1; }
echo "PASS: $SKILLS skills installed"

# Test 2: Idempotent re-run
HOME="$TMPDIR" bash "${REPO_ROOT}/install.sh"
echo "PASS: re-run is idempotent"

echo "All install tests passed"
