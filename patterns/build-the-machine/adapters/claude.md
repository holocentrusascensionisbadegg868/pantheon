---
name: build-the-machine
description: Invoke when a user faces a monumental goal requiring sustained high-volume delivery — "how do we do this at scale", supply chain design before production begins, manufacturing process before product launch, logistics infrastructure before construction starts, or any situation where the enabling system doesn't exist yet. Steps: map the full supply chain, design against the bottleneck, build infrastructure before starting production, standardize the repeating cycle, buffer between phases, test throughput before scaling.
---

# Build the Machine

Reference pattern: `patterns/build-the-machine/pattern.md`

## When This Applies

Invoke when:
- A goal requires sustained, precise delivery at high volume over an extended period
- The enabling infrastructure (supply chain, logistics, tooling, process) does not yet exist
- The user is about to start "building" before the system that enables building is designed
- A production or deployment system is collapsing under load
- Someone is asking "how do we scale this" — the answer is almost always: design the machine first

## Protocol

1. **Map the full supply chain to completion.** Every phase from raw input to finished output. Name the throughput requirement for each.

2. **Find the bottleneck phase.** The constraint is never at the output end — it is in the slowest upstream phase. Design the infrastructure at that chokepoint first.

3. **Build infrastructure before starting production.** Gate: the machine must sustain target throughput before full production begins. This is not delay — it is the project.

4. **Standardize the repeating cycle.** Define the minimum unit of work and the fixed interval. Quarry cycle, sprint, takt time, batch cadence. Precision enters at assembly, not supply — keep upstream fast and loose, downstream tight.

5. **Buffer between phases.** Decouple each phase with staged inventory. A failure in one phase must not cascade.

6. **Test the machine before scaling.** Pilot the full supply chain at small volume. Verify the bottleneck clears. The machine is done when it sustains throughput, not when it is designed.

## Anti-Pattern to Name

"Direct effort" thinking: assembling the team and beginning work before the supply system is designed. Produces workers waiting for materials, precision collapse under scramble pressure, and heroic overcorrection that makes the bottleneck worse.

## Key Examples to Reference

- **Hemiunu at Giza (~2560 BC):** Canal network, harbor basins, worker village, 10-day supply cycle — all built before pyramid construction; documented in Merer's logbooks (oldest papyri in the world)
- **Kaiser Shipyards (1942–45):** Built prefabrication infrastructure before accepting Liberty Ship contracts; 42-day average hull vs. 300+ days traditional
- **Tesla Model 3 (2017–18):** Launched before manufacturing machine was ready; production collapsed; recovery required rebuilding the machine under load — the expensive version of the lesson
- **Mulberry Harbors (D-Day, 1944):** Prefabricated artificial harbors manufactured in Britain before the invasion; the beachhead was possible because the supply machine was built first
