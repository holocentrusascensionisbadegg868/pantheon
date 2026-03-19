---
name: complementarity
description: When two valid but contradictory frameworks both make correct predictions in different contexts, resist choosing one. Instead, identify the context switch that determines which applies, draw the exclusion boundary, and build a meta-framework that governs when each is used. Use when the user says "it depends," faces two architectures that both work but contradict, or is trying to force-merge incompatible approaches.
---

# Complementarity — Claude Code Adapter

## When to invoke

- The user has two valid approaches, architectures, or models that contradict each other but each captures something the other misses
- A design decision is framed as either/or, but both options have genuine merit and genuine drawbacks
- The user is trying to unify two systems or approaches and the merge keeps producing compromises that weaken both
- Someone says "it depends on how you look at it" or "both of these are right but they can't both be right"
- Two well-established patterns or best practices conflict in a specific context

## Protocol

1. **Name both frameworks.** State explicitly what each one captures that the other misses. If one is strictly better, say so and skip this pattern — just use that one.

2. **Find the context switch.** Identify what changes between the situations where framework A works and framework B works. This is the "experimental arrangement" — the variable that determines which description applies. Examples: read-heavy vs. write-heavy workloads, exploration vs. exploitation phases, greenfield vs. legacy codebases.

3. **Draw the exclusion boundary.** State what you cannot do: you cannot apply both simultaneously in the same context. A system optimized for consistency cannot simultaneously be optimized for availability (CAP theorem). A codebase cannot simultaneously be maximally DRY and maximally readable at every point. Name the trade-off explicitly.

4. **Build the meta-framework.** Deliver not a single answer but a decision rule: "In context X, use framework A. In context Y, use framework B. Here is how to tell which context you're in." This map is the actual deliverable.

5. **Use tension as diagnostic.** When a new case doesn't fit cleanly, that's signal — it reveals a context boundary worth investigating, not a failure of either framework.

## Anti-pattern

Premature unification: forcing both approaches into a hybrid that "gets the best of both worlds" but actually captures the weaknesses of both. If the merge keeps feeling like a compromise, stop merging — you're probably in a complementarity situation.

## Example application

**Scenario:** A team debates microservices vs. monolith. Both architectures have proven track records. The microservices advocates cite independent deployment and scaling. The monolith advocates cite simplicity, debugging ease, and lower latency.

**Context switch identified:** Team size and domain boundary clarity. Small teams with unclear domain boundaries → monolith works better. Large teams with well-defined domain boundaries → microservices work better.

**Exclusion boundary:** You cannot get independent deployment (microservices) and single-process debugging (monolith) simultaneously for the same component. The two benefits are complementary — mutually exclusive in a single context.

**Meta-framework delivered:** "Start monolithic. When you can draw a clean domain boundary AND have a team large enough to own each side independently, extract that boundary into a service. The trigger for extraction is organizational, not technical. Components without clear ownership boundaries stay in the monolith."
