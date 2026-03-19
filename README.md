# Pantheon

> "Elon Musk didn't invent first principles thinking. Toyota didn't invent the factory stop. Steve Jobs didn't invent subtraction. Every modern genius is a synthesizer — standing on shoulders built across centuries of human problem-solving. Pantheon codifies those shoulders into a deployable AI library."

---

## What is Pantheon?

Pantheon is a library of executable cognitive patterns — distilled from history's greatest problem solvers and packaged as AI skills you can drop into any AI coding environment.

These are not quotes. Not principles. Not motivational frameworks. They are **protocols**: trigger conditions, step-by-step procedures, and anti-patterns that your AI can run when it detects the right context. History's best mental models, made executable.

Every pattern answers the same question: *what did this genius actually do differently when faced with this class of problem?*

---

## Install (Claude Code)

```bash
# Commands — invoke manually with /pantheon, /pantheon-musk-filter, etc.
cp ~/Dev-Projects/pantheon/commands/*.md ~/.claude/commands/

# Skills — auto-trigger when Claude detects the right context
cp ~/Dev-Projects/pantheon/patterns/*/adapters/claude.md ~/.claude/skills/
```

Restart Claude Code after installing.

**Available commands:**
- `/pantheon` — index, lists all patterns
- `/pantheon-andon-cord` — invoke the factory stop protocol
- `/pantheon-musk-filter` — run the pre-build gate
- `/pantheon-feynman-clarity` — run the debugging clarity test

---

## Available Patterns

See [`PATTERNS.md`](PATTERNS.md) for the full dispatch table.

| Trigger | Pattern | Genius |
|---------|---------|--------|
| Frustration signal / repeated failure | Andon Cord | Toyota |
| Any build/automate/create request | Musk Filter | Elon Musk |
| "Why isn't this working" / stuck debugger | Feynman Clarity Test | Richard Feynman |

v0.1 — 3 of 10 patterns complete. Building in stealth. Public launch when all 10 are ready.

---

## Pattern Format

Every pattern follows a canonical schema: trigger conditions, protocol, anti-pattern, real examples, and origin. See [`SCHEMA.md`](SCHEMA.md).

```
patterns/
  {pattern-name}/
    pattern.md          ← canonical content (platform-agnostic)
    adapters/
      claude.md         ← Claude Code skill
      cursor.md         ← (coming) .cursorrules entry
      openai.md         ← (coming) system prompt drop-in
```

---

## Why this exists

I burned through a session's worth of Claude tokens because an agent automated a broken process instead of questioning whether the process should exist. Classic Step 5 before Step 1. I needed the Musk Filter — I just didn't have it installed anywhere.

The Andon Cord came from the same frustration: agents that see you're stuck and keep going anyway, trying variation #4 of the same failed approach. Toyota solved this problem in 1960. It's a pull cord. Anyone can use it.

The patterns in this library are not new. They have been sitting in history books, biographies, and manufacturing manuals for decades. Pantheon is the packaging. Your AI gets the shoulders of giants, available in the moment you need them.

---

## Status

**v0.1 — private, stealth mode**

- [x] Andon Cord Protocol (Toyota)
- [x] Musk Filter (Elon Musk)
- [x] Feynman Clarity Test (Richard Feynman)
- [ ] Jobs Subtraction (Steve Jobs)
- [ ] Working Backwards (Jeff Bezos)
- [ ] Inversion (Charlie Munger)
- [ ] First Principles (Tesla / Musk)
- [ ] Hamming's Question (Richard Hamming)
- [ ] Kaizen (Toyota)
- [ ] Shannon Compression (Claude Shannon)

Going public at 10 patterns.

---

## Contributing

Coming when public. For now: [open an issue](../../issues) if you have a pattern suggestion. Include the genius, the problem class, and a real example of the pattern in action.

---

*Built by [@dkschrei](https://github.com/dkschrei) — 2026*
