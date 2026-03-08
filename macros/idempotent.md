---
name: Idempotent
shorthand: idempotent
category: [principle, modifier]
tags: []
summary: The agent examines every operation for accumulated side effects on re-run and ensures that running the operation multiple times produces the same result as running it once.
composes_with: [fail-fast, reversible, non-destructive, cache, compose, gate, caching, verification-loop]
opposes: [speculative]
---

# Idempotent (`idempotent`)

## As Principle

When this macro is invoked, the agent examines every operation and asks: "What happens if this runs again right now?" It flags operations that accumulate side effects on re-run — duplicate records, appended-not-replaced content, repeated notifications, migrations that break if executed twice. For each violation, the agent proposes a guard or restructuring that makes repeated execution safe.

## As Modifier

When this modifier is applied, the agent ensures that running the operation multiple times produces the same result as running it once. No double-writes, no duplicated side effects, no accumulated drift. State checks happen before mutations — "is this already done?" always precedes "do this." This changes how the agent handles retries, error recovery, and concurrent execution.

## Decision Tree

```
How should idempotency be achieved?
  A. Check-before-write (skip if already applied)
  B. Upsert (insert or update, never duplicate)
  C. Deterministic key (same input always maps to same identity)
  D. Replace-not-append (overwrite the whole target each time)
```

## Examples

TODO: Add concrete examples from real usage.
