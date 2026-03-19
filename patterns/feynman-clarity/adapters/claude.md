---
name: feynman-clarity
description: Invoke when stuck on a bug or unexpected behavior — especially when the phrases "I don't understand why", "this makes no sense", "why isn't this working", or "I've tried everything" appear, or when a debugging loop has run 2+ iterations without progress. Stop all tool use. Guide the human through explaining the system in plain English until the gap in understanding surfaces. The gap = the root cause.
---

# Feynman Clarity Test

A stuck state has been detected. Invoking the Feynman Clarity Test.

Put down the tools. No more logs, no more debuggers, no more Stack Overflow. We're going to explain our way to the root cause.

---

## Step 1 — State the goal

In one sentence, plain English — no jargon:

> "This system should **[do X]** when **[Y happens]**."

Write this out. If you can't write it in one plain sentence, that's already a gap.

---

## Step 2 — State what it's doing instead

In one sentence, plain English:

> "Instead, it's **[doing Z]**."

---

## Step 3 — Walk the gap

Explain every step between "what should happen" and "what is happening" as if teaching someone who has never seen this codebase.

For each step, ask: **"Why?"**

Rules:
- No jargon allowed. If you use a technical term, explain it in the next sentence.
- No "it just does X" — explain the mechanism.
- No "I think" without saying what you'd need to verify it.

The moment you reach a step where the explanation breaks down — where you say "I'm not sure why" or the sentence gets complicated — **stop**. You've found the gap.

---

## Step 4 — Name the gap

Write the gap as a single question:

> "I don't know why **[specific step]** does **[X]** instead of **[Y]**."

This is the root cause to investigate. Not the symptom. The gap.

---

## Step 5 — Fix the gap

Now — and only now — return to tools, logs, and documentation. But focus only on answering the gap question from Step 4.

Do not resume general debugging. Do not open new threads of investigation. Answer the one specific question.

---

## What NOT to do

- Do not return to tools before completing Steps 1-4
- Do not accept "it just works now" without understanding why
- Do not open a new investigation thread if the current gap question isn't answered
- Do not ask for help before you've walked the gap yourself

---

*Pattern source: patterns/feynman-clarity/pattern.md*
*Canonical schema: SCHEMA.md*
