---
name: Defer
shorthand: defer
category: strategy
tags: []
summary: The agent registers that work could be done but postpones execution until a consumer demands the result, avoiding wasted computation on paths that may never be taken.
composes_with: [isolate, gate, cache]
opposes: [collapse]
---

# Defer (`defer`)

When this macro is invoked, the agent registers that work could be done but postpones execution until a consumer actually demands the result. This avoids wasted computation on paths that may never be taken. The agent ensures preconditions are still valid at execution time, not just at registration time — a deferred action that fires against stale state is a bug.

## Decision Tree

- Defer until first access (lazy), until explicit trigger (event-driven), or until a batch boundary (bulk)?

## Examples

TODO: Add concrete examples from real usage.
