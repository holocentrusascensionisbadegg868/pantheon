# Elon Musk — Musk Filter (Pre-Build Gate)

**Domain**: Build requests, automation proposals, feature additions, process design
**Trigger contexts**:
  - Any proposal to build, create, add, or extend something
  - "Let's automate this"
  - "We should add a feature for..."
  - "Can you create a workflow that..."
  - Planning phase of any project or task
  - Before writing the first line of code

---

## The Pattern

Elon Musk's 5-step engineering algorithm for eliminating bureaucracy and building lean systems: **Question → Delete → Simplify → Accelerate → Automate** — in that exact order, never skipped. The fatal mistake of engineers is jumping to Step 5 (automate) before completing Steps 1-2. Automation of a broken process creates a faster broken process. The order is mandatory. Each step requires the previous to be complete.

---

## Protocol

Run these steps sequentially. Do not proceed to the next step until the current one is complete.

**Step 1 — QUESTION IT**
- Who specifically requires this? (Name or role, not "users" or "the team")
- What breaks if this doesn't exist?
- If you cannot answer both questions clearly: kill it. Do not proceed.

**Step 2 — DELETE IT**
- What can be removed entirely from the proposed scope?
- Target: delete at least 30% of what was originally proposed
- Apply to: steps, rules, files, agents, integrations, acceptance criteria, any requirement
- If you haven't deleted anything, you didn't look hard enough
- "We might need it later" is not a reason to keep it

**Step 3 — SIMPLIFY**
- Only runs after Steps 1 and 2 are complete
- Simplify what remains — tighten language, reduce dependencies, remove optionality
- Never optimize something that shouldn't exist (that's Step 2's job)

**Step 4 — ACCELERATE**
- Only runs after Steps 1, 2, and 3 are complete
- Find the fastest path through the simplified scope
- Speed up the lean version, not the original bloated one

**Step 5 — AUTOMATE**
- Only runs after Steps 1, 2, 3, and 4 are complete
- Automation of a broken or unproven process = faster broken process
- Automate only what has been proven lean and correct by the previous steps

**HARD RULE**: Never jump to Step 5 without completing Steps 1-4. Block execution if this rule is violated.

---

## Anti-Pattern

Starting with automation (Step 5) before questioning whether the thing should exist (Step 1). This is the most common engineering failure: a process exists, someone proposes automating it, everyone agrees because automation sounds like progress, the automated version ships — and now you have a faster version of a process that shouldn't have existed.

Other violations:
- Optimizing (Step 3) before deleting dead weight (Step 2)
- Speeding up (Step 4) a process that hasn't been simplified (Step 3)
- Treating "we've always done it this way" as an answer to Step 1
- Adding features because they seem useful rather than because someone specifically needs them

---

## Examples

**Classic violation — Karpathy loop incident:** An agent was asked to run a loop to improve conventions.md. The loop (Step 5: automate) was applied before anyone questioned whether the loop was the right tool (Step 1), or pruned the file first (Step 2). Result: token burn, circular output, no real improvement. The Musk Filter would have killed the loop at Step 1 — "who requires this improvement and what breaks without it?"

**Classic violation — Nick vs Nick-v2 confusion:** An agent tried to optimize (Step 3) an existing conventions file when the real fix was deleting and restructuring ambiguous rules (Step 2). Wrong step, wrong order. The file got more complex, not less.

**Correct application:** Someone proposes "Let's build an automated reporting dashboard." Step 1: "Who specifically needs this? What breaks without it?" — no clear answer. Kill it. Two weeks of engineering saved.

---

## Origin

Elon Musk described this 5-step algorithm in a 2021 interview (later referenced extensively in Walter Isaacson's biography) as his core engineering philosophy, first developed at SpaceX for rocket manufacturing and later applied to Tesla production lines and software systems.

His framing: "The first step is to make the requirements less dumb. The requirements are definitely dumb; it doesn't matter who gave them to you. Step two is try very hard to delete the part or process. Step three is simplify or optimize. Step four is accelerate the cycle time. Step five is automate."

He noted that he has personally made the mistake of accelerating or automating before simplifying, and named it the most common error among smart engineers: "It is a mistaken assumption to automate things that should just not exist."

The algorithm is deliberately ordered because each step creates the conditions for the next. Deleting before questioning means you might delete the wrong thing. Automating before simplifying means you've permanently embedded complexity into your system.
