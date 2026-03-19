# Pantheon Pattern Schema

Every pattern in the Pantheon library follows this canonical format.
Pattern files live at `patterns/{name}/pattern.md`.
Platform adapters live at `patterns/{name}/adapters/{platform}.md`.

---

## pattern.md Format

```markdown
# {Genius Name} — {Pattern Name}

**Domain**: {The class of problems this pattern solves}
**Trigger contexts**:
  - {Situation 1 where this pattern should fire}
  - {Situation 2}
  - {Situation 3}

---

## The Pattern

{The distilled mental model in 2-3 sentences. What the genius actually does differently.
Not biography — the move.}

---

## Protocol

{Numbered steps. Concrete and executable. No vague advice.}

---

## Anti-Pattern

{What happens when this pattern is NOT applied — the specific failure mode it prevents.
Name the failure, describe what it looks like in practice.}

---

## Examples

{Real incidents where this pattern applied or was violated. Specific > generic.}

---

## Origin

{Who the genius is, where this pattern comes from, why it works.
1-2 paragraphs. Historical grounding, not motivational framing.}
```

---

## adapters/{platform}.md Format

Adapters translate the canonical pattern into platform-specific syntax.

### Claude Code Adapter (adapters/claude.md)

```markdown
---
name: {pattern-name}
description: {One sentence trigger condition — when Claude Code should invoke this skill.
             Be specific: include trigger phrases, contexts, and what the skill does.}
---

{Pattern content formatted as a Claude Code skill.
Reference the canonical pattern.md for source of truth.
Keep the protocol executable — Claude follows it step by step.}
```

---

## Rules for Pattern Authors

1. **Trigger first** — the trigger condition must be unambiguous. If a reader can't tell when to invoke it, rewrite it.
2. **Protocol beats prose** — numbered steps, not paragraphs. An agent must be able to execute it without interpretation.
3. **Anti-pattern is mandatory** — every pattern must name the failure mode it prevents. The anti-pattern is half the value.
4. **Examples must be real** — invented examples are weaker than real incidents. If you don't have one, note it as (pending) and add one when it fires.
5. **Origin is history, not hype** — cite where the pattern comes from. No hagiography.
6. **One genius, one domain** — patterns should have a clear owner and a specific problem class. Avoid patterns that "apply to everything."
