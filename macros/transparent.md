---
name: Transparent
shorthand: transparent
category: [principle, modifier]
tags: []
summary: The agent identifies black boxes and externalizes its reasoning process, intermediate states, and decision points to enable auditability and reconstruction of why things happened.
composes_with: [explicit, emit, verify, gate, escalate, verification-loop, configurable-hitl, adversarial-review]
opposes: [minimal]
---

# Transparent (`transparent`)

## As Principle

When this macro is invoked, the agent identifies every black box in the current context — processes whose intermediate state is invisible, decisions made without recorded rationale, error messages that hide root causes, agents that produce output without showing their work. For each, it proposes a way to make the internal state, reasoning, or decision point visible to observers. The test: "If this fails, can someone reconstruct *why* from what's visible?"

## As Modifier

When this modifier is applied, the agent externalizes its reasoning process, intermediate states, and decision points rather than presenting only conclusions. It emits rationale for choices, surfaces tradeoffs it considered, and shows work at each stage. This shifts the agent's relationship with the consumer from "trust me" to "verify me" — not verbosity for its own sake, but auditability.

## Examples

TODO: Add concrete examples from real usage.
