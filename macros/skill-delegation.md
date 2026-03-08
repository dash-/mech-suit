---
name: Skill Delegation
shorthand: skill-delegation
category: pattern
tags: [coordination, cost]
summary: Instead of reimplementing capability inline, delegate to a named, reusable skill.
composes_with: []
opposes: []
---

# Skill Delegation (`skill-delegation`)

**Tags:** `coordination` `cost`

Instead of reimplementing capability inline, delegate to a named, reusable skill. The delegating agent doesn't need to know how the skill works — just what it does and what it returns. Skills are the composability primitive of agent systems.

```
/ticket needs to check for duplicates
  → delegates to /find-ticket (a reusable search skill)
    → delegates to Linear search MCP
      → returns matching tickets
```

**Different from Orchestrator-Subagent:** An orchestrator spawns one-off workers for a specific task. Skill Delegation invokes a *named, reusable capability* that exists independently and is used by many consumers. **The test:** does this capability exist before this task, and will it exist after? If yes, it's a skill. If the capability is created for this task and dissolved after, it's a subagent.

**When to use:**
- The capability already exists as a tested, named skill
- Multiple commands/agents need the same capability
- You want to avoid reimplementing (and re-debugging) common operations

**Tradeoffs:**
- **Pro:** DRY — build once, use everywhere
- **Pro:** Skills can be tested and improved independently of their consumers
- **Pro:** New agents get powerful capabilities on day one by composing existing skills
- **Con:** Skill interfaces become implicit contracts — changing a skill can break consumers
- **Con:** Indirection makes debugging harder ("why did /ticket fail?" → "/find-ticket failed" → "Linear search failed")

**Key decisions:**
- Skill discovery: how does an agent know what skills are available?
- Interface stability: how do you evolve skills without breaking consumers?
- Error propagation: how do skill failures surface to the delegating agent?

## Examples

TODO: Add concrete examples from real usage.
