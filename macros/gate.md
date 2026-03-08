---
name: Gate
shorthand: gate
category: strategy
tags: []
summary: The agent evaluates a precondition and either allows progress or blocks it — gates are binary with no middle ground or workarounds for unmet requirements.
composes_with: [verify, isolate, escalate]
opposes: []
---

# Gate (`gate`)

When this macro is invoked, the agent evaluates a precondition and either allows progress (pass) or blocks it (halt). There is no middle ground — gates are binary. The agent does not attempt workarounds for unmet requirements. Gates enforce invariants at transition points, not after the fact.

## Examples

TODO: Add concrete examples from real usage.
