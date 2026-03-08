---
name: Don't Repeat Yourself
shorthand: DRY
category: principle
tags: []
summary: Identify every instance where the same knowledge exists in more than one place and propose collapsing each duplication to a single authoritative source.
composes_with: [composable, SoC, collapse]
opposes: [generate]
---

# Don't Repeat Yourself (`DRY`)

When this macro is invoked, the agent identifies every instance where the same knowledge exists in more than one place. It flags duplicated logic, copy-pasted text, parallel structures that will drift, and any spot where a change in one location demands a corresponding change elsewhere. The agent then proposes how to collapse each duplication to a single authoritative source.

## Decision Tree

```
How should the duplication be eliminated?
  A. Abstraction (extract shared logic into a function, module, or component)
  B. Configuration (single config source referenced by all consumers)
  C. Generation (one source template that produces the variants)
  D. Reference (replace copies with pointers to a canonical location)
```

## Examples

TODO: Add concrete examples from real usage.
