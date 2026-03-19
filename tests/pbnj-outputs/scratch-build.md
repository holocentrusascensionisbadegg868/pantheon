# PB&J Test — scratch-build

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

## Scratch Build: PB&J

**1. Identify the core computation.**
Minimum input → output: `bread + fat + sweet = edible portable meal`. Strip everything else — no crusts debate, no diagonal vs. square cut, no toasting.

**2. Propose a minimal reimplementation.**
One version. No tools beyond a knife. Target: two slices, two spreads, one sandwich.

**3. Build it end-to-end.**
- Slice 1: spread peanut butter edge-to-edge (fat layer)
- Slice 2: spread jelly edge-to-edge (sweet layer)
- Press together, peanut butter facing jelly

No cutting. No plating. That's accidental complexity.

**4. Verify it works.**
Take a bite. Does it hold together? Does it taste like PB&J? Yes → core computation is correct.

**5. Harvest understanding.**
Now you see what the original system actually does differently:
- Crusts exist to *seal* the edges — structural, not aesthetic
- Diagonal cut increases surface-area-to-bite ratio — functional, not decorative
- Toasting prevents sogginess — a real problem at scale (packed lunch)

**What scratch-build reveals:** most PB&J "opinions" are solutions to real problems. Now you can make intentional choices instead of following ritual.
