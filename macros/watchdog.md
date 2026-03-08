---
name: Watchdog & Circuit Breaker
shorthand: watchdog
category: pattern
tags: [monitoring, reliability]
summary: A monitoring agent observes system behavior in real time, watching for anomalies, runaway costs, or safety violations.
composes_with: [configurable-hitl, notification-hooks, provenance]
opposes: []
---

# Watchdog & Circuit Breaker (`watchdog`)

**Tags:** `monitoring` `reliability`

A monitoring agent observes system behavior in real time, watching for anomalies, runaway costs, or safety violations. When a threshold is crossed, execution halts and a human is alerted.

```
System Running → Watchdog monitors (cost, time, quality, safety)
             → Normal → Continue
             → Anomaly → Circuit breaker → Halt + Alert Human
```

**When to use:**
- System runs autonomously for extended periods
- Hard constraints (budget, time) must not be exceeded
- Failure modes include runaway loops or cascading errors

**What to monitor:**
- Cost burn rate (are we spending faster than planned?)
- Output quality trends (are results degrading?)
- Agent error rates (is something failing repeatedly?)
- Time per step (is something hanging?)
- Safety signals (did the ethics agent flag something concerning?)

**Key decisions:**
- Threshold calibration: too sensitive = false alarms, too lax = missed problems
- Recovery: can the system resume after tripping, or must a human restart?

**Notes:** Pairs with **Notification Hooks** (alert humans on circuit break), **Configurable HITL** (human decides whether to resume), and **Provenance** (anomaly events feed the audit trail).


**Additional trigger types:**
- **Drift detection** — Monitor for degradation in agent performance over time due to changes in input data distribution or environmental shifts. Sustained quality decline triggers investigation, not just single anomalies
- **Before-tool callbacks** — Proactive parameter validation before tool execution (e.g., verifying user permissions, checking argument bounds). Prevents bad tool calls rather than detecting their aftermath
- **LLM-based overseer** — A separate, lightweight LLM monitors the primary agent's event stream and call graph for behavioral anomalies (loops, stagnation, off-task drift). More nuanced than threshold-based rules

## Examples

TODO: Add concrete examples from real usage.
