---
name: Strategy
type: category
---

# Strategy

**Role:** Approaches to action — the "how to approach" behind execution.

**Form:** Verbs. Invoking a strategy tells an agent what kind of action to take without prescribing specific structure.

**Distinguishing trait:** Strategies are domain-agnostic and structure-agnostic. `verify` tells the agent to check output against criteria, but doesn't prescribe *how* to check (a pattern does that). If a concept has prescribed flow control (loops, branches, specific step sequences), it's a pattern, not a strategy.

**Examples:** `compose`, `collapse`, `delegate`, `verify`, `generate`

**Relationship to other categories:** Strategies compose into patterns (e.g., `delegate + SoC → orchestrator-subagent`). Modifiers adjust how strategies execute (e.g., `verify + incremental`). Some strategies like `defer` have corresponding modifiers (`lazy`) — the strategy is the active choice, the modifier adjusts another macro's timing.
