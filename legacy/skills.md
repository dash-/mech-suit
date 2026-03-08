# Skill Index

Skills are macro compositions bound to specific tools and contexts — the executable layer. Implementations live in skill files; this index maps each skill to the macros it composes from.

Useful for:
- **Auditing** — "Does `/pr-review` cover `transparent`? Should it?"
- **Designing new skills** — "I need `verify + incremental + publishable` — does a skill already do this?"
- **Understanding skills** — Quick reference for what a skill actually does under the hood

| Skill | Patterns | Strategies | Modifiers |
|-------|----------|------------|-----------|
| `/pr-review` | caching, progressive-refinement, adversarial-review | refine, verify, cache | incremental, publishable |
| `/deck` | content-factory | compose, collapse | publishable, eager |
| `/publish` | verification-loop, configurable-hitl | verify, gate | publishable |
| `/pattern` | catalog, retrieval-subagent | compose | lazy |
| `/pattern-ideate` | divergent-brainstorm, adversarial-review | generate, verify | non-destructive |
| `/pattern-create` | content-factory | compose, verify | publishable |
| `/perf` | discovery-loop, bayesian-steering | decompose, verify | incremental |
| `/standup` | memory-retrieval, context-assembly | compose, collapse | publishable |
| `/synopsis` | progressive-refinement, memory-retrieval | refine, cache | publishable, incremental |

*Extend as skills are added or modified.*
