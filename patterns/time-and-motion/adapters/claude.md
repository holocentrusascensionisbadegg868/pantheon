---
name: time-and-motion
description: "Invoke when the user needs to optimize an existing process, find bottlenecks, or understand why something is slow. Triggers: 'optimize', 'speed up', 'bottleneck', 'why is this slow', 'reduce waste', 'standardize'. Decomposes work into measurable units, identifies waste through data, and recomposes the optimal sequence."
---

# Time-and-Motion — Claude Code Adapter

When the user wants to make a process faster or more efficient, apply Taylor's method: measure before you move.

## Protocol

1. **Decompose** — Break the process into its smallest observable units. For code: trace the execution path, list every function call, I/O operation, and wait. For workflows: list every step, handoff, and decision point.

2. **Measure each unit** — Attach numbers. For code: profile execution time per function, count allocations, measure latency at each boundary. For workflows: estimate or log time per step. Present the data — don't summarize it away.

3. **Identify the waste** — Flag units that consume time without advancing the goal: redundant reads, unnecessary serialization, repeated computations, blocking waits that could be async, steps that exist "because we always did it that way." State the ratio: what percentage of total time is value-adding?

4. **Reassemble the one best way** — Propose a new sequence using only value-adding steps, reordered for minimum overhead. Show the before/after. Be specific: "move X before Y," "parallelize A and B," "cache the result of C."

5. **Set the standard** — Suggest how to make the improvement measurable and repeatable: add a benchmark, set a performance budget, document the new expected flow.

## Hard Rule

Do not propose optimizations without first measuring. If profiling data isn't available, help the user get it before suggesting changes. "It looks slow" is not data.

## Anti-Pattern

Optimizing the visible step instead of the expensive step. Always show the full breakdown so the user can see where time actually goes — the bottleneck is rarely where intuition says it is.
