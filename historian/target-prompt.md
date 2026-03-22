Research {TARGET} and identify the single most important cognitive pattern it represents.

{TARGET} may be a person, historical event, organization, era, or competitive dynamic.

Requirements:
1. ONE pattern only — not a list. The ONE defining move or mental model.
2. The move, not the biography — what was actually done differently that explains the result.
3. Executable — expressible as numbered steps someone else can follow today.
4. Historically grounded — at least one real event where the pattern was applied (or violated).
5. Duplicate check — before creating a new file, run `ls patterns/` and skim each existing pattern.md.
   - If {TARGET}'s pattern is substantially the same as an existing gem, add the relevant practitioners/events to that existing gem instead of creating a new file.
   - If it's a distinct pattern, create a new gem.

For events and eras (not individual people):
- Identify the practitioner(s) most responsible for the pattern in this context
- Use the event/era as the primary evidence in the events[] field
- Name the gem after the pattern itself, not the event

Output:
- If new gem: write `patterns/{gem-name}/pattern.md` and `patterns/{gem-name}/adapters/claude.md` using SCHEMA.md
- If existing gem: update the practitioners[] and events[] in the existing pattern.md frontmatter

Gem naming: use the most recognizable label for the underlying cognitive pattern. Prefer concept names over person names unless the person IS the concept (e.g. "feynman-clarity").

After writing, run:
  bash scripts/generate-patterns.sh
  bash scripts/generate-practitioners.sh
  python3 scripts/generate-commands.py .
