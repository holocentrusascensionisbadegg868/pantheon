---
name: musk-filter
description: Invoke before any build, create, automate, or extend request — including feature proposals, new tools, new workflows, new rules, new agents, or any "let's add X" statement. Run the 5-step Musk Filter in order: (1) Question — who needs this and what breaks without it? (2) Delete — remove at least 30% of scope. (3) Simplify — only after 1 and 2. (4) Accelerate — only after 1-3. (5) Automate — only after 1-4. Block any jump to Step 5 without completing the prior steps.
---

# Musk Filter — Pre-Build Gate

A build/create/automate request has been detected. Running the Musk Filter before any plan or code is written.

## Step 1 — QUESTION IT

Before anything else, answer these two questions:

1. **Who specifically requires this?** (Name or role — not "users" or "the team")
2. **What breaks if this doesn't exist?**

If you cannot answer both questions clearly and specifically: **kill it**. Do not proceed to Step 2. Report back with the finding.

---

## Step 2 — DELETE IT

Look at the proposed scope. What can be removed entirely?

- Target: **delete at least 30%** of what was originally proposed
- Apply to: steps, rules, files, agents, integrations, acceptance criteria, requirements
- Ask for each element: "What breaks if we remove this?" If the answer is "nothing" or "maybe someday" — delete it
- If you haven't deleted anything, you didn't look hard enough

Do not proceed to Step 3 until something has been deleted.

---

## Step 3 — SIMPLIFY

With the surviving scope (after Step 2), simplify what remains:
- Tighten language, reduce dependencies, remove optionality
- One way to do it, not three
- Never optimize something that should have been deleted in Step 2

Do not proceed to Step 4 until the scope is lean.

---

## Step 4 — ACCELERATE

Find the fastest path through the simplified scope:
- What's the minimum to make this real?
- What can be deferred without blocking the core?
- Speed up the lean version — not the original bloated one

Do not proceed to Step 5 until the fast path is identified.

---

## Step 5 — AUTOMATE

Only now: consider automation.
- Automate only what has been proven lean and correct by Steps 1-4
- Automation of a broken process = faster broken process
- If uncertain whether it's lean enough: don't automate yet

---

## Output

After running the filter, report:
1. What survived Steps 1-2 (what's left)
2. What was deleted and why
3. The simplified, accelerated scope for approval
4. Whether automation is appropriate now or should wait

Do not write code or create files until the filtered scope is approved.

---

*Pattern source: patterns/musk-filter/pattern.md*
*Canonical schema: SCHEMA.md*
