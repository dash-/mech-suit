# Modifiers

Modifiers are tools in the arsenal that attach to other macros — strategies, patterns, or skills — to change *how* they execute. A modifier never fires alone; it has no meaning without a target. When you attach a modifier, you are adjusting the agent's execution contract: same goal, different constraints. Multiple modifiers can stack; some pairs create productive tension that must be resolved explicitly before execution begins.

---

### Non-destructive (`non-destructive`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent keeps all source material intact and produces derived output alongside it rather than replacing it. Every transformation becomes a derivation step with provenance — the agent must plan for storage of both forms, maintain a clear lineage from source to output, and reason about which form to surface to the consumer.

**Composes with:** `compose`, `collapse`, `refine`, `content-factory`, `progressive-refinement`

**Opposes:** `eager` (eagerly deriving many forms while preserving all sources creates storage and complexity pressure)

---

### Lazy (`lazy`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent defers all work until the result is actually needed by a downstream consumer. Instead of building everything upfront, it identifies the immediate need and produces only that. Downstream steps are planned but not executed — the agent operates in just-in-time mode and actively resists speculative work.

**Composes with:** `delegate`, `cache`, `decompose`, `catalog`, `cascade-fallback`

**Opposes:** `eager`, `publishable` (a publishable artifact must be fully resolved, which conflicts with deferred work)

---

### Eager (`eager`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent invests in pre-computation, pre-fetching, or pre-validation before results are explicitly requested. It anticipates what will be needed and produces it now, trading compute cost for reduced latency later. The agent must distinguish what is *likely* needed from what is *certainly* needed — over-eagerness wastes resources.

**Composes with:** `compose`, `generate`, `cache`, `content-factory`, `verification-loop`

**Opposes:** `lazy`, `incremental` (eagerly processing everything conflicts with processing only what changed)

---

### Incremental (`incremental`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent processes only what has changed since the last execution. It must first establish a baseline (what was the prior state?), then compute a delta. All downstream logic operates on the delta, not the full corpus. The agent must reason about change detection, staleness, and whether partial updates preserve correctness of the whole.

**Decision tree:**
- Detect changes by **hash comparison**, **timestamp**, **diff against prior output**, or **explicit signal from caller**?

**Composes with:** `refine`, `verify`, `cache`, `progressive-refinement`, `verification-loop`

**Opposes:** `eager` (doing everything upfront conflicts with doing only the delta), `exhaustive` (incremental skips unchanged work; exhaustive touches everything)

---

### Publishable (`publishable`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent treats the output as audience-facing: it must be self-contained, properly formatted, and free of internal shorthand, TODOs, or draft markers. The agent applies a higher quality bar, reasons about the target audience and medium, and makes review and verification steps mandatory rather than optional.

**Decision tree:**
- Publish to **file**, **API**, **message channel**, or **external service**?
- Audience: **technical peers**, **non-technical stakeholders**, or **general public**?

**Composes with:** `compose`, `verify`, `gate`, `content-factory`, `adversarial-review`, `configurable-hitl`

**Opposes:** `lazy` (deferred work and audience-ready output conflict), `speculative` (speculative output is explicitly not audience-ready)

---

### Reversible (`reversible`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent captures sufficient state before acting to enable rollback. It reasons about what "undo" means for each step, what state to snapshot, and whether partial rollback is meaningful. Execution order is biased toward safety: reversible steps first, irreversible ones last and only after confirmation.

**Composes with:** `delegate`, `gate`, `escalate`, `orchestrator-subagent`, `configurable-hitl`

**Opposes:** `eager` (eagerly executing many steps makes the rollback surface area large and fragile)

---

### Exhaustive (`exhaustive`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent optimizes for coverage over speed. It enumerates the full input space before acting, tracks what has been visited, and uses systematic search rather than heuristic sampling. When exhaustive coverage is infeasible, the agent must flag this and propose bounded alternatives rather than silently sampling.

**Composes with:** `verify`, `decompose`, `verification-loop`, `adversarial-review`

**Opposes:** `incremental` (only-what-changed vs. everything), `lazy` (exhaustive demands upfront completeness)

---

### Speculative (`speculative`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent treats its output as explicitly provisional — a hypothesis to validate, not a final answer. This frees the agent to explore broadly, generate multiple candidates, and tolerate lower individual confidence. Uncertainty must be made visible rather than hidden behind confident-sounding language; every speculative output expects a downstream validation step.

**Composes with:** `generate`, `refine`, `divergent-brainstorm`, `redundant-generation`, `progressive-refinement`

**Opposes:** `publishable` (speculative output is not audience-ready by definition), `idempotent` (speculative generation may intentionally produce different candidates each run)

---

### Idempotent (`idempotent`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent ensures that running the operation multiple times produces the same result as running it once. No double-writes, no duplicated side effects, no accumulated drift. State checks happen before mutations — "is this already done?" always precedes "do this." This changes how the agent handles retries, error recovery, and concurrent execution.

**Composes with:** `cache`, `compose`, `gate`, `caching`, `verification-loop`

**Opposes:** `speculative` (speculative generation may produce different candidates each run, which is intentionally non-idempotent)

---

### Scoped (`scoped`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent establishes an explicit boundary before acting — what files, what time range, what subsystem — and constrains all subsequent reasoning to that boundary. The agent actively rejects drift beyond scope. Discovered dependencies outside the boundary are noted but not pursued; they become inputs for a future scoped pass.

**Composes with:** `decompose`, `delegate`, `verify`, `orchestrator-subagent`, `context-windowing`

**Opposes:** `exhaustive` (exhaustive-within-a-scope is coherent, but the scope itself limits what "exhaustive" means — the tension is about where the boundary is drawn)

---

### Transparent (`transparent`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent externalizes its reasoning process, intermediate states, and decision points rather than presenting only conclusions. It emits rationale for choices, surfaces tradeoffs it considered, and shows work at each stage. This shifts the agent's relationship with the consumer from "trust me" to "verify me" — not verbosity for its own sake, but auditability.

**Composes with:** `verify`, `gate`, `escalate`, `verification-loop`, `configurable-hitl`, `adversarial-review`

**Opposes:** None directly, but excessive transparency combined with `eager` execution can produce overwhelming output volume.

---

### Versionable (`versionable`)

**Category:** modifier

**Expansion:** When this modifier is applied, the agent treats every meaningful state of the artifact as a version that can be referenced, compared, or restored. It must decide on a versioning mechanism, assign version identifiers, and ensure that prior versions remain accessible. The agent reasons about what constitutes a "meaningful change" worth versioning versus noise, and maintains enough metadata to support diff, rollback, and audit.

**Decision tree:**
- Version via **git commits**, **filename suffixes**, **single file + metadata header**, **external system (API/DB)**, or **append-only log**?
- Granularity: **every save**, **every meaningful change**, or **explicit checkpoints only**?

**Composes with:** `non-destructive`, `reversible`, `incremental`, `cache`, `progressive-refinement`

**Opposes:** `lazy` (versioning requires capturing state at each meaningful point, which conflicts with deferring work)

---

*This catalog is not exhaustive. A modifier earns its place when attaching it demonstrably changes how an agent plans and executes — if removing it from an instruction wouldn't change the agent's behavior, it doesn't belong here.*
