---
name: Skill
type: category
---

# Skill

**Role:** Executable implementations — the "do it" layer.

**Form:** Commands bound to specific tools and contexts. Skills are invoked directly (e.g., `/pr-review`, `/deck`).

**Distinguishing trait:** Skills are the only macros that execute directly against real tools. Everything else (principles, strategies, patterns, modifiers) is composed *into* skills or used to guide ad-hoc agent behavior. A skill without a bound tool/context is just a pattern.

**Examples:** `/pr-review`, `/deck`, `/publish`, `/pattern`, `/perf`

**Relationship to other categories:** Skills are macro compositions bound to specific environments. `/pr-review` composes `caching + progressive-refinement + adversarial-review + incremental + publishable`. Analyzing a skill's macro composition reveals coverage gaps and design rationale.
