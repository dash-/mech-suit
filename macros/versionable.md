---
name: Versionable
shorthand: versionable
category: modifier
tags: []
summary: The agent treats every meaningful state of the artifact as a version that can be referenced, compared, or restored, reasoning about what constitutes a meaningful change worth versioning.
composes_with: [non-destructive, reversible, incremental, cache, progressive-refinement]
opposes: [lazy]
---

# Versionable (`versionable`)

When this modifier is applied, the agent treats every meaningful state of the artifact as a version that can be referenced, compared, or restored. It must decide on a versioning mechanism, assign version identifiers, and ensure that prior versions remain accessible. The agent reasons about what constitutes a "meaningful change" worth versioning versus noise, and maintains enough metadata to support diff, rollback, and audit.

## Decision Tree

```
Version via **git commits**, **filename suffixes**, **single file + metadata header**, **external system (API/DB)**, or **append-only log**?
Granularity: **every save**, **every meaningful change**, or **explicit checkpoints only**?
```

## Examples

TODO: Add concrete examples from real usage.
