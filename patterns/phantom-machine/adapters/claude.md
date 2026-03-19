---
name: phantom-machine
description: "Invoke when the user faces a problem that seems to require human judgment or is declared 'impossible to automate' — construct the specific machine that would solve it, then interrogate its limits."
---

# Phantom Machine — Claude Code Adapter

## When to invoke

- User says something is "impossible," "can't be automated," "requires human judgment"
- User is debating feasibility without constructing a mechanism
- User is stuck on a design problem and arguing about possibility in the abstract
- User needs to determine whether a problem is an engineering gap or a fundamental limit

## Protocol

1. **Construct the machine.** Ask: "What would a system that solves this need to do?" Specify inputs, operations, and outputs concretely. Write pseudocode or a system diagram — even if the machine can't be built yet.
2. **Run it on paper.** Trace the machine's behavior on the user's actual problem instance. Identify where it succeeds and where it gets stuck.
3. **Interrogate the limits.** Classify each stuck point:
   - **Engineering gap:** solvable with more data, better algorithms, faster hardware, or existing techniques combined differently.
   - **Fundamental limit:** no machine of this type can solve this (complexity bound, undecidability, information-theoretic limit).
4. **Build or bound.** For engineering gaps: propose the implementation path. For fundamental limits: name the bound explicitly and redefine the problem to work within it.

## Hard rule

Always construct the machine first. Never debate possibility without a concrete mechanism to interrogate. Philosophy without mechanism is the anti-pattern.

## Example application

User: "We can't automate code review — it requires human judgment."

1. **Construct:** What would an automated code review machine need? Inputs: diff, codebase context, style guide, test results. Operations: pattern matching against known bug classes, style conformance checking, complexity analysis, test coverage verification. Output: annotated diff with findings.
2. **Run on paper:** On a real diff — catches style violations, missing tests, known anti-patterns. Gets stuck on: design intent, business context, naming quality beyond convention.
3. **Interrogate:** Style/pattern/test coverage = engineering gap (solvable now). Design intent = requires context the machine doesn't have (engineering gap — solvable with better context injection). Subjective "good naming" = harder, but decomposable into measurable proxies.
4. **Build or bound:** Build the machine for the engineering-gap parts (80%+ of review burden). Bound the remainder: flag for human review with specific questions, not "please review."
