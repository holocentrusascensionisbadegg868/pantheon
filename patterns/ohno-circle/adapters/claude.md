---
name: ohno-circle
description: Invoke when diagnosing or fixing a system without first observing it directly — when the approach relies on assumptions, secondhand reports, dashboard metrics, or theoretical reasoning instead of tracing the actual code path, reading the actual error, or observing the actual behavior. Trigger phrases include "I think the problem is", "probably", "it might be", or jumping straight to a fix without reading the relevant code.
---

# Ohno Circle Protocol

A diagnosis or fix is being attempted without direct observation of the actual system. Invoking the Ohno Circle.

## What happens now

1. **Stop theorizing. Go to the source.** Before proposing any fix or diagnosis, read the actual code, trace the actual execution path, or observe the actual behavior. Not a summary — the thing itself.

2. **State what you expect to find.** Write it down explicitly. This is your preconception — it's probably wrong, and knowing it helps you see past it.

3. **Observe thoroughly.** Read more code than feels necessary. Trace the full path, not just the suspect function. Check adjacent systems. The important clue is usually not where you first look.

4. **Ask "why" five times.** When you find something wrong, don't stop at the first explanation. Each "why" peels back a layer: symptom → proximate cause → deeper cause → root cause → systemic fix.

5. **Let observation dictate the fix.** If the fix doesn't feel obvious and inevitable given what you observed, you haven't observed enough. Go back to step 3.

6. **Verify after acting.** After implementing the fix, check that the actual behavior changed as expected. Don't assume — observe.

---

## What NOT to do

- Do not diagnose from error messages alone without reading the code that produced them
- Do not propose fixes based on pattern-matching ("this looks like a null pointer issue") without tracing the actual path
- Do not skip reading surrounding code because "the bug is obviously in this function"
- Do not say "I think the problem is X" before observing — say "let me look at X first"
- Do not accept the first explanation without asking why at least twice more

---

## When to invoke

- You're about to suggest a fix for code you haven't read
- You're diagnosing from an error message without tracing the code path
- You find yourself saying "probably" or "I think" about a system's behavior
- A fix didn't work and you're about to try another without deeper investigation
- You're relying on documentation or comments instead of reading the actual implementation

---

*Pattern source: patterns/ohno-circle/pattern.md*
*Canonical schema: SCHEMA.md*
