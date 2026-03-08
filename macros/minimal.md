---
name: Minimal Footprint
shorthand: minimal
category: principle
tags: []
summary: Challenge every piece of structure, dependency, and scope, proposing removals or simplifications wherever what exists is merely bigger rather than meaningfully better than the simplest thing that could work.
composes_with: [DRY, SoC, lazy]
opposes: [transparent, composable]
---

# Minimal Footprint (`minimal`)

When this macro is invoked, the agent challenges every piece of structure, dependency, and scope in the current context. It flags premature abstractions, unused parameters, speculative features, dependencies pulled in for a single function, and framework choices that outweigh the problem. For each, it asks: "What is the simplest thing that could work here, and is what we have meaningfully better or just bigger?" It proposes removals or simplifications.

## Decision Tree

```
What kind of excess is being removed?
  A. Unused code/structure (dead code, empty abstractions)
  B. Premature abstraction (generalized before needed — inline it)
  C. Heavyweight dependency (replace with focused alternative or hand-roll)
  D. Speculative scope (features/parameters for futures that haven't arrived)
```

## Examples

TODO: Add concrete examples from real usage.
