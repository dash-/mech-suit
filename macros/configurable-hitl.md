---
name: Configurable Human-in-the-Loop
shorthand: configurable-hitl
category: pattern
tags: [coordination, reliability]
summary: System defines checkpoints where human review may be required.
composes_with: []
opposes: []
---

# Configurable Human-in-the-Loop (`configurable-hitl`)

**Tags:** `coordination` `reliability`

System defines checkpoints where human review may be required. Level of involvement is configurable along a spectrum. Set at engagement start, adjustable during execution.

```
Action → Checkpoint → Check config
  → Level 1 (Full Approval): Block until human approves
  → Level 2 (Supervised): Notify, auto-proceed after timeout
  → Level 3 (Autonomous): Log and proceed
```

**When to use:**
- Different users/clients have different risk tolerances
- Trust builds over time
- Regulatory requirements vary by domain

**Tradeoffs:**
- **Pro:** One system serves cautious to autonomous
- **Pro:** Trust builds naturally — start Level 1, graduate to Level 3
- **Con:** Must design for all levels (more complex)
- **Con:** Level 2 timeout can be dangerous if humans aren't actually monitoring

**Non-configurable:** Emergency stop. Always available. Every level.


**Variants:**
- **Plan approval checkpoint** — Human reviews and approves the agent's plan before execution begins, then the agent runs autonomously within the approved plan
- **Human-on-the-Loop** — Humans set policy constraints and guardrails; the agent executes autonomously within those bounds without per-action approval. Distinct from Level 3 (Autonomous) because the human actively designs the policy, not just disengages. Examples: trading rules that bound agent behavior, call-routing policies that define escalation criteria

## Examples

TODO: Add concrete examples from real usage.
