# PB&J Test — time-and-motion

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

## Time-and-Motion: PB&J Sandwich

**1. Decompose into observable units**

| Step | Operation |
|------|-----------|
| A | Open bread bag, extract 2 slices |
| B | Open PB jar, unscrew lid |
| C | Dip knife into PB, spread slice 1 |
| D | Wipe knife on bread edge |
| E | Open jelly jar, unscrew lid |
| F | Dip knife into jelly, spread slice 2 |
| G | Press slices together |
| H | Close both jars |

**2. Measure each unit** (estimated seconds)

A=4, B=3, C=8, D=2, E=3, F=7, G=1, H=6 → **Total: 34s**

**3. Identify the waste**

- Step D (knife wipe): 2s of zero-value contamination prevention — solved by sequencing, not wiping
- Steps B and E are sequential jar-opens that could be batched
- H is deferred cleanup happening after the goal is complete

**4. Reassemble the one best way**

Open both jars first (batch B+E = 4s). Spread PB. Flip knife to clean side, spread jelly — eliminates D entirely. Press. Close jars.

**New total: ~28s. 18% faster.**

**5. Set the standard**

New sequence: Open all containers → PB → flip knife → jelly → assemble → close. The knife flip is the critical technique. Benchmark: under 30 seconds.
