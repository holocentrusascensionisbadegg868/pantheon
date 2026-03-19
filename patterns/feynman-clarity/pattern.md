# Richard Feynman — Feynman Clarity Test

**Domain**: Debugging, stuck states, "I don't understand why this isn't working"
**Trigger contexts**:
  - "I don't understand why..."
  - "This makes no sense"
  - "Why isn't this working?"
  - "I've tried everything"
  - Debugging loop with no progress after 2+ attempts
  - Logs and tools are consulted but the problem doesn't resolve
  - Explanation of the bug becomes increasingly complex

---

## The Pattern

Richard Feynman's teaching method: if you cannot explain something simply, you don't understand it yet. The corollary for debugging: if you cannot explain *each step* of why something fails in plain language — no jargon, no hand-waving, no "and then it just doesn't work" — you have not yet identified the root cause. You've identified a symptom.

The technique is to stop all tools and logs and explain the system aloud as if teaching a 12-year-old. The moment you cannot explain a step simply is the moment you've found the gap. Fix that gap, not the symptom.

---

## Protocol

1. **Stop** — close all debuggers, logs, and tool output. No more data until step 5.
2. **State the goal** — in one sentence, plain English: "This system should [do X] when [Y happens]."
3. **State what it's doing** — in one sentence, plain English: "Instead, it's [doing Z]."
4. **Walk the gap** — explain every step between the goal and the actual behavior as if teaching a 12-year-old. For each step, ask: "Why?" If the answer is "I don't know" or requires jargon, stop — you've found the gap.
5. **The step you can't explain simply = the root cause.** Investigate that specific step now.
6. **Fix the root cause**, not the symptom you've been chasing.

---

## Anti-Pattern

Adding complexity to the investigation while the root cause remains unexplained. More logs. More print statements. More tools. More variations of the same failing approach. The investigation grows larger but understanding doesn't grow deeper. This is the Feynman violation: the assumption that *more data* will produce understanding without *clearer thinking* first.

Other violations:
- "It must be a [framework/library/environment] bug" — before being able to explain exactly why
- Asking for someone else to look at it before completing steps 2-4 yourself
- Accepting "it just works now" after a random change — without understanding why
- Jumping to solutions before the diagnosis is complete

---

## Examples

**Correct application — Null pointer hunt:** An engineer spends an hour on a null pointer exception. Tools show where it crashes. Step 1: stop tools. Step 2: "The user object should be populated after login." Step 3: "It's null when the profile page loads." Step 4: walking the gap — "Login sets the user... session stores it... profile page retrieves it from session... wait, I can't explain why the session variable is accessible at login but not at profile load. That's the gap." Root cause found: session scope mismatch. The logs had this data the whole time but the explanation surfaced the gap in 2 minutes.

**Classic violation — The growing investigation:** Agent is asked why an API call fails. Agent checks logs, adds more logging, tries a different endpoint, checks network tab, searches Stack Overflow, tries a header variation. 45 minutes pass. The investigation has grown but understanding hasn't. Feynman Clarity Test applied: "What should happen?" — "The API should return a user object." "What happens instead?" — "It returns 401." "Walk me through the auth flow in plain English." — "It sends the token... wait, I can't explain which token it sends or where it came from." Gap found immediately.

---

## Origin

Richard Feynman (1918–1988) was a theoretical physicist who won the Nobel Prize in 1965 for his work in quantum electrodynamics. He was equally famous for his ability to explain complex physics to non-physicists — a skill he developed deliberately, not incidentally.

His learning technique, now called the Feynman Technique, has four steps: choose a concept, explain it in plain language as if teaching a child, identify the gaps where the explanation breaks down, and review the source material to fill exactly those gaps. The technique treats the inability to explain simply as *diagnostic information* — not a sign that the concept is too hard, but a precise locator of where understanding is missing.

Feynman applied this to his own research. When stuck on a physics problem, he would return to first principles and rebuild his understanding from scratch, in plain language, until the gap surfaced. He believed that if you couldn't explain something simply, you had borrowed the words without the understanding.

The debugging application is a direct translation: treat a broken system like a physics problem. Explain it from first principles. The gap in your explanation is the bug.
