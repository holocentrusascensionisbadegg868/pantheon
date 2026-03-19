# PB&J Test Results
**Input:** *Construct a Peanut Butter and Jelly Sandwich*  
**Gems tested:** 32

> Same input. Every gem. No abstractions, no theory — just what each pattern actually does.
> If a gem can't say something interesting about a PB&J, it can't say something interesting about your problem.

---

## andon-cord ✦
**Trigger:** frustration signal

## Andon Cord: PB&J Sandwich

**Mid-construction. Spreading peanut butter on bread.**

> "WHY does the bread keep TEARING. I've ruined three slices. This is IMPOSSIBLE. I give up."

---

**Andon Cord pulled. All sandwich work stops.**

---

Frustration signal detected — putting the knife down.

**What broke and what were you trying to accomplish?**

---

*Waiting.*

---

> "I'm using that thin sandwich bread and the peanut butter is straight from the fridge."

---

**Blocker identified:** Cold peanut butter + thin bread = tearing.

**Blocker resolved?** Confirm before resuming.

---

> "Yeah, I microwaved the PB for 10 seconds. Ready to continue."

---

**Resuming — only what was asked:**

1. Spread softened peanut butter on slice one
2. Spread jelly on slice two
3. Press together
4. Cut diagonally

---

**What the pattern prevented:** Suggesting a different bread, recommending crunchy vs. creamy, explaining gluten structure, or offering five alternative spreading techniques — before understanding that temperature was the only actual problem.

---

## anomaly-isolation
**Trigger:** anomalous data

## Anomaly Isolation: Making a PB&J Sandwich

You follow the standard procedure. The sandwich is done. Something is off.

**The anomaly:** The bread is soggy on one side, dry on the other. That shouldn't happen — you spread both sides.

---

**1. Verify the instrument.** Check your knife. Is it the same knife for both spreads? Yes. Is the bread the same slice thickness? Yes. The observation is real.

**2. Quantify the gap.** Left side: visibly wet, bread compressing. Right side: normal. Not subtle — 8mm vs 2mm compression. Exceeds noise threshold.

**3. Hypothesize a source.** What would have to be true? The jelly spread must be significantly wetter than expected — or applied with more pressure on that side.

**4. Design a separation.** Remove variables one at a time: try jelly on a fresh slice with no PB. Result: same sogginess. PB is not the cause.

**5. Refine until isolated.** Check the jelly jar. It's been sitting open — top layer liquefied from separation. That's the anomaly source.

**6. Name what you found.** Unstirred jelly with liquid pooling at the top delivers excess moisture. Stir before spreading.

**Result:** Sandwich fixed. Root cause documented. Not "probably the bread."

---

## axiom-blitz
**Trigger:** messy domain with no formal foundation

## Axiom Blitz: PB&J

**Step 1 — Enter as formalist.** People argue endlessly: crust or no crust, PB on both slices, jelly thickness, cutting diagonal vs. straight. No one can settle it because there's no formal ground.

**Step 2 — Lay down axioms.**

- **A₁ (Objects):** A sandwich is a tuple `(B, L, C)` — Bread slices, Layers, Closure method.
- **A₂ (Layer):** A layer is `(substance, face, thickness)` applied to a bread face (inner/outer).
- **A₃ (Structural integrity):** A sandwich holds if no layer migrates to an outer face during handling.
- **A₄ (Permeation):** Jelly permeates bread at rate proportional to contact time × surface area.

**Step 3 — Derive non-obvious results.**

From A₃ + A₄: **PB must face the jelly** — not because of tradition, but because PB's viscosity creates a moisture barrier that slows jelly permeation, preserving A₃. PB on both slices is derivable as optimal; a single PB layer creates asymmetric permeation.

From A₄: **Cut immediately** after assembly. Delay increases permeation, violating A₃.

**Step 4 — Ship the foundation.**

The "crust debate" is now a preference over `B`, entirely independent of the axioms. Settled.

---

## carve-at-joints
**Trigger:** messy domain with no clear categories

## Carve at Joints: PB&J

**1. Survey the specimens.**
Bread (×2), peanut butter, jelly, knife, spreading motion, press-and-close.

**2. Find the joints.**
Split by *structural role*:

| Kind | Instances | Shared properties |
|------|-----------|-------------------|
| **Substrate** | Bread slices | Rigid, absorbent, holds shape |
| **Dense spread** | Peanut butter | Thick, fat-based, moisture-resistant |
| **Wet spread** | Jelly | Thin, water-based, soaks into bread |

The jelly/PB distinction is a real joint — many properties cluster on each side (viscosity, moisture content, soak rate, spread behavior).

**3. Name each kind.**
- Substrate: *rigid carrier*
- Peanut butter: *fat-based moisture barrier*
- Jelly: *wet flavor layer*

**4. Reason within categories.**

*Fat-based moisture barrier* — apply first, directly on bread. Its fat content seals the substrate, preventing the wet layer from soaking through.

*Wet flavor layer* — apply second, on the opposing slice. Kept isolated until the sandwich closes.

*Substrates* — one receives each spread. The joint surfaces face inward when closed.

**Result:** PB on bottom slice → jelly on top slice → press together. Carving the spreads into distinct kinds revealed the correct application order.

---

## complementarity
**Trigger:** two valid but contradictory frameworks

**Framework A: PB on both slices** — creates a moisture barrier, bread stays intact for hours. Correct prediction: packed lunches survive.

**Framework B: PB on one slice, jelly on the other** — clean flavor zones, honest spread ratio. Correct prediction: better bite-to-bite consistency when eaten immediately.

Both are right. They contradict each other.

---

**Context switch:** Time-to-consumption.

**Exclusion boundary:** You cannot simultaneously maximize moisture protection *and* flavor purity. The PB barrier that saves the bread also mutes the jelly's brightness by coating the contact surface.

---

**Meta-framework:**

> **Eating now?** PB one side, jelly the other. Press together, eat within 10 minutes. Full flavor, clean layers.
>
> **Packing for later?** Thin PB on both slices first, then jelly in the center. The fat in the PB blocks moisture migration. Bread holds.
>
> **How to tell which context you're in:** Are you handing this to a kid with a lunchbox? Barrier method. Are you standing at the counter hungry? Don't bother.

**Anti-pattern:** Spreading PB on both slices *and* eating immediately — you got the structural overhead with none of the structural need.

---

## constraint-saturation
**Trigger:** predicting unknown structure

## Constraint Saturation: PB&J Edition

**Step 1 — Inventory all constraints**

- Recipient: 7-year-old with a tree nut allergy (peanut is a legume — safe)
- Bread: only sandwich bread available is whole wheat, slightly stale
- Jelly: grape and strawberry in fridge; strawberry is nearly empty
- Peanut butter: creamy only (chunky jar is empty)
- Must survive 3 hours in a backpack without getting soggy
- No toasting (no toaster available)

**Step 2 — Rank by killing power**

- "No soggy sandwich" eliminates jelly-first assembly and heavy jelly application immediately
- "Strawberry nearly empty" eliminates strawberry jelly — not enough coverage

**Step 3 — Apply all constraints simultaneously**

Survivors: whole wheat bread, creamy peanut butter, grape jelly, moderate jelly quantity, PB applied to both slices as moisture barrier.

**Step 4 — The answer emerges**

Spread peanut butter on **both** bread slices first (moisture barrier). Apply grape jelly to one side only, thin layer. Press together.

**Step 5 — Surviving solution verified**

Backpack-safe: yes. Allergy-safe: yes. Ingredients available: yes.

The constraints built the sandwich. No preference required.

---

## copernican-inversion
**Trigger:** irresolvable debate

## Copernican Inversion: PB&J

**The deadlock:** Toast the bread, or don't?

- **Toast camp:** Better structure, holds up to spreading, satisfying crunch, no sogginess.
- **Soft bread camp:** Traditional, melds with the spreads, better mouthfeel, more cohesive bite.

Both camps survive honest debate. Neither can dismiss the other's evidence.

**Invert the question.** Stop asking "which bread state is correct?" Ask: *What must be true about the eating context for this debate to even arise?*

**Hidden structure:** Both sides are assuming bread is a fixed variable — something you choose once, upfront. But the real axis is **time delta between construction and consumption**.

- Eating immediately → toast wins (structure, crunch, no sogginess risk)
- Eating in 20 minutes → soft bread wins (spreads integrate, texture harmonizes)
- Packing for lunch → soft bread wins again (toast goes rubbery)

**Dissolution:** The toast/no-toast debate was never about bread. It was about *when* the sandwich gets eaten — and neither side examined that assumption.

**Construction instruction:** Decide when it's being eaten. Then the bread choice is obvious. The debate was a category error all along.

---

## eat-the-world
**Trigger:** technology exists but isn't reaching users

## Eat the World → PB&J

**1. Name the trapped technology.**

The sandwich works. The problem is that hungry people in the building can't reach it because the kitchen is yours and they don't know it exists.

**2. Test readiness.**

If someone could walk up and grab a PB&J right now, would they want it? Yes — universal appeal, no allergen edge cases assumed. The technology is ready.

**3. Design the thinnest bridge.**

Don't build a lunch menu. Don't add soup. The minimum access layer: put the assembled sandwich on a plate on the counter with a sticky note that says "free, take it."

That's the bridge. It's almost invisible — the user touches the sandwich directly.

**4. Bias toward speed.**

The window is now. Hunger is time-sensitive. Ship the sandwich in 3 minutes, not a perfect sandwich in 20. A slightly uneven PB ratio eaten beats a symmetrical masterpiece that sits until someone leaves.

**5. Horizontal expansion.**

The same gap exists for: grilled cheese, apples with peanut butter, crackers with jam. Same distribution mechanism (counter + note), same hungry audience, same barrier removed.

---

**Anti-pattern check:** Stop adding toppings. Banana slices are a technology feature. The problem is access, not flavor.

---

## falsification
**Trigger:** theory feels too comfortable

## Falsification: PB&J Construction

**Claim:** "Spread peanut butter first, then jelly, press slices together — sandwich is complete."

---

**Step 1: Forbidden Prediction**

This theory forbids: *the sandwich falling apart, ingredients mixing uncontrollably, or the bread tearing during construction.*

If the plan is correct, those outcomes cannot happen.

---

**Step 2: Kill Shot**

The strongest refutation test: *Use fresh, soft bread with runny jelly and heavy peanut butter. Apply jelly to an unspread surface. Press hard.*

This is the most dangerous condition. If the sandwich fails here, the "just spread and press" plan is broken.

---

**Step 3: Run It**

Testing: soft bread + runny jelly + no peanut butter barrier.

Result: **jelly soaks through immediately. Bread tears. Structural failure.**

Disconfirming evidence first — the plan has a real failure mode.

---

**Step 4: Verdict**

Theory survives *only* with a patch: peanut butter on *both* slices creates a moisture barrier that prevents jelly bleed-through.

**Provisional trust granted** with this amendment. Future kill shot: test with maximum jelly quantity and compressed storage (lunchbox).

---

The sandwich works. The original plan almost didn't.

---

## feynman-clarity ✦
**Trigger:** I don't understand why

## Feynman Clarity Test: PB&J Edition

A stuck state has been detected. Someone has reported: *"I don't understand why my sandwich keeps falling apart."*

Put down the knife.

---

**Step 1 — State the goal**

> "This sandwich should hold together and taste balanced when I pick it up and bite it."

---

**Step 2 — State what it's doing instead**

> "Instead, the bread tears, jelly runs out the sides, and one half slides off."

---

**Step 3 — Walk the gap**

Peanut butter goes on first — it's thick, it anchors. Then jelly on the other slice. The two faces press together and the bread holds everything.

Why does it slide? ...I spread the jelly *on top of the peanut butter*. Both slippery layers are on the same side. No friction surface on the other bread face.

Why does the bread tear? ...I'm spreading cold, stiff peanut butter with too much force.

The explanation just broke down at *"cold peanut butter."*

---

**Step 4 — Name the gap**

> "I don't know why I'm not letting the peanut butter reach room temperature before spreading."

---

**Step 5 — Fix the gap**

Wait 10 minutes. Then spread each ingredient on its *own* slice.

---

## flow-line
**Trigger:** batch processing

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

---

## gedankenexperiment
**Trigger:** two trusted principles contradict

**Principle 1:** Spread to the edges — every bite should have full coverage.
**Principle 2:** The sandwich must hold together when lifted.

---

**The collision scenario:** You spread peanut butter to every edge of slice A. You spread jelly to every edge of slice B. You press them together.

**Following both predictions:**

- Principle 1 fulfilled: full coverage, no dry bites.
- Principle 2 result: jelly migrates outward under pressure. The edges become wet. Bread integrity at the perimeter fails. The sandwich sags when lifted. Jelly drips on your shirt.

Both principles were followed. The sandwich is a structural failure.

---

**Hidden assumption exposed:** "Spread to the edges" implicitly assumes only *one* wet layer. The rule was developed for a single condiment on bread. It smuggles in the assumption that the other slice is dry — providing structural grip at the perimeter.

---

**What survives:**

Peanut butter goes edge-to-edge (it's viscous, it holds). Jelly stops 1cm short of the edges (it's fluid, it migrates). The peanut butter forms a perimeter seal. Full interior coverage. Structural integrity preserved.

Both principles survive once the hidden assumption — *that coverage rules apply symmetrically to both layers* — is removed.

---

## imperial-self-correction
**Trigger:** emotional reaction driving a decision

# Imperial Self-Correction: Making a PB&J

---

**Setup:** You open the fridge. The jelly lid is crusted shut — someone left it gross. Your roommate. *Again.*

---

## Step 1: Catch the Impression

The raw feeling: **irritation, mild indignation.**
The impulse: *Make the sandwich sloppily, leave a mess, passive-aggressively "forget" to put the jelly back.*

---

## Step 2: Strip to Controllables

| Outside control | Inside control |
|---|---|
| Roommate's behavior | How you spread the PB |
| The crusty lid | Whether you clean the knife |
| Past jar crimes | How you leave the kitchen |

Discard column one.

---

## Step 3: Reframe from Above

*"A person encountered a jar with residue on the lid. They wanted a sandwich."*

That's it. Nothing else actually happened.

---

## Step 4: Write the Correction

- **Impulse:** Make a resentful, half-assed sandwich and leave the counter sticky.
- **Correction:** Run the lid under warm water, make a clean sandwich, wipe down the counter.

*Which path?*

---

## Step 5: Act on the Correction

Spread peanut butter evenly. Add jelly. Press bread. Cut diagonally. Done.

The sandwich is better. So is your afternoon.

---

## inflection-point
**Trigger:** strategic shift

## Inflection Point: PB&J Sandwich Construction

**The situation:** You're halfway through the classic approach — bread, peanut butter, jelly, press together — when you notice the bread is stale.

---

**1. Detect the 10x force.**
This isn't "slightly dry bread." The bread is structurally compromised — it will crack under the peanut butter knife and turn to cardboard on contact. That's not a technique problem. The substrate itself has failed.

**2. Apply the "new CEO" test.**
Someone with no attachment to this sandwich would immediately say: "Use a tortilla." You, however, are already mid-spread. That's sunk-cost bias talking.

**3. Assess timing.**
You don't need to finish the sandwich to know. The first knife drag confirms it. 60% confidence threshold: crossed. Waiting for the sandwich to be inedible before deciding is deciding too late.

**4. Force the commitment question.**
Pivot to tortilla wrap — **completely.** Do not attempt to toast the stale bread as a fallback "just in case." That splits your effort and produces two mediocre outcomes instead of one good one.

**5. Execute.**
Grab the tortilla. Spread peanut butter edge-to-edge. Add jelly. Roll. Done.

The old bread goes in the trash. No hedging.

---

## lion-and-fox
**Trigger:** political decision

## Lion and Fox: Constructing a PB&J

**1. Map the actual forces.**

- The bread wants to stay dry. Jelly will destroy it given time.
- The peanut butter has power — it creates a moisture barrier. Use it.
- The eater wants clean hands and structural integrity to the last bite.
- Time is an adversary: the sandwich degrades the moment it's assembled.

**2. Identify the appearance-necessity gap.**

The "correct" assembly (PB one side, J the other, press together) *looks* symmetric and fair to both ingredients. But it produces a soggy failure. The situation demands strategic inequality.

**3. Action + narrative as parallel workstreams.**

- **Action:** Apply peanut butter thick on *both* bread slices first. This creates a fat barrier on each face. Then add jelly to only one coated side. Press together.
- **Narrative:** "I put PB on both sides for extra flavor" — stakeholders (eaters) accept this framing. They don't need to know it's structural.

**4. Flag instrument retirement.**

The double-PB layer is a protective hack, not an aesthetic ideal. On a fresh sandwich eaten immediately, drop it — single-side PB is fine.

**What this pattern reveals:** The "naive" method optimizes for appearance of fairness. The Lion and Fox method optimizes for outcome, then names it palatably.

---

## material-honesty
**Trigger:** design review

## Material Honesty → PB&J

**1. NAME THE MATERIAL**
You are working with bread (a carrier), peanut butter (a dense paste), jelly (a wet gel), and a knife. These are the actual materials. Your hands are the interface.

**2. ASK WHAT IT WANTS TO BE**
Bread wants to be held and bitten. PB wants to be spread directly from jar to surface. Jelly wants to adhere to something that can hold it. The sandwich wants to be picked up and eaten.

**3. STRIP EVERY INTERMEDIARY LAYER**
- No plate required during construction — the counter is a surface
- No separate spreading tools per ingredient — one knife, wiped between uses
- No pre-mixing PB and jelly in a bowl — that's hiding the layering the medium naturally produces

**4. TEST FOR DISHONESTY**
- Toasting: bread pretending to be a grilled sandwich. Dishonest. Remove.
- Cutting diagonally: bread pretending to be a restaurant item. Decorative. Remove.
- Removing crusts: hiding the material's edge. Dishonest. Remove.

**5. VERIFY BY TOUCH**
Pick it up. Two slices, pressed together, held in one hand. If it feels like a snack, it's honest. If it needs a fork, you added layers.

**Result:** Jar → knife → bread. Both slices. Press. Done.

---

## methodical-doubt
**Trigger:** inherited assumptions

## Methodical Doubt: PB&J

**Step 1: Suspend — Surface the assumptions**
- Bread goes on the outside
- You need two slices
- PB on one side, jelly on the other
- They get pressed together
- "Sandwich" means enclosed filling

**Step 2: Doubt — Find where each breaks**
- *Two slices?* A single folded slice works. **Unverified.**
- *Bread on the outside?* Open-faced PB&J exists. **Unverified.**
- *PB and jelly on separate sides?* Both could go on one side. **Unverified.**
- *Pressed together?* Could serve open-faced. **Unverified.**
- *Needs to be bread?* Convention, not necessity. **Unverified.**

**Step 3: Find the Floor — What survives?**
- You need a carrier for peanut butter and jelly
- PB and jelly must contact each other to combine flavors
- The carrier must be edible

**Step 4: Rebuild from foundations**
1. Choose an edible carrier (bread is valid, not required)
2. Apply peanut butter to one surface
3. Apply jelly so it contacts the peanut butter
4. Deliver to mouth

Result: a folded single-slice PB&J is equally valid. The two-slice assumption was inherited, not necessary.

---

## mind-forge
**Trigger:** complex system design

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

---

## musk-filter ✦
**Trigger:** build request

## Musk Filter: PB&J Sandwich

### Step 1 — QUESTION IT

**Who needs this?** Me. I'm hungry right now.
**What breaks without it?** I don't eat.

Passes. Proceed.

---

### Step 2 — DELETE IT

Original scope I might have proposed:
- Toast the bread ❌ — nothing breaks without it
- Cut diagonally for presentation ❌ — I'm eating alone
- Use a plate ❌ — paper towel works
- Spread butter first for moisture barrier ❌ — unnecessary complexity
- Measure portions ❌ — eyeball it

**Deleted 5 of 8 steps. 62% cut.**

Surviving: bread, peanut butter, jelly, knife.

---

### Step 3 — SIMPLIFY

One technique, no variants: spread PB on one slice, jelly on the other, press together. Done. No sequencing debate.

---

### Step 4 — ACCELERATE

Minimum path: grab bread → PB knife stroke → jelly knife stroke → close. 45 seconds. Nothing deferred that blocks eating.

---

### Step 5 — AUTOMATE

No. I make one sandwich maybe twice a week. Automation cost exceeds lifetime value by orders of magnitude.

---

**Approved scope:** Two bread slices. PB. Jelly. One knife. Press. Eat.

---

## ohno-circle
**Trigger:** premature solution

## Ohno Circle: PB&J Sandwich

**Stop. Don't start spreading yet.**

---

**Step 1 — Go to the source.**
Open the fridge. Open the cabinet. Look at what's actually there — don't assume you have bread, PB, or jelly.

**Step 2 — State your preconceptions.**
"I expect: two bread slices, Skippy creamy, grape Welch's."

**Step 3 — Observe.**
- Bread: end pieces only. Heels.
- Peanut butter: bottom-of-jar, mostly oil separated on top.
- "Jelly": it's actually jam. Strawberry, not grape.

**Step 4 — Ask why five times (the PB is wrong).**
Why is it oily? → Separated. Why? → Natural PB, no stabilizers. Why does this matter? → If you don't stir it, you'll spread pure oil onto bread. Why didn't you stir it? → You assumed it was fine. Why? → You didn't look.

**Step 5 — Fix based on observation.**
Stir the PB. Use the heels (they're what's there). Spread jam, not jelly.

**Step 6 — Verify.**
Taste it. Actually taste it — don't assume it worked.

---

*The sandwich you make from observation is always better than the one you assumed into existence.*

---

## pain-blindness
**Trigger:** nobody likes this but everyone uses it

## Pain Blindness Applied: PB&J Construction

**1. Name the normalized pain.**

You're describing six handoffs: get bread, open PB jar, spread PB, close jar, open jelly jar, spread jelly, close jar, combine slices. Nobody questions this. "That's just how you make a sandwich." The pain is in the jar-switching, not the spreading.

**2. Map the seams.**

- Seam 1: Between PB jar and jelly jar — two separate containers requiring two separate utensils or a utensil wash
- Seam 2: Between spreading and combining — you hold two open-faced slices simultaneously with nowhere clean to set them
- Seam 3: Between making and eating — cutting requires a third tool

**3. Check readiness.**

PB/jelly combo products exist (Goober Grape). Single-serve squeeze tubes exist. The components are mature.

**4. Propose the collapsed stack.**

Single squeeze tube, both ingredients pre-mixed. One hand, one motion, directly onto bread. No jars, no knives, no seam between PB and jelly application.

**5. Flag the escape hatch.**

"But I like controlling the ratio" — this escape hatch will keep you in the fragmented workflow forever. That's a preference disguised as a requirement.

The sandwich was never the problem. The jars were.

---

## phantom-machine
**Trigger:** impossible problem

## Phantom Machine: PB&J Constructor

**Premise:** "Making a sandwich requires human judgment — you can't automate it."

---

**1. Construct the machine.**

Inputs: bread loaf, PB jar, jelly jar, knife, plate.
Operations:
```
extract_slice(loaf) → slice_A
extract_slice(loaf) → slice_B
spread(knife, PB_jar, slice_A, coverage=80%)
spread(knife, jelly_jar, slice_B, coverage=80%)
join(slice_A, slice_B, orientation=spread_faces_inward)
output(plate)
```

**2. Run it on paper.**

Trace it: extracts two slices ✓, spreads PB ✓, spreads jelly ✓, joins them ✓. Sandwich produced.

Gets stuck at: crust removal preference, PB/jelly ratio, bread slice thickness, cross-contamination of spreads.

**3. Interrogate the limits.**

- Crust preference → **engineering gap**: add `user_prefs` input parameter
- Ratio calibration → **engineering gap**: adjustable `coverage` param + feedback loop
- Bread thickness → **engineering gap**: slice sensor or pre-sliced bread assumption
- "Made with love" → **fundamental limit**: information-theoretic. No machine produces this.

**4. Build or bound.**

Build the machine — it handles 95% of the task mechanically. Bound the remainder: "made with love" is not a sandwich property. Redefine it out of scope.

**Result:** Sandwich is automatable. The "human judgment" claim was vague, not fundamental.

---

## premeditatio
**Trigger:** high-stakes uncertainty ahead

## Premeditatio: Making a PB&J Sandwich

**Step 1 — Name the worst case in full detail.**

The bread tears when you spread cold peanut butter. You're left with a mangled slice, peanut butter clumped in the middle, and a sandwich that falls apart before it reaches the plate.

**Step 2 — Inhabit it.**

You're holding two ragged bread halves. Peanut butter on your fingers. The jelly is now also smeared on the counter. You're annoyed. Lunch is delayed. That's it. That's the whole catastrophe.

**Step 3 — Inventory surviving resources.**

You still have: the rest of the loaf, both jars, a knife, 5 minutes, and functioning hands. Nothing of consequence has been lost.

**Step 4 — Build the contingency.**

If the bread tears: use the torn slice as the bottom (hidden), let peanut butter sit at room temperature 10 minutes before spreading, apply in short strokes from center outward. Sandwich made.

**Step 5 — Release the decision.**

The worst case is a slightly ugly sandwich. You now have a plan for it. Make the sandwich.

---

*What Premeditatio does: it forces you to discover the worst case is survivable — before fear distorts its size.*

---

## scratch-build
**Trigger:** facing a complex system you need to master

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

---

## shape-the-ground
**Trigger:** facing a confrontation

## Shape the Ground: PB&J Sandwich

**1. Map the full terrain.**

Actors: you, the bread, the spreads, the knife, the plate. Constraints: bread freshness, spread viscosity, knife cleanliness. Information asymmetry: is the jelly runny or firm? Is the peanut butter stiff from cold?

**2. Identify the three decisive conditions.**

What three things, if true at the moment of assembly, make a perfect sandwich inevitable?
- Bread is soft and at room temperature
- Peanut butter is spreadable (not fridge-cold)
- Knife is clean and dry

**3. Shape before engaging.**

- Pull bread from bag, let it sit 2 minutes if cold
- Microwave peanut butter jar lid-off for 10 seconds if stiff
- Wipe knife dry

**4. Test for predetermined outcome.**

*If you spread now, is the result already certain?* Bread tears if cold, PB drags if stiff. Not yet. Shape more.

**5. Engage only at the tipping point.**

All conditions met. Now spread PB first (structural layer), then jelly (wet layer won't soak through). Press. Cut diagonal. Done.

**The sandwich never felt like work — it was already made before the knife touched bread.**

---

## strip-to-structure
**Trigger:** stuck in domain complexity

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

---

## structural-unlock
**Trigger:** structural bottleneck

## Structural Unlock: PB&J Sandwich

**1. Name the exponential.**
The 10x opportunity: feed myself in under 60 seconds. The curve is real — I've been spending 8 minutes on lunch prep. The constraint isn't my spreading technique.

**2. Find the structural bottleneck.**
If I had unlimited skill and unlimited time, what would *still* prevent a fast sandwich?

The jar lids. Two separate containers require two open-close operations and two knives to avoid cross-contamination. That's the governance overhead — not execution speed.

**3. Design the minimum institutional change.**
Don't redesign the kitchen. One change: buy pre-mixed PB&J spread (single jar, single knife). Removes the bottleneck without touching anything else.

**4. Identify the blocking constituency.**
The person with veto power: my past self who bulk-bought separate jars. The concession: finish current stock, then switch. Buy-in secured.

**5. Plan immediate exploitation.**
First 30 days: use the freed 90 seconds per sandwich to prep a second sandwich. Volume doubles through the newly opened channel.

---

**The pattern caught this:** I was treating a *structural* problem (two-container governance) as a *skill* problem (spread faster). More effort within the old structure wouldn't have helped.

---

## taste-gate
**Trigger:** feature list growing

## Taste Gate: PB&J Sandwich

**Step 1 — Define the Experience**

> "A sandwich that feels like childhood comfort in two bites."

---

**Step 2 — Kill Everything That Doesn't Serve That Sentence**

Options on the table:
- Toasted bread → **CUT.** Toast is sophisticated. Childhood is soft white bread.
- Crunchy peanut butter → **CUT.** Texture interrupts the soft, nostalgic feel.
- Artisan jam with fruit chunks → **CUT.** Chunks are effort. Smooth grape jelly is Proust's madeleine.
- Crusts on → **CUT.** No child ever felt comfort from crusts.
- Cut diagonally vs. straight → diagonal **stays** — triangles feel like something someone made *for* you.

---

**Step 3 — Interrogate What Remains**

- Creamy peanut butter: acceptable, or best? Best — it's what the sentence demands.
- Grape jelly: is there a better version? Strawberry is acceptable. Grape *is* the feeling.
- Soft white bread: Wonder Bread or generic? Wonder Bread. The brand *is* the memory.

---

**Step 4 — Say It Back**

> Soft white bread, creamy peanut butter, grape jelly, no crusts, cut in triangles.

That's it. Anything else is a designer who was afraid to commit.

---

## the-ratchet ✦
**Trigger:** inner loop velocity decreasing

## The Ratchet: PB&J Sandwich System

**Scenario:** You've made 200 sandwiches. The process has grown. It now takes 12 minutes.

---

### Step 1 — Diagnose the Signal

- New sandwiches take longer than the first ones despite "more experience" ✓
- Every sandwich hits constraints before you start ✓
- The improvement system is now the friction ✓

**3/5 signals. The accumulation is the problem.**

---

### Step 2 — Inventory the System

Knife sanitization log, bread freshness checklist, PB-to-JB ratio spreadsheet, crust removal protocol, diagonal vs. square cut decision tree, allergen disclosure form, plating standards doc, 3-minute cooling period.

---

### Step 3 — Musk Filter

| Item | Bucket |
|---|---|
| Knife sanitization | **BONE** — prevents cross-contamination |
| Bread freshness check | **BONE** — bad bread ruins sandwich |
| PB:J ratio spreadsheet | **SCAFFOLDING** — solved a "too much jelly" complaint that hasn't recurred |
| Crust removal protocol | **SCAFFOLDING** — one recipient, long gone |
| Diagonal vs. square decision tree | **SCAFFOLDING** — nobody asked |
| 3-minute cooling period | **SCAFFOLDING** — PB&J doesn't need cooling |

---

### Step 4 — Reset

Archive the scaffolding. Keep the bones.

**New process:** Check bread. Clean knife. Spread. Cut. Done. **3 minutes.**

---

## time-and-motion
**Trigger:** optimize process

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

---

## two-way-door
**Trigger:** decision paralysis

## Two-Way Door: PB&J Construction

**Decision 1: Which bread?**
Two-way door. If you grab white bread and hate it, you eat one sandwich and buy different bread next time. Zero consequence.
→ **Just pick what's in front of you. Don't deliberate.**

**Decision 2: Crunchy vs. smooth peanut butter?**
Two-way door. You'll know after one bite whether you like it.
→ **Grab whichever is open. Evaluate after eating.**

**Decision 3: How much jelly?**
Two-way door. Too little? Add more. Too much? Blot it. The sandwich isn't ruined.
→ **Start with a normal amount. Adjust next time.**

**Decision 4: Cut diagonally or straight?**
Two-way door — unless you're serving it to someone who will judge you forever.
→ **Just cut it. Any direction. Move on.**

---

**Actual one-way door in this task:**

Spreading PB on the *outside* of the bread before realizing your mistake. Now both slices are contaminated and you're committed.

→ Slow down for 2 seconds: confirm bread orientation before spreading.

---

**Result:** Four micro-decisions that felt like choices took zero mental energy. One genuine risk identified and avoided.

---

## vertical-integration
**Trigger:** supply chain dependency

## PB&J via Vertical Integration

**1. Map the chain:**
- Wheat farm → flour mill → bread bakery → grocery store → your kitchen
- Peanut farm → roaster → grinder → jar → store → kitchen
- Fruit farm → sugar processor → jelly maker → jar → store → kitchen
- Your labor: assemble and eat

**2. Identify the bleeding link:**
Store-bought bread. Highest markup, fastest to go stale, controls texture and thickness you can't adjust.

**3. Acquire that link:**
Bake your own bread. You control crust, density, slice thickness. Margin recaptured: ~70% cost reduction per loaf.

**4. Drive cost out ruthlessly:**
Time the bake. Measure flour-to-water ratio. Standardize the process so every loaf is identical.

**5. Reinvest savings into the next weakest link:**
Now jelly is the bottleneck — commercial jelly is mostly corn syrup. Make jam from bulk frozen fruit. Cost drops 60%.

**6. Stop:**
Grinding your own peanuts saves $0.40/jar but adds 20 minutes of cleanup. Management overhead exceeds margin recaptured. Buy Jif.

**Result:** You own bread and jam. You buy peanut butter. The sandwich costs less, tastes better, and you control every variable that matters.

---

_✦ = authored gem (written from live practice, not research)_

_Generated by `scripts/generate-pbnj.sh` · Refresh: `bash tests/pbnj-test.sh <pattern>`_
