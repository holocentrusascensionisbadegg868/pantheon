#!/usr/bin/env bash
# Usage: bash tests/validate-schema.sh patterns/musk-filter/pattern.md
set -euo pipefail

FILE="${1:-}"
[[ -z "$FILE" ]] && { echo "Usage: $0 <pattern.md>"; exit 1; }
[[ -f "$FILE" ]] || { echo "ERROR: file not found: $FILE"; exit 1; }

REQUIRED_FIELDS=(name aliases domain trigger practitioners events lineage origin-earliest origin-modern)
ERRORS=0

if ! grep -q "^---" "$FILE"; then
  echo "FAIL: $FILE — no YAML frontmatter found"
  exit 1
fi

for field in "${REQUIRED_FIELDS[@]}"; do
  if ! grep -q "^${field}:" "$FILE"; then
    echo "FAIL: $FILE — missing field: ${field}"
    ERRORS=$((ERRORS + 1))
  fi
done

for section in "## Protocol" "## The Book" "### The Pattern" "### Protocol (extended)" "### Anti-Pattern (extended)" "### Examples" "### Practitioners" "### Historical Events" "### Lineage" "### Origin"; do
  if ! grep -qF "$section" "$FILE"; then
    echo "FAIL: $FILE — missing section: ${section}"
    ERRORS=$((ERRORS + 1))
  fi
done

if [[ $ERRORS -eq 0 ]]; then
  echo "PASS: $FILE"
else
  echo "TOTAL FAILURES: $ERRORS in $FILE"
  exit 1
fi
