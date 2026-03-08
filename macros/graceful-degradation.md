---
name: Graceful Degradation
shorthand: graceful-degradation
category: pattern
tags: [quality, reliability]
summary: When an agent produces a *subtly wrong* result — not a hard failure, but a partial success — the system detects the quality shortfall and degrades gracefully rather than propagating a flawed output or
composes_with: [confidence-signaling, watchdog]
opposes: []
---

# Graceful Degradation (`graceful-degradation`)

**Tags:** `quality` `reliability`

When an agent produces a *subtly wrong* result — not a hard failure, but a partial success — the system detects the quality shortfall and degrades gracefully rather than propagating a flawed output or failing entirely. Different from Cascade & Fallback (which handles hard failures) and Verification Loop (which retries until pass). This pattern accepts that the output is imperfect and chooses the best available response.

```
Agent output → Quality assessment → Full quality? → proceed normally
                                  → Partial quality? → degrade gracefully:
                                      → Use output with caveats/disclaimers
                                      → Use output for low-stakes path only
                                      → Return partial result + flag for human review
                                      → Fall back to cached/stale version
                                  → Unacceptable? → hard fail (Cascade & Fallback)
```

**When to use:**
- Outputs exist on a quality spectrum, not a binary pass/fail
- A partial or caveated result is better than no result
- Downstream consumers can handle varying quality levels
- The system needs to keep running even when some components underperform

**Tradeoffs:**
- **Pro:** System stays available even when quality is imperfect
- **Pro:** Explicit quality signals let downstream consumers adjust their behavior
- **Con:** Silent quality degradation can compound — a "good enough" result used as input produces worse downstream output
- **Con:** Defining the quality spectrum (full/partial/unacceptable) requires domain expertise

**Key decisions:**
- Quality assessment: automated scoring? confidence threshold? domain-specific heuristics?
- Degradation strategy: caveats? scope reduction? human escalation? stale cache?
- Transparency: does the consumer know they're getting a degraded result?

**Notes:** Often works with **Confidence Signaling** (confidence score drives the quality assessment). Pairs with **Watchdog** (track degradation frequency — if it's always degrading, something is wrong).

## Examples

TODO: Add concrete examples from real usage.
