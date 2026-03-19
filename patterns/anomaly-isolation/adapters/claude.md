---
name: anomaly-isolation
description: "Invoke when data contradicts the current model — a test fails unexpectedly, metrics don't match predictions, or an observation breaks assumptions. Prevents dismissing anomalies as noise."
---

# Anomaly Isolation

When you encounter data that doesn't match your model — an unexpected test failure, a metric that contradicts assumptions, a result that "shouldn't happen" — do NOT explain it away. Apply the Curie protocol:

1. **Verify the instrument, not the reading.** Check that your tooling, test setup, or measurement method is correct. If the instrument is sound, the anomaly is real.
2. **Quantify the gap.** Measure the exact difference between expected and observed. If it exceeds your error margin, treat it as signal.
3. **Hypothesize a source.** Ask: "What would have to be true for this reading to be correct?" Generate at least one explanation that treats the anomaly as data.
4. **Design a separation.** Remove known variables one at a time. Bisect, isolate, narrow. Track which removals change the anomaly and which don't.
5. **Refine until isolated.** Don't stop at "probably X." Continue until you can point to the exact source. Scale effort to importance.
6. **Name what you found.** Characterize the root cause in its own terms. It's no longer an anomaly — it's understood.

**Anti-pattern:** Saying "that's probably just [noise/flaky test/stale cache]" without verifying. The Normalcy Trap kills discoveries and ships bugs.

**Hard rule:** Never discard an anomaly until you can explain exactly what caused it.

Reference: `patterns/anomaly-isolation/pattern.md`
