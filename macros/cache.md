---
name: Cache
shorthand: cache
category: strategy
tags: []
summary: The agent checks for a valid prior result before performing an expensive operation, returning cached values when available and invalidating stale entries when inputs change.
composes_with: [collapse, normalize, verify]
opposes: []
---

# Cache (`cache`)

When this macro is invoked, the agent checks for a valid prior result before performing an expensive operation. If one exists, it returns the cached value. If not, it performs the operation and stores the result. The agent maintains cache validity — when inputs change, it invalidates stale entries rather than serving outdated results.

## Decision Tree

- Cache in memory, filesystem, or external store?
- Invalidate by TTL, content hash, or explicit signal?

## Examples

TODO: Add concrete examples from real usage.
