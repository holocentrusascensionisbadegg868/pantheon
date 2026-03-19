---
name: constraint-saturation
description: When the user faces a problem with too many possible solutions and needs to narrow to the right one — invoke this skill to systematically apply known constraints until the solution space collapses. Trigger phrases include "too many options", "which architecture", "what structure", "narrow it down", "how do I choose between".
---

# Constraint Saturation

When the solution space is too large to search exhaustively, saturate it with constraints until only the right answer survives.

## Protocol

1. **Inventory every known constraint.** Ask the user (or derive from context) every rule, requirement, measurement, compatibility need, performance bound, or hard limit the solution must satisfy. Be greedy — more constraints means fewer survivors. List them explicitly.

2. **Rank constraints by killing power.** Identify which constraints eliminate the most candidates. Apply the most discriminating constraints first. A single hard constraint (e.g., "must run on 4GB RAM", "must be backwards-compatible with API v2") can eliminate 90% of options instantly.

3. **Apply constraints simultaneously, not sequentially.** Do not pick a solution and then check constraints one by one. Instead, hold all constraints active and find what survives all of them at once. Sequential checking leads to anchoring on early favorites.

4. **Let constraints dictate the answer.** Do not impose assumptions about what the answer "should" look like. If the constraints point to an unfamiliar architecture, a non-standard pattern, or a surprising choice — trust the constraints. Pauling found 3.6 residues per turn when everyone expected a round number. The constraints were right.

5. **Flag missing constraints.** If the surviving solution space still has multiple viable candidates, the problem is under-constrained. Ask: "What additional requirement or measurement would distinguish between these remaining options?" Surface this to the user.

6. **Test the survivor.** Once a single candidate (or small set) survives, verify it against any data or requirements held back during the constraint pass. If it fails, a constraint was missed — find it.

## Anti-pattern

Picking a solution first and then rationalizing why it satisfies constraints. This is confirmation bias disguised as analysis. The constraint-saturation method works in the opposite direction: constraints first, solution emergent.

## Hard rule

Never relax a well-established constraint to make a preferred answer work. If the candidate violates a known requirement, the candidate is wrong — no matter how elegant it looks.
