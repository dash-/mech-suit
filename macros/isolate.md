---
name: Isolate
shorthand: isolate
category: strategy
tags: []
summary: The agent sets up boundaries — sandboxes, scoped permissions, or working copies — so that a risky or uncertain operation cannot affect anything outside its designated area.
composes_with: [delegate, gate, defer]
opposes: []
---

# Isolate (`isolate`)

When this macro is invoked, the agent sets up boundaries — sandboxes, scoped permissions, or working copies — so that a risky or uncertain operation cannot affect anything outside its designated area. Isolation is applied before the risky action, not as cleanup after. If the operation fails, damage is contained to the isolated scope.

## Decision Tree

- Isolate by process boundary, filesystem copy, or permission scope?

## Examples

TODO: Add concrete examples from real usage.
