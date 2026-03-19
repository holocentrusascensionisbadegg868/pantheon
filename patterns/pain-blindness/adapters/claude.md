---
name: pain-blindness
description: Detect when a user is tolerating a fragmented, painful workflow that could be collapsed into an integrated solution. Trigger on phrases like "it's always been this way", "everyone hates this but", "we've always done it like this", or when describing a multi-step process with obvious seams between systems.
---

# Pain Blindness — Claude Code Adapter

## When to invoke
- User describes a workflow with multiple handoffs between tools, systems, or manual steps
- User says "it's always been this way" or "everyone just deals with it"
- User is building a point solution that optimizes one fragment of a clearly broken chain
- User's codebase reveals fragmented experience paths with visible seams

## Protocol

1. **Name the normalized pain.** State plainly what the user (or their users) have stopped noticing. "You're describing five steps where one would do. The pain is in the handoffs, not the individual steps."

2. **Map the seams.** Identify where the experience crosses boundaries — between services, tools, manual steps, or teams. List them explicitly: "The seam is between X and Y. Nobody owns that transition."

3. **Check readiness.** Before proposing a collapsed solution, verify the components exist. Can the APIs talk to each other? Does the infrastructure support it? If the technology isn't ready, say so — "This is a General Magic situation. The pieces aren't mature yet."

4. **Propose the collapsed stack.** Design an integrated solution that eliminates the handoffs. Don't improve individual steps — remove the boundaries between them. Show what the experience looks like when no seam is visible.

5. **Flag escape hatches.** If the proposed design includes fallbacks to the old fragmented workflow, flag them: "This escape hatch will prevent adoption. Users will take the familiar path every time."

## Anti-pattern
Do not optimize individual fragments while leaving seams intact. If a user asks you to "make step 3 faster," check whether steps 1-5 should exist as separate steps at all.

## Hard rule
Never propose collapsing a stack when the underlying components aren't ready. Premature integration is worse than fragmentation — it creates a brittle system that fails at every seam it tried to hide.
