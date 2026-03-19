# PB&J Test — mind-forge

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

## Mind Forge: PB&J Sandwich

**Step 1 — Complete mental model first**

Components: 2 bread slices, peanut butter jar, jelly jar, knife, plate.

Interfaces: knife-to-bread (spreading surface), bread-to-bread (mating face), knife-to-jar (extraction).

Data flows: PB exits jar → knife → slice A (bottom face). Jelly exits jar → knife → slice B (bottom face). Slice B inverts onto slice A.

**Step 2 — Simulate operation**

Trace the assembly: Spread PB on slice A. Knife now has PB residue. Knife goes into jelly jar → jelly is now contaminated with PB. Cross-contamination failure detected.

Edge case: if jelly is applied first, PB residue goes into jelly jar. Same failure either way.

Scale scenario: making 10 sandwiches — contamination compounds.

**Step 3 — Redesign and re-simulate**

Fix: use two knives (one per jar) OR wipe knife between spreads.

Re-simulate: knife 1 spreads PB on slice A. Knife 2 spreads jelly on slice B. Flip B onto A. Jars remain uncontaminated. Design survives.

**Step 4 — Build as verification**

Execute the assembly. The two-knife approach works exactly as modeled. No surprises.
