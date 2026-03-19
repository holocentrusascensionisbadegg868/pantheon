# Pantheon v1.0 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build all v1.0 foundation tooling so Nick can execute the Historian agent loop and produce a 25-30 gem library ready for public launch by May 6, 2026.

**Architecture:** Phase A (this plan) builds the schema, tooling, and historian agent scaffolding. Phase B (Nick executes autonomously) runs the research loop and pruning pass. Phase C (Dana) reviews and launches.

**Tech Stack:** Bash (install.sh, loop.sh, prune.sh, generate-patterns.sh), YAML frontmatter (pattern metadata), Markdown (gem content), Python optional (YAML validation)

**Spec:** `docs/specs/2026-03-18-pantheon-v1-design.md`

---

## File Map

### Files to Create
- `install.sh` — one-command install for Claude Code users
- `scripts/generate-patterns.sh` — regenerates PATTERNS.md from all pattern frontmatter
- `historian/seed-list.md` — 50 curated heroes for Phase 1 research
- `historian/prompt.md` — the research template Nick uses per hero
- `historian/pruning-criteria.md` — the 4 quality criteria for Phase 2
- `historian/loop.sh` — Phase 1 runner
- `historian/prune.sh` — Phase 2 runner (writes pruning-report.md)
- `historian/README.md` — how to run the Historian agent yourself
- `CONTRIBUTING.md` — how to submit a new gem via PR
- `tests/validate-schema.sh` — validates a single pattern.md has required YAML fields
- `tests/validate-patterns.sh` — runs validate-schema.sh against all patterns
- `tests/test-install.sh` — tests install.sh in a temp directory

### Files to Modify
- `patterns/andon-cord/pattern.md` — add YAML frontmatter + The Book sections
- `patterns/musk-filter/pattern.md` — add YAML frontmatter + The Book sections
- `patterns/feynman-clarity/pattern.md` — add YAML frontmatter + The Book sections
- `PATTERNS.md` — regenerate via generate-patterns.sh after upgrades
- `README.md` — add stacking demo, update status to v1.0 in-progress
- `commands/pantheon.md` — update to reference v1.0 launch and install.sh

---

## Phase A: Foundation

### Task 1: Schema Validation — Tests First

Write the validator before touching existing patterns so every change is immediately verifiable.

**Files:**
- Create: `tests/validate-schema.sh`
- Create: `tests/validate-patterns.sh`

- [ ] **Step 1: Write `tests/validate-schema.sh`**

```bash
#!/usr/bin/env bash
# Usage: bash tests/validate-schema.sh patterns/musk-filter/pattern.md
set -euo pipefail

FILE="${1:-}"
[[ -z "$FILE" ]] && { echo "Usage: $0 <pattern.md>"; exit 1; }
[[ -f "$FILE" ]] || { echo "ERROR: file not found: $FILE"; exit 1; }

REQUIRED_FIELDS=(name aliases domain trigger practitioners events lineage origin-earliest origin-modern)
ERRORS=0

if ! grep -q "^---" "$FILE"; then
  echo "FAIL: $FILE — no YAML frontmatter found"
  exit 1
fi

for field in "${REQUIRED_FIELDS[@]}"; do
  if ! grep -q "^${field}:" "$FILE"; then
    echo "FAIL: $FILE — missing field: ${field}"
    ERRORS=$((ERRORS + 1))
  fi
done

for section in "## Protocol" "## The Book" "### The Pattern" "### Protocol (extended)" "### Anti-Pattern (extended)" "### Examples" "### Practitioners" "### Historical Events" "### Lineage" "### Origin"; do
  if ! grep -qF "$section" "$FILE"; then
    echo "FAIL: $FILE — missing section: ${section}"
    ERRORS=$((ERRORS + 1))
  fi
done

if [[ $ERRORS -eq 0 ]]; then
  echo "PASS: $FILE"
else
  echo "TOTAL FAILURES: $ERRORS in $FILE"
  exit 1
fi
```

- [ ] **Step 2: Write `tests/validate-patterns.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
PASS=0; FAIL=0

for pattern_file in "${REPO_ROOT}"/patterns/*/pattern.md; do
  if bash "${SCRIPT_DIR}/validate-schema.sh" "$pattern_file"; then
    PASS=$((PASS + 1))
  else
    FAIL=$((FAIL + 1))
  fi
done

echo "Results: ${PASS} passed, ${FAIL} failed"
[[ $FAIL -eq 0 ]] || exit 1
```

- [ ] **Step 3: Run — expect FAIL (no frontmatter yet)**

```bash
bash tests/validate-patterns.sh
```

Expected: 3 FAIL messages. Confirms validator works.

- [ ] **Step 4: Commit**

```bash
git add tests/
git commit -m "test: schema validator — validate-schema.sh + validate-patterns.sh"
```

---

### Task 2: Upgrade Existing 3 Patterns to New Schema

Add YAML frontmatter and The Book sections. Validate after each one.

**Files:**
- Modify: `patterns/andon-cord/pattern.md`
- Modify: `patterns/musk-filter/pattern.md`
- Modify: `patterns/feynman-clarity/pattern.md`

- [ ] **Step 1: Upgrade `patterns/andon-cord/pattern.md`**

Write the following **complete file content** (replacing the existing file entirely):

```markdown
---
name: andon-cord
aliases: [factory-stop, jidoka, line-stop-protocol, toyota-andon]
domain: [engineering, team-dynamics, quality-control, debugging]
trigger: [frustration signal, F-bomb, "going in circles", "WHY", "I give up", repeated failure, debugging loop with no improvement]
practitioners:
  - name: Taiichi Ohno
    era: 1950-1990
    application: Toyota Production System — any worker stops the entire line on detecting a defect
  - name: Elon Musk
    era: 2003-present
    application: Tesla manufacturing — adopted TPS principles including line-stop authority
events:
  - name: Toyota Production System deployment
    year: 1950-1970
    gem-role: applied — Ohno systematized line-stop authority across all Toyota plants, reducing defect escape rate to near-zero
  - name: Tesla Model 3 production ramp
    year: 2017-2018
    gem-role: applied — Musk applied stop-and-fix discipline during production hell at Fremont factory
lineage: sakichi-toyoda-autoloom-1896 → taiichi-ohno-jidoka-1950 → toyota-production-system-1970 → elon-musk-2003
origin-earliest: ohno-1950
origin-modern: toyota-1970
---

# Toyota — Andon Cord Protocol

## Protocol  ← TLDR zone (always at the top)

**Trigger:** Frustration signal — F-bomb, "going in circles", "WHY" (all caps), "I give up", repeated failure, debugging loop with no improvement after 2+ attempts

**Steps:**
1. ALL current tasks PAUSE immediately — no exceptions
2. Acknowledge the stop in exactly 1 sentence — no defending the strategy
3. Ask one question only: "What broke and what were you trying to accomplish?"
4. Wait for the answer — do not offer solutions yet
5. Do NOT resume any paused work until the human explicitly confirms the blocker is resolved

**Anti-pattern:** Continuing the same failed approach while softening tone — sympathetic words + variation #4 of the same broken strategy

**Hard rule:** The line does not restart until the root cause is confirmed resolved

---

## The Book  ← depth zone (always at the bottom)

### The Pattern

In Toyota's manufacturing plants, any worker who sees a defect can pull a cord that stops the entire production line. Work halts. The team gathers. The root cause is identified and fixed before production resumes. No workarounds. No "keep moving and fix later." The stop is respected, not punished.

Applied to knowledge work: when a frustration signal fires, all current tasks pause. The AI acknowledges the stop in one sentence, asks what broke and what the goal was, and does not resume until the blocker is explicitly resolved. This is a full strategy reset — not a tone adjustment, not a sympathy response.

### Protocol (extended)

1. **ALL current tasks PAUSE immediately** — no exceptions, no "let me just finish this one thing"
2. **Acknowledge the stop in exactly 1 sentence** — no defending the strategy, no explaining, no apologizing
3. **Ask one question only:** "What broke and what were you trying to accomplish?"
4. **Wait for the answer** — do not offer solutions, suggestions, or alternatives yet
5. **Do NOT resume any paused work** until the human explicitly confirms the blocker is resolved
6. **If other tasks were running:** deprioritize non-critical work, stand by, do not introduce new complexity

**Rationale for step 3 (one question only):** Multiple questions create cognitive load at exactly the wrong moment. One question forces prioritization.

**Rationale for step 5 (wait for explicit confirmation):** Implicit "okay I think we're good" is not the same as "the blocker is resolved." The cord is pulled until the worker says it can be released.

### Anti-Pattern (extended)

The most common violation: the AI says something empathetic and then immediately tries variation #4 of the same broken strategy. The line never stopped. The root cause was never identified.

Other violations:
- **Defending the strategy that just failed:** "The approach was sound, it's just that..." — rationalization, not a reset
- **Introducing new complexity before the blocker is cleared:** "While we're at it..." — the line is still stopped
- **Asking multiple clarifying questions at once** — cognitive overload at the exact moment bandwidth is lowest

### Examples

**Classic violation — Karpathy loop:** An agent runs a loop to improve a conventions file. Each iteration produces output. The loop continues. No improvement signal exists but the loop doesn't stop. The Andon Cord should have fired at the first sign of circular output — same input, same failure, no delta.

**Classic violation — Strategy defense:** Engineer says "WHY isn't this working, this is the third time." Agent responds: "I understand your frustration. The approach we're using should work because [explanation of the broken approach]. Let me try adjusting [minor variation]." The cord was never pulled.

**Correct application:** Engineer drops an F-bomb mid-session. Agent responds: "Stopping everything. What broke and what were you trying to accomplish?" Engineer explains. Agent resets strategy from scratch, addresses the actual blocker.

### Practitioners

**Taiichi Ohno (1912–1990)**
Industrial engineer who created the Toyota Production System. Ohno gave every worker the authority — and obligation — to stop the entire production line when they detected a defect. This was radical: traditional manufacturing assumed workers should flag defects but keep moving. Ohno proved the opposite: a defect caught at Station 1 costs 1x. A defect that passes ten stations costs 10x.

**Elon Musk (1971–present)**
Synthesized the Toyota Production System at Tesla and SpaceX. Applied the line-stop principle to software engineering and AI agent contexts. The Andon Cord is one of the TPS patterns he explicitly credits in Walter Isaacson's biography.

### Historical Events

**Toyota Production System Deployment (1950–1970)**
Workers initially resisted — stopping the line felt like failure. Ohno reframed it: pulling the cord is the highest-quality action a worker can take. By 1970, Toyota's defect escape rate was a fraction of American competitors. The Andon cord was a primary cause.

**Tesla Model 3 Production Ramp (2017–2018)**
During "production hell," Musk camped in the Fremont factory applying stop-and-fix discipline. When a bottleneck appeared: stop, root-cause, fix — not keep moving and hope.

### Lineage

Sakichi Toyoda's auto-loom (1896, machine stops itself on thread break) → Kiichiro Toyoda quality-first production (1930s) → Taiichi Ohno jidoka formalization (1950s) → Toyota global deployment (1960s-70s) → Western adoption via "The Machine That Changed the World" (1990) → Elon Musk (Tesla/SpaceX, 2000s)

### Origin

The Andon system takes its name from the Japanese word for "lantern." Taiichi Ohno formalized it as part of the Toyota Production System in the 1950s, building on *jidoka* (自働化): "automation with a human touch." The philosophical core: quality over speed. A line that runs fast and produces defects is worse than one that stops and fixes. Toyota's dominance through the 1970s-90s vindicated the approach.

Elon Musk has cited the Toyota Production System as a direct influence on Tesla's manufacturing philosophy. The Andon cord is one of the patterns he synthesized and brought into software and hardware engineering contexts.
```

- [ ] **Step 2: Validate andon-cord**

```bash
bash tests/validate-schema.sh patterns/andon-cord/pattern.md
```

Expected: `PASS: patterns/andon-cord/pattern.md`

- [ ] **Step 3: Upgrade `patterns/musk-filter/pattern.md`**

Write the following **complete file content** (replacing the existing file entirely):

```markdown
---
name: musk-filter
aliases: [pre-build-gate, elon-filter, 5-step-algorithm, question-delete-simplify]
domain: [engineering, decision-making, process-design, product-management]
trigger: [build request, "let's add", "we should create", automation proposal, scope creep, planning phase, before first line of code]
practitioners:
  - name: Elon Musk
    era: 2002-present
    application: SpaceX rocket cost reduction, Tesla Gigafactory design, Boring Company tunneling
  - name: Henry Ford
    era: 1908-1927
    application: Model T production — systematically eliminated steps to hit $290 price point (from $825 at launch)
  - name: Taiichi Ohno
    era: 1950-1990
    application: Toyota muda elimination — remove waste before optimizing remaining steps
events:
  - name: SpaceX Falcon 9 cost reduction
    year: 2002-2010
    gem-role: applied — Musk decomposed rocket costs to raw materials, eliminated 90% of assumed requirements; cost per kg to orbit dropped 10x
  - name: Karpathy loop incident
    year: 2026
    gem-role: violated — agent applied loop automation (Step 5) without questioning whether the loop should exist (Step 1); result: token burn, no improvement
  - name: Ford Model T price reduction
    year: 1908-1916
    gem-role: applied — eliminated every non-essential manufacturing step until Model T reached $290
lineage: aristotle-analytics-350bc → descartes-systematic-doubt-1637 → ford-waste-elimination-1908 → ohno-muda-1950 → musk-filter-2002
origin-earliest: aristotle-350bc
origin-modern: musk-2002
---

# Elon Musk — Musk Filter (Pre-Build Gate)

## Protocol  ← TLDR zone (always at the top)

**Trigger:** Any proposal to build, create, add, or automate — before the first line of code is written

**Steps:**
1. QUESTION IT — who specifically requires this, and what breaks if it doesn't exist? If unclear: kill it
2. DELETE IT — remove at least 30% of the proposed scope; if nothing was deleted, look harder
3. SIMPLIFY — tighten what remains; one way to do it, not three
4. ACCELERATE — find the fastest path through the simplified scope
5. AUTOMATE — only now; automation of a broken process = faster broken process

**Anti-pattern:** Starting with automation (Step 5) before questioning whether the thing should exist (Step 1)

**Hard rule:** Never jump to Step 5 without completing Steps 1-4. Block execution if this rule is violated.

---

## The Book  ← depth zone (always at the bottom)

### The Pattern

Elon Musk's 5-step engineering algorithm for eliminating bureaucracy and building lean systems: **Question → Delete → Simplify → Accelerate → Automate** — in that exact order, never skipped. The fatal mistake of engineers is jumping to Step 5 (automate) before completing Steps 1-2. Automation of a broken process creates a faster broken process. The order is mandatory.

### Protocol (extended)

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

### Anti-Pattern (extended)

Starting with automation (Step 5) before questioning whether the thing should exist (Step 1). A process exists, someone proposes automating it, everyone agrees because automation sounds like progress, the automated version ships — and now you have a faster version of a process that shouldn't have existed.

Other violations:
- Optimizing (Step 3) before deleting dead weight (Step 2)
- Speeding up (Step 4) a process that hasn't been simplified (Step 3)
- Treating "we've always done it this way" as an answer to Step 1
- Adding features because they seem useful rather than because someone specifically needs them

### Examples

**Classic violation — Karpathy loop incident:** An agent was asked to run a loop to improve conventions.md. The loop (Step 5: automate) was applied before anyone questioned whether the loop was the right tool (Step 1), or pruned the file first (Step 2). Result: token burn, circular output, no real improvement. The Musk Filter would have killed the loop at Step 1.

**Classic violation — Nick vs Nick-v2 confusion:** An agent tried to optimize (Step 3) an existing conventions file when the real fix was deleting and restructuring ambiguous rules (Step 2). Wrong step, wrong order.

**Correct application:** Someone proposes "Let's build an automated reporting dashboard." Step 1: "Who specifically needs this? What breaks without it?" — no clear answer. Kill it. Two weeks of engineering saved.

### Practitioners

**Elon Musk (1971–present)**
Described the 5-step algorithm in a 2021 presentation and Walter Isaacson's 2023 biography. Emerged from SpaceX experience: engineers consistently jumped to optimization (Step 3) and automation (Step 5) without questioning requirements (Step 1). "Requirements are definitely dumb. It doesn't matter who gave them to you."

**Henry Ford (1863–1947)**
Model T launched at $825 in 1908. By 1916: $290. Ford achieved this by eliminating manufacturing steps — not optimizing the existing process. He questioned every requirement before touching the line. Delete before optimize.

**Taiichi Ohno (1912–1990)**
Formalized waste elimination as *muda* (無駄) in the Toyota Production System. Seven types of waste must be eliminated before any optimization is applied. Direct ancestor of the Musk Filter.

### Historical Events

**SpaceX Falcon 9 (2002–2010)**
Musk decomposed rocket costs to raw materials: raw materials cost 2% of typical aerospace price. Result: cost per kg to orbit from ~$54,000 (Space Shuttle) to ~$2,720 (Falcon 9).

**Karpathy Loop Incident (2026)**
A Nexus agent was asked to run a loop to improve conventions.md. Loop automation (Step 5) applied before questioning whether the loop was the right tool (Step 1) or pruning the file first (Step 2). Token burn, circular output, no real improvement. The canonical modern example of Step 5 before Step 1.

### Lineage

Aristotle's *Posterior Analytics* (350 BC, question assumptions) → Descartes' *Meditations* (1637, systematic doubt before building) → Taylor's Scientific Management (1911, eliminate wasted motion) → Ford waste elimination (1908-1916) → Ohno muda (1950s) → Lean Manufacturing (1990s) → Musk Filter (2002-present)

### Origin

Elon Musk described this 5-step algorithm in a 2021 interview and Walter Isaacson's 2023 biography as his core engineering philosophy, first developed at SpaceX for rocket manufacturing and later applied to Tesla production lines and software systems.

His framing: "The first step is to make the requirements less dumb. The requirements are definitely dumb; it doesn't matter who gave them to you. Step two is try very hard to delete the part or process. Step three is simplify or optimize. Step four is accelerate the cycle time. Step five is automate."

He noted the most common error among smart engineers: "It is a mistaken assumption to automate things that should just not exist."
```

- [ ] **Step 4: Validate musk-filter**

```bash
bash tests/validate-schema.sh patterns/musk-filter/pattern.md
```

Expected: `PASS: patterns/musk-filter/pattern.md`

- [ ] **Step 5: Upgrade `patterns/feynman-clarity/pattern.md`**

Write the following **complete file content** (replacing the existing file entirely):

```markdown
---
name: feynman-clarity
aliases: [feynman-technique, explain-it-simply, rubber-duck-debugging, clarity-test]
domain: [debugging, learning, communication, problem-solving]
trigger: ["I don't understand why", "why isn't this working", stuck debugging loop, "it should work but doesn't", can't explain simply]
practitioners:
  - name: Richard Feynman
    era: 1940-1988
    application: Manhattan Project debugging, Challenger investigation, physics education reform
  - name: Albert Einstein
    era: 1905-1955
    application: general relativity via thought experiments — plain-language mental models before mathematics
  - name: Socrates
    era: 470-399bc
    application: Socratic method — expose contradictions in assumed knowledge through simple questions
events:
  - name: Manhattan Project debugging
    year: 1943-1945
    gem-role: applied — Feynman found critical calculation errors by demanding plain-language explanation of every assumption
  - name: Challenger disaster investigation
    year: 1986
    gem-role: applied — Feynman bypassed NASA bureaucracy, asked simple questions, demonstrated O-ring failure with ice water in 30 seconds
  - name: Feynman Lectures on Physics
    year: 1961-1963
    gem-role: applied — rebuilt physics curriculum using plain-language explanation as quality bar
lineage: socratic-method-470bc → aristotle-analytics-350bc → descartes-clear-ideas-1637 → einstein-thought-experiments-1905 → feynman-clarity-1950s
origin-earliest: socrates-470bc
origin-modern: feynman-1950
---

# Richard Feynman — Feynman Clarity Test

## Protocol  ← TLDR zone (always at the top)

**Trigger:** "I don't understand why this isn't working" / debugging loop with no progress after 2+ attempts / explanation of the bug keeps growing in complexity

**Steps:**
1. STOP — close all debuggers, logs, and tool output
2. State the goal in one sentence (plain English, no jargon)
3. State what it's actually doing in one sentence (plain English)
4. Walk the gap step by step as if teaching a 12-year-old — stop at the first step you can't explain simply
5. That step = the root cause. Investigate it specifically.
6. Fix the root cause, not the symptom you've been chasing

**Anti-pattern:** Adding more logs, more tools, more data while the root cause remains unexplained

---

## The Book  ← depth zone (always at the bottom)

### The Pattern

Richard Feynman's teaching method: if you cannot explain something simply, you don't understand it yet. The corollary for debugging: if you cannot explain each step of why something fails in plain language — no jargon, no hand-waving — you have not yet identified the root cause. You've identified a symptom.

The technique is to stop all tools and logs and explain the system aloud as if teaching a 12-year-old. The moment you cannot explain a step simply is the moment you've found the gap.

### Protocol (extended)

1. **Stop** — close all debuggers, logs, and tool output. No more data until step 5.
2. **State the goal** — in one sentence, plain English: "This system should [do X] when [Y happens]."
3. **State what it's doing** — in one sentence, plain English: "Instead, it's [doing Z]."
4. **Walk the gap** — explain every step between the goal and the actual behavior as if teaching a 12-year-old. For each step, ask: "Why?" If the answer is "I don't know" or requires jargon, stop — you've found the gap.
5. **The step you can't explain simply = the root cause.** Investigate that specific step now.
6. **Fix the root cause**, not the symptom you've been chasing.

**Rationale for step 1 (stop all tools):** More data without clearer thinking produces more confusion. The investigation must pause before it can reset.

**Rationale for step 4 (12-year-old standard):** Jargon is a hiding place for gaps. "The middleware layer intercepts the request" is not an explanation — "the request goes through X before reaching Y" is. If you can't say the latter, you don't know what X does.

### Anti-Pattern (extended)

Adding complexity to the investigation while the root cause remains unexplained. More logs. More print statements. More tools. More variations of the same failing approach. The investigation grows larger but understanding doesn't grow deeper.

Other violations:
- "It must be a [framework/library/environment] bug" — before being able to explain exactly why
- Asking for someone else to look at it before completing steps 2-4 yourself
- Accepting "it just works now" after a random change — without understanding why
- Jumping to solutions before the diagnosis is complete

### Examples

**Correct application — Null pointer hunt:** An engineer spends an hour on a null pointer exception. Tools show where it crashes. Step 1: stop tools. Step 2: "The user object should be populated after login." Step 3: "It's null when the profile page loads." Step 4: walking the gap — "Login sets the user... session stores it... profile page retrieves it from session... wait, I can't explain why the session variable is accessible at login but not at profile load. That's the gap." Root cause found: session scope mismatch.

**Classic violation — The growing investigation:** Agent is asked why an API call fails. Agent checks logs, adds more logging, tries a different endpoint, checks network tab, searches Stack Overflow, tries a header variation. 45 minutes pass. The investigation has grown but understanding hasn't. Feynman Clarity Test applied: "Walk me through the auth flow." — "It sends the token... wait, I can't explain which token it sends or where it came from." Gap found immediately.

### Practitioners

**Richard Feynman (1918–1988)**
Theoretical physicist who won the Nobel Prize in 1965. His rule: if you cannot explain something in plain language without jargon, you've memorized it — you haven't understood it. Applied as a debugging tool: when something wasn't working, stop and explain it from scratch until the gap becomes obvious.

**Albert Einstein (1879–1955)**
Derived general relativity through thought experiments — plain-language mental models — before mathematics. His principle: "If you can't explain it simply, you don't understand it well enough."

**Socrates (470–399 BC)**
Original practitioner. The Socratic method: stop, ask simple questions, expose contradictions in assumed knowledge. Socrates claimed superiority only in knowing he didn't know — that epistemic humility is the foundation of the clarity test.

### Historical Events

**Manhattan Project (1943–1945)**
Feynman joined at 24 and became known for finding errors senior physicists had missed — not through superior mathematics, but by asking "explain this to me simply" until the error surfaced.

**Challenger Investigation (1986)**
Feynman bypassed NASA's formal process, called engineers directly, and asked simple questions. Discovered that NASA managers and engineers had different failure probability estimates: 1-in-100 vs 1-in-100,000. Demonstrated O-ring failure live on television with a glass of ice water in 30 seconds. The clarity test applied to an engineering disaster.

**Feynman Lectures on Physics (1961–1963)**
Caltech asked Feynman to teach introductory physics. He rebuilt the curriculum from scratch: if a concept couldn't be explained without jargon, the curriculum didn't understand it well enough yet. The lectures are still in print.

### Lineage

Socratic method (470 BC) → Aristotle's first principles explanation (350 BC) → Descartes' clear and distinct ideas (1637) → scientific method plain-language hypothesis (Enlightenment) → Einstein's thought experiments (1905) → Feynman's clarity rule (1950s) → rubber duck debugging (1999, *The Pragmatic Programmer*)

### Origin

Feynman developed his approach at MIT and Princeton, noticing that many physicists could manipulate equations without understanding what they described. His test: explain it without the equations.

The technique became formalized posthumously as the "Feynman Technique": choose a concept, explain in plain language as if teaching a child, identify where the explanation breaks down, return to source, repeat until smooth. The debugging application is a direct translation: treat a broken system like a physics problem. Explain it from first principles. The gap in your explanation is the bug.
```

- [ ] **Step 6: Validate feynman-clarity**

```bash
bash tests/validate-schema.sh patterns/feynman-clarity/pattern.md
```

Expected: `PASS: patterns/feynman-clarity/pattern.md`

- [ ] **Step 7: Run full validation suite**

```bash
bash tests/validate-patterns.sh
```

Expected: `Results: 3 passed, 0 failed`

- [ ] **Step 8: Commit**

```bash
git add patterns/
git commit -m "feat(patterns): upgrade all 3 patterns to v1.0 schema — frontmatter + The Book"
```

---

### Task 3: `scripts/generate-patterns.sh`

Auto-regenerates PATTERNS.md dispatch table from frontmatter. Run after any gem is added.

**Files:**
- Create: `scripts/generate-patterns.sh`

- [ ] **Step 1: Write the script**

```bash
#!/usr/bin/env bash
# Regenerates PATTERNS.md from all patterns/*/pattern.md frontmatter
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT="${REPO_ROOT}/PATTERNS.md"

{
  echo "# Pantheon — Pattern Dispatch Table"
  echo ""
  echo "> Auto-generated by \`scripts/generate-patterns.sh\`. Do not edit manually."
  echo "> Last generated: $(date '+%Y-%m-%d')"
  echo ""
  echo "| Command | Pattern | Domain | Trigger |"
  echo "|---------|---------|--------|---------|"

  for pattern_file in "${REPO_ROOT}"/patterns/*/pattern.md; do
    gem_name=$(basename "$(dirname "$pattern_file")")
    name=$(grep "^name:" "$pattern_file" | head -1 | sed 's/^name: *//')
    domain=$(grep "^domain:" "$pattern_file" | head -1 | sed 's/^domain: *\[//' | sed 's/,.*//' | sed 's/\].*//')
    trigger=$(grep "^trigger:" "$pattern_file" | head -1 | sed 's/^trigger: *\[//' | sed 's/,.*//' | tr -d '"')
    echo "| \`/pantheon-${gem_name}\` | ${name} | ${domain} | ${trigger} |"
  done

  echo ""
  echo "---"
  echo ""
  echo "_Install: \`curl -fsSL https://raw.githubusercontent.com/dkschrei/pantheon/main/install.sh | bash\`_"
} > "$OUTPUT"

COUNT=$(grep -c "^| \`" "$OUTPUT" || true)
echo "✓ PATTERNS.md regenerated — ${COUNT} patterns"
```

- [ ] **Step 2: Run it**

```bash
chmod +x scripts/generate-patterns.sh
bash scripts/generate-patterns.sh
cat PATTERNS.md
```

Expected: table with 3 rows matching current patterns.

- [ ] **Step 3: Commit**

```bash
git add scripts/ PATTERNS.md
git commit -m "feat(scripts): generate-patterns.sh — auto-regenerate dispatch table from frontmatter"
```

---

### Task 4: `install.sh`

One-command install for Claude Code users.

**Files:**
- Create: `install.sh`
- Create: `tests/test-install.sh`

- [ ] **Step 1: Write `tests/test-install.sh`** (test first)

```bash
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

echo "Testing install.sh in temp dir: $TMPDIR"

# Test 1: Fresh install
HOME="$TMPDIR" bash "${REPO_ROOT}/install.sh"

COMMANDS=$(ls "${TMPDIR}/.claude/commands/"*.md 2>/dev/null | wc -l | tr -d ' ')
[[ "$COMMANDS" -ge 3 ]] || { echo "FAIL: expected ≥3 commands, got $COMMANDS"; exit 1; }
echo "PASS: $COMMANDS commands installed"

SKILLS=$(ls "${TMPDIR}/.claude/skills/"*.md 2>/dev/null | wc -l | tr -d ' ')
[[ "$SKILLS" -ge 3 ]] || { echo "FAIL: expected ≥3 skills, got $SKILLS"; exit 1; }
echo "PASS: $SKILLS skills installed"

# Test 2: Idempotent re-run
HOME="$TMPDIR" bash "${REPO_ROOT}/install.sh"
echo "PASS: re-run is idempotent"

echo "All install tests passed"
```

- [ ] **Step 2: Run test — expect FAIL** (install.sh doesn't exist yet)

```bash
bash tests/test-install.sh
```

Expected: error. Confirms test is wired.

- [ ] **Step 3: Write `install.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

PANTHEON_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_COMMANDS="${HOME}/.claude/commands"
CLAUDE_SKILLS="${HOME}/.claude/skills"

echo "Installing Pantheon..."

[[ -d "${PANTHEON_DIR}/commands" ]] || { echo "ERROR: commands/ not found. Run from repo root."; exit 1; }
[[ -d "${PANTHEON_DIR}/patterns" ]] || { echo "ERROR: patterns/ not found. Run from repo root."; exit 1; }

mkdir -p "${CLAUDE_COMMANDS}" "${CLAUDE_SKILLS}"

cp "${PANTHEON_DIR}"/commands/*.md "${CLAUDE_COMMANDS}/"
COMMANDS_COUNT=$(ls "${PANTHEON_DIR}"/commands/*.md | wc -l | tr -d ' ')
echo "  ✓ ${COMMANDS_COUNT} commands → ${CLAUDE_COMMANDS}/"

SKILLS_COUNT=0
for adapter in "${PANTHEON_DIR}"/patterns/*/adapters/claude.md; do
  gem_name=$(basename "$(dirname "$(dirname "$adapter")")")
  cp "$adapter" "${CLAUDE_SKILLS}/pantheon-${gem_name}.md"
  SKILLS_COUNT=$((SKILLS_COUNT + 1))
done
echo "  ✓ ${SKILLS_COUNT} skills → ${CLAUDE_SKILLS}/"

echo ""
echo "Pantheon installed. Restart Claude Code to activate."
echo ""
echo "Available commands:"
for cmd in "${PANTHEON_DIR}"/commands/*.md; do
  echo "  /$(basename "$cmd" .md)"
done
```

- [ ] **Step 4: Run test**

```bash
chmod +x install.sh
bash tests/test-install.sh
```

Expected: `All install tests passed`

- [ ] **Step 5: Smoke test directly**

```bash
bash install.sh
```

Verify output lists correct commands and skill counts.

- [ ] **Step 6: Commit**

```bash
git add install.sh tests/test-install.sh
git commit -m "feat: install.sh + test — one-command Claude Code install"
```

---

### Task 5: Historian Agent Tooling

Everything Nick needs to execute Phase 1 and Phase 2.

**Files:**
- Create: `historian/seed-list.md`
- Create: `historian/prompt.md`
- Create: `historian/pruning-criteria.md`
- Create: `historian/loop.sh`
- Create: `historian/prune.sh`
- Create: `historian/README.md`

- [ ] **Step 1: Write `historian/seed-list.md`**

```markdown
# Pantheon Historian — Seed List

50 curated heroes for Phase 1 research. Processed in order by loop.sh.
Progress auto-tracked in `historian/.progress`.

## Modern Builders (10)
- [ ] Elon Musk — SpaceX, Tesla, Neuralink
- [ ] Steve Jobs — Apple, Pixar
- [ ] Jeff Bezos — Amazon, Blue Origin
- [ ] Tony Fadell — iPod, iPhone, Nest
- [ ] Andrej Karpathy — Tesla AI, OpenAI, educator
- [ ] Andy Grove — Intel, high-output management
- [ ] Jony Ive — Apple industrial design
- [ ] Taiichi Ohno — Toyota Production System
- [ ] Sam Altman — Y Combinator, OpenAI
- [ ] Marc Andreessen — Netscape, software-eats-the-world thesis

## Scientists (10)
- [ ] Richard Feynman — quantum physics, Manhattan Project, Challenger
- [ ] Claude Shannon — information theory, entropy
- [ ] John Von Neumann — game theory, computing architecture
- [ ] Alan Turing — computation, AI foundations
- [ ] Albert Einstein — special/general relativity, thought experiments
- [ ] Nikola Tesla — AC current, electromagnetic resonance
- [ ] Marie Curie — radioactivity research under extreme constraint
- [ ] Linus Pauling — chemical bonding, vitamin C controversy
- [ ] Niels Bohr — complementarity, quantum mechanics
- [ ] Stephen Hawking — physics communication under physical constraint

## Philosophers & Strategists (8)
- [ ] Aristotle — logic, first principles, categories
- [ ] René Descartes — systematic doubt, clear ideas
- [ ] Marcus Aurelius — Stoic practice, journaling for clarity
- [ ] Seneca — time management, letters on urgency
- [ ] Sun Tzu — asymmetric advantage, terrain analysis
- [ ] Niccolò Machiavelli — political realism, power dynamics
- [ ] Immanuel Kant — categorical imperative, duty-based reasoning
- [ ] Karl Popper — falsifiability, open society

## Industrial Pioneers (6)
- [ ] Henry Ford — assembly line, waste elimination, accessibility
- [ ] Frederick Winslow Taylor — scientific management, time-motion study
- [ ] Andrew Carnegie — vertical integration, systematic philanthropy
- [ ] W. Edwards Deming — quality systems, PDCA cycle
- [ ] Alfred Sloan — decentralized management, GM restructuring
- [ ] John D. Rockefeller — standard oil, systematic cost reduction

## Military Leaders (6)
- [ ] Alexander the Great — logistics as strategy, speed-of-decision
- [ ] Napoleon Bonaparte — corps system, information advantage
- [ ] Hannibal Barca — encirclement, outnumbered victory
- [ ] Ernest Shackleton — leadership under survival conditions
- [ ] Winston Churchill — narrative framing, refusing capitulation
- [ ] George Washington — strategic retreat, long-game patience

## Artists & Creators (5)
- [ ] Leonardo da Vinci — cross-domain curiosity, notebook method
- [ ] Michelangelo — constraint as creativity
- [ ] Wolfgang Amadeus Mozart — compositional speed, pattern saturation
- [ ] Pablo Picasso — deconstruction-reconstruction, period focus
- [ ] Johann Sebastian Bach — structural mastery, constraint-driven variation

## Investors & Economists (5)
- [ ] Charlie Munger — inversion, mental model lattice
- [ ] Warren Buffett — circle of competence, moat thinking
- [ ] Daniel Kahneman — cognitive bias mapping, System 1/2
- [ ] Nassim Taleb — antifragility, Black Swan preparation
- [ ] John Maynard Keynes — counter-cyclical thinking, animal spirits
```

- [ ] **Step 2: Write `historian/prompt.md`**

```markdown
# Historian Research Prompt

Template: replace `{HERO}` with the hero name from seed-list.md.

---

Research {HERO} and identify their single most important cognitive pattern — the move they made repeatedly across their career that explains their results.

Requirements:
1. ONE pattern only — not a list. The ONE defining move.
2. The move, not the biography — what they actually did differently.
3. Executable — expressible as numbered steps someone else can follow.
4. Historically grounded — at least one real event where the pattern was applied.
5. Duplicate check — before creating a new file, run `ls patterns/` and skim each existing pattern.md. If {HERO}'s pattern is substantially the same as an existing gem, add them as a practitioner instead of creating a new file.

Output:
- If new gem: write `patterns/{gem-name}/pattern.md` and `patterns/{gem-name}/adapters/claude.md` using SCHEMA.md
- If existing gem: update the practitioners[] and events[] in the existing pattern.md frontmatter

Gem naming: use the most recognizable label for this pattern (may be hero-based or concept-based).
```

- [ ] **Step 3: Write `historian/pruning-criteria.md`**

```markdown
# Pruning Criteria — 4 Quality Gates

Every gem must pass all 4. Used in Phase 2 (prune.sh).

---

## 1. TRIGGER_SPECIFIC
Trigger condition is a precise phrase or observable signal — not vague.
- PASS: "Any proposal to build, create, add, or extend something"
- FAIL: "When things are hard" / "During complex projects"

## 2. EXECUTABLE
Protocol steps are numbered, concrete, produce a specific output. No interpretation required.
- PASS: "Delete at least 30% of the proposed scope"
- FAIL: "Think carefully about the problem" / "Apply good judgment"

## 3. DISTINCT
Running this gem produces meaningfully different output than all other gems on the same problem.
- PASS: Different trigger condition AND different output from all others
- FAIL: Near-identical to another gem → MERGE into the more specific one

## 4. GROUNDED
Has at least 1 named practitioner with a real application AND 1 named historical event.
- PASS: Taiichi Ohno + Toyota Production System deployment (1950-1970)
- FAIL: "Many great leaders" / no events cited

---

## Scoring → Flag

| Criteria passed | Flag |
|----------------|------|
| All 4 | KEEP |
| 1-2 fail | REVISE — specify criterion + proposed fix |
| Substantially same as another | MERGE — specify which gem to merge into |
| 3-4 fail | DELETE |
```

- [ ] **Step 4: Write `historian/loop.sh`**

```bash
#!/usr/bin/env bash
# Historian Phase 1 — Build Loop
# Usage: bash historian/loop.sh
# Interactive: pauses after each hero for review
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
PROGRESS="${SCRIPT_DIR}/.progress"
SEED="${SCRIPT_DIR}/seed-list.md"
PROMPT_TPL="${SCRIPT_DIR}/prompt.md"

touch "$PROGRESS"

# Extract unchecked heroes
mapfile -t HEROES < <(grep "^- \[ \]" "$SEED" | sed 's/^- \[ \] //' | sed 's/ —.*//')
echo "Phase 1 — ${#HEROES[@]} heroes remaining"

for hero in "${HEROES[@]}"; do
  grep -qF "$hero" "$PROGRESS" && { echo "SKIP: $hero"; continue; }

  echo ""
  echo "=== $hero ==="
  echo "--- RESEARCH PROMPT ---"
  sed "s/{HERO}/$hero/g" "$PROMPT_TPL"
  echo "--- END PROMPT ---"
  echo ""
  echo "Execute the prompt above, write gem files, then press ENTER..."
  read -r

  echo "$hero" >> "$PROGRESS"
  sed -i.bak "s/- \[ \] ${hero}/- [x] ${hero}/" "$SEED" && rm "${SEED}.bak"

  cd "$REPO_ROOT"
  bash scripts/generate-patterns.sh

  if ! git diff --quiet || ! git diff --staged --quiet; then
    git add patterns/ commands/ PATTERNS.md historian/seed-list.md
    git commit -m "feat(patterns): $hero gem added"
    echo "✓ Committed: $hero"
  else
    echo "WARNING: No changes detected — may be duplicate, check patterns/"
  fi
done

echo ""
echo "Phase 1 complete. Run: bash historian/prune.sh"
```

- [ ] **Step 5: Write `historian/prune.sh`**

```bash
#!/usr/bin/env bash
# Historian Phase 2 — Pruning Pass
# Generates historian/pruning-report.md for Dana's review
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
REPORT="${SCRIPT_DIR}/pruning-report.md"
TOTAL=$(ls -d "${REPO_ROOT}"/patterns/*/ 2>/dev/null | wc -l | tr -d ' ')

cat > "$REPORT" << HEADER
# Pantheon Pruning Report
**Generated:** $(date '+%Y-%m-%d')
**Total gems evaluated:** ${TOTAL}

Review DELETE and MERGE sections only. Check boxes to approve.
Nick executes approved cuts. KEEP and REVISE require no decision.

---
HEADER

echo "Phase 2 — evaluating ${TOTAL} gems against pruning-criteria.md"
echo "Enter flag for each: KEEP / REVISE: reason | fix / MERGE: gem-name | reason / DELETE: reason"

for pattern_file in "${REPO_ROOT}"/patterns/*/pattern.md; do
  gem=$(basename "$(dirname "$pattern_file")")
  name=$(grep "^name:" "$pattern_file" | head -1 | sed 's/^name: *//')
  echo ""
  echo "[$gem] Read pattern then enter flag:"
  read -r result

  case "$result" in
    KEEP*)
      echo "- **${name}** (\`${gem}\`) — passes all 4 criteria" >> "$REPORT"
      ;;
    REVISE*)
      printf "\n### %s (\`%s\`)\n- Result: REVISE\n- Detail: %s\n- Dana action: auto-approved (Nick fixes)\n" \
        "$name" "$gem" "${result#REVISE: }" >> "$REPORT"
      ;;
    MERGE*)
      printf "\n### %s (\`%s\`)\n- Result: MERGE into %s\n- Dana action: [ ] Approved  [ ] Reject\n" \
        "$name" "$gem" "${result#MERGE: }" >> "$REPORT"
      ;;
    DELETE*)
      printf "\n### %s (\`%s\`)\n- Result: DELETE\n- Reason: %s\n- Dana action: [ ] Approved  [ ] Reject\n" \
        "$name" "$gem" "${result#DELETE: }" >> "$REPORT"
      ;;
  esac
done

echo ""
echo "Pruning report: historian/pruning-report.md"
echo "Send to Dana for DELETE/MERGE approval."
```

- [ ] **Step 6: Write `historian/README.md`**

```markdown
# Historian Agent

Open-sourced research tool. Run it to add gems to Pantheon and submit PRs.

## Run Phase 1 (Build)

```bash
git clone https://github.com/dkschrei/pantheon.git && cd pantheon
bash historian/loop.sh
```

Interactive — pauses after each hero. Review the generated gem, press ENTER to commit.

## Run Phase 2 (Prune)

```bash
bash historian/prune.sh
```

Generates `historian/pruning-report.md`. Review DELETE + MERGE sections. Check boxes and open a PR with the pruning-report.md for maintainer review.

## Quality Criteria

See `historian/pruning-criteria.md` — 4 gates every gem must pass.

## Manual Contribution

1. Read `SCHEMA.md`
2. Create `patterns/{name}/pattern.md` + `patterns/{name}/adapters/claude.md`
3. `bash tests/validate-schema.sh patterns/{name}/pattern.md`
4. `bash scripts/generate-patterns.sh`
5. Open a PR
```

- [ ] **Step 7: Make scripts executable and commit**

```bash
chmod +x historian/loop.sh historian/prune.sh
git add historian/
git commit -m "feat(historian): Phase 1 + Phase 2 tooling — loop, prune, seed list, prompt, criteria"
```

---

### Task 6: Community Docs + README

**Files:**
- Create: `CONTRIBUTING.md`
- Modify: `README.md`
- Modify: `commands/pantheon.md`

- [ ] **Step 1: Write `CONTRIBUTING.md`**

```markdown
# Contributing to Pantheon

Every gem that passes quality review makes the library more useful for every engineer who installs it.

## What makes a good gem

One question: **what did this genius actually do differently when faced with this class of problem?**
Not what they believed. Not what they said. The move.

Before writing:
- [ ] Does this pattern already exist? (`ls patterns/`)
- [ ] Is the trigger specific enough to know immediately if it applies?
- [ ] Are Protocol steps executable without judgment?
- [ ] Do I have a real historical event with a real outcome?

## How to contribute

```bash
git clone https://github.com/dkschrei/pantheon.git && cd pantheon
mkdir -p patterns/{gem-name}/adapters

# Write the gem (use SCHEMA.md as template)
# Validate
bash tests/validate-schema.sh patterns/{gem-name}/pattern.md
bash scripts/generate-patterns.sh

# PR
git checkout -b gem/{gem-name}
git add patterns/{gem-name}/ PATTERNS.md
git commit -m "feat(patterns): {gem-name} — {hero}"
git push origin gem/{gem-name}
```

## PR checklist

- [ ] `validate-schema.sh` passes
- [ ] All YAML frontmatter fields present
- [ ] Protocol is numbered steps, not prose
- [ ] Anti-pattern names a specific failure mode
- [ ] ≥1 real practitioner + ≥1 real historical event
- [ ] Not a near-duplicate of an existing gem

## Using the Historian agent

Want to add many gems? See `historian/README.md` to run the research loop yourself.
```

- [ ] **Step 2: Update `README.md` Status section**

Find `## Status` in README.md and replace the entire section with:

```markdown
## Status

**v1.0 — Building. Target: May 6, 2026 (Anthropic Developer Conference, SF)**

- [x] Schema v1.0 — YAML frontmatter + two-zone format (Protocol TLDR + The Book)
- [x] Andon Cord Protocol (Toyota / Taiichi Ohno)
- [x] Musk Filter (Elon Musk)
- [x] Feynman Clarity Test (Richard Feynman)
- [ ] 22-27 more gems via Historian agent research loop
- [ ] Public launch + community contributions open

3-gem preview available now via install above.
```

- [ ] **Step 3: Add stacking demo to README.md**

Insert before `## Why this exists`:

```markdown
## The Stacking Demo

Same problem. Three patterns. Three different lenses.

**Problem:** "I want to build a reporting dashboard."

**`/pantheon-musk-filter`:**
→ Who specifically requires this? What breaks without it? Delete 30% of scope first.

**`/pantheon-feynman-clarity`:**
→ Explain in plain English what decision this dashboard helps make.
  If you can't answer that, you don't understand the problem yet.

**`/pantheon-andon-cord`:**
→ (If you're adding this because your team is frustrated with existing reports)
  Stop. Ask: what broke and what were you trying to accomplish?

Three useful outputs. You synthesize. You decide. This is not a prompt library — it's a council of advisors.
```

- [ ] **Step 4: Update `commands/pantheon.md` install section**

Replace the `## Install` section with:

```markdown
## Install

```bash
curl -fsSL https://raw.githubusercontent.com/dkschrei/pantheon/main/install.sh | bash
```

Restart Claude Code after installing.
```

- [ ] **Step 5: Run full suite**

```bash
bash tests/validate-patterns.sh
bash tests/test-install.sh
bash scripts/generate-patterns.sh
```

All expected to pass.

- [ ] **Step 6: Commit**

```bash
git add CONTRIBUTING.md README.md commands/pantheon.md
git commit -m "docs: CONTRIBUTING + README stacking demo + v1.0 status + install.sh reference"
```

---

### Task 7: Final Validation + Push

- [ ] **Step 1: Run all tests**

```bash
bash tests/validate-patterns.sh && bash tests/test-install.sh
```

Expected: all pass.

- [ ] **Step 2: Verify structure**

```bash
ls -la
ls patterns/ historian/ commands/ scripts/ tests/ docs/
```

Confirm all directories and files exist.

- [ ] **Step 3: Push to GitHub**

```bash
git push origin main
```

- [ ] **Step 4: Verify README renders on GitHub**

Open `https://github.com/dkschrei/pantheon` — confirm stacking demo, install section, and status all render correctly.

---

## Phase B: Nick Executes (Reference)

After Phase A is pushed:

```
Nick: bash historian/loop.sh
  → 50 heroes, ~35-45 gems committed over 14 days

Nick: bash historian/prune.sh
  → historian/pruning-report.md generated

Dana: Review pruning-report.md
  → Check DELETE + MERGE boxes (one sitting)
  → Return approved report to Nick

Nick: Execute approved cuts → library is v1.0
```

---

## Phase C: Launch Prep (Reference)

- Dana spot-checks 10 gems — read as a stranger
- Test install.sh on a machine with no existing `~/.claude/`
- Make repo public
- Drop origin story post

---

*Plan: 2026-03-19 | Spec: docs/specs/2026-03-18-pantheon-v1-design.md*
