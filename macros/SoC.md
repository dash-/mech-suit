---
name: Separation of Concerns
shorthand: SoC
category: principle
tags: []
summary: Examine each unit and identify any that serve multiple masters, proposing splits such that each resulting piece changes for exactly one reason.
composes_with: [DRY, composable, least-priv, delegate]
opposes: [collapse]
---

# Separation of Concerns (`SoC`)

When this macro is invoked, the agent examines each unit — function, file, agent, document — and identifies any that serve multiple masters. It flags functions that both compute and format, configs that mix deployment and business logic, prompts that conflate instruction with context. For each violation, the agent proposes a split such that each resulting piece changes for exactly one reason.

## Examples

TODO: Add concrete examples from real usage.
