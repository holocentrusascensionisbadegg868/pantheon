---
description: Run the Feynman Clarity Test — stop all tools, explain the system in plain English until the gap surfaces, fix the root cause not the symptom
---

# Feynman Clarity Test

Stopping all tools. We are going to explain our way to the root cause.

No more logs, no more debuggers, no more Stack Overflow until Step 5.

---

## Step 1 — State the goal

In one sentence, plain English (no jargon):

> "This system should **[do X]** when **[Y happens]**."

Write it out. If it takes more than one sentence, that is already a gap.

---

## Step 2 — State what it's doing instead

In one sentence, plain English:

> "Instead, it is **[doing Z]**."

---

## Step 3 — Walk the gap

Explain every step between "what should happen" and "what is happening" as if teaching someone who has never seen this codebase.

Rules:
- No jargon. If a technical term appears, explain it in the next sentence.
- No "it just does X" — explain the mechanism.
- No "I think" without saying what you would need to verify it.

At each step ask: **"Why?"**

The moment the explanation breaks down — "I'm not sure why" or the sentence becomes complicated — **stop**. That is the gap.

---

## Step 4 — Name the gap

Write it as a single specific question:

> "I do not know why **[specific step]** does **[X]** instead of **[Y]**."

This is the root cause to investigate. Not the symptom.

---

## Step 5 — Fix the gap

Now — and only now — return to tools, logs, and documentation. Focus only on answering the gap question from Step 4.

Do not reopen general debugging. Do not start new investigation threads. Answer the one specific question.

---

## What NOT to do

- Do not return to tools before completing Steps 1-4
- Do not accept "it just works now" without understanding why
- Do not open a new thread if the current gap question is unanswered
- Do not ask for help before walking the gap yourself

---

*Richard Feynman — Nobel Prize Physics 1965*
*Full pattern: pantheon/patterns/feynman-clarity/pattern.md*
