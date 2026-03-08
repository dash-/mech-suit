---
name: Emit
shorthand: emit
category: strategy
tags: []
summary: The agent produces structured, observable signals about internal state or progress as a non-blocking side channel, making reasoning legible without requiring interruption.
composes_with: [verify, escalate, refine]
opposes: []
---

# Emit (`emit`)

When this macro is invoked, the agent produces structured, observable signals about internal state or progress — logs, progress indicators, intermediate results — as a side channel. Emission is non-blocking: it does not wait for acknowledgment and does not alter control flow. It makes the agent's reasoning or progress legible to supervisors without requiring interruption.

## Examples

TODO: Add concrete examples from real usage.
