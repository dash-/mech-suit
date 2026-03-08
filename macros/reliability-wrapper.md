---
name: Reliability Wrapper
shorthand: reliability-wrapper
category: pattern
tags: [reliability]
summary: **Cascade & Fallback** → **Watchdog** → **Configurable HITL**
composes_with: []
opposes: []
---

# Reliability Wrapper (`reliability-wrapper`)

**Tags:** `reliability`

**Cascade & Fallback** → **Watchdog** → **Configurable HITL**

Try primary approach, fall back if needed, monitor for anomalies, let humans intervene.

**When to use:**
- The system must produce *some* output even when components fail
- Autonomous operation over extended periods
- Hard constraints (budget, time, safety) that must not be exceeded

## Examples

TODO: Add concrete examples from real usage.
