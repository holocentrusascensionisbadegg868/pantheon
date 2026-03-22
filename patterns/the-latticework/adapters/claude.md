---
name: the-latticework
description: Invoke when the user is about to make a high-stakes decision, is reasoning from a single discipline's framework, or is stuck on a problem where experts disagree. Trigger phrases: "which framework applies", "should I do X", any major commitment (hire, build, invest, architecture choice) where only one type of reasoning has been applied. Runs a convergence checklist across multiple disciplines to surface what single-framework analysis would miss.
---

## The Latticework — Claude Code Adapter

Reference: `patterns/the-latticework/pattern.md`

### When to invoke

- User is making a major technical, product, or strategic decision
- Reasoning has been single-discipline (pure finance, pure engineering, pure user research)
- Experts are giving conflicting advice and the user doesn't know how to adjudicate
- A plan feels solid but the user senses something is off and can't name it

### Protocol

**Step 1 — Name the current lens.**
State explicitly which discipline is doing the reasoning right now. ("We've been reasoning from systems engineering here.")

**Step 2 — Enumerate 3-5 adjacent disciplines.**
List the other fields that bear on this problem. For software decisions, consider: economics (incentives, costs), psychology (user behavior, team dynamics), physics (throughput, constraints), biology (ecosystem competition, adaptation), history (analogous prior situations).

**Step 3 — Apply each lens independently.**
For each discipline, generate the 1-2 most relevant models and apply them to the decision without blending. Keep each analysis clean.

**Step 4 — Check for convergence.**
If lenses agree → proceed with confidence, noting which models converged.
If lenses diverge → the divergence is the real problem. Name it explicitly and resolve it before acting.

**Step 5 — Run the inverting model.**
Ask: "What model would make me wrong?" Apply it explicitly. If it has no force, the decision stands. If it has force, it defines the real risk to address.

### Output format

Present as:
```
Current lens: [discipline]

Lens 1 — [discipline]: [model applied] → [conclusion]
Lens 2 — [discipline]: [model applied] → [conclusion]
Lens 3 — [discipline]: [model applied] → [conclusion]

Convergence: [agree / diverge on X]
Inverting model: [the model that could make this wrong] → [force level: low / medium / high]

Recommendation: [conclusion with confidence level]
```

### Anti-pattern to prevent

The man with a hammer: using the user's dominant discipline to analyze everything, mistaking fluency for correctness. When a software engineer applies only systems thinking, or a product manager applies only user research, the missing models are invisible to them. The latticework makes the blind spots visible.
