---
name: ohno-circle
aliases: [genchi-genbutsu, chalk-circle, go-and-see, reality-first, standing-observation]
domain: [engineering, debugging, systems, decision-making, quality-control]
trigger: [premature solution, theorizing without evidence, debugging from logs alone, "I think the problem is", solving from a dashboard, never visited the actual system, armchair diagnosis]
practitioners:
  - name: Taiichi Ohno
    era: 1947-1990
    application: Toyota Production System — stood on factory floors for entire shifts observing waste before allowing any process change
  - name: W. Edwards Deming
    era: 1950-1993
    application: Statistical quality control — insisted managers walk the production floor and measure actual processes rather than relying on reports
events:
  - name: Toyota machine shop rearrangement
    year: 1947
    gem-role: applied — Ohno observed workers standing idle during machine cycles, then rearranged machines so one worker could operate three or four
  - name: Kanban invention from supermarket observation
    year: 1948-1956
    gem-role: applied — Ohno observed supermarket restocking patterns (pull, not push), transplanted the observed principle into manufacturing as the kanban card system
  - name: Chalk circle engineer training
    year: 1950-1970
    gem-role: applied — Ohno drew a chalk circle on the factory floor and required engineers to stand in it for 8+ hours doing nothing but observing before proposing any improvement
lineage: sakichi-toyoda-loom-observation-1896 → taiichi-ohno-chalk-circle-1950 → toyota-genchi-genbutsu-1970 → lean-movement-gemba-walk-1990
origin-earliest: ohno-1947
origin-modern: toyota-1970
---

# Ohno Circle — Observe Before You Theorize

## Protocol  ← TLDR zone (always at the top)

**Trigger:** You are about to diagnose, optimize, or fix a system you have not directly observed in its actual operating environment — or you are theorizing a root cause from secondhand data (logs, reports, dashboards, someone else's summary).

**Steps:**
1. Go to where the work actually happens — the real system, the real code path, the real user flow. Not a summary. Not a metric. The thing itself.
2. Write down what you expect to see. Set it aside. Your job is to observe, not confirm.
3. Observe for at least 3x longer than feels necessary. Catalogue what actually happens — sequence, timing, idle states, handoffs, waste. The important things appear only after the obvious ones are exhausted.
4. For anything wrong, surprising, or wasteful: ask "why" five times. Do not accept the first causal explanation. Each "why" peels back a layer of assumption until you reach a structural root cause.
5. Let the observation dictate the action. If the intervention doesn't feel obvious and inevitable given what you saw, you haven't observed long enough. Go back to step 3.
6. After acting, return and observe again. Verify reality changed as expected. The new state becomes the baseline for the next cycle.

**Anti-pattern:** Conference Room Kaizen — analyzing dashboards, reading reports, brainstorming solutions, and implementing changes without ever having observed the actual system long enough to see what the data cannot show you.

**Hard rule:** No action before observation. No observation from a distance. No theory unchecked against the floor.

---

## The Book  ← depth zone (always at the bottom)

### The Pattern

Taiichi Ohno's defining cognitive move was not waste elimination, not kanban, not just-in-time. Those are outputs. The upstream move that generated all of them was the same: he forced prolonged, unfiltered contact with reality before allowing any action. He refused to let anyone act, theorize, or solve until observation was complete. The Ohno Circle, the Five Whys, genchi genbutsu — all implementations of one principle: destroy your preconceptions, observe until reality dictates the action, then act.

### Protocol (extended)

1. **Go to the actual place.** Not a conference room. Not a dashboard. Not a report. Stand physically (or trace through code) where the real process occurs. Ohno: "The workplace is a teacher. You can find answers only in the workplace."

2. **Destroy your preconceptions before observing.** Write down what you think is happening, then set it aside. Your job is not to confirm your model. Ohno: "We are doomed to failure without a daily destruction of our various preconceptions."

3. **Observe for far longer than feels necessary — at least 3x longer.** Ohno's engineers stood in chalk circles for 8-hour shifts. You feel done after 20 minutes. Stay. The gap between "looking" and "observing" is time. The important things reveal themselves only after the obvious things have been catalogued and dismissed.

4. **Ask "why" at least five times.** Do not accept the first causal explanation. Each "why" peels back a layer of assumption. A machine bearing fails → why? Overloaded → why? Pump malfunction → why? Dirt in shaft → why? No filter → why? Nobody thought it was needed. Root cause: install a filter. The surface symptom (broken bearing) was four layers above the structural fix.

5. **Let observation dictate the action.** Do not brainstorm. Do not apply frameworks. The intervention should feel obvious given what you observed. If it doesn't, return to step 3.

6. **Act, then observe again.** Implement the change, return to the place, repeat the observation cycle. Ohno: "Where there is no standard there can be no kaizen." The new standard becomes the baseline for the next round.

### Anti-Pattern (extended)

**Conference Room Kaizen:** The team analyzes metrics, reads incident reports, brainstorms solutions on a whiteboard, and ships changes — without anyone having observed the actual system in operation. They solve the wrong problem, or solve the right problem at the wrong layer.

Specific violations:
- **Dashboard diagnosis:** Staring at Grafana instead of reading the actual code path or watching real user behavior. Metrics show *what* happened but not *why*.
- **Premature theorizing:** "I think the problem is X" before observing. Your first theory is almost always wrong — it's a projection of your mental model, not a reading of reality.
- **Shallow root cause:** Accepting the first explanation. The bearing broke, so replace the bearing. The bug crashed, so add a nil check. Both fix symptoms, not causes.
- **Speed over observation:** "We don't have time to investigate, just ship the fix." The fix that skips observation creates the next incident.

### Examples

**The machine shop rearrangement (1947):** When Ohno became manager of Toyota's machine shop, he did not redesign the layout on paper. He observed workers operating single machines and noticed they stood idle during machine cycles. Reality showed him the waste. He rearranged machines in L-shaped configurations so one worker could operate three or four. Workers and managers resisted fiercely — it was called "the abominable Ohno system" for years. But Ohno had seen the idle time with his own eyes, and that observation gave him the conviction to persist through years of resistance.

**The supermarket and kanban (1948–1956):** Ohno observed a structural truth about American supermarkets: customers pull what they need, when they need it, and shelves are restocked accordingly. He transplanted this observed principle into manufacturing — parts are "pulled" by downstream stations, not "pushed" by upstream production schedules. In 1956, he visited American supermarkets in person, confirmed his observations, and formalized the kanban card system. By 1962 it was company-wide.

**The chalk circle (1950s–1970s):** Ohno's most famous practice. He drew a chalk circle on the factory floor and told an engineer: "Stand here. Watch." He returned hours later. "What do you see?" If the answer was superficial, he sent them back. Engineers stood for entire 8-hour shifts. Ohno had usually stood in the same circle the day before, so he could immediately detect whether the engineer had truly observed or merely looked. As one student later realized: "He didn't care about the answers. He was teaching me the questions."

**The Five Whys and the bearing (canonical example):** A machine bearing failed. Most engineers would replace the bearing. Ohno asked why five times. Why did it fail? Overloaded. Why overloaded? Pump malfunctioned. Why? Dirt in the shaft. Why dirt? No filter. Why no filter? Nobody thought it was needed. Root cause: install a filter. The fix was invisible until you refused to accept the surface and kept observing deeper.

### Practitioners

**Taiichi Ohno (1912–1990)**
Industrial engineer who created the Toyota Production System. Ohno's method was not cleverness — it was patience. He forced himself and others into sustained, direct observation of reality until the reality itself dictated the action. Every signature Toyota technique — kanban, the Five Whys, jidoka, multi-machine handling — emerged not from theory but from Ohno standing on factory floors, watching, and refusing to act until he understood. His own words: "Don't look with your eyes, look with your feet. Don't think with your head, think with your hands."

**W. Edwards Deming (1900–1993)**
American statistician who taught Japanese industry that quality comes from understanding variation in actual processes. Deming's insistence on measurement over opinion and his disdain for "management by objective" without process understanding parallel Ohno's observation-first method. Deming called it "profound knowledge" — understanding the system as it actually operates, not as you wish it would.

### Historical Events

**Toyota Machine Shop Rearrangement (1947)**
Ohno's first major application. He observed idle time that no one else had bothered to see, then reorganized the physical layout to eliminate it. The resistance was fierce — workers and unions fought multi-machine handling for years. But Ohno's conviction came from observation, not theory, and he outlasted the resistance.

**Kanban System Deployment (1948–1962)**
The pull-production system that revolutionized manufacturing originated from Ohno observing how supermarket shelves were restocked. He did not invent it from engineering theory — he observed a working system in a different domain and transplanted the principle. Observation across domains is still observation.

**Chalk Circle Engineer Training (1950s–1970s)**
Ohno used the chalk circle as a pedagogical tool for decades. It was not a technique for finding specific problems — it was a method for training the cognitive habit of sustained observation. Engineers who survived the chalk circle became the core team that spread TPS globally.

### Lineage

Sakichi Toyoda's automatic loom (1896, machine stops on thread break — observation built into the machine) → Kiichiro Toyoda's quality-first production (1930s) → Taiichi Ohno's chalk circle and genchi genbutsu (1947–1970) → Toyota Production System global deployment (1970s–80s) → "The Machine That Changed the World" (1990, Lean manufacturing enters Western vocabulary) → Lean startup / gemba walks / modern engineering observability practices (2000s–present)

### Origin

Taiichi Ohno formalized the practice at Toyota beginning in 1947, but the principle is older than manufacturing. The Japanese concept of *genchi genbutsu* (現地現物) — "go to the actual place and see the actual thing" — predates Ohno. What Ohno added was the *discipline of duration*: not just visiting the floor, but standing there until reality spoke. The chalk circle was his forcing function — a physical constraint that prevented you from leaving until you had truly observed.

Ohno's own writing makes the hierarchy explicit: "Data is of course important in manufacturing, but I place the greatest emphasis on facts." Data is abstracted. Facts are observed. The distinction is the entire pattern.
