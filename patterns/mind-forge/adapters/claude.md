---
name: mind-forge
description: Invoke when designing a complex multi-component system and the user wants to complete the design mentally/on paper before building — or when prototyping costs are high and the user should simulate before constructing.
---

# Mind Forge — Claude Code Adapter

## When to invoke

- User is designing a system with many interacting components
- Physical or computational prototyping is expensive (infrastructure, hardware, deployments)
- User is tempted to "just try it and see" in a domain where the interactions are predictable from first principles
- Architecture decisions where the cost of iteration is high (database schema, API contracts, distributed system topology)

## Protocol

1. **Construct the complete mental model first.** Before writing any code or config, map every component, interface, data flow, and failure mode. Write it out as a complete specification — not pseudocode, not a sketch, the full system.

2. **Simulate operation.** Walk through the system's behavior under normal load, edge cases, failure scenarios, and scale. Trace specific requests end-to-end. Identify where components interact in non-obvious ways. Document what you find.

3. **Modify and re-simulate.** For each failure or weakness found in step 2, redesign in the specification. Re-run the mental simulation. Repeat until the design survives every scenario.

4. **Build as verification.** Implement the design. The implementation should confirm the specification, not explore unknowns. If the build surprises you, the mental model was incomplete — return to step 1.

## Anti-pattern

Jumping to code before the design is complete. Rapid prototyping is valuable when the domain is unfamiliar, but when you have deep knowledge of the components and their interactions, building to think is waste.

## Hard rule

Only apply this pattern in domains where you have strong mental models of component behavior. In novel or chaotic domains (user behavior, market response, emergent system properties), build-to-learn is correct — the mind forge is not.

## Adaptation for software

In software, the "build cost" is lower than in hardware, which makes the anti-pattern (building to think) more tempting and sometimes correct. Apply the mind forge specifically to:

- **Database schema design** — migrations are expensive; simulate query patterns and data growth before committing
- **API contract design** — breaking changes are expensive; trace every consumer's usage before publishing
- **Distributed system architecture** — topology changes are expensive; simulate failure modes and network partitions before deploying
- **Security architecture** — vulnerabilities are expensive; trace every attack surface before implementing

Do NOT apply to UI components, feature experiments, or anything where user feedback is the primary unknown.
