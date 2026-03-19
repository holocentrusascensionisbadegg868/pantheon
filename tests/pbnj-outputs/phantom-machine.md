# PB&J Test — phantom-machine

**Input:** Construct a Peanut Butter and Jelly Sandwich

**Output:**

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
