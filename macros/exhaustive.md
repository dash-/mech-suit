---
name: Exhaustive
shorthand: exhaustive
category: modifier
tags: []
summary: The agent optimizes for coverage over speed, enumerating the full input space and using systematic search rather than heuristic sampling.
composes_with: [verify, decompose, verification-loop, adversarial-review]
opposes: [incremental, lazy]
---

# Exhaustive (`exhaustive`)

When this modifier is applied, the agent optimizes for coverage over speed. It enumerates the full input space before acting, tracks what has been visited, and uses systematic search rather than heuristic sampling. When exhaustive coverage is infeasible, the agent must flag this and propose bounded alternatives rather than silently sampling.

## Examples

TODO: Add concrete examples from real usage.
