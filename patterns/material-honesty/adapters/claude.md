---
name: material-honesty
description: Invoke when a design adds intermediary layers between user and function — decorative wrappers, fake textures, coatings over honest materials, UI chrome that hides the mechanism. Strips layers so the material and form communicate directly.
---

# Material Honesty — Claude Code Adapter

## When to invoke
- Design review where layers are accumulating between user and core function
- UI adding chrome, decoration, or skeuomorphic elements that don't match the actual medium
- Architecture wrapping honest interfaces in unnecessary abstraction layers
- API surface hiding its true behavior behind decorative naming or redundant wrappers
- Someone proposes coating, hiding, or decorating something that could speak for itself

## Protocol

1. **NAME THE MATERIAL** — What is the actual medium the user touches? (screen, API, CLI, physical object) Don't design for an abstraction — design for the real substance.

2. **ASK WHAT IT WANTS TO BE** — Given the medium's real properties, what form does it naturally enable? A CLI wants to be terse and composable. An API wants to be predictable and self-describing. A touch screen wants to be direct and gestural. Follow the material.

3. **STRIP EVERY INTERMEDIARY LAYER** — For each layer between user and function: does it exist because the material requires it, or because someone is hiding something? If hiding → remove.

4. **TEST FOR DISHONESTY** — Does the design claim a property the material doesn't have? A CLI pretending to be a GUI (ASCII art menus). An API wrapping simple operations in enterprise abstractions. A config file hiding behind a wizard. If the medium is pretending to be something else, the design is lying.

5. **VERIFY BY TOUCH** — Put it in someone's hands. If they sense the honesty — the directness of a clean API, the clarity of an undecorated interface — the design is working. If it feels "enterprise" or "overengineered" despite simple underlying operations, a dishonest layer is hiding the truth.

## Anti-pattern
Designing an arbitrary interface shape and then implementing it in a medium that fights it. The software equivalent: wrapping a simple function in three layers of abstraction because "that's how you do it" — coating an intrinsically clean operation in unnecessary architecture.

## Hard rule
Never wrap an honest interface in decoration. Never fake a capability the system doesn't have.
