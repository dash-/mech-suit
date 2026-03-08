---
name: Rate Limiting & Backpressure
shorthand: rate-limiting
category: pattern
tags: [cost, reliability, coordination]
summary: Govern the rate at which agents spawn subagents, make tool calls, or hit external APIs.
composes_with: [budget-aware-execution, watchdog]
opposes: []
---

# Rate Limiting & Backpressure (`rate-limiting`)

**Tags:** `cost` `reliability` `coordination`

Govern the rate at which agents spawn subagents, make tool calls, or hit external APIs. When the system produces work faster than downstream consumers can handle, backpressure signals slow the producer. Prevents runaway parallelism, API rate limit errors, and resource exhaustion.

```
Orchestrator spawns subagents
  → Concurrency limiter: max N in flight
  → Queue: excess work waits
  → Backpressure: if queue exceeds threshold, orchestrator slows down or stops spawning

External API calls
  → Rate limiter: max M calls per second
  → Retry with backoff on 429/throttle
  → Circuit break if sustained throttling
```

**When to use:**
- The system makes external API calls with rate limits (LLM APIs, search APIs, tool integrations)
- An orchestrator can spawn many parallel subagents, risking resource exhaustion
- Downstream systems (databases, services) have throughput limits
- You want predictable, sustainable execution rather than bursts followed by throttling

**Tradeoffs:**
- **Pro:** Prevents 429 errors, API bans, and resource exhaustion
- **Pro:** Smoother, more predictable execution — easier to monitor and budget
- **Pro:** Backpressure signals are useful information (system is overloaded → adjust plan)
- **Con:** Limits throughput — tasks that could parallelize heavily are artificially slowed
- **Con:** Queue management adds complexity (priority ordering, starvation prevention)

**Key decisions:**
- Concurrency limit: fixed N? adaptive based on error rate? per-resource?
- Backpressure strategy: queue and wait? drop low-priority work? alert human?
- Rate limit awareness: hardcoded? discovered from API response headers? adaptive?

**Notes:** Pairs with **Budget-Aware Execution** (budget governs total spend, rate limiting governs spend *velocity*) and **Watchdog** (monitor for sustained throttling as an anomaly signal).

## Examples

TODO: Add concrete examples from real usage.
