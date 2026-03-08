---
name: Notification Hooks
shorthand: notification-hooks
category: pattern
tags: [communication, monitoring]
summary: Async notifications triggered by system events, separate from the main workflow.
composes_with: []
opposes: []
---

# Notification Hooks (`notification-hooks`)

**Tags:** `communication` `monitoring`

Async notifications triggered by system events, separate from the main workflow. Fire-and-forget awareness signals to humans, not blocking gates. Different from **Configurable HITL** (which blocks execution for approval).

```
System event (idle, permission prompt, completion, error)
  → Hook fires → Notification sent (Slack, email, push)
  → Main workflow continues (does NOT block)
```

**When to use:**
- Humans need awareness of system state but shouldn't gate every action
- Long-running processes where humans check in periodically
- Error conditions that need human attention but not immediate action

**Tradeoffs:**
- **Pro:** Humans stay informed without being a bottleneck
- **Pro:** Cheap — no workflow interruption
- **Con:** Notifications can be ignored or lost
- **Con:** Too many notifications → alert fatigue → notifications get ignored

**Key decisions:**
- Which events trigger notifications? (Be selective — alert fatigue is real)
- Which channel? (Slack for urgent, email for daily digest, push for critical)
- Escalation: if notification is ignored for X time, escalate?

## Examples

TODO: Add concrete examples from real usage.
