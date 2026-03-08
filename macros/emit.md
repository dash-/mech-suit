---
name: Emit
shorthand: emit
category: strategy
tags: [communication, monitoring]
summary: The agent produces structured, observable signals about internal state or progress as a non-blocking side channel.
composes_with: [verify, escalate, refine]
opposes: []
---

# Emit (`emit`)

When this macro is invoked, the agent produces structured, observable signals about internal state or progress — logs, progress indicators, intermediate results — as a side channel. Emission is non-blocking: it does not wait for acknowledgment and does not alter control flow. It makes the agent's reasoning or progress legible to supervisors without requiring interruption.

```
System event (idle, permission prompt, completion, error)
  → Hook fires → Notification sent (Slack, email, push)
  → Main workflow continues (does NOT block)
```

## Decision Tree

- Which events trigger emissions? (Be selective — alert fatigue is real)
- Which channel? (Slack for urgent, email for digest, push for critical, log for audit)
- Escalation: if emission is ignored for X time, escalate?

## When to Use

- Humans need awareness of system state but shouldn't gate every action
- Long-running processes where humans check in periodically
- Error conditions that need human attention but not immediate action

## Tradeoffs

- **Pro:** Humans stay informed without being a bottleneck
- **Pro:** Cheap — no workflow interruption
- **Con:** Notifications can be ignored or lost
- **Con:** Too many emissions → alert fatigue → signals get ignored

## Examples

TODO: Add concrete examples from real usage.
