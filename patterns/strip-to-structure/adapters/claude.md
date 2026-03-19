---
name: strip-to-structure
description: "When a problem feels irreducibly complex in its native domain — too many variables, special cases, or entangled concerns — strip away all domain-specific content to expose the formal structure underneath, then solve there."
---

# Strip to Structure

When you encounter a problem drowning in domain specifics — too many special cases, too many variables, too much entangled context — apply the Shannon move:

## Protocol

1. **Name what you're ignoring.** Identify the semantic content everyone treats as essential (meaning, intent, business context, physical form). Explicitly set it aside. Write it down: "I am deliberately ignoring X because it is not structural."

2. **Find the formal skeleton.** Ask: what are the actual operations, inputs, outputs, and transformations here? Rewrite the problem using only structural relationships — sets, flows, states, mappings, graphs. Look for isomorphisms: does this structure match a known solved problem in another domain?

3. **Solve in the formal system.** Work the problem in its structural form. Use the tools native to that formal system (graph algorithms, type theory, information theory, algebra). The answer is often already known — just in a different field.

4. **Map the solution back.** Translate the structural answer into domain-specific terms. The domain details stripped in step 1 become implementation constraints, not architectural decisions.

## Anti-pattern: Domain Capture

The failure mode is believing that because a problem lives in a specific domain, it requires domain-specific solutions. Signs of domain capture:
- Adding more special cases to an already complex design
- The problem keeps getting more complex as you add more domain knowledge
- Multiple domain experts disagree on the approach
- The solution "depends on context" for every case

The fix is not more domain expertise. It is a different lens entirely.

## Hard Rule

Never distort the formal model to fit domain assumptions. If the structure says a domain assumption is wrong, trust the structure.

## Example Application

A user is struggling with a complex permissions system that has dozens of special cases for different user types, resources, and contexts. Instead of adding more `if` statements:

1. **Strip:** Ignore the business meaning of "admin," "editor," "viewer" — they are just labels.
2. **Formalize:** This is a directed graph where nodes are (subject, action, resource) tuples and edges are permission grants. The question "can X do Y to Z?" is a reachability query.
3. **Solve:** Graph reachability is a solved problem. Use an adjacency list with BFS/DFS. Inheritance is just edge transitivity.
4. **Map back:** Re-label the graph nodes with business terms. The architecture is clean because it was designed from structure, not from accumulated special cases.
