---
name: Pattern
type: category
---

# Pattern

**Role:** Concrete reusable structures — the "what shape" of execution.

**Form:** Recipes with trigger, structure, and outcome. Patterns have prescribed flow control: sequences, loops, branches, agent roles.

**Distinguishing trait:** Patterns are the most "recipe-like" macros. They tell an agent not just what to do but *in what order, with what roles, and with what flow control*. If a concept has no prescribed structure, it's a strategy. If it's bound to specific tools, it's a skill.

**Examples:** `orchestrator-subagent`, `verification-loop`, `content-factory`, `adversarial-review`

**Relationship to other categories:** Patterns compose from strategies and principles (e.g., `verification-loop` embodies `verify + refine + fail-fast`). Modifiers adjust pattern execution. Skills are patterns bound to specific tools and contexts.

**Full catalog:** The detailed pattern catalog lives at `~/labs/claude/patterns/pattern-catalog.md`. Macro files in `macros/` contain the standard macro entry; the full catalog has extended descriptions, tradeoffs, and implementation notes.
