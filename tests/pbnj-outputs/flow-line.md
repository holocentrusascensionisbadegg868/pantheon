# PB&J Test — flow-line

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

## Flow Line: PB&J Sandwich

**The batch way:** Gather ALL ingredients → lay out ALL bread → open ALL jars → spread ALL peanut butter → spread ALL jelly → assemble ALL sandwiches → cut ALL sandwiches.

Work piles up between stages. If you're making 4 sandwiches, you have 4 open-faced PB halves sitting idle waiting for jelly.

---

**Flow Line applied:**

**1. DECOMPOSE**
Lay bread → spread PB → spread jelly → close → cut → plate

**2. SEQUENCE**
Strict linear order. No pre-opening jars ahead of time. No pre-spreading.

**3. BRING WORK TO THE WORKER**
The sandwich moves left to right across the counter. You stay put. Bread → you → done.

**4. SYNCHRONIZE**
Slowest station: spreading PB (thick, takes 8 sec). Split: scoop first, then spread. Now no single step dominates.

**5. STOP THE STALLS**
Stall identified: bread bag twist-tie. Replace with fold-over. Sandwich never waits on the bag.

---

**Result:** Sandwich #1 is plated before Sandwich #2 is started. No idle inventory. Defects (too little jelly) caught immediately — not after 4 sandwiches are already assembled wrong.
