---
name: Checkpoint & Resume
shorthand: checkpoint-resume
category: pattern
tags: [reliability]
summary: The ability to save system state, pause, and resume later.
composes_with: []
opposes: []
---

# Checkpoint & Resume (`checkpoint-resume`)

**Tags:** `reliability`

The ability to save system state, pause, and resume later. Critical for processes that span hours or days (e.g., waiting for a 24-hour test cycle to complete).

**When to use:**
- The process spans hours or days (e.g., waiting for external test cycles)
- Human reviewers may take significant time to approve intermediate results
- System failures are possible and accumulated state is expensive to recompute
- You want humans to be able to pause, inspect, adjust, and resume

**What to checkpoint:**
- Current hypothesis states (priors/posteriors)
- Budget spent and remaining
- Wave history and results
- Pending decisions and their context
- HITL approval states

**Tradeoffs:**
- **Pro:** Process survives across sessions, crashes, and human delays
- **Pro:** Enables "pause and think" — human can intervene, adjust, resume
- **Con:** Checkpoint format must be versioned — schema changes can break resumability
- **Con:** Resuming from stale state can produce inconsistent results if the world changed while paused

**Key decisions:**
- Storage format: JSON files? database records? git commits?
- Checkpoint frequency: every step? every N steps? at HITL gates only?
- Staleness detection: how do you know if the world changed since the checkpoint was saved?

## Examples

TODO: Add concrete examples from real usage.
