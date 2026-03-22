---
name: time-and-motion
aliases: [taylor-method, one-best-way, scientific-management, work-decomposition]
domain: [engineering, systems]
trigger: [optimize process, improve throughput, reduce waste, standardize workflow, why is this slow]
practitioners:
  - name: Frederick Winslow Taylor
    era: 1874-1915
    application: Invented scientific management — decomposed factory work into timed motions to find the provably fastest method
  - name: Frank and Lillian Gilbreth
    era: 1885-1924
    application: Extended Taylor's method with motion-capture photography, reducing bricklaying from 18 motions to 5
  - name: W. Edwards Deming
    era: 1950-1993
    application: Applied measurement-driven process control to Japanese manufacturing, adding statistical rigor to Taylor's stopwatch
events:
  - name: Bethlehem Steel pig-iron experiment
    year: 1899
    gem-role: applied — Taylor measured shoveling pig iron, found workers moved 12.5 tons/day using habit; redesigned the sequence to 47.5 tons/day with less fatigue by timing rest intervals and motion paths
    practitioner: Frederick Winslow Taylor
    outcome: Taylor's time-and-motion studies at Bethlehem Steel increased worker output from 12.5 to 47.5 tons per day while reducing the workforce from 600 to 140 and saving the yard $78,000/year (~$2.8M today); his Principles of Scientific Management (1911) became one of the most influential management books of the 20th century.
  - name: Resistance at Watertown Arsenal
    year: 1911
    gem-role: violated — Taylor applied time studies to skilled machinists without their input; the resulting worker revolt led to a Congressional investigation, showing the pattern fails when it treats humans as interchangeable machine parts
    practitioner: Frederick Winslow Taylor
    outcome: Workers struck and Congress investigated, temporarily banning stopwatch studies in government work; the episode demonstrated that time-and-motion analysis applied without worker input or consent generates organized resistance that destroys the efficiency gains the method was designed to produce.
  - name: Gilbreth bricklaying study
    year: 1909
    gem-role: applied — Frank Gilbreth filmed bricklayers, decomposed the task into atomic motions, eliminated 13 of 18 movements, tripled output per worker
    practitioner: Frank Gilbreth
    outcome: Gilbreth's micromotion studies reduced bricklaying from 18 movements to 5 and tripled output per worker; his therbligs (fundamental motion elements) became the standard vocabulary for motion analysis and the direct ancestor of ergonomics and industrial engineering as formal disciplines.
lineage: Taylor-1880s → Gilbreths-1910s → Deming-1950s → Toyota Production System-1960s
origin-earliest: Taylor-1881
origin-modern: Taylor-1911
---

# Time-and-Motion

## Protocol

**Trigger:** You need to make an existing process faster or cheaper, and no one has measured where the time actually goes.
**Steps:**
1. **Decompose** — break the process into the smallest observable units of work (individual motions, function calls, pipeline stages).
2. **Measure each unit** — time every atomic step independently. Record, don't estimate. The stopwatch is the authority, not intuition.
3. **Identify the waste** — flag motions that move nothing closer to done: unnecessary travel, idle waits, redundant handling, context switches.
4. **Reassemble the one best way** — recompose only the value-adding steps into a new sequence. Optimize the order. Standardize it.
5. **Set the standard and iterate** — publish the new method as the baseline. Measure again. The standard is a floor, not a ceiling.
**Anti-pattern:** Optimizing by intuition — rearranging steps based on what *feels* slow instead of what *measures* slow. The bottleneck is almost never where you think it is.
**Hard rule:** Measure before you move. No redesign without data.

---

## The Book

### The Pattern

Taylor's defining move was to refuse to improve anything until he had measured everything. Where others saw "work" as a single blob, Taylor saw a sequence of discrete, timeable motions — and he insisted that the right sequence was not a matter of opinion but of measurement. Decompose, measure, eliminate, recompose. The genius was not in any single optimization but in the discipline of making the invisible visible before touching it.

### Protocol (extended)

1. **Decompose** — Walk the process end to end. Write down every discrete action. If an action can be split further, split it. You want the atoms, not the molecules. In software: trace the request path; in manufacturing: film the workstation; in knowledge work: log every task switch for a day.

2. **Measure each unit** — Attach a number to each atom. Wall-clock time is the primary metric, but also note: wait time vs. active time, distance traveled, handoffs between actors. Repeat measurements across multiple cycles to get stable averages. Taylor used a stopwatch and a clipboard. Use whatever instrument gives you ground truth.

3. **Identify the waste** — Classify each atom: does it move the product closer to done, or does it exist because "that's how we've always done it"? Common waste categories: unnecessary motion, waiting, overprocessing, transport, rework. The ratio of value-adding to non-value-adding time is usually shocking — Taylor routinely found 60-80% waste in "optimized" processes.

4. **Reassemble the one best way** — Take only the value-adding atoms. Reorder them for minimum transition cost. Where two steps can be parallelized, parallelize. Where a tool change eliminates a motion, change the tool. The output is a specific, repeatable sequence — not guidelines, but a protocol.

5. **Set the standard and iterate** — The new method becomes the documented standard. Train everyone on it. Then measure again, because the new sequence will reveal its own waste layer. Each cycle compresses further. Standards are living documents.

### Anti-Pattern (extended)

**Gut-feel optimization**: A manager watches a process, decides step 7 "looks slow," and redesigns it. Meanwhile step 3 — which takes 3x longer but happens behind a wall — goes untouched. Without measurement, optimization effort flows to the most *visible* problem, not the most *expensive* one.

**Premature automation**: Automating a bad process makes it fail faster. Taylor's insight was that you must find the right sequence *before* you invest in making it permanent. This is why the musk-filter pattern starts with "question the requirement" — but Taylor's contribution is the specific method for what comes after: once you've decided the work must be done, how do you find the best way to do it?

**Dehumanization failure**: Taylor's method works on motions, not on people. When applied without worker input or treated as a way to extract maximum labor rather than eliminate unnecessary labor, it produces revolt (Watertown Arsenal, 1911). The pattern optimizes the *method*; it does not optimize the *human* into a machine.

### Examples

**Bethlehem Steel, 1899**: Taylor studied pig-iron handlers who loaded 12.5 long tons per day. He decomposed the work: pick up pig, walk to railcar, set it down, walk back. He timed each segment, experimented with load weights, rest intervals, and walking paths. Result: 47.5 tons/day with *scheduled rest breaks* — the workers were less tired because wasted motion was eliminated and rest was scientifically timed rather than ad hoc.

**Gilbreth bricklaying, 1909**: Frank Gilbreth filmed bricklayers and decomposed the task into 18 distinct motions. He found that 13 of them — bending to pick up bricks, turning them to find the good side, tapping them into place — could be eliminated by redesigning the scaffold (adjustable height), pre-sorting bricks (good side up), and pre-buttering mortar. Output tripled. The remaining 5 motions were the minimum necessary to lay a brick.

**Watertown Arsenal, 1911**: When Taylor's disciples applied time studies to skilled machinists at a government arsenal without consultation, workers saw it as surveillance and speedup. They struck. Congress investigated and temporarily banned stopwatch studies in government work. The failure was not in the method but in its application: treating measurement as control rather than as a tool for finding better methods collaboratively.

### Practitioners

**Frederick Winslow Taylor (1856-1915)**: A mechanical engineer who spent his career in steel mills, Taylor became obsessed with the question: "What is the fastest way to do this specific task?" He developed time study as a formal method at Midvale Steel in the 1880s, published *The Principles of Scientific Management* in 1911, and spent his later years consulting and lecturing. His work is the direct ancestor of industrial engineering, operations research, and modern process optimization.

**Frank and Lillian Gilbreth (1868-1924 / 1878-1972)**: The Gilbreths refined Taylor's methods by adding motion photography and ergonomic analysis. Frank started as a bricklayer and brought a practitioner's eye; Lillian brought psychology and insisted that motion study serve the worker, not just the output. Their synthesis — therbligs (fundamental motion elements) — became the standard vocabulary for motion analysis.

**W. Edwards Deming (1900-1993)**: Deming took Taylor's measurement-first instinct and added statistical process control. Where Taylor measured individual tasks, Deming measured variation across the entire system. His work in post-war Japan — teaching Toyota and others to measure everything and reduce variation — is a direct lineage from Taylor's stopwatch to modern lean manufacturing.

### Historical Events

**Midvale Steel, 1881-1889**: Taylor's first systematic time studies. Working as a gang boss, he noticed that workers deliberately slowed output ("soldiering") because there was no agreed standard for a fair day's work. His response: measure what was physically possible, set the standard from data, and pay a premium for meeting it. This was the birth of scientific management.

**Bethlehem Steel, 1898-1901**: Taylor's most famous experiments. Beyond pig-iron, he studied the "science of shoveling" — discovering that the optimal shovel load was 21 pounds, and that providing different-sized shovels for different materials (instead of one shovel for everything) reduced the labor force from 600 to 140 while increasing output. The yard saved $78,000/year (≈$2.8M today).

**Congressional Hearings, 1912**: Following the Watertown Arsenal strike, the House held hearings on "Taylor and Other Systems of Shop Management." Taylor testified for three days. The hearings exposed the tension between scientific management as a tool (finding better methods) and scientific management as an ideology (maximum extraction). Taylor himself insisted the goal was mutual prosperity, but the damage was done — organized labor opposed time study for decades.

### Lineage

**Origin**: Taylor at Midvale Steel, 1881 — first systematic stopwatch studies of factory work.

**Transmission**: Taylor → Gilbreths (added motion capture and ergonomics, 1910s) → Henry Gantt (added scheduling and visual management, 1910s) → Industrial Engineering as a discipline (1920s) → Deming and Shewhart (added statistical process control, 1930s-50s) → Taiichi Ohno at Toyota (synthesized Taylor's measurement with Ford's flow and Deming's statistics, 1950s-60s) → modern lean/agile/DevOps (1990s-present).

The irony of Taylor's legacy: his name is associated with dehumanizing factory work, but his core method — measure before you optimize — is the foundation of every modern performance discipline from software profiling to clinical process improvement.

### Origin

Frederick Winslow Taylor began his time studies in 1881 at Midvale Steel Company in Philadelphia. As a newly promoted gang boss, he faced workers who deliberately limited output. Rather than argue about what was fair, he decided to measure what was possible. He broke each task into timed components, experimented with variables (tool shape, rest intervals, motion sequence), and derived standards from data.

His 1911 book *The Principles of Scientific Management* codified the method and became one of the most influential management texts ever published. The core idea — that there is "one best way" to perform any task, discoverable through measurement and experiment — was revolutionary in an era when craft knowledge was oral, proprietary, and unquestioned. Taylor made work legible, and in doing so, made it improvable.
