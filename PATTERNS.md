# Pantheon Pattern Dispatch Table

Match your problem class to a pattern. Install the adapter for your AI platform and invoke it.

---

## Available Patterns (v0.1 — 3 of 10)

| Problem Class | Pattern | Genius | Directory |
|--------------|---------|--------|-----------|
| Frustration signal — profanity, "going in circles", repeated failure | **Andon Cord** | Toyota / Taiichi Ohno | `patterns/andon-cord/` |
| Build / create / automate / add request | **Musk Filter** | Elon Musk | `patterns/musk-filter/` |
| "I don't understand why this isn't working" / debugging loops | **Feynman Clarity Test** | Richard Feynman | `patterns/feynman-clarity/` |

---

## Planned Patterns (v1.0 target — 10 total)

| Problem Class | Pattern | Genius |
|--------------|---------|--------|
| Over-engineering / scope creep | Jobs Subtraction | Steve Jobs |
| Starting to build before defining done | Working Backwards | Jeff Bezos |
| Can't see a path forward — invert the problem | Inversion | Charlie Munger |
| Iterating on broken instead of reimagining from scratch | First Principles | Nikola Tesla / Elon Musk |
| Losing focus — "am I working on the most important problem?" | Hamming's Question | Richard Hamming |
| Skipping steps that create rework downstream | Kaizen | Toyota |
| Signal vs noise — cutting what doesn't change the output | Shannon Compression | Claude Shannon |

---

## How to use this table

1. Identify the problem class you're experiencing
2. Find the matching pattern
3. Copy `patterns/{name}/adapters/claude.md` to `.claude/skills/` (or your platform's equivalent)
4. Invoke the skill when the trigger condition fires

See `SCHEMA.md` for the canonical pattern format and adapter specifications.
