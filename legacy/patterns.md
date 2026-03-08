# Pattern Macros

Patterns are macros with concrete structure — a trigger, a shape, and an outcome. They are the most "recipe-like" macros in the library. The full catalog with detailed expansions lives in [`../patterns/pattern-catalog.md`](../patterns/pattern-catalog.md).

This file maps each pattern to the strategy and principle macros it composes from. This is useful for:
- **Discovering patterns** — "I want to `verify + refine`, what pattern does that?"
- **Auditing patterns** — "Does this pattern cover `transparent`? Should it?"
- **Designing new patterns** — "I need `delegate + scoped + incremental`, does anything exist?"

## Composition Map

| Pattern | Strategies | Principles | Notes |
|---------|-----------|-----------|-------|
| `adversarial-review` | verify, generate | fail-fast, transparent | Generate attacks, verify defenses |
| `orchestrator-subagent` | delegate, decompose | SoC, least-priv | |
| `verification-loop` | verify, refine | fail-fast, transparent | |
| `caching` | cache | DRY, idempotent | |
| `progressive-refinement` | refine | DRY | Iterative application |
| `redundant-generation` | generate | *opposes* DRY | Intentional redundancy for quality |
| `divergent-brainstorm` | generate | SoC | Diversity is structural, not random |
| `content-factory` | generate, refine, verify | SoC, fail-fast, transparent | Full lifecycle pipeline |
| `cascade-fallback` | escalate, delegate | fail-fast, least-priv | |
| `decomposition-reassembly` | decompose, compose | SoC, DRY | |
| `context-windowing` | collapse | DRY, least-surprise | |
| `skill-delegation` | delegate | SoC, least-priv | |
| `configurable-hitl` | gate, escalate | least-priv, transparent | |
| `catalog` | compose | DRY, SoC | This library is an instance |
| `contract-interface` | normalize, gate | explicit, composable | |
| `tournament-selection` | generate, verify | fail-fast | Compete then select |
| `hybrid-synthesis` | compose, refine | DRY, composable | Merge best parts of multiple candidates |
| `bayesian-steering` | verify, refine | transparent, minimal | Update beliefs, narrow search |
| `routing` | delegate | SoC, minimal | Select path by criteria |
| `escalation-ladder` | escalate, delegate | fail-fast, least-priv, minimal | Cheapest viable agent first |
| `memory-retrieval` | cache, compose | DRY | Retrieve before regenerating |
| `workspace-isolation` | isolate | least-priv, reversible | Sandbox for risky operations |
| `checkpoint-resume` | cache | idempotent, reversible | Snapshot state for recovery |
| `discovery-loop` | verify, refine, cache | transparent, minimal | Bayesian exploration with budget |

*Extend as patterns are added. A pattern earns its row when it has a distinct structure — if it's just a strategy combination with no prescribed shape, it belongs in strategies.md instead.*
