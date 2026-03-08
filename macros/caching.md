---
name: Caching
shorthand: caching
category: pattern
tags: [cost]
summary: 'Cache expensive results and reuse them when inputs haven''t changed.'
composes_with: []
opposes: []
---

# Caching (`caching`)

**Tags:** `cost`

Cache expensive results and reuse them when inputs haven't changed. Use hashing, timestamps, or diff detection to identify what's new, and only recompute the delta.

```
Request → Check cache (hash/timestamp) → Hit → Return cached result
                                        → Miss → Compute → Store in cache → Return
```

**When to use:**
- Operations are expensive (LLM calls, API calls, computation) and inputs change infrequently
- Iterative systems that re-run on evolving data where most data is unchanged between runs
- Any repeated lookup or computation with stable inputs

**Tradeoffs:**
- **Pro:** Massive cost and time savings on repeated operations
- **Pro:** Makes frequent re-runs practical where full recomputation would be prohibitive
- **Con:** Cache invalidation is hard — dependencies between items can mean a change in one invalidates others
- **Con:** Stale caches silently return wrong results if invalidation logic is buggy

**Key decisions:**
- Change detection: content hash? timestamp? git diff?
- Storage: local files? database? in-memory?
- Invalidation scope: just the changed item, or its dependents too?
- TTL: time-based expiry, or purely change-driven?

## Examples

TODO: Add concrete examples from real usage.
