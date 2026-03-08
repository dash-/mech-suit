---
name: Cache
shorthand: cache
category: strategy
tags: [cost]
summary: The agent checks for a valid prior result before performing an expensive operation, returning cached values when available and invalidating stale entries when inputs change.
composes_with: [collapse, normalize, verify]
opposes: []
---

# Cache (`cache`)

When this macro is invoked, the agent checks for a valid prior result before performing an expensive operation. If one exists, it returns the cached value. If not, it performs the operation and stores the result. The agent maintains cache validity — when inputs change, it invalidates stale entries rather than serving outdated results.

```
Request → Check cache (hash/timestamp) → Hit → Return cached result
                                        → Miss → Compute → Store in cache → Return
```

## Decision Tree

- Cache in memory, filesystem, or external store?
- Invalidate by TTL, content hash, or explicit signal?
- Invalidation scope: just the changed item, or its dependents too?

## When to Use

- Operations are expensive (LLM calls, API calls, computation) and inputs change infrequently
- Iterative systems that re-run on evolving data where most data is unchanged between runs
- Any repeated lookup or computation with stable inputs

## Tradeoffs

- **Pro:** Massive cost and time savings on repeated operations
- **Pro:** Makes frequent re-runs practical where full recomputation would be prohibitive
- **Con:** Cache invalidation is hard — dependencies between items can mean a change in one invalidates others
- **Con:** Stale caches silently return wrong results if invalidation logic is buggy

## Examples

TODO: Add concrete examples from real usage.
