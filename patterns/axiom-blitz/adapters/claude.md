---
name: axiom-blitz
description: "When a domain or problem space has no formal foundation — people reason from intuition, competing frameworks coexist, or debates cannot be settled — axiomatize the domain by defining primitives and rules, then derive results unreachable by informal reasoning."
---

# Axiom Blitz

When you encounter a domain or problem space running on informal reasoning — no shared definitions, competing mental models, debates that go in circles because there's no formal ground to stand on — apply the Von Neumann move:

## Protocol

1. **Enter as a formalist, not a practitioner.** Absorb the domain's key phenomena and results, but refuse to reason in its informal language. Ask: what are the actual *objects* here? What *operations* act on them? What do people argue about, and why can't they settle it?

2. **Lay down axioms.** Define the minimal set of primitives and rules from which known results should follow as consequences. Test: do the domain's established facts emerge from your axioms? If not, fix the axioms. If unexpected results also emerge, investigate — you may have found something new.

3. **Derive what informal reasoning cannot.** Work within the formal system. Prove what must be true, what cannot be true, and what is optimally true. These results — impossibility proofs, existence guarantees, optimality bounds — are the payoff. If the axioms only restate what was already known, you have transcribed, not axiomatized.

4. **Ship the foundation.** Present the axioms as the new shared language for the domain. Others should be able to build on them without re-deriving your results.

## Anti-pattern: Formalism Theater

Creating mathematical notation that merely restates domain knowledge in symbols, without enabling any new derivations. The test: can you derive at least one result that surprises domain experts? If not, you have dressed up the domain, not formalized it.

## Hard Rule

The axioms must be **productive** — they must generate at least one non-obvious result. Transcription is not axiomatization.

## When to Invoke

- A design discussion keeps going in circles because participants use the same words to mean different things
- A system has accumulated special cases and no one can explain the underlying logic
- Two competing approaches to a problem both have merit and no framework exists to compare them
- You need to prove that something is impossible, not just that you haven't found it yet

## Example Application

A team is debating how to handle permissions across microservices. Some want role-based access, some want attribute-based, some want capability tokens. The debate is informal and going in circles.

1. **Formalist entry:** What are the objects? Principals, actions, resources, policies. What operation matters? "Can principal P perform action A on resource R under context C?"
2. **Axioms:** A policy is a function P(principal, action, resource, context) → {allow, deny}. Policies compose: multiple policies combine via a resolution rule (deny-wins, first-match, etc.). A system is consistent if no reachable state produces contradictory policy evaluations.
3. **Derive:** From these axioms, prove: (a) role-based, attribute-based, and capability models are all representable as policy functions — they differ only in how the function is structured internally; (b) any composition rule that isn't deny-wins can produce inconsistencies in the presence of negative policies; (c) the minimum information needed to evaluate a policy is bounded by the axioms.
4. **Ship:** The team now has a shared formal model. The "which approach" debate dissolves — they're all implementations of the same axioms. The real decision is the composition rule.
