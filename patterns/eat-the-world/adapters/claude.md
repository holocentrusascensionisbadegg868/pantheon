---
name: eat-the-world
description: "Invoke when the user has built or is building technology that works but isn't reaching users — expertise barriers, complex interfaces, or missing access layers are blocking adoption. Also triggers on: 'nobody uses this', 'too hard for non-engineers', 'how do we get adoption', distribution strategy, go-to-market for technical products."
---

# Eat the World — Claude Code Adapter

When you detect that the user's problem is distribution (not invention), apply this protocol:

## Protocol

1. **Name the trapped technology.** State clearly: "The technology works. The problem is that [specific audience] can't reach it because [specific barrier]."

2. **Test readiness.** Ask: "If a non-expert could access this easily right now, would they want it?" If the answer is uncertain, the technology may not be ready — flag this risk before proceeding.

3. **Design the thinnest bridge.** Propose the minimum access layer that connects the working technology to the target user. Strip every feature that doesn't serve access. The bridge should be almost invisible — the user should feel like they're touching the technology directly.

4. **Bias toward speed.** Distribution windows are land grabs. Recommend shipping the minimum bridge fast over perfecting it slowly. "First adequate bridge captures the market; best bridge built second often captures nothing."

5. **Identify horizontal expansion.** Once the bridge design is clear, note adjacent domains where the same technology-distribution gap exists.

## Anti-Pattern Check

Watch for these failure modes:
- **"Build it and they will come"** — if the user is adding more technology features when the problem is access, flag it.
- **Premature bridging** — if the underlying technology isn't ready, say so. "The readiness threshold hasn't been crossed yet."
- **Over-engineering the bridge** — if the access layer is becoming complex enough to need its own documentation, it's too thick. Simplify.

## Hard Rule

Never recommend building the distribution layer before confirming the technology actually works reliably. Premature distribution burns credibility and capital.

## Source

See `patterns/eat-the-world/pattern.md` for the full pattern, historical examples, and lineage.
