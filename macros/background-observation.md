---
name: Background Observation
shorthand: background-observation
category: pattern
tags: [learning, monitoring]
summary: Non-blocking data collection decoupled from analysis.
composes_with: [confidence-signaling, memory-retrieval, scoped-promotion]
opposes: []
---

# Background Observation (`background-observation`)

**Tags:** `learning` `monitoring`

Non-blocking data collection decoupled from analysis. Hooks or event listeners write observations to a queue (JSONL file, event stream, database). A separate background agent processes the queue asynchronously. The main workflow is never slowed by observation.

```
Main Workflow (uninterrupted)
  │
  ├─ PreToolUse hook → writes to observations.jsonl
  ├─ PostToolUse hook → writes to observations.jsonl
  │
  └─ (continues working, zero latency impact)

Background Observer (async, low-cost model)
  │
  ├─ Reads observations.jsonl periodically
  ├─ Detects patterns, errors, user corrections
  └─ Creates learnings → feeds into Memory & Retrieval
```

**Different from Watchdog:** **Watchdog** monitors for anomalies and *halts* execution. **Background Observation** passively collects data for *learning*. Watchdog is a safety mechanism; Background Observation is a learning mechanism.

**When to use:**
- You want the system to learn from its own behavior without slowing down
- Observation collection must be cheap and non-blocking
- Analysis can happen later (seconds, minutes, or end-of-session)

**Tradeoffs:**
- **Pro:** Zero performance impact on the main workflow
- **Pro:** Can capture 100% of interactions (hooks are reliable)
- **Pro:** Background analysis can use cheaper models (Haiku) since it's not latency-sensitive
- **Con:** Observations queue can grow large if not processed regularly
- **Con:** Learning is delayed — patterns aren't available until the background agent processes them
- **Con:** Queue format must be stable and parseable

**Notes:** Feeds into **Memory & Retrieval** (observations become memories), **Scoped Promotion** (learnings start project-scoped), and **Confidence Signaling** (learnings carry confidence from evidence count).

## Examples

TODO: Add concrete examples from real usage.
