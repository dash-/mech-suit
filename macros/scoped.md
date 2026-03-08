---
name: Scoped
shorthand: scoped
category: modifier
tags: []
summary: The agent establishes an explicit boundary before acting and constrains all subsequent reasoning to that boundary, actively rejecting drift beyond scope.
composes_with: [decompose, delegate, verify, orchestrator-subagent, context-windowing]
opposes: [exhaustive]
---

# Scoped (`scoped`)

When this modifier is applied, the agent establishes an explicit boundary before acting — what files, what time range, what subsystem — and constrains all subsequent reasoning to that boundary. The agent actively rejects drift beyond scope. Discovered dependencies outside the boundary are noted but not pursued; they become inputs for a future scoped pass.

## Examples

TODO: Add concrete examples from real usage.
