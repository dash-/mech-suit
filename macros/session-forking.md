---
name: Session Forking & Base Context
shorthand: session-forking
category: pattern
tags: [context, coordination]
summary: 'Establish shared context once in a "base session." Fork from the base for parallel workstreams.'
composes_with: []
opposes: []
---

# Session Forking & Base Context (`session-forking`)

**Tags:** `context` `coordination`

Establish shared context once in a "base session." Fork from the base for parallel workstreams. Subagents inherit the full base context rather than receiving thin task descriptions through a pinhole.

```
Base Session (domain knowledge, conventions, project context)
  ├→ Fork: Planning workstream (inherits base)
  ├→ Fork: Research workstream (inherits base)
  └→ Fork: Content workstream (inherits base)
```

**Analogous to:** Git branching — `main` holds shared context, feature branches diverge for specific work.

**Why it matters:**
- Subagents with full context make dramatically better decisions than those getting a one-paragraph task description
- Eliminates redundant context-establishment across parallel workstreams
- Base session can be versioned and updated — all forks benefit

**Key decisions:**
- What goes in the base? (Domain knowledge, conventions, platform context, project goals)
- When to re-fork? (When base context changes significantly)
- Fork depth: can forks fork? (Yes, but manage complexity)

**Fork hygiene — the Stale Fork problem:**
Forks inherit context at a point in time, but the world keeps moving. This applies to two scenarios:

*Parallel (sibling) forks:* Fork B doesn't know what Fork A did to the filesystem, database, or external systems. Context goes stale the moment a sibling acts.

*Serial (clone) forks:* Fork 1 completes and dies. Fork 2 starts later from the same base. The base (CLAUDE.md, memory files, project context) may not reflect what Fork 1 did to the world. Fork 2 wakes up trusting inherited context that is now wrong. This is especially common when a human orchestrates the forking manually (e.g., starting new sessions from a shared project) — the fork has no awareness that it's a fork at all.

Rules for forked agents:
- **Tell the fork it's a fork.** The forked agent must know it's operating on potentially stale context. For serial forks, this means injecting a wake-up message at session start.
- **Verify before acting.** Check the actual state of files, data, and systems before assuming your context is current. Trust the filesystem, not your memory. For serial forks: check git log, re-read memory files, diff assumptions against reality.
- **Scope changes narrowly.** The less a fork touches, the less it conflicts with siblings.
- **Report changes back.** When a fork completes, its changes should be discoverable by the next fork (commit messages, changelogs, file timestamps).
- **Update the base.** After a fork completes meaningful work, the base context (memory files, CLAUDE.md) should be updated so the next serial fork starts closer to reality.

**The human-as-orchestrator case:**
Not all forking is agent-directed. A human using `/fork` and `/rename` to manage sessions is performing `session-forking` without naming it. The structural concern is identical — each new session is a clone that doesn't know prior clones existed. Standing instructions (CLAUDE.md, `/rules`) can inject fork-awareness automatically so the human doesn't have to re-explain it each time.

## Examples

TODO: Add concrete examples from real usage.
