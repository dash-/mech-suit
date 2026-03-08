---
name: Normalize
shorthand: normalize
category: strategy
tags: []
summary: The agent maps diverse representations to a single canonical form early in the pipeline, eliminating branching and surprise for all downstream logic.
composes_with: [compose, collapse, cache]
opposes: []
---

# Normalize (`normalize`)

When this macro is invoked, the agent maps diverse representations — formats, naming conventions, structures — to a single canonical form early in the pipeline. All downstream logic handles only one shape, eliminating branching and surprise. The agent preserves the original when the transformation is lossy, but all processing operates on the normalized version.

## Examples

TODO: Add concrete examples from real usage.
