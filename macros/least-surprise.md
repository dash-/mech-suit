---
name: Principle of Least Surprise
shorthand: least-surprise
category: principle
tags: []
summary: Audit naming, return values, defaults, and side effects for anything that would confuse a person or system encountering them for the first time without documentation.
composes_with: [explicit, transparent]
opposes: []
---

# Principle of Least Surprise (`least-surprise`)

When this macro is invoked, the agent audits naming, return values, defaults, and side effects for anything that would confuse a person or system encountering them for the first time without documentation. It flags misleading names, return values that violate convention, side effects hidden behind innocent-looking interfaces, and defaults no one would guess. The test: "If someone encountered this cold, what would they expect?"

## Examples

TODO: Add concrete examples from real usage.
