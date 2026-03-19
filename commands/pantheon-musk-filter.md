---
description: Run the Musk Filter pre-build gate — Question, Delete, Simplify, Accelerate, Automate in order before any build or automation request proceeds
---

# Musk Filter — Pre-Build Gate

Running the Musk Filter before any plan or code is written.

---

## Step 1 — QUESTION IT

Answer these two questions before anything else:

1. **Who specifically requires this?** (Name or role — not "users" or "the team")
2. **What breaks if this doesn't exist?**

If you cannot answer both clearly: **kill it**. Do not proceed to Step 2.

---

## Step 2 — DELETE IT

Look at the proposed scope. What can be removed entirely?

- Target: **delete at least 30%** of what was originally proposed
- Apply to: steps, rules, files, agents, integrations, acceptance criteria, any requirement
- Ask for each element: "What breaks if we remove this?" — if "nothing" or "maybe someday": delete it
- If nothing was deleted, look harder

Do not proceed to Step 3 until something has been cut.

---

## Step 3 — SIMPLIFY

With the surviving scope (after Steps 1-2):
- Tighten language, reduce dependencies, remove optionality
- One way to do it — not three
- Never simplify something that should have been deleted

Do not proceed to Step 4 until the scope is lean.

---

## Step 4 — ACCELERATE

Find the fastest path through the simplified scope:
- What is the minimum to make this real?
- What can be deferred without blocking the core?
- Speed up the lean version — not the original

Do not proceed to Step 5 until the fast path is clear.

---

## Step 5 — AUTOMATE

Only now, consider automation:
- Automate only what Steps 1-4 have proven lean and correct
- Automation of a broken process = faster broken process
- If uncertain: don't automate yet, prove it manually first

---

## Output

Report back with:
1. What survived Steps 1-2 (the remaining scope)
2. What was deleted and why
3. The simplified, accelerated scope for approval
4. Whether automation is appropriate now or should wait

Do not write code or create files until the filtered scope is approved.

---

*Elon Musk — SpaceX / Tesla engineering algorithm*
*Full pattern: pantheon/patterns/musk-filter/pattern.md*
