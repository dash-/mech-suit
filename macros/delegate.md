---
name: Delegate
shorthand: delegate
category: strategy
tags: []
summary: The agent identifies work outside its core responsibility and passes it to a specialist with only the authority and context needed for that sub-task.
composes_with: [decompose, isolate, gate]
opposes: [escalate]
---

# Delegate (`delegate`)

When this macro is invoked, the agent identifies work that falls outside its core responsibility or optimal scope and passes it to a specialist with only the authority and context needed for that sub-task. It defines the interface clearly — inputs, expected outputs, constraints — and reclaims control when the delegate returns.

## Decision Tree

- Delegate to subagent, external service, or human?
- Pass full context or minimal context (need-to-know)?

## Examples

TODO: Add concrete examples from real usage.
