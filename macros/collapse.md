---
name: Collapse
shorthand: collapse
category: strategy
tags: []
summary: The agent walks all dependency chains, inlines referenced content, and resolves variables to produce a flat, self-contained artifact requiring no further resolution.
composes_with: [normalize, verify, cache]
opposes: [defer]
---

# Collapse (`collapse`)

When this macro is invoked, the agent walks all dependency chains, inlines referenced content, and resolves variables or lookups, producing a flat, self-contained artifact that requires no further resolution. The consumer never performs lookups or chases references. If a reference cannot be resolved, the agent fails immediately rather than emitting a broken link.

## Decision Tree

- Resolve via inlining (embed content), compilation (transform to target), or snapshot (freeze current state)?

## Examples

TODO: Add concrete examples from real usage.
