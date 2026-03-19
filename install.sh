#!/usr/bin/env bash
set -euo pipefail

PANTHEON_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_COMMANDS="${HOME}/.claude/commands"
CLAUDE_SKILLS="${HOME}/.claude/skills"

echo "Installing Pantheon..."

[[ -d "${PANTHEON_DIR}/commands" ]] || { echo "ERROR: commands/ not found. Run from repo root."; exit 1; }
[[ -d "${PANTHEON_DIR}/patterns" ]] || { echo "ERROR: patterns/ not found. Run from repo root."; exit 1; }

mkdir -p "${CLAUDE_COMMANDS}" "${CLAUDE_SKILLS}"

cp "${PANTHEON_DIR}"/commands/*.md "${CLAUDE_COMMANDS}/"
COMMANDS_COUNT=$(ls "${PANTHEON_DIR}"/commands/*.md | wc -l | tr -d ' ')
echo "  ✓ ${COMMANDS_COUNT} commands → ${CLAUDE_COMMANDS}/"

SKILLS_COUNT=0
for adapter in "${PANTHEON_DIR}"/patterns/*/adapters/claude.md; do
  gem_name=$(basename "$(dirname "$(dirname "$adapter")")")
  cp "$adapter" "${CLAUDE_SKILLS}/pantheon-${gem_name}.md"
  SKILLS_COUNT=$((SKILLS_COUNT + 1))
done
echo "  ✓ ${SKILLS_COUNT} skills → ${CLAUDE_SKILLS}/"

echo ""
echo "Pantheon installed. Restart Claude Code to activate."
echo ""
echo "Available commands:"
for cmd in "${PANTHEON_DIR}"/commands/*.md; do
  echo "  /$(basename "$cmd" .md)"
done
