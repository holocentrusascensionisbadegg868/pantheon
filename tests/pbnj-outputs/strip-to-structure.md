# PB&J Test — strip-to-structure

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

## Strip to Structure: PB&J Edition

**Step 1 — Name what I'm ignoring.**
I am deliberately ignoring: bread type, PB brand, smooth vs. crunchy, jelly vs. jam, crust preferences, knife material. These are domain content, not structure.

**Step 2 — Find the formal skeleton.**
What actually exists here?

- 3 surfaces: `top_bread`, `bottom_bread`, `air_gap`
- 2 substances: `substance_A`, `substance_B`
- 1 operation: `coat(substance, surface)`
- 1 operation: `join(surface_1, surface_2)`
- Constraint: coated faces must face inward at join

The problem reduces to: **assign two substances to two surfaces such that coated faces are interior after join.**

**Step 3 — Solve in the formal system.**
Valid assignments: coat A on top, coat B on bottom → join(top↓, bottom↑). That's it. There's only one structural class of solution (swapping A/B is isomorphic).

**Step 4 — Map back.**
- `substance_A` = peanut butter, applied to bottom slice
- `substance_B` = jelly, applied to top slice
- `join` = press slices together, coated faces inward

**What the pattern reveals:** The "complexity" of PB&J (which side? which order?) was entirely domain noise. The structure has exactly one solution class.
