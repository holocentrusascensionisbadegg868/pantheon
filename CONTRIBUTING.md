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
