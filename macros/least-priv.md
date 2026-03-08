---
name: Least Privilege
shorthand: least-priv
category: principle
tags: []
summary: Audit every permission grant, scope, and capability in the current context and propose the minimum viable permission for each.
composes_with: [SoC, scoped, delegate]
opposes: []
---

# Least Privilege (`least-priv`)

When this macro is invoked, the agent audits every permission grant, scope, and capability in the current context. It flags overly broad permissions, god-objects that can touch everything, API tokens with unnecessary scopes, agents with write access when they only need read, and any situation where the blast radius of a mistake is larger than necessary. For each finding, it proposes the minimum viable permission.

## Examples

TODO: Add concrete examples from real usage.
