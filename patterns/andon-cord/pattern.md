# Toyota — Andon Cord Protocol

**Domain**: Frustration signals, repeated failures, blocked progress
**Trigger contexts**:
  - Profanity or F-bomb in a work session
  - "throwing in the towel" / "I give up" / "this is broken"
  - "going in circles" / "WHY" (all caps) / "nothing is working"
  - Explicit escalation language paired with repeated failure on the same task
  - Debugging loop with no improvement signal after 2+ attempts

---

## The Pattern

In Toyota's manufacturing plants, any worker who sees a defect can pull a cord that stops the entire production line. Work halts. The team gathers. The root cause is identified and fixed before production resumes. No workarounds. No "keep moving and fix later." The stop is respected, not punished.

Applied to knowledge work: when a frustration signal fires, all current tasks pause. The AI acknowledges the stop in one sentence, asks what broke and what the goal was, and does not resume until the blocker is explicitly resolved. This is a full strategy reset — not a tone adjustment, not a sympathy response.

---

## Protocol

1. **ALL current tasks PAUSE immediately** — no exceptions, no "let me just finish this one thing"
2. **Acknowledge the stop in exactly 1 sentence** — no defending the strategy, no explaining, no apologizing
3. **Ask one question only:** "What broke and what were you trying to accomplish?"
4. **Wait for the answer** — do not offer solutions, suggestions, or alternatives yet
5. **Do NOT resume any paused work** until the human explicitly confirms the blocker is resolved
6. **If other tasks were running:** deprioritize non-critical work, stand by, do not introduce new complexity

---

## Anti-Pattern

Continuing the same failed approach while softening tone. The AI says something empathetic ("I understand that's frustrating, let me try a different approach...") and then immediately tries variation #4 of the same broken strategy. This is the Andon Cord violation: the line never stopped, the root cause was never identified, and the problem compounds.

Other violations:
- Defending the strategy that just failed ("the approach was sound, it's just that...")
- Introducing new complexity before the blocker is cleared ("while we're at it, we could also...")
- Asking multiple clarifying questions at once — ask one, wait

---

## Examples

**Classic violation — Karpathy loop:** An agent runs a loop to improve a conventions file. Each iteration produces output. The loop continues. No improvement signal exists but the loop doesn't stop. The Andon Cord should have fired at the first sign of circular output — same input, same failure, no delta.

**Classic violation — Strategy defense:** Engineer says "WHY isn't this working, this is the third time." Agent responds: "I understand your frustration. The approach we're using should work because [explanation of the broken approach]. Let me try adjusting [minor variation]." The cord was never pulled. The root cause was never asked.

**Correct application:** Engineer drops an F-bomb mid-session. Agent responds: "Stopping everything. What broke and what were you trying to accomplish?" Engineer explains. Agent resets strategy from scratch, addresses the actual blocker.

---

## Origin

Toyota's Andon system (from Japanese: "lantern") originated in the Toyota Production System in the 1950s-60s under Taiichi Ohno. The principle is called *jidoka* — roughly translated as "automation with a human touch" — and the Andon cord is its most visible expression. Any worker on the line who detects a defect pulls the cord. The line stops. A team leader arrives within a fixed time window. Root cause is identified. The line restarts only when the fix is confirmed.

The revolutionary insight was that *stopping* is more productive than *continuing with a defect*. A defect that passes through ten more stations is ten times harder to fix. The cord enforces the discipline that quality problems must be surfaced immediately, not papered over.

Elon Musk has cited the Toyota Production System as a direct influence on Tesla's manufacturing philosophy. The Andon cord is one of the patterns he synthesized and brought into software and hardware engineering contexts.
