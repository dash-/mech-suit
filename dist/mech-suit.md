# The Macro Library

A mech suit for building things with agents.

## What This Is

A library of named, precise, reusable concepts — **macros** — that any agent (human or AI) can invoke, compose, and rely on for predictable behavior. Each macro expands into specific agent behavior that is the same every time, across any context.

## The Problem It Solves

When you tell an agent "make this incremental," the result depends on the agent's interpretation. Two agents will do two different things. Repeated instructions drift. This is the genie problem: you asked for what you wanted but got what you said.

Macros raise the floor of interpretation quality. Instead of vague instructions that each agent interprets differently, you invoke a named concept with a precise expansion. The agent restates the expansion applied to your specific context. You confirm or adjust. Then execution happens.

## How to Use It

1. **Invoke** with the `/with` command: `/with collapse, non-destructive`
2. The agent **expands** each macro and synthesizes them in context
3. The agent **restates** the combined behavior: "Here's what I'll do: resolve all references into a flat artifact, but preserve the compositional source alongside it. Does that match your intent?"
4. You **confirm or adjust** — this is contract negotiation, not deployment
5. Execution happens

Macros compose freely. Tensions between macros (e.g., `/with lazy, fail-fast`) are surfaced explicitly for resolution rather than silently resolved by the agent.

## Who It's For

- **Humans** instructing agents — precise shorthand for complex behavior
- **Agents** delegating to subagents — compressed instructions that decompress losslessly via catalog lookup
- **Skill authors** designing new capabilities — composable building blocks with known behaviors


---


# Categories

# Principle

**Role:** Values and invariants — the "why" behind decisions.

**Form:** Lenses. Invoking a principle causes the agent to examine the current context through that lens and surface violations or opportunities.

**Distinguishing trait:** Principles don't tell an agent *what to build* or *how to act*. They tell it *what to notice*. A principle invocation always produces findings, not actions.

**Examples:** `DRY`, `SoC`, `fail-fast`, `explicit`, `minimal`

**Relationship to other categories:** Principles ground strategies (a strategy may embody or deliberately oppose a principle). Some concepts like `idempotent` and `transparent` are both principles and modifiers — the principle says "value this," the modifier says "apply this to a specific operation."

---

# Strategy

**Role:** Approaches to action — the "how to approach" behind execution.

**Form:** Verbs. Invoking a strategy tells an agent what kind of action to take without prescribing specific structure.

**Distinguishing trait:** Strategies are domain-agnostic and structure-agnostic. `verify` tells the agent to check output against criteria, but doesn't prescribe *how* to check (a pattern does that). If a concept has prescribed flow control (loops, branches, specific step sequences), it's a pattern, not a strategy.

**Examples:** `compose`, `collapse`, `delegate`, `verify`, `generate`

**Relationship to other categories:** Strategies compose into patterns (e.g., `/with delegate, SoC` → orchestrator-subagent). Modifiers adjust how strategies execute (e.g., `/with verify, incremental`). Some strategies like `defer` have corresponding modifiers (`lazy`) — the strategy is the active choice, the modifier adjusts another macro's timing.

---

# Pattern

**Role:** Concrete reusable structures — the "what shape" of execution.

**Form:** Recipes with trigger, structure, and outcome. Patterns have prescribed flow control: sequences, loops, branches, agent roles.

**Distinguishing trait:** Patterns are the most "recipe-like" macros. They tell an agent not just what to do but *in what order, with what roles, and with what flow control*. If a concept has no prescribed structure, it's a strategy. If it's bound to specific tools, it's a skill.

**Examples:** `orchestrator-subagent`, `verification-loop`, `content-factory`, `adversarial-review`

**Relationship to other categories:** Patterns compose from strategies and principles (e.g., `verification-loop` embodies `verify + refine + fail-fast`). Modifiers adjust pattern execution. Skills are patterns bound to specific tools and contexts.

**Full catalog:** The detailed pattern catalog lives at `~/labs/claude/patterns/pattern-catalog.md`. Macro files in `macros/` contain the standard macro entry; the full catalog has extended descriptions, tradeoffs, and implementation notes.

---

# Modifier

**Role:** Cross-cutting constraints — the "with what adjustment" of execution.

**Form:** Adjectives. Modifiers attach to other macros to change how they execute. A modifier never fires alone.

**Distinguishing trait:** Modifiers change the agent's execution contract without changing the goal. `/with verify, incremental` still verifies — but only the delta. If removing the modifier wouldn't change behavior, it doesn't belong in this category.

**Examples:** `non-destructive`, `lazy`, `incremental`, `publishable`, `scoped`, `versionable`

**Relationship to other categories:** Modifiers are orthogonal — they can attach to strategies, patterns, or skills. Multiple modifiers can stack. Some pairs create productive tension (`lazy + fail-fast`) that must be resolved explicitly. Some concepts like `idempotent` and `transparent` are both principles and modifiers.

---

# Skill

**Role:** Executable implementations — the "do it" layer.

**Form:** Commands bound to specific tools and contexts. Skills are invoked directly (e.g., `/pr-review`, `/deck`).

**Distinguishing trait:** Skills are the only macros that execute directly against real tools. Everything else (principles, strategies, patterns, modifiers) is composed *into* skills or used to guide ad-hoc agent behavior. A skill without a bound tool/context is just a pattern.

**Examples:** `/pr-review`, `/deck`, `/publish`, `/pattern`, `/perf`

**Relationship to other categories:** Skills are macro compositions bound to specific environments. `/pr-review` composes `caching + progressive-refinement + adversarial-review + incremental + publishable`. Analyzing a skill's macro composition reveals coverage gaps and design rationale.

---


# Macro Catalog


## Principles

### Don't Repeat Yourself (`DRY`)

*Identify every instance where the same knowledge exists in more than one place and propose collapsing each duplication to a single authoritative source.*

When this macro is invoked, the agent identifies every instance where the same knowledge exists in more than one place. It flags duplicated logic, copy-pasted text, parallel structures that will drift, and any spot where a change in one location demands a corresponding change elsewhere. The agent then proposes how to collapse each duplication to a single authoritative source.

## Decision Tree

```
How should the duplication be eliminated?
  A. Abstraction (extract shared logic into a function, module, or component)
  B. Configuration (single config source referenced by all consumers)
  C. Generation (one source template that produces the variants)
  D. Reference (replace copies with pointers to a canonical location)
```

## Examples

TODO: Add concrete examples from real usage.

---

### Separation of Concerns (`SoC`)

*Examine each unit and identify any that serve multiple masters, proposing splits such that each resulting piece changes for exactly one reason.*

When this macro is invoked, the agent examines each unit — function, file, agent, document — and identifies any that serve multiple masters. It flags functions that both compute and format, configs that mix deployment and business logic, prompts that conflate instruction with context. For each violation, the agent proposes a split such that each resulting piece changes for exactly one reason.

## Examples

TODO: Add concrete examples from real usage.

---

### Composable (`composable`)

*Examine every component for whether it can be used in contexts its author didn't anticipate, proposing interface changes that enable free connection through simple, consistent contracts.*

When this macro is invoked, the agent examines every component and asks: "Can this be used in a context its author didn't anticipate?" It flags components that work only in their original context, outputs that require transformation before the next step can consume them, tightly coupled pairs that cannot be recombined, and interfaces that demand knowledge of internal implementation. For each, it proposes interface changes that enable free connection through simple, consistent contracts.

## Examples

TODO: Add concrete examples from real usage.

---

### Explicit over Implicit (`explicit`)

*Hunt for anything that requires "you just have to know" to understand and propose stating the intention, dependency, or assumption directly.*

When this macro is invoked, the agent hunts for anything that requires "you just have to know" to understand. It flags magic values, hidden coupling between modules, behavior that depends on execution order or ambient state, and undocumented prerequisites. For each finding, it proposes stating the intention, dependency, or assumption directly — accepting verbosity as the price of eliminating mystery.

## Examples

TODO: Add concrete examples from real usage.

---

### Fail Fast (`fail-fast`)

*Trace every error path and identify where bad state can travel far from its origin before detection, proposing to move detection to the earliest possible moment.*

When this macro is invoked, the agent traces every error path and identifies where bad state can travel far from its origin before detection. It flags silent failures, bare exception handlers that swallow errors, functions returning ambiguous sentinel values, and late validation of input that was available earlier. For each finding, the agent proposes moving detection to the earliest possible moment.

## Decision Tree

```
How should the early failure surface?
  A. Throw/raise (halt execution with a clear error)
  B. Return typed error (let the caller decide)
  C. Validate at boundary (reject bad input before it enters the system)
  D. Assert invariant (crash on impossible state in development)
```

## Examples

TODO: Add concrete examples from real usage.

---

### Idempotent (`idempotent`)

*The agent examines every operation for accumulated side effects on re-run and ensures that running the operation multiple times produces the same result as running it once.*

## As Principle

When this macro is invoked, the agent examines every operation and asks: "What happens if this runs again right now?" It flags operations that accumulate side effects on re-run — duplicate records, appended-not-replaced content, repeated notifications, migrations that break if executed twice. For each violation, the agent proposes a guard or restructuring that makes repeated execution safe.

## As Modifier

When this modifier is applied, the agent ensures that running the operation multiple times produces the same result as running it once. No double-writes, no duplicated side effects, no accumulated drift. State checks happen before mutations — "is this already done?" always precedes "do this." This changes how the agent handles retries, error recovery, and concurrent execution.

## Decision Tree

```
How should idempotency be achieved?
  A. Check-before-write (skip if already applied)
  B. Upsert (insert or update, never duplicate)
  C. Deterministic key (same input always maps to same identity)
  D. Replace-not-append (overwrite the whole target each time)
```

## Examples

TODO: Add concrete examples from real usage.

---

### Least Privilege (`least-priv`)

*Audit every permission grant, scope, and capability in the current context and propose the minimum viable permission for each.*

When this macro is invoked, the agent audits every permission grant, scope, and capability in the current context. It flags overly broad permissions, god-objects that can touch everything, API tokens with unnecessary scopes, agents with write access when they only need read, and any situation where the blast radius of a mistake is larger than necessary. For each finding, it proposes the minimum viable permission.

## Examples

TODO: Add concrete examples from real usage.

---

### Principle of Least Surprise (`least-surprise`)

*Audit naming, return values, defaults, and side effects for anything that would confuse a person or system encountering them for the first time without documentation.*

When this macro is invoked, the agent audits naming, return values, defaults, and side effects for anything that would confuse a person or system encountering them for the first time without documentation. It flags misleading names, return values that violate convention, side effects hidden behind innocent-looking interfaces, and defaults no one would guess. The test: "If someone encountered this cold, what would they expect?"

## Examples

TODO: Add concrete examples from real usage.

---

### Minimal Footprint (`minimal`)

*Challenge every piece of structure, dependency, and scope, proposing removals or simplifications wherever what exists is merely bigger rather than meaningfully better than the simplest thing that could work.*

When this macro is invoked, the agent challenges every piece of structure, dependency, and scope in the current context. It flags premature abstractions, unused parameters, speculative features, dependencies pulled in for a single function, and framework choices that outweigh the problem. For each, it asks: "What is the simplest thing that could work here, and is what we have meaningfully better or just bigger?" It proposes removals or simplifications.

## Decision Tree

```
What kind of excess is being removed?
  A. Unused code/structure (dead code, empty abstractions)
  B. Premature abstraction (generalized before needed — inline it)
  C. Heavyweight dependency (replace with focused alternative or hand-roll)
  D. Speculative scope (features/parameters for futures that haven't arrived)
```

## Examples

TODO: Add concrete examples from real usage.

---

### Reversible (`reversible`)

*The agent identifies every point of no return and captures sufficient state before acting to enable rollback, biasing execution order toward safety.*

## As Principle

When this macro is invoked, the agent identifies every point of no return in the current context — destructive operations without backup, one-way deployments, writes that overwrite without preserving the original. For each, it proposes an alternative that preserves a recovery path: soft deletes, backup-before-write, staged rollouts, or undo mechanisms. The test: "If this turns out to be wrong, what's the recovery path?"

## As Modifier

When this modifier is applied, the agent captures sufficient state before acting to enable rollback. It reasons about what "undo" means for each step, what state to snapshot, and whether partial rollback is meaningful. Execution order is biased toward safety: reversible steps first, irreversible ones last and only after confirmation.

## Examples

TODO: Add concrete examples from real usage.

---

### Transparent (`transparent`)

*The agent identifies black boxes and externalizes its reasoning process, intermediate states, and decision points to enable auditability and reconstruction of why things happened.*

## As Principle

When this macro is invoked, the agent identifies every black box in the current context — processes whose intermediate state is invisible, decisions made without recorded rationale, error messages that hide root causes, agents that produce output without showing their work. For each, it proposes a way to make the internal state, reasoning, or decision point visible to observers. The test: "If this fails, can someone reconstruct *why* from what's visible?"

## As Modifier

When this modifier is applied, the agent externalizes its reasoning process, intermediate states, and decision points rather than presenting only conclusions. It emits rationale for choices, surfaces tradeoffs it considered, and shows work at each stage. This shifts the agent's relationship with the consumer from "trust me" to "verify me" — not verbosity for its own sake, but auditability.

## Examples

TODO: Add concrete examples from real usage.

---


## Strategys

### Cache (`cache`)  `cost`

*The agent checks for a valid prior result before performing an expensive operation, returning cached values when available and invalidating stale entries when inputs change.*

When this macro is invoked, the agent checks for a valid prior result before performing an expensive operation. If one exists, it returns the cached value. If not, it performs the operation and stores the result. The agent maintains cache validity — when inputs change, it invalidates stale entries rather than serving outdated results.

```
Request → Check cache (hash/timestamp) → Hit → Return cached result
                                        → Miss → Compute → Store in cache → Return
```

## Decision Tree

- Cache in memory, filesystem, or external store?
- Invalidate by TTL, content hash, or explicit signal?
- Invalidation scope: just the changed item, or its dependents too?

## When to Use

- Operations are expensive (LLM calls, API calls, computation) and inputs change infrequently
- Iterative systems that re-run on evolving data where most data is unchanged between runs
- Any repeated lookup or computation with stable inputs

## Tradeoffs

- **Pro:** Massive cost and time savings on repeated operations
- **Pro:** Makes frequent re-runs practical where full recomputation would be prohibitive
- **Con:** Cache invalidation is hard — dependencies between items can mean a change in one invalidates others
- **Con:** Stale caches silently return wrong results if invalidation logic is buggy

## Examples

TODO: Add concrete examples from real usage.

---

### Collapse (`collapse`)

*The agent walks all dependency chains, inlines referenced content, and resolves variables to produce a flat, self-contained artifact requiring no further resolution.*

When this macro is invoked, the agent walks all dependency chains, inlines referenced content, and resolves variables or lookups, producing a flat, self-contained artifact that requires no further resolution. The consumer never performs lookups or chases references. If a reference cannot be resolved, the agent fails immediately rather than emitting a broken link.

## Decision Tree

- Resolve via inlining (embed content), compilation (transform to target), or snapshot (freeze current state)?

## Examples

TODO: Add concrete examples from real usage.

---

### Compose (`compose`)

*The agent builds a whole from existing, well-defined parts by inventorying sub-components, wiring them through explicit seams, and preferring reuse over reinvention.*

When this macro is invoked, the agent builds a whole from existing, well-defined parts. It inventories available sub-components, wires them together through explicit seams, and prefers reuse over reinvention. The agent makes the assembly structure visible — which parts were combined and how they connect.

## Examples

TODO: Add concrete examples from real usage.

---

### Decompose (`decompose`)

*The agent splits a complex input or task along natural boundaries into independent, addressable parts that can be understood or acted on without reference to each other.*

When this macro is invoked, the agent splits a complex input or task along natural boundaries into independent, addressable parts. Each part can be understood, acted on, or delegated without reference to the others. The agent ensures loose coupling — changing one part must not require changing another.

## Decision Tree

- Split by responsibility, by data shape, or by lifecycle stage?
- Flat decomposition (all parts peer-level) or hierarchical (parts contain sub-parts)?

## Examples

TODO: Add concrete examples from real usage.

---

### Defer (`defer`)

*The agent registers that work could be done but postpones execution until a consumer demands the result, avoiding wasted computation on paths that may never be taken.*

When this macro is invoked, the agent registers that work could be done but postpones execution until a consumer actually demands the result. This avoids wasted computation on paths that may never be taken. The agent ensures preconditions are still valid at execution time, not just at registration time — a deferred action that fires against stale state is a bug.

## Decision Tree

- Defer until first access (lazy), until explicit trigger (event-driven), or until a batch boundary (bulk)?

## Examples

TODO: Add concrete examples from real usage.

---

### Delegate (`delegate`)  `coordination` `cost`

*The agent identifies work outside its core responsibility and passes it to a specialist with only the authority and context needed.*

When this macro is invoked, the agent identifies work that falls outside its core responsibility or optimal scope and passes it to a specialist with only the authority and context needed for that sub-task. It defines the interface clearly — inputs, expected outputs, constraints — and reclaims control when the delegate returns.

The delegating agent doesn't need to know *how* the delegate works — just what it does and what it returns.

```
/ticket needs to check for duplicates
  → delegates to /find-ticket (a reusable search skill)
    → delegates to Linear search MCP
      → returns matching tickets
```

## Decision Tree

- Delegate to subagent, external service, or human?
- Pass full context or minimal context (need-to-know)?
- Is the capability a named, reusable skill (exists before and after this task) or a one-off worker (created and dissolved for this task)?

## When to Use

- The capability already exists as a tested, named skill or service
- Multiple commands/agents need the same capability
- Work falls outside the current agent's specialization

## Tradeoffs

- **Pro:** DRY — build once, use everywhere
- **Pro:** Delegates can be tested and improved independently of their consumers
- **Con:** Interfaces become implicit contracts — changing a delegate can break consumers
- **Con:** Indirection makes debugging harder (failure chains across delegates)

## Examples

TODO: Add concrete examples from real usage.

---

### Emit (`emit`)  `communication` `monitoring`

*The agent produces structured, observable signals about internal state or progress as a non-blocking side channel.*

When this macro is invoked, the agent produces structured, observable signals about internal state or progress — logs, progress indicators, intermediate results — as a side channel. Emission is non-blocking: it does not wait for acknowledgment and does not alter control flow. It makes the agent's reasoning or progress legible to supervisors without requiring interruption.

```
System event (idle, permission prompt, completion, error)
  → Hook fires → Notification sent (Slack, email, push)
  → Main workflow continues (does NOT block)
```

## Decision Tree

- Which events trigger emissions? (Be selective — alert fatigue is real)
- Which channel? (Slack for urgent, email for digest, push for critical, log for audit)
- Escalation: if emission is ignored for X time, escalate?

## When to Use

- Humans need awareness of system state but shouldn't gate every action
- Long-running processes where humans check in periodically
- Error conditions that need human attention but not immediate action

## Tradeoffs

- **Pro:** Humans stay informed without being a bottleneck
- **Pro:** Cheap — no workflow interruption
- **Con:** Notifications can be ignored or lost
- **Con:** Too many emissions → alert fatigue → signals get ignored

## Examples

TODO: Add concrete examples from real usage.

---

### Escalate (`escalate`)

*The agent surfaces a problem or decision to a higher authority with full context of what was attempted, why it was insufficient, and what is needed to proceed.*

When this macro is invoked, the agent surfaces a problem or decision to a higher authority with full context: what was attempted, why it was insufficient, and what information or permission is needed to proceed. The agent does not guess or silently degrade — it halts its current path and makes the blocker explicit.

## Examples

TODO: Add concrete examples from real usage.

---

### Gate (`gate`)

*The agent evaluates a precondition and either allows progress or blocks it — gates are binary with no middle ground or workarounds for unmet requirements.*

When this macro is invoked, the agent evaluates a precondition and either allows progress (pass) or blocks it (halt). There is no middle ground — gates are binary. The agent does not attempt workarounds for unmet requirements. Gates enforce invariants at transition points, not after the fact.

## Examples

TODO: Add concrete examples from real usage.

---

### Generate (`generate`)

*The agent produces multiple distinct outputs intentionally favoring breadth over efficiency, deferring convergence to a subsequent verify or refine pass.*

When this macro is invoked, the agent produces multiple distinct outputs — ideas, drafts, solutions — intentionally favoring breadth over efficiency. Redundancy is the point: overlapping candidates increase the chance of finding high-quality results. The agent does not self-filter during generation; convergence happens in a subsequent `verify` or `refine` pass.

## Decision Tree

- Generate N candidates with variation in what dimension (approach, style, scope)?
- Constrained generation (within guardrails) or unconstrained (maximize diversity)?

## Examples

TODO: Add concrete examples from real usage.

---

### Isolate (`isolate`)  `setup`

*The agent sets up boundaries so that a risky or uncertain operation cannot affect anything outside its designated area.*

When this macro is invoked, the agent sets up boundaries — sandboxes, scoped permissions, or working copies — so that a risky or uncertain operation cannot affect anything outside its designated area. Isolation is applied before the risky action, not as cleanup after. If the operation fails, damage is contained to the isolated scope.

```
Ticket A → Worktree A (isolated branch, files, state)
Ticket B → Worktree B (isolated branch, files, state)
  (no cross-contamination)
```

## Decision Tree

- Isolate by process boundary, filesystem copy (worktree), or permission scope?
- Shared resources (databases, ports) — isolate those too, or accept the risk?
- Cleanup: auto-dispose on completion, or preserve for debugging?

## When to Use

- Multiple tasks run in parallel on the same codebase or system
- Tasks might conflict (touching the same files, conflicting dependencies)
- You need to context-switch between tasks without stashing/resetting
- An operation is risky and you want to contain the blast radius

## Tradeoffs

- **Pro:** Zero cross-contamination between parallel work
- **Pro:** Instant context switching between isolated environments
- **Con:** Disk space / resource cost for multiple copies
- **Con:** Shared resources can still conflict despite isolation

## Examples

TODO: Add concrete examples from real usage.

---

### Normalize (`normalize`)

*The agent maps diverse representations to a single canonical form early in the pipeline, eliminating branching and surprise for all downstream logic.*

When this macro is invoked, the agent maps diverse representations — formats, naming conventions, structures — to a single canonical form early in the pipeline. All downstream logic handles only one shape, eliminating branching and surprise. The agent preserves the original when the transformation is lossy, but all processing operates on the normalized version.

## Examples

TODO: Add concrete examples from real usage.

---

### Refine (`refine`)  `convergent` `quality`

*The agent takes a prior output and applies targeted modifications while preserving what already works, with each pass having diminishing scope.*

When this macro is invoked, the agent takes a prior output and applies targeted modifications — fixing defects, tightening language, improving structure — while preserving what already works. Each refinement pass has a diminishing scope of changes. The agent does not regenerate wholesale when a scalpel will do.

```
Draft → Clarity Agent → Accuracy Agent → Tone Agent → Conciseness Agent → Final
```

## Decision Tree

- Refine for correctness, clarity, or performance?
- Single pass or iterate until a quality threshold is met?
- Single agent refining all dimensions, or successive specialized agents each focused on one dimension?

## When to Use

- Output quality has multiple independent dimensions
- A single agent optimizing all simultaneously produces mediocre results
- You want predictable, incremental improvement

## Tradeoffs

- **Pro:** Each refinement agent has a simple, focused job
- **Pro:** Add or remove refinement stages without redesigning the system
- **Con:** Later stages can undo earlier improvements
- **Con:** Order matters and has diminishing returns

## Examples

TODO: Add concrete examples from real usage.

---

### Verify (`verify`)

*The agent checks produced output against defined criteria before passing it downstream, rejecting failures with explanation or routing them to refine.*

When this macro is invoked, the agent checks produced output against defined criteria — correctness, completeness, format, or constraints — before passing it downstream. Verification happens before handoff, never after. When verification fails, the agent either rejects the output with a clear explanation or routes it to `refine`.

## Examples

TODO: Add concrete examples from real usage.

---


## Patterns

### Abstraction Mining (`abstraction-mining`)  `context` `learning`

*Extracting reusable abstractions from working implementations.*

**Tags:** `context` `learning`

Extracting reusable abstractions from working implementations. Instead of designing abstractions top-down, examine systems that work well (internal tools, open-source projects, competitor products) and reverse-engineer *why* they work into named, reusable concepts.

**Process:**
1. Identify a system that works notably well
2. Map its structure — what exists, how the parts interact, what makes it effective
3. Abstract the structure away from the specific domain
4. Name it, define it, add it to a catalog

**Sources:** Internal implementations, well-known open-source systems, published research, delivery retrospectives.

**Key insight:** The goal is not to copy implementations, but to extract the *structural reason* something works so it can be applied elsewhere.

## Examples

TODO: Add concrete examples from real usage.

---

### Addressable Output (`addressable-output`)  `communication`

*Structure agent output so every item is uniquely referenceable.*

**Tags:** `communication`

Structure agent output so every item is uniquely referenceable. Use numbers for top-level items (issues, decisions, steps) and letters for sub-options within each. This lets humans (or downstream agents) respond precisely — "approve 2B, reject 3A" — instead of ambiguously quoting text.

```
Agent output:
  1. Database migration strategy
     A. Run migrations in-place (recommended)
     B. Blue-green deployment with cutover
     C. Shadow writes during transition period
  2. API versioning approach
     A. URL path versioning (recommended)
     B. Header-based versioning

Human response: "1A, 2A" → unambiguous, complete
```

**When to use:**
- Agent presents multiple decisions or recommendations that need human approval
- Output contains lists where the human needs to accept, reject, or modify individual items
- Downstream agents need to parse human feedback and map it back to specific items
- Any multi-turn interaction where "which one?" ambiguity would waste a round-trip

**Tradeoffs:**
- **Pro:** Eliminates ambiguity — "2B" is unambiguous, "the second option" is not
- **Pro:** Humans can respond in shorthand, which is faster
- **Pro:** Machine-parseable — downstream agents can reliably extract choices from "1A, 2B, 3C"
- **Con:** Can feel overly formal for simple, single-choice interactions
- **Con:** Deep nesting (1A-ii-b) defeats the purpose — keep it to two levels max

**Key decisions:**
- Numbering scheme: numbers + letters? hierarchical (1.1, 1.2)? flat?
- Recommended option: always list it first? mark it explicitly?
- Response format: do you tell the human how to respond (e.g., "reply with 1A or 1B")?

**Notes:** Natural partner to **Inversion of Control** (agent drives the process, human picks from addressable options) and **Configurable HITL** (addressable items map to approval checkpoints).

## Examples

TODO: Add concrete examples from real usage.

---

### Adversarial Review (`adversarial-review`)  `convergent` `quality` `coordination`

*A producer agent generates an artifact (plan, content, code, hypothesis — any output).*

**Tags:** `convergent` `quality` `coordination`

A producer agent generates an artifact (plan, content, code, hypothesis — any output). A red team of adversarial agents attacks it, finding weaknesses, gaps, and failure modes. A blue team proposes patches. Judge agents evaluate whether patches are sufficient. The cycle repeats until judges are satisfied or iteration limit is reached.

```
Producer → Artifact → Red Team (attack) → Blue Team (patch) → Judges (grade)
    ↑                                                               │
    └──────────────── iterate if insufficient ─────────────────────┘
```

**Applies to any artifact:**
- **Plans** — find methodological gaps, budget risks, unstated assumptions
- **Content** — find off-brand messaging, weak arguments, ethical issues
- **Code** — find bugs, security vulnerabilities, performance issues
- **Hypotheses** — find confounds, alternative explanations, measurement problems
- **Experiment designs** — find sources of bias, power issues, missing controls

**When to use:**
- The artifact has high consequences for failure
- You want to surface non-obvious failure modes before committing resources
- The domain has known adversarial dynamics

**Tradeoffs:**
- **Pro:** Dramatically reduces shipping artifacts with obvious holes
- **Pro:** Red team agents can be specialized by failure mode (ethical, methodological, statistical, budgetary)
- **Con:** Expensive — multiple agents, multiple rounds (5-15x single agent cost)
- **Con:** Can be overly conservative if judges have low risk tolerance

**Key decisions:**
- Red team specialization: one generalist or multiple specialists?
- Convergence criteria: score threshold? unanimous agreement? max rounds?
- Patch granularity: individual issues or full artifact regeneration?
- Scope: review the whole artifact each round, or focus on previously identified weaknesses?

**Notes:** Often preceded by **Inversion of Control** (interview → then red-team the result). Pairs with **Ethics Gating** (ethics as a specialized red team dimension) and **Configurable HITL** (human approves after judges).

## Examples

TODO: Add concrete examples from real usage.

---

### Agent Discovery (`agent-discovery`)  `setup` `coordination`

*Enable agents to discover each other''s capabilities at runtime rather than hardcoding agent references.*

**Tags:** `setup` `coordination`

Enable agents to discover each other's capabilities at runtime rather than hardcoding agent references. Agents publish machine-readable capability manifests (Agent Cards); consumers discover them via well-known URIs, registries, or direct configuration.

```
Agent publishes: /.well-known/agent.json
  → { name, skills, supported I/O, auth requirements, endpoint }

Consumer discovers: query registry or well-known URI
  → Finds agent with matching capability
  → Negotiates interaction mode (sync, async, streaming)
  → Delegates task
```

**When to use:**
- Multi-agent systems where agents are independently deployed and evolve separately
- Dynamic composition — agents added or removed without redeploying consumers
- Cross-team or cross-organization agent interoperability

**Tradeoffs:**
- **Pro:** Loose coupling — agents can be swapped, upgraded, or added without redeploying consumers
- **Pro:** Enables dynamic composition of agent pipelines at runtime
- **Con:** Discovery adds latency and a point of failure (registry unavailable = can't find agents)
- **Con:** Security implications — discovered agents must be authenticated and authorized

**Discovery strategies:**
- **Well-known URI** — Agents expose a manifest at a standard path (zero-infrastructure)
- **Registry** — Centralized catalog with search, access control, and versioning
- **Direct configuration** — Static agent references for private or embedded agents

**Key decisions:**
- Manifest format: what fields describe an agent's capabilities? (skills, I/O types, auth, versioning)
- Registry governance: who can register agents? How are stale entries cleaned up?
- Trust model: how does a consumer verify a discovered agent is legitimate?

**Notes:** Pairs with **Contract Interface** (the manifest is a capability contract) and **Skill Delegation** (discovered agents are invoked as skills).

## Examples

TODO: Add concrete examples from real usage.

---

### Agent Versioning (`agent-versioning`)  `deployment` `reliability`

*Manage the lifecycle of agent configurations (prompts, tools, parameters) as versioned artifacts.*

**Tags:** `deployment` `reliability`

Manage the lifecycle of agent configurations (prompts, tools, parameters) as versioned artifacts. Roll out new versions incrementally, A/B test them against the current version, and roll back if quality regresses. The same discipline applied to software releases, applied to agent behavior.

```
Agent v1 (current, serving 100% of traffic)
  → Deploy Agent v2 (candidate)
  → Route 10% of tasks to v2, 90% to v1
  → Compare quality metrics
  → v2 better? → gradually shift traffic → v2 becomes current
  → v2 worse? → roll back → v1 continues, v2 goes back to development
```

**Different from Canary & Shadow Mode:** Canary compares AI vs human process. Agent Versioning compares AI v1 vs AI v2. Canary is about initial deployment; Versioning is about ongoing evolution.

**When to use:**
- Agents are in production and changes carry risk of quality regression
- Multiple people modify agent configurations (prompts, tools, parameters)
- You need rollback capability when a change underperforms
- You want data-driven decisions about which agent configuration is better

**Tradeoffs:**
- **Pro:** Changes are reversible — bad deployments don't stick
- **Pro:** A/B testing produces real evidence, not guesswork
- **Pro:** Version history creates an audit trail of agent evolution
- **Con:** Requires infrastructure for traffic splitting and quality comparison
- **Con:** Slow — you need enough samples to reach statistical significance
- **Con:** Some changes are hard to A/B test (personality/tone changes require subjective judgment)

**Key decisions:**
- Version scope: whole agent? individual prompts? tool configurations?
- Traffic splitting: percentage-based? by task type? by client?
- Comparison metric: automated quality scores? human evaluation? downstream outcomes?
- Rollback trigger: automatic (metric threshold) or manual (human reviews data)?

**Notes:** Pairs with **Prompt Configuration** (what gets versioned), **Canary & Shadow Mode** (initial deployment strategy), **Warm-up & Calibration** (test against historical cases before live traffic), and **Decision Calibration** (track whether versioning decisions led to actual improvements).

## Examples

TODO: Add concrete examples from real usage.

---

### Agent Workspace (`agent-workspace`)  `setup`

***Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly***

**Tags:** `setup`

**Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly**

Frontload permissions, create an isolated environment, fork a context-rich session, assemble context from all relevant sources, then start working.

**When to use:**
- Agent needs to operate on a codebase or project with multiple context sources
- Parallel tasks must not contaminate each other
- The environment has permission gates that could block mid-task

## Examples

TODO: Add concrete examples from real usage.

---

### Background Observation (`background-observation`)  `learning` `monitoring`

*Non-blocking data collection decoupled from analysis.*

**Tags:** `learning` `monitoring`

Non-blocking data collection decoupled from analysis. Hooks or event listeners write observations to a queue (JSONL file, event stream, database). A separate background agent processes the queue asynchronously. The main workflow is never slowed by observation.

```
Main Workflow (uninterrupted)
  │
  ├─ PreToolUse hook → writes to observations.jsonl
  ├─ PostToolUse hook → writes to observations.jsonl
  │
  └─ (continues working, zero latency impact)

Background Observer (async, low-cost model)
  │
  ├─ Reads observations.jsonl periodically
  ├─ Detects patterns, errors, user corrections
  └─ Creates learnings → feeds into Memory & Retrieval
```

**Different from Watchdog:** **Watchdog** monitors for anomalies and *halts* execution. **Background Observation** passively collects data for *learning*. Watchdog is a safety mechanism; Background Observation is a learning mechanism.

**When to use:**
- You want the system to learn from its own behavior without slowing down
- Observation collection must be cheap and non-blocking
- Analysis can happen later (seconds, minutes, or end-of-session)

**Tradeoffs:**
- **Pro:** Zero performance impact on the main workflow
- **Pro:** Can capture 100% of interactions (hooks are reliable)
- **Pro:** Background analysis can use cheaper models (Haiku) since it's not latency-sensitive
- **Con:** Observations queue can grow large if not processed regularly
- **Con:** Learning is delayed — patterns aren't available until the background agent processes them
- **Con:** Queue format must be stable and parseable

**Notes:** Feeds into **Memory & Retrieval** (observations become memories), **Scoped Promotion** (learnings start project-scoped), and **Confidence Signaling** (learnings carry confidence from evidence count).

## Examples

TODO: Add concrete examples from real usage.

---

### Bayesian Steering (`bayesian-steering`)  `decisions` `learning`

*The system maintains hypotheses with probabilities.*

**Tags:** `decisions` `learning`

The system maintains hypotheses with probabilities. Actions are chosen to maximize expected information gain. After each observation, beliefs update via Bayes' rule.

```
Hypotheses (with priors) → Select action maximizing E[info gain] → Execute
         ↑                                                            │
         └──────────── Update posteriors with observation ────────────┘
```

**When to use:**
- Iterative process with a budget (time, money, compute)
- Each iteration produces results bearing on multiple hypotheses
- Meaningful priors exist (historical data, domain knowledge)

**Tradeoffs:**
- **Pro:** Provably optimal resource allocation for uncertainty reduction
- **Pro:** Natural stopping criteria (Bayes factor thresholds)
- **Pro:** Priors from historical data encode institutional knowledge
- **Con:** Requires well-defined hypothesis space
- **Con:** Prior miscalibration can misdirect early iterations
- **Con:** More computationally complex than simple heuristics

**Key decisions:**
- Prior source: expert judgment, historical data, literature, uninformative?
- Hypothesis granularity: broad or specific?
- Multi-hypothesis actions: can one action update multiple hypotheses? (Yes — this is where efficiency comes from)

**Notes:** Pairs with **Memory & Retrieval** (historical data informs priors), **Escalation Ladder** (escalate modality as uncertainty narrows), and **Checkpoint & Resume** (save hypothesis state across sessions).

## Examples

TODO: Add concrete examples from real usage.

---

### Budget-Aware Execution (`budget-aware-execution`)  `cost` `decisions`

*Agents know their cost budget and make quality/cost tradeoffs accordingly.*

**Tags:** `cost` `decisions`

Agents know their cost budget and make quality/cost tradeoffs accordingly. An orchestrator allocates budget to subtasks based on their importance and difficulty. Agents choose which quality patterns to apply based on their allocation.

```
Orchestrator: "Generate content variants. Budget: $5 LLM cost. Importance: high."

Agent reasoning:
  - $5 budget, high importance
  - Redundant Generation (3 agents) = ~$3
  - Hybrid Synthesis = ~$1
  - Verification Loop = ~$1
  - Total: $5 → use full quality stack

vs.

Orchestrator: "Format results for display. Budget: $0.50 LLM cost. Importance: low."

Agent reasoning:
  - $0.50 budget, low importance
  - Reflection only = ~$0.30
  - Total: $0.30 → use budget quality play
```

**When to use:**
- Total system budget is constrained
- Not all subtasks deserve the same quality investment
- You want the system to be cost-aware without manually tuning every step

**Tradeoffs:**
- **Pro:** Automatically allocates quality effort where it matters most
- **Pro:** Prevents the Kitchen Sink anti-pattern — expensive patterns used only when justified
- **Pro:** Makes cost predictable and auditable
- **Con:** Budget estimation is imprecise — actual LLM costs vary
- **Con:** Agents may under-invest in tasks that seem unimportant but turn out to matter

**Key decisions:**
- Budget unit: dollars? tokens? abstract "quality points"?
- Allocation strategy: orchestrator decides up-front? agents negotiate? fixed percentages?
- Over-budget handling: hard stop? borrow from reserve? alert human?

**Notes:** Natural partner to **Confidence Signaling** (high confidence → spend less on verification) and **Escalation Ladder** (start cheap, escalate only if needed).


**Router-agent architecture:**
A practical implementation combines three agents: a Router (classifies input complexity and selects the appropriate model/pipeline), an Answering Agent (executes with the selected resources), and a Critique Agent (evaluates response quality and feeds back into routing logic to improve allocation over time).

**Scaling Inference Law:** LLM performance predictably improves with increased compute at inference time. A smaller model with more "thinking budget" (structured reasoning steps, self-correction passes) can surpass a larger model with simpler generation. This provides the theoretical foundation for budget allocation decisions — investing in inference compute is a legitimate alternative to model upgrades.

## Examples

TODO: Add concrete examples from real usage.

---

### Canary & Shadow Mode (`canary`)  `deployment`

*Run the new system in parallel with the existing human process.*

**Tags:** `deployment`

Run the new system in parallel with the existing human process. Compare outputs, but don't let AI outputs reach production. Build confidence before switching over.

```
Client Request → Human Process → Production Output
              → AI Process → Shadow Output (logged, not delivered)
              → Compare → Learning
```

**When to use:**
- Replacing an existing human process with AI
- You need to demonstrate equivalence or superiority before switching
- Stakeholders need to see the system working before they trust it

**Differs from Warm-up:** Warm-up uses historical cases. Canary uses live cases in real time, but shields the client from the AI output.

## Examples

TODO: Add concrete examples from real usage.

---

### Cascade & Fallback (`cascade-fallback`)  `reliability`

*Primary agent attempts the task.*

**Tags:** `reliability`

Primary agent attempts the task. On failure, system falls back to alternative agent/approach. Each level has different characteristics, not necessarily "better."

```
Primary → success → done
       → failure → Fallback A → success → done
                              → failure → Fallback B → ...
```

**When to use:**
- Reliability is critical — you need *some* output
- Different approaches have different failure modes
- Integrating external services that may be unavailable

**Tradeoffs:**
- **Pro:** Dramatically improves system reliability
- **Con:** Fallback quality may be lower — inconsistent experience
- **Con:** Silent quality degradation if not monitored


**Distinction from Routing:** Cascade & Fallback is *failure-triggered* — try the primary, fall back on failure. **Routing** is *classification-triggered* — classify the input and dispatch to the best handler directly. Both select among alternatives, but the trigger mechanism and error model are different. Cascade assumes a preferred option that might fail; Routing assumes multiple equally valid options selected by input characteristics.

## Examples

TODO: Add concrete examples from real usage.

---

### Catalog (`catalog`)  `context`

*A shared, maintained document that names and defines the concepts a team uses.*

**Tags:** `context`

A shared, maintained document that names and defines the concepts a team uses. By giving things names, teams can discuss architecture at a higher level of abstraction ("let's use Adversarial Review here" instead of re-explaining the red team / blue team / judge structure every time).

**Why it matters:**
- Shared vocabulary reduces miscommunication
- New team members can learn the playbook
- Compositions become discussable ("this is a Quality Stack with Ethics Gating")
- Prevents reinventing the same thing under different names

**Maintenance:** A catalog is a living document. Entries are added when they're proven in at least one implementation, refined when experience reveals nuances, and deprecated when better alternatives emerge.

## Examples

TODO: Add concrete examples from real usage.

---

### Checkpoint & Resume (`checkpoint-resume`)  `reliability`

*The ability to save system state, pause, and resume later.*

**Tags:** `reliability`

The ability to save system state, pause, and resume later. Critical for processes that span hours or days (e.g., waiting for a 24-hour test cycle to complete).

**When to use:**
- The process spans hours or days (e.g., waiting for external test cycles)
- Human reviewers may take significant time to approve intermediate results
- System failures are possible and accumulated state is expensive to recompute
- You want humans to be able to pause, inspect, adjust, and resume

**What to checkpoint:**
- Current hypothesis states (priors/posteriors)
- Budget spent and remaining
- Wave history and results
- Pending decisions and their context
- HITL approval states

**Tradeoffs:**
- **Pro:** Process survives across sessions, crashes, and human delays
- **Pro:** Enables "pause and think" — human can intervene, adjust, resume
- **Con:** Checkpoint format must be versioned — schema changes can break resumability
- **Con:** Resuming from stale state can produce inconsistent results if the world changed while paused

**Key decisions:**
- Storage format: JSON files? database records? git commits?
- Checkpoint frequency: every step? every N steps? at HITL gates only?
- Staleness detection: how do you know if the world changed since the checkpoint was saved?

## Examples

TODO: Add concrete examples from real usage.

---

### Confidence Signaling (`confidence-signaling`)  `quality` `cost` `decisions`

*Agents report their confidence level alongside their output.*

**Tags:** `quality` `cost` `decisions`

Agents report their confidence level alongside their output. Downstream agents or orchestrators use this signal to decide whether to verify, escalate, or accept. Low confidence triggers **Verification Loop** or **Redundant Generation**. High confidence allows skipping expensive quality checks.

```
Agent Output: {
  result: "Peer testimonial framing recommended",
  confidence: 0.85,
  confidence_rationale: "Strong historical signal from 47 similar studies"
}

Orchestrator: confidence > 0.8 → accept
              confidence 0.5-0.8 → verify
              confidence < 0.5 → escalate to redundant generation
```

**When to use:**
- You want adaptive quality assurance — not every output needs the same scrutiny
- Agents vary in how certain they are about different tasks
- You're budget-conscious and want to skip expensive checks when confidence is high

**Tradeoffs:**
- **Pro:** Enables cost-efficient quality assurance — expensive patterns only where needed
- **Pro:** Surfacing uncertainty is itself valuable information for downstream decisions
- **Con:** Agents may be miscalibrated — high confidence doesn't guarantee correctness
- **Con:** Agents may learn to game confidence scores if they're rewarded for high confidence

**Key decisions:**
- Confidence format: numeric (0-1)? categorical (low/medium/high)? multi-dimensional?
- Calibration: how do you verify that stated confidence correlates with actual accuracy?
- Routing rules: what confidence thresholds trigger which quality patterns?

**Notes:** Natural partner to **Verification Loop**, **Escalation Ladder**, and **Budget-Aware Execution**. The confidence signal is what drives adaptive routing through quality patterns.

## Examples

TODO: Add concrete examples from real usage.

---

### Configurable Human-in-the-Loop (`configurable-hitl`)  `coordination` `reliability`

*System defines checkpoints where human review may be required.*

**Tags:** `coordination` `reliability`

System defines checkpoints where human review may be required. Level of involvement is configurable along a spectrum. Set at engagement start, adjustable during execution.

```
Action → Checkpoint → Check config
  → Level 1 (Full Approval): Block until human approves
  → Level 2 (Supervised): Notify, auto-proceed after timeout
  → Level 3 (Autonomous): Log and proceed
```

**When to use:**
- Different users/clients have different risk tolerances
- Trust builds over time
- Regulatory requirements vary by domain

**Tradeoffs:**
- **Pro:** One system serves cautious to autonomous
- **Pro:** Trust builds naturally — start Level 1, graduate to Level 3
- **Con:** Must design for all levels (more complex)
- **Con:** Level 2 timeout can be dangerous if humans aren't actually monitoring

**Non-configurable:** Emergency stop. Always available. Every level.


**Variants:**
- **Plan approval checkpoint** — Human reviews and approves the agent's plan before execution begins, then the agent runs autonomously within the approved plan
- **Human-on-the-Loop** — Humans set policy constraints and guardrails; the agent executes autonomously within those bounds without per-action approval. Distinct from Level 3 (Autonomous) because the human actively designs the policy, not just disengages. Examples: trading rules that bound agent behavior, call-routing policies that define escalation criteria

## Examples

TODO: Add concrete examples from real usage.

---

### Content Factory (`content-factory`)  `quality` `divergent` `convergent`

***Specialization Ensemble** → **Redundant Generation** → **Tournament Selection** → **Hybrid Synthesis** → **Ethics Gating***

**Tags:** `quality` `divergent` `convergent`

**Specialization Ensemble** → **Redundant Generation** → **Tournament Selection** → **Hybrid Synthesis** → **Ethics Gating**

Experts analyze the brief from different angles, multiple agents generate, tournament selects, synthesis combines strengths, ethics reviews.

**When to use:**
- High-volume creative content production
- Quality must be consistently high across varied briefs
- Content has ethical, brand, or regulatory constraints

## Examples

TODO: Add concrete examples from real usage.

---

### Multi-Source Context Assembly (`context-assembly`)  `context` `setup`

*Gather context from multiple heterogeneous sources in parallel, then synthesize into a unified brief before work begins.*

**Tags:** `context` `setup`

Gather context from multiple heterogeneous sources in parallel, then synthesize into a unified brief before work begins. Different from **Decomposition & Reassembly** (which breaks a *task* apart) — this assembles *context* from existing sources.

```
Linear ticket ──┐
PR history     ──┼→ Parallel fetch → Synthesis Agent → Unified Brief → Ready to work
Figma designs  ──┤
Doc links      ──┤
Comments       ──┘
```

**When to use:**
- Work requires understanding from multiple systems (ticketing, code, design, docs)
- Context sources are independent and can be fetched in parallel
- The agent doing the work shouldn't have to know where context lives

**Tradeoffs:**
- **Pro:** Agent starts work with complete context, not a partial view
- **Pro:** Parallel fetching minimizes wall-clock time
- **Pro:** Synthesis step eliminates redundancy and contradiction across sources
- **Con:** Synthesis can lose important nuance from individual sources
- **Con:** Some sources may be unavailable — need graceful degradation

## Examples

TODO: Add concrete examples from real usage.

---

### Context Windowing (`context-windowing`)  `context`

*The general principle of deliberately curating what information an agent sees.*

**Tags:** `context`

The general principle of deliberately curating what information an agent sees. Too much context = noise and distraction. Too little = blind spots and bad decisions. This is the umbrella pattern; **TOC Index** and **Retrieval Subagent** are specific implementations.

**When to use:**
- The total available context exceeds what an agent can process effectively
- Different agents need different slices of the same information
- Sensitive information should only be visible to certain agents

**Techniques:**
- **Relevance filtering** — only include context related to the current subtask
- **Summarization layers** — compress verbose context into key points
- **Progressive disclosure** — start with summary, let agent request detail
- **Role-based access** — ethics agent sees everything, content generator sees only the brief

**Context efficiency progression:**
```
Full context (naive) → Context Windowing (curated) → TOC Index (indexed) → Retrieval Subagent (delegated)
```
Each level trades latency for context efficiency.

**Implementations:** **TOC Index** and **Retrieval Subagent** are specific implementations of this pattern, listed separately below because they're substantial enough to stand alone.

## Examples

TODO: Add concrete examples from real usage.

---

### Contract Interface (`contract-interface`)  `coordination` `reliability`

*Define strict input/output schemas between agents.*

**Tags:** `coordination` `reliability`

Define strict input/output schemas between agents. Like API contracts between microservices. Each agent declares what it expects to receive and what it promises to return. Prevents agents from passing ambiguous blobs to each other.

```
Agent A                          Agent B
  │                                │
  ├─ Output Schema: {              ├─ Input Schema: {
  │    hypothesis: string,         │    hypothesis: string,
  │    prior: float 0-1,           │    prior: float 0-1,
  │    evidence: string[],         │    evidence: string[],
  │    confidence: enum            │    confidence: enum
  │  }                             │  }
  │                                │
  └──────── validated handoff ─────┘
```

**When to use:**
- 5+ agents in a pipeline — ambiguity compounds at each handoff
- Different teams build different agents — contracts are the integration surface
- You need to swap out an agent without breaking downstream consumers
- Debugging: when something goes wrong, contracts tell you which agent broke the contract

**Tradeoffs:**
- **Pro:** Eliminates "what did the previous agent mean by this?" problems
- **Pro:** Enables independent development and testing of agents
- **Pro:** Failed validation catches errors at handoff, not three steps later
- **Con:** Schema design is work — over-constraining limits agent flexibility
- **Con:** Schema evolution requires coordination (versioning)

**Key decisions:**
- Strictness: hard validation (reject if non-conforming) or soft (warn and attempt)?
- Schema language: JSON Schema? TypeScript types? Natural language spec?
- Versioning: how do you evolve contracts without breaking existing agents?


**Agent Card variant:** A machine-readable capability manifest declaring an agent's identity, skills, supported I/O modes, authentication requirements, and endpoint URL. Extends the contract concept from schema agreements to full capability advertisement, enabling **Agent Discovery**.

**Contractor Model (formalized contracts):**
Evolving from simple schema contracts to rich, negotiable specifications:
1. **Formalized spec** — The contract is a detailed document (deliverables, scope, data sources, cost, completion criteria) serving as single source of truth
2. **Negotiation** — The agent can flag ambiguities, request clarification, or propose scope adjustments before committing
3. **Iterative self-validation** — Internal generate-review-improve loop against the contract's criteria before declaring completion
4. **Hierarchical subcontracts** — Complex contracts are decomposed into subcontracts delegated to specialist agents (project-manager-style)

## Examples

TODO: Add concrete examples from real usage.

---

### Debate & Consensus (`debate-consensus`)  `convergent` `decisions` `coordination`

*Multiple agents argue different positions in structured rounds.*

**Tags:** `convergent` `decisions` `coordination`

Multiple agents argue different positions in structured rounds. A moderator tracks agreement/disagreement. Process continues until consensus or max rounds, then moderator synthesizes.

```
Round 1: Agent A argues → Agent B argues → Agent C argues
Round 2: Agent A rebuts B,C → Agent B rebuts A,C → Agent C rebuts A,B
...
Moderator: Synthesizes agreement, flags unresolved disagreements
```

**When to use:**
- The question is genuinely ambiguous with multiple legitimate perspectives
- You want the reasoning, not just the conclusion
- The domain has real disagreement (ethics, strategy, creative direction)

**Tradeoffs:**
- **Pro:** Surfaces reasoning and tradeoffs a single agent might miss
- **Pro:** Debate transcript documents *why* a decision was made
- **Con:** Can be slow and expensive (3-10x cost)
- **Con:** Agents may converge too quickly (groupthink) or too slowly (circular arguments)

**Key decisions:**
- Assigned vs. organic positions
- Structured rounds (claim → evidence → rebuttal) vs. freeform
- Consensus threshold: unanimous? majority? moderator's judgment?


**Variants:**
- **Chain of Debates (CoD)** — Linear: agents argue in sequence, each responding to the previous speaker
- **Graph of Debates (GoD)** — Non-linear: arguments form a graph with support and refutation edges between nodes. Conclusions are found by identifying the most robust argument clusters. Richer than linear debate but harder to manage and synthesize

## Examples

TODO: Add concrete examples from real usage.

---

### Decision Calibration (`decision-calibration`)  `learning` `decisions`

*At the time of making a decision, record the decision, the reasoning, the predicted outcome, and a mandatory future review date.*

**Tags:** `learning` `decisions`

At the time of making a decision, record the decision, the reasoning, the predicted outcome, and a mandatory future review date. At review time, compare the prediction to the actual outcome. Use the delta to update decision-making heuristics.

```
Decide → Record prediction → Set review date → ... time passes ...
  → Review: Did we predict correctly? → Update beliefs / heuristics
```

**When to use:**
- The organization makes recurring decisions of similar types
- You want to get better at predicting outcomes over time
- Decisions are consequential enough to warrant structured review
- You want to build institutional memory about what works

**Tradeoffs:**
- **Pro:** Systematic improvement of decision quality over time
- **Pro:** Creates an audit trail of why decisions were made
- **Pro:** Surfaces overconfidence and blind spots
- **Con:** Requires discipline to actually do the review
- **Con:** Outcome quality is often ambiguous — hard to say definitively if a decision was "right"

**Relationship to Bayesian Steering:** This is **Bayesian Steering** applied to organizational decisions rather than automated experiments. The "priors" are the team's intuitions, the "test" is the real-world outcome, and the "posterior update" is the lesson learned.

## Examples

TODO: Add concrete examples from real usage.

---

### Decomposition & Reassembly (`decomposition-reassembly`)  `coordination`

*A complex task is broken into smaller subtasks, solved independently (potentially in parallel), then reassembled into a coherent whole.*

**Tags:** `coordination`

A complex task is broken into smaller subtasks, solved independently (potentially in parallel), then reassembled into a coherent whole.

```
Complex Task → Decomposer → Subtask 1 → Result 1 ─┐
                           → Subtask 2 → Result 2 ──┼→ Reassembly Agent → Final
                           → Subtask 3 → Result 3 ─┘
```

**When to use:**
- The task is too complex for a single agent
- Subtasks are relatively independent (low coupling)
- You want to parallelize execution

**Tradeoffs:**
- **Pro:** Makes complex tasks tractable and parallelizable
- **Con:** Bad decomposition = bad results
- **Con:** Information loss at boundaries — subtask agents lack full context
- **Con:** Reassembly must handle cross-subtask dependencies and ensure coherence

## Examples

TODO: Add concrete examples from real usage.

---

### Discovery Loop (`discovery-loop`)  `learning` `decisions`

***Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop***

**Tags:** `learning` `decisions`

**Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop**

Use information gain to decide what to explore, escalate modality as uncertainty narrows, learn from history, verify each step.

**When to use:**
- Iterative exploration with a budget constraint
- Each iteration should inform the next (not independent trials)
- Historical data exists to set meaningful priors


**Generate-Debate-Evolve variant (from scientific discovery systems):**
A richer instantiation using specialized agents: Generation agents produce hypotheses → Reflection agents critique them (peer review) → Ranking agents evaluate via Elo-style tournament → Evolution agents refine top candidates → Proximity agents cluster similar ideas → Meta-review agents synthesize across clusters. This mirrors the scientific method and is particularly effective for open-ended exploration where the solution space is poorly understood.

## Examples

TODO: Add concrete examples from real usage.

---

### Divergent Brainstorm (`divergent-brainstorm`)  `divergent` `coordination` `quality`

*Multiple agents independently generate ideas, approaches, or solutions without evaluating them.*

**Tags:** `divergent` `coordination` `quality`

Multiple agents independently generate ideas, approaches, or solutions without evaluating them. Quantity over quality. No filtering, no critique, no convergence — just raw option generation. Evaluation happens later via convergent patterns.

```
Prompt → Agent A generates ideas ─┐
Prompt → Agent B generates ideas ──┼→ Collect all → Deduplicate → Pass to convergent pattern
Prompt → Agent C generates ideas ─┘
```

**Different from Redundant Generation:** Redundant Generation gives agents the same task and judges pick the best *output*. Divergent Brainstorm asks agents to generate *many ideas each* — the goal is volume and variety, not polished outputs.

**When to use:**
- The solution space is large and you don't know where the best ideas live
- You want to avoid premature convergence (anchoring on the first decent idea)
- The downstream convergent pattern (Adversarial Review, Tournament Selection) needs a rich candidate pool

**Tradeoffs:**
- **Pro:** Surfaces non-obvious options that a single agent would never consider
- **Pro:** Different agent personas/temperatures produce genuinely different ideas
- **Pro:** Cheap per idea — agents generate without the overhead of evaluation
- **Con:** Produces many bad ideas alongside good ones — requires strong downstream filtering
- **Con:** Deduplication can be tricky when ideas overlap partially

**Key decisions:**
- Agent diversity: same prompt with different temperatures? different personas? different framings?
- Volume target: how many ideas per agent? When is enough enough?
- Deduplication: exact match? semantic similarity? human review?

**Notes:** Natural precursor to **Adversarial Review** (brainstorm then attack), **Tournament Selection** (brainstorm then compete), or **Redundant Generation** (brainstorm then judge). Pairs with **Persona Injection** to ensure genuine diversity of perspective.

## Examples

TODO: Add concrete examples from real usage.

---

### Escalation Ladder (`escalation-ladder`)  `cost` `quality` `decisions`

*Start with cheapest/fastest approach.*

**Tags:** `cost` `quality` `decisions`

Start with cheapest/fastest approach. If quality threshold isn't met, escalate to more expensive/slower/higher-quality approach. Continue up the ladder.

```
Level 1 (fast/cheap) → meets threshold? → yes → done
                                         → no  → Level 2 (slower/better) → ...
```

**When to use:**
- Wide range of task difficulty — many easy, some hard
- Natural ordering from cheap/fast to expensive/thorough
- You're exploring a space and want to narrow before investing in rich artifacts

**Tradeoffs:**
- **Pro:** Dramatic cost reduction when most tasks handled by lower levels
- **Pro:** Higher levels benefit from information gathered at lower levels
- **Con:** Escalation criteria must be well-calibrated

**Variants:**
- **Modality escalation** — text → image → video
- **Model escalation** — small model → large model
- **Agent escalation** — single agent → ensemble → full adversarial pipeline

**Notes:** Natural partner to **Confidence Signaling** (confidence drives escalation decisions) and **Budget-Aware Execution** (budget determines how far up the ladder you can go).

## Examples

TODO: Add concrete examples from real usage.

---

### Ethics Gating (`ethics-gating`)  `convergent` `quality` `reliability`

*Dedicated ethics agent evaluates plans/content/actions against codified ethical framework.*

**Tags:** `convergent` `quality` `reliability`

Dedicated ethics agent evaluates plans/content/actions against codified ethical framework. Hard veto power — can block any action regardless of other agents. Only human intervention can override.

```
Proposed Action → Ethics Agent → Approve → Execute
                               → Veto → Block + Explanation → Human Review
```

**When to use:**
- System outputs affect real people
- Defined ethical boundaries that must never be crossed
- Regulatory or organizational compliance requires audit trail

**Tradeoffs:**
- **Pro:** Prevents harmful outputs reaching production
- **Pro:** Audit trail; can be a positive selling point
- **Con:** False positives block legitimate work
- **Con:** Can only catch violations it's trained to recognize

**Key decisions:**
- Scope: plans only? content only? both?
- Framework source: regulatory, organizational, industry standards?
- Override mechanism: which humans, what escalation path?


**Scope beyond ethics:** While the core pattern is ethics-focused, production systems apply the same gating structure to broader safety concerns: jailbreak detection, off-topic filtering, brand safety, competitive information blocking, and regulatory compliance. The structural pattern is identical — a dedicated gate with veto power — but the evaluation criteria differ.

**Variants:**
- **Rule-based** — Allow/deny lists, regex filters, schema validation. Fast and deterministic but brittle against novel threats
- **LLM-as-guardrail** — A fast, cheap model acts as a dedicated policy enforcer, screening inputs/outputs against detailed safety directives. Semantically aware — catches threats that rules miss (prompt injection, subtle policy violations)
- **Layered defense** — Input gate (pre-processing) + behavioral constraints (prompt-level) + tool-use restrictions (callback-based) + output gate (post-processing). Defense in depth

## Examples

TODO: Add concrete examples from real usage.

---

### Graceful Degradation (`graceful-degradation`)  `quality` `reliability`

*When an agent produces a *subtly wrong* result — not a hard failure, but a partial success — the system detects the quality shortfall and degrades gracefully rather than propagating a flawed output or*

**Tags:** `quality` `reliability`

When an agent produces a *subtly wrong* result — not a hard failure, but a partial success — the system detects the quality shortfall and degrades gracefully rather than propagating a flawed output or failing entirely. Different from Cascade & Fallback (which handles hard failures) and Verification Loop (which retries until pass). This pattern accepts that the output is imperfect and chooses the best available response.

```
Agent output → Quality assessment → Full quality? → proceed normally
                                  → Partial quality? → degrade gracefully:
                                      → Use output with caveats/disclaimers
                                      → Use output for low-stakes path only
                                      → Return partial result + flag for human review
                                      → Fall back to cached/stale version
                                  → Unacceptable? → hard fail (Cascade & Fallback)
```

**When to use:**
- Outputs exist on a quality spectrum, not a binary pass/fail
- A partial or caveated result is better than no result
- Downstream consumers can handle varying quality levels
- The system needs to keep running even when some components underperform

**Tradeoffs:**
- **Pro:** System stays available even when quality is imperfect
- **Pro:** Explicit quality signals let downstream consumers adjust their behavior
- **Con:** Silent quality degradation can compound — a "good enough" result used as input produces worse downstream output
- **Con:** Defining the quality spectrum (full/partial/unacceptable) requires domain expertise

**Key decisions:**
- Quality assessment: automated scoring? confidence threshold? domain-specific heuristics?
- Degradation strategy: caveats? scope reduction? human escalation? stale cache?
- Transparency: does the consumer know they're getting a degraded result?

**Notes:** Often works with **Confidence Signaling** (confidence score drives the quality assessment). Pairs with **Watchdog** (track degradation frequency — if it's always degrading, something is wrong).

## Examples

TODO: Add concrete examples from real usage.

---

### Hybrid Synthesis (`hybrid-synthesis`)  `convergent` `quality`

*Given multiple outputs, a synthesis agent identifies the strongest elements of each and combines them into a single superior output.*

**Tags:** `convergent` `quality`

Given multiple outputs, a synthesis agent identifies the strongest elements of each and combines them into a single superior output. Not selecting a winner — extracting and recombining the best parts.

```
Output A ─┐                    ┌→ Strength Analysis
Output B ──┼→ Synthesis Agent ──┼→ Combination Strategy
Output C ─┘                    └→ Synthesized Output
```

**When to use:**
- Multiple outputs each have different strengths
- No single attempt nails every dimension
- You're willing to spend additional compute for higher quality

**Tradeoffs:**
- **Pro:** Can produce outputs strictly better than any individual attempt
- **Con:** Synthesis can introduce incoherence if elements don't compose well
- **Con:** Requires deep task understanding to judge what "best parts" means

**Notes:** Almost always follows **Redundant Generation**. Often followed by **Verification Loop**.

## Examples

TODO: Add concrete examples from real usage.

---

### Inversion of Control (`inversion-of-control`)  `coordination` `communication`

*The agent drives the process; the human (or calling agent) provides input on demand.*

**Tags:** `coordination` `communication`

The agent drives the process; the human (or calling agent) provides input on demand. Instead of "human tells agent what to do," the agent asks the human targeted questions, drives through a framework, and assembles the result. The agent has better judgment about *process*; the human has better judgment about *content*.

```
Traditional:    Human → "Do X" → Agent → Output
Inverted:       Agent → "What is your goal?" → Human answers
                Agent → "What constraints?" → Human answers
                Agent → "Here are 3 options..." → Human picks
                Agent → Output
```

**Applies at multiple levels:**
- **Agent ↔ Human** — Planning Agent interviews the client instead of taking a brief
- **Agent ↔ Agent** — Orchestrator asks a subagent "what should I do next?" and follows its recommendation
- **Skill ↔ User** — `/decide` drives the user through a decision framework rather than accepting a pre-formed decision

**When to use:**
- The process has known structure but the content is unique each time
- Humans skip important steps when left to drive themselves (incomplete briefs, missing constraints)
- You want consistent, thorough process regardless of who the human is
- The agent has access to a framework or checklist the human might not know

**Tradeoffs:**
- **Pro:** Ensures completeness — the agent asks about things humans forget
- **Pro:** Consistent process quality regardless of human expertise level
- **Pro:** Captures structured data that downstream agents can consume directly
- **Con:** Can feel paternalistic if the human already knows what they want
- **Con:** Rigid interview flows frustrate expert users — consider adaptive depth
- **Con:** Agent must handle unexpected answers gracefully (humans go off-script)

**Key decisions:**
- Adaptive vs. fixed flow: does the agent skip questions based on prior answers?
- Escape hatch: can the human say "just take this brief and run with it"?
- Depth calibration: expert users get fewer questions, novices get more?

**Notes:** Natural entry point for **Adversarial Review** (agent interviews, then red-teams the result) and **Configurable HITL** (the interview itself sets the HITL level for execution).

## Examples

TODO: Add concrete examples from real usage.

---

### Learning Loop (`learning-loop`)  `learning`

***Background Observation** → **Memory & Retrieval** → **Scoped Promotion** → **Decision Calibration***

**Tags:** `learning`

**Background Observation** → **Memory & Retrieval** → **Scoped Promotion** → **Decision Calibration**

Passively observe agent behavior, store learnings in scoped memory, promote proven patterns to broader scope, review decisions to calibrate future heuristics.

**When to use:**
- The system operates across multiple projects or engagements
- You want institutional memory that compounds over time
- Learnings should be validated before being applied broadly


**Variants:**
- **Self-modification** — The agent reviews an archive of its own past versions and performance scores, proposes modifications to its own codebase or prompts, tests the modifications, and records results. Requires containerized execution and an asynchronous overseer for safety
- **Evolutionary optimization** — An ensemble of LLMs generates code/algorithm proposals, automated evaluators score them, and an evolutionary selection process iteratively refines the population. Combines **Tournament Selection** with LLM-generated mutations

## Examples

TODO: Add concrete examples from real usage.

---

### Memory & Retrieval Augmentation (`memory-retrieval`)  `context` `learning`

*Agents query a knowledge base to inform decisions.*

**Tags:** `context` `learning`

Agents query a knowledge base to inform decisions. May contain structured data, past outputs, historical results, or domain knowledge. Retrieval can be keyword, semantic, or structured queries.

```
Agent receives task → Queries knowledge base → Incorporates context → Produces output
```

**When to use:**
- Decisions should be informed by historical data or domain knowledge
- Knowledge base is too large for every prompt
- System should get smarter over time as knowledge base grows

**Tradeoffs:**
- **Pro:** Grounds decisions in real data, not just parametric knowledge
- **Pro:** Knowledge base improves over time — compounding advantage
- **Con:** Retrieval quality is critical — bad retrievals degrade output
- **Con:** Knowledge base requires curation and maintenance

**Variants:**
- **Read-only** — agents query, can't write (externally curated)
- **Read-write** — agents add to the knowledge base (learning loop)
- **Episodic** — records of specific past experiments
- **Semantic** — generalized knowledge extracted from episodes


**Memory taxonomy (from cognitive science):**
- **Semantic memory** — Facts, preferences, and domain knowledge (e.g., "user prefers dark mode," "client's fiscal year ends in March"). Stored as profiles, document collections, or knowledge graphs
- **Episodic memory** — Records of specific past experiences (e.g., "last deployment failed due to migration timeout"). Often implemented as few-shot examples or case libraries
- **Procedural memory** — Rules, instructions, and behavioral norms (e.g., system prompts, CLAUDE.md). Can be updated via reflection — the agent rewrites its own instructions based on experience

**Retrieval backends:**
- **Vector database** — Semantic similarity search over embeddings. Good for conceptual relevance, poor for exact matches
- **Knowledge graph** — Entity-relationship traversal. Excels at synthesizing fragmented, multi-document answers but requires significant graph construction effort
- **Hybrid** — Combine keyword search (BM25) with vector search to capture both literal matches and conceptual relevance

**Managed memory extraction:** A background service analyzes conversation histories to automatically extract key facts, stores them by scope (user, project, global), and consolidates/resolves contradictions over time.

## Examples

TODO: Add concrete examples from real usage.

---

### Orchestrator-Subagent (`orchestrator-subagent`)  `coordination`

*A single orchestrator agent holds the overall goal and state.*

**Tags:** `coordination`

A single orchestrator agent holds the overall goal and state. It delegates specific tasks to specialized subagents, collects their outputs, and decides what to do next. Subagents have no awareness of each other or the broader plan — they receive a task and return a result.

**When to use:**
- The overall task requires coordination across multiple capabilities
- You need a single point of control for state, budget, and decision-making
- Subtasks are relatively independent and can be specified clearly

**Tradeoffs:**
- **Pro:** Clear accountability. The orchestrator owns the outcome.
- **Pro:** Subagents can be simple and focused — easier to build, test, and swap.
- **Con:** Single point of failure. If the orchestrator makes a bad decision, subagents can't correct it.
- **Con:** The orchestrator needs enough context to delegate well, which can be a bottleneck.

**Variants:**
- **Flat** — orchestrator talks to all subagents directly
- **Hierarchical** — orchestrators delegate to sub-orchestrators (fractal)
- **Dynamic** — orchestrator decides at runtime which subagents to invoke


**Communication topologies:**
- **Flat (Supervisor)** — Orchestrator talks to all subagents directly. Simple but doesn't scale
- **Hierarchical** — Orchestrators delegate to sub-orchestrators, each overseeing a tier below. Enables structured scalability for large systems
- **Network (Peer-to-Peer)** — Agents communicate directly with each other without a central coordinator. Resilient but hard to maintain coherent decision-making
- **Agent-as-Tool** — A subagent is wrapped as a callable tool, making invocation look like a function call. Reduces autonomy but simplifies integration and makes the agent composable with any tool-using system

## Examples

TODO: Add concrete examples from real usage.

---

### Output Posture (`output-posture`)  `communication`

*How assertive and proactive the agent is in its communication.*

**Tags:** `communication`

How assertive and proactive the agent is in its communication. A spectrum from "just answer what was asked" to "actively drive the conversation forward." Configured per agent, per context, or per user preference.

```
Passive:     User asks → Agent answers → stops
Suggestive:  User asks → Agent answers → "You might want to also consider X"
Proactive:   User asks → Agent answers → "Here's what I'd do next: ..." → drives forward
Opinionated: User asks → Agent recommends → "I'd go with B because ..." → defends position
```

**Named postures:**
- **Passive** — answer only what's asked, add nothing. Good for expert users who know what they want.
- **Suggestive** — answer, then offer a next step or related consideration. Good default for most interactions.
- **Proactive** — actively suggest the next action and offer to execute it. Good for workflows where the agent should drive.
- **Opinionated** — lead with a recommendation and rationale. Good for decision support where the human wants a point of view, not a menu.

**When to use:**
- Different users want different levels of agent initiative (experts vs. novices)
- Different tasks call for different postures (brainstorming → proactive, code review → passive)
- You want agents to feel helpful without being overbearing

**Tradeoffs:**
- **Pro:** Matching posture to context makes agents feel natural rather than robotic or pushy
- **Pro:** Proactive posture catches things the user didn't think to ask about
- **Con:** Wrong posture is jarring — proactive when the user wants passive feels paternalistic
- **Con:** Opinionated agents can anchor the human on a premature conclusion

**Key decisions:**
- Default posture: suggestive is usually safest
- Override mechanism: can the user say "just answer, don't suggest"?
- Task-adaptive: should posture shift automatically based on task type?

**Notes:** Pairs with **Inversion of Control** (proactive posture is a light version of IoC). Interacts with **Addressable Output** (opinionated posture should still present alternatives, just with a clear recommendation).

## Examples

TODO: Add concrete examples from real usage.

---

### Output Register (`output-register`)  `communication`

*How the agent calibrates detail level, language complexity, and information density.*

**Tags:** `communication`

How the agent calibrates detail level, language complexity, and information density. Not about what to say — about how to say it. Like a musician adjusting volume and tempo to the room.

**Named registers:**
- **Brief** — short, direct, minimal. Lead with the answer. Skip reasoning unless asked. Good for experienced users, simple tasks, chat-style interaction.
- **Detailed** — thorough, includes reasoning and context. Good for complex decisions, unfamiliar domains, documentation-style output.
- **Simple** — plain language, short sentences, no jargon. Good for broad audiences, client-facing content, cross-functional communication.
- **Dense** — high conceptual density, assumes shared vocabulary, packs maximum information per sentence. Good for expert-to-expert communication, technical specs, internal notes.
- **Pedagogical** — explains concepts as it goes, builds understanding, uses examples and analogies. Good for teaching, onboarding, knowledge transfer.

**When to use:**
- Agent output goes to audiences with different expertise levels
- The same information needs different presentations (executive summary vs. technical deep-dive)
- User preference varies — some people want "just the answer," others want the full reasoning chain

**Tradeoffs:**
- **Pro:** Matching register to audience dramatically improves comprehension and trust
- **Pro:** Same agent can serve expert and novice users by shifting register
- **Con:** Wrong register wastes time (too detailed) or loses information (too brief)
- **Con:** Dense register can feel exclusionary; Simple register can feel condescending

**Key decisions:**
- Default register: Brief or Detailed? Depends on the primary audience.
- Audience detection: explicit configuration? inferred from the user's own language? task-based?
- Mixing: can an agent use Brief for the answer and Detailed for the appendix?

**Notes:** Pairs with **Persona Injection** (persona may imply a default register) and **Output Posture** (posture and register are independent axes — you can be Brief+Proactive or Detailed+Passive).

## Examples

TODO: Add concrete examples from real usage.

---

### Permission Warm-up (`permission-warmup`)  `setup`

*Before starting real work, identify every distinct permission category the plan requires and trigger each one with a small, harmless, *relevant* operation.*

**Tags:** `setup`

Before starting real work, identify every distinct permission category the plan requires and trigger each one with a small, harmless, *relevant* operation. This frontloads all access prompts to the beginning of execution, so the agent can confirm it has the access it needs before investing effort that might be blocked mid-stream.

```
Plan work → Identify permission categories (file writes, MCP tools, shell commands, git, etc.)
  → For each category: trigger with small, relevant operation
    (e.g., read the first file you'll actually edit, run a benign form of the command you'll use)
  → All granted? → Proceed with real work
  → Any denied? → Stop and discuss before proceeding
```

**When to use:**
- The agent operates in a permission-gated environment (approval prompts, sandboxes, ACLs)
- The plan touches multiple permission categories that the user must approve
- Mid-task permission denial would waste significant work already done
- You want the human to see the full scope of access needed up front, not piecemeal

**Tradeoffs:**
- **Pro:** No wasted work — if a permission is denied, you find out before investing effort
- **Pro:** Human sees the full access scope at once, which builds trust and reduces surprise
- **Pro:** Forces the agent to plan before acting — the permission audit is itself a planning step
- **Con:** Adds a small upfront latency cost for the warm-up operations
- **Con:** Warm-up operations must be genuinely relevant — contrived triggers feel like busywork

**Key decisions:**
- Granularity: warm up every individual file, or one file per permission category?
- Failure handling: if one category is denied, abort entirely or proceed with reduced scope?
- Caching: if permissions were granted in a recent session, skip warm-up?

**Notes:** Natural partner to **Configurable HITL** (warm-up happens at the most restrictive HITL level). Pairs with **Provenance** (log which permissions were requested and granted).

## Examples

TODO: Add concrete examples from real usage.

---

### Persona Injection (`persona-injection`)  `context` `setup`

*Giving an agent a specific identity, expertise, or perspective to shape its behavior.*

**Tags:** `context` `setup`

Giving an agent a specific identity, expertise, or perspective to shape its behavior. More than a system prompt — it includes domain knowledge, decision-making frameworks, and behavioral norms.

**When to use:**
- You want agents specialized for specific industries or client types
- Different agents in the same system need genuinely different perspectives
- You want consistent behavior across sessions

**Examples:**
- Healthcare persuasion specialist (knows FDA messaging rules, health literacy levels)
- Political campaign strategist (knows FEC rules, voter psychology research)
- CPG brand expert (knows category dynamics, retail media norms)

**Key decisions:**
- Static vs. dynamic personas (fixed at design time or assembled at runtime from components?)
- Persona depth: light touch (a paragraph) or deep (pages of domain knowledge)?
- Persona testing: how do you verify the persona produces the right behavioral changes?

## Examples

TODO: Add concrete examples from real usage.

---

### Planning Pipeline (`planning-pipeline`)  `quality` `convergent` `coordination`

***Orchestrator-Subagent** → **Adversarial Review** → **Debate & Consensus** → **Ethics Gating** → **Configurable HITL***

**Tags:** `quality` `convergent` `coordination`

**Orchestrator-Subagent** → **Adversarial Review** → **Debate & Consensus** → **Ethics Gating** → **Configurable HITL**

Orchestrator builds the plan with subagents, red team attacks it, judges debate, ethics reviews, human approves.

**When to use:**
- The plan commits significant resources (budget, time, reputation)
- Multiple stakeholder perspectives must be represented
- Ethical or regulatory review is required before execution

## Examples

TODO: Add concrete examples from real usage.

---

### Prioritization (`prioritization`)  `decisions` `cost`

*Agents assess and rank competing tasks, objectives, or actions based on urgency, importance, dependencies, resource availability, and cost/benefit.*

**Tags:** `decisions` `cost`

Agents assess and rank competing tasks, objectives, or actions based on urgency, importance, dependencies, resource availability, and cost/benefit. Ensures focus on the most critical work first. Distinct from **Budget-Aware Execution** (which manages *resource allocation*) — Prioritization manages *task ordering*.

```
Task Queue → Prioritization Agent → Ranked Tasks
  → Execute highest priority
  → Re-prioritize when circumstances change (new events, completed tasks, deadlines)
```

**When to use:**
- An agent must autonomously manage multiple, potentially conflicting tasks
- Resources (time, compute, budget) are insufficient to do everything at once
- Priorities shift dynamically as new information arrives

**Tradeoffs:**
- **Pro:** Prevents wasted effort on low-value tasks when high-value work is waiting
- **Pro:** Dynamic re-prioritization keeps the system adaptive to changing conditions
- **Con:** Sophisticated ranking criteria require more computation
- **Con:** Low-priority tasks may starve if re-prioritization always favors new urgent work

**Levels:**
- **Strategic** — Which goals to pursue (OKR-level)
- **Tactical** — Which plan steps to execute next (within a goal)
- **Immediate** — Which action to take right now (within a step)

**Key decisions:**
- Ranking criteria: urgency? importance? dependencies? cost/benefit ratio? Weighted combination?
- Re-prioritization trigger: on every new task? on schedule? on significant events only?
- Starvation prevention: age-based priority boost? reserved capacity for low-priority work?

**Notes:** Natural partner to **Budget-Aware Execution** (budget constrains how far down the priority list you can go) and **Rate Limiting & Backpressure** (backpressure signals trigger re-prioritization).

## Examples

TODO: Add concrete examples from real usage.

---

### Prompt Configuration (`prompt-configuration`)  `setup` `quality`

*Treat prompt templates as first-class configurable artifacts — versioned, tested, and swappable without code changes.*

**Tags:** `setup` `quality`

Treat prompt templates as first-class configurable artifacts — versioned, tested, and swappable without code changes. Prompts are not hardcoded strings; they're configuration that shapes agent behavior, and they deserve the same rigor as any other configuration.

```
Prompt template (versioned, stored externally)
  → Variables injected at runtime (context, task, constraints)
  → Agent executes with assembled prompt
  → Output quality tracked per prompt version
  → A/B test: version A vs version B on same inputs → compare quality
```

**Different from Persona Injection:** Persona Injection shapes *who the agent is* (identity, expertise, norms). Prompt Configuration shapes *how the agent is instructed* (task framing, output format, constraints). A persona is one component that might be assembled into a prompt configuration.

**When to use:**
- Multiple people tune prompts and need version control / rollback
- You want to A/B test different prompt strategies on the same task
- Prompt changes are frequent and shouldn't require code deployments
- You need an audit trail of which prompt version produced which outputs

**Tradeoffs:**
- **Pro:** Prompts can be iterated without code changes — faster experimentation
- **Pro:** Version history enables rollback when a new prompt underperforms
- **Pro:** A/B testing reveals which prompt strategies actually work vs which seem clever
- **Con:** Adds infrastructure — template storage, variable injection, version management
- **Con:** Prompt interactions are complex — changing one section can break behavior elsewhere

**Key decisions:**
- Storage: files in a repo? database? config service?
- Templating: simple variable substitution? conditional sections? composable fragments?
- Testing: manual review? automated quality regression? A/B with statistical significance?
- Versioning: semantic versioning? hash-based? per-agent or global?

**Notes:** Pairs with **Persona Injection** (persona is a composable fragment within prompt configuration), **Warm-up & Calibration** (test new prompt versions against historical cases before going live), and **Canary & Shadow Mode** (shadow-test new prompts against production).

## Examples

TODO: Add concrete examples from real usage.

---

### Provenance & Audit Trail (`provenance`)  `monitoring` `reliability`

*Every decision, output, and agent interaction is logged with rationale, inputs, and timestamps.*

**Tags:** `monitoring` `reliability`

Every decision, output, and agent interaction is logged with rationale, inputs, and timestamps. Creates a complete record of how the system arrived at its outputs.

**When to use:**
- Clients or stakeholders need visibility into what the system did and why
- Debugging requires tracing back through the decision chain
- Regulatory or organizational compliance demands audit trails
- You want retrospectives to identify which patterns and decisions led to good/bad outcomes

**Tradeoffs:**
- **Pro:** Builds trust — clients and admins can see exactly what happened
- **Pro:** Debugging becomes tracing a log, not guessing what went wrong
- **Pro:** Retrospectives have concrete data to analyze
- **Con:** Logging adds storage and (minor) latency overhead
- **Con:** Verbose logs can be hard to navigate without good tooling
- **Con:** Sensitive information in logs requires access control

**What to log:**
- Agent identity and role
- Input received (or summary if large)
- Decision made and rationale
- Output produced
- Confidence level
- Time and cost

**Key decisions:**
- Granularity: every tool call? every agent decision? only major milestones?
- Storage: structured (database) vs. append-only (JSONL) vs. integrated (Linear/GitHub comments)?
- Retention: how long do you keep logs? Compliance may dictate minimums.

## Examples

TODO: Add concrete examples from real usage.

---

### Quality Stack (`quality-stack`)  `quality` `convergent`

***Redundant Generation** → **Hybrid Synthesis** → **Verification Loop** → **Progressive Refinement***

**Tags:** `quality` `convergent`

**Redundant Generation** → **Hybrid Synthesis** → **Verification Loop** → **Progressive Refinement**

Generate multiple attempts, synthesize the best parts, verify the synthesis, then refine.

**When to use:**
- Output quality is paramount and justifies 10-20x cost
- The task has a wide solution space where multiple attempts yield meaningfully different results
- You have clear verification criteria to catch synthesis errors

## Examples

TODO: Add concrete examples from real usage.

---

### Rate Limiting & Backpressure (`rate-limiting`)  `cost` `reliability` `coordination`

*Govern the rate at which agents spawn subagents, make tool calls, or hit external APIs.*

**Tags:** `cost` `reliability` `coordination`

Govern the rate at which agents spawn subagents, make tool calls, or hit external APIs. When the system produces work faster than downstream consumers can handle, backpressure signals slow the producer. Prevents runaway parallelism, API rate limit errors, and resource exhaustion.

```
Orchestrator spawns subagents
  → Concurrency limiter: max N in flight
  → Queue: excess work waits
  → Backpressure: if queue exceeds threshold, orchestrator slows down or stops spawning

External API calls
  → Rate limiter: max M calls per second
  → Retry with backoff on 429/throttle
  → Circuit break if sustained throttling
```

**When to use:**
- The system makes external API calls with rate limits (LLM APIs, search APIs, tool integrations)
- An orchestrator can spawn many parallel subagents, risking resource exhaustion
- Downstream systems (databases, services) have throughput limits
- You want predictable, sustainable execution rather than bursts followed by throttling

**Tradeoffs:**
- **Pro:** Prevents 429 errors, API bans, and resource exhaustion
- **Pro:** Smoother, more predictable execution — easier to monitor and budget
- **Pro:** Backpressure signals are useful information (system is overloaded → adjust plan)
- **Con:** Limits throughput — tasks that could parallelize heavily are artificially slowed
- **Con:** Queue management adds complexity (priority ordering, starvation prevention)

**Key decisions:**
- Concurrency limit: fixed N? adaptive based on error rate? per-resource?
- Backpressure strategy: queue and wait? drop low-priority work? alert human?
- Rate limit awareness: hardcoded? discovered from API response headers? adaptive?

**Notes:** Pairs with **Budget-Aware Execution** (budget governs total spend, rate limiting governs spend *velocity*) and **Watchdog** (monitor for sustained throttling as an anomaly signal).

## Examples

TODO: Add concrete examples from real usage.

---

### Redundant Generation with Judging (`redundant-generation`)  `divergent` `quality`

*N agents (typically 3-5) do the same task independently.*

**Tags:** `divergent` `quality`

N agents (typically 3-5) do the same task independently. Judge agents evaluate, rank, and provide rationale.

```
Task → Agent A ─┐
Task → Agent B ──┼→ Judge Panel → Ranked Results + Rationale
Task → Agent C ─┘
```

**When to use:**
- Output quality matters more than cost
- The task has a wide solution space
- You want to reduce single-agent variance

**Tradeoffs:**
- **Pro:** Significantly reduces bad output risk — best of N
- **Pro:** Ranking rationale is itself valuable signal
- **Con:** Linear cost scaling (N+1x)
- **Con:** Judges can have systematic biases

**Variants:**
- **Diverse generation** — different instructions/temperatures per agent to increase diversity
- **Blind judging** — judges don't know which agent produced which output
- **Multi-criteria judging** — independent scores on multiple dimensions, then composite

## Examples

TODO: Add concrete examples from real usage.

---

### Reflection & Self-Critique (`reflection`)  `convergent` `quality` `cost`

*An agent reviews its own output before submitting — identifies weaknesses, then revises.*

**Tags:** `convergent` `quality` `cost`

An agent reviews its own output before submitting — identifies weaknesses, then revises.

```
Agent produces draft → Agent critiques own draft → Agent revises → Submit
```

**When to use:**
- You want better output without a separate verification agent
- The task benefits from a "step back and think" moment
- Budget pattern, not quality ceiling pattern

**Tradeoffs:**
- **Pro:** Cheap — one agent, ~1.5-2x cost
- **Pro:** Agent has full context on its own reasoning
- **Con:** Systematic blind spots persist through self-critique
- **Con:** Can be performative rather than substantive

**When NOT to use:** When stakes justify external verification. Self-critique is a budget play.

## Examples

TODO: Add concrete examples from real usage.

---

### Reliability Wrapper (`reliability-wrapper`)  `reliability`

***Cascade & Fallback** → **Watchdog** → **Configurable HITL***

**Tags:** `reliability`

**Cascade & Fallback** → **Watchdog** → **Configurable HITL**

Try primary approach, fall back if needed, monitor for anomalies, let humans intervene.

**When to use:**
- The system must produce *some* output even when components fail
- Autonomous operation over extended periods
- Hard constraints (budget, time, safety) that must not be exceeded

## Examples

TODO: Add concrete examples from real usage.

---

### Research Pipeline (`research-pipeline`)  `learning` `quality`

***Structured Reasoning** → **Retrieval Subagent** → **Verification Loop** → **Progressive Refinement***

**Tags:** `learning` `quality`

**Structured Reasoning** → **Retrieval Subagent** → **Verification Loop** → **Progressive Refinement**

Autonomous iterative research: reason about what to search, retrieve information, verify findings, identify gaps, search again, and synthesize into a comprehensive report. Time- or budget-bounded.

**When to use:**
- Open-ended research questions requiring multiple search-and-synthesis cycles
- The agent must discover what it doesn't know (unknown unknowns) rather than just answering what it's asked
- Quality requires iterative deepening — first pass finds surface answers, subsequent passes find nuance

## Examples

TODO: Add concrete examples from real usage.

---

### Retrieval Subagent (`retrieval-subagent`)  `context` `coordination`

*One step beyond **TOC Index**.*

**Tags:** `context` `coordination`

One step beyond **TOC Index**. Don't even keep the index in the consumer's context. A dedicated subagent (or forked session pre-loaded with the index) acts as a librarian. The consumer agent says "I need info about X", the retrieval subagent finds and delivers just the narrow slice.

```
Consumer Agent: "What do we know about loss framing for 18-24 year olds?"
         │
         ▼
Retrieval Subagent (pre-loaded with TOC + access to full corpus)
         │
         ▼
Consumer Agent receives: [relevant excerpt, 200 words, with source reference]
```

**When to use:**
- Even the TOC is too large for the consumer's context
- You want to keep the consumer agent's context maximally focused on its primary task
- Multiple consumer agents need access to the same knowledge base (the retrieval subagent serves all of them)

**Tradeoffs:**
- **Pro:** Consumer context stays clean — no index clutter
- **Pro:** Retrieval subagent can be specialized and optimized for search quality
- **Pro:** Single point of access to the knowledge base — easy to update, cache, and audit
- **Con:** Adds a round-trip — consumer must wait for retrieval
- **Con:** Retrieval subagent may return irrelevant or insufficient information
- **Con:** Consumer can't browse — it can only get what it asks for

**Notes:** Combines powerfully with **Session Forking** — fork the retrieval subagent from a base pre-loaded with the corpus index, so it starts ready with zero setup cost.


**Agentic retrieval capabilities:**
Beyond simple query-and-return, a mature retrieval subagent performs:
- **Source validation** — Assess recency, authority, and relevance of retrieved documents before passing them upstream
- **Conflict reconciliation** — When sources contradict, identify the conflict and either resolve it or flag it explicitly
- **Query decomposition** — Break complex questions into sub-queries, retrieve for each, and synthesize
- **Gap detection** — Identify when retrieved information is insufficient and proactively search for missing pieces using additional tools or queries

## Examples

TODO: Add concrete examples from real usage.

---

### Routing (`routing`)  `decisions` `cost`

*Evaluate incoming input (intent, type, complexity) and dispatch to the most appropriate handler, tool, or sub-agent.*

**Tags:** `decisions` `cost`

Evaluate incoming input (intent, type, complexity) and dispatch to the most appropriate handler, tool, or sub-agent. Unlike **Cascade & Fallback** (which tries options sequentially on failure), Routing classifies first and dispatches to the *best* handler directly.

```
Input → Classifier → Category A → Handler A
                   → Category B → Handler B
                   → Category C → Handler C
```

**When to use:**
- The system must choose between multiple distinct workflows based on input characteristics
- Different input types require genuinely different processing (not just fallback alternatives)
- You want to optimize cost/latency by routing simple inputs to cheaper handlers

**Tradeoffs:**
- **Pro:** Each handler is optimized for its input type — better quality than one-size-fits-all
- **Pro:** Cost savings by routing simple queries to cheap/fast models, complex to expensive
- **Con:** Misclassification sends input to the wrong handler — errors are systematic, not random
- **Con:** Routing logic itself adds latency and requires maintenance

**Variants:**
- **LLM-based** — Use the LLM itself to classify input and output a routing label
- **Embedding-based** — Convert input to a vector embedding, compare against route embeddings, dispatch to nearest match
- **Rule-based** — Deterministic rules (regex, keyword matching, input length)
- **ML-classifier** — Train a small discriminative model on labeled routing data (cheaper and faster than LLM routing at inference, but requires training data)

**Key decisions:**
- Classification method: LLM, embedding similarity, trained classifier, or rules?
- Fallback: what happens when no route matches confidently? (Default handler? Escalate?)
- Monitoring: track misrouting rate to detect classification drift

**Notes:** Distinct from **Cascade & Fallback** (failure-triggered sequential fallback) and **Escalation Ladder** (cost-triggered escalation). Routing is classification-triggered dispatch. Often precedes **Orchestrator-Subagent** (router dispatches to specialized sub-agents).

## Examples

TODO: Add concrete examples from real usage.

---

### Scoped Promotion (`scoped-promotion`)  `learning`

*Learnings, patterns, and behaviors start scoped to a specific context (project, client, industry, engagement).*

**Tags:** `learning`

Learnings, patterns, and behaviors start scoped to a specific context (project, client, industry, engagement). They're promoted to broader scope only when consensus is reached — the same pattern independently emerges across multiple contexts.

```
Project A learns: "validate user input at API boundary"  (confidence: 0.8)
Project B learns: "validate user input at API boundary"  (confidence: 0.7)
  → Consensus: 2+ projects, avg confidence ≥ 0.75
  → Promote to global scope
```

**When to use:**
- A system operates across multiple projects, clients, or domains
- You want to learn from each context without overfitting to one
- Universal patterns should be shared; context-specific ones should not

**Tradeoffs:**
- **Pro:** Prevents overfitting — a React pattern doesn't leak into Python projects
- **Pro:** Universal patterns get stronger evidence before being broadly applied
- **Pro:** Promotion creates a natural quality filter
- **Con:** Consensus threshold must be calibrated — too high and nothing promotes, too low and noise leaks through
- **Con:** Context detection must be reliable (project identity, domain classification)

**Key decisions:**
- Scope levels: project → team → organization → global? Or simpler?
- Promotion criteria: N contexts + confidence threshold? Manual review?
- Demotion: can promoted patterns be demoted if they stop working in new contexts?

**Notes:** Natural partner to **Memory & Retrieval** (scoped memories), **Confidence Signaling** (drives promotion), and **Workspace Isolation** (defines the scope boundaries).

## Examples

TODO: Add concrete examples from real usage.

---

### Session Forking & Base Context (`session-forking`)  `context` `coordination`

*Establish shared context once in a "base session." Fork from the base for parallel workstreams.*

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

---

### Specialization Ensemble (`specialization-ensemble`)  `divergent` `quality` `coordination`

*Multiple agents, each expert in a different aspect of the task, independently analyze the same input.*

**Tags:** `divergent` `quality` `coordination`

Multiple agents, each expert in a different aspect of the task, independently analyze the same input. A synthesis agent merges their outputs.

```
Input → Expert A (messaging) ─┐
Input → Expert B (audience)  ──┼→ Synthesis Agent → Integrated Output
Input → Expert C (format)    ─┘
```

**When to use:**
- The task has multiple dimensions requiring genuinely different expertise
- A single generalist can't go deep enough on all dimensions
- You want deep analysis per dimension rather than shallow coverage of all

**Tradeoffs:**
- **Pro:** Each expert goes deeper than a generalist could
- **Pro:** Easy to add new specialists without redesigning the system
- **Con:** Specialists may produce conflicting recommendations — synthesis is the hard part
- **Con:** Specialists lack awareness of each other's constraints

**Different from Redundant Generation:** Specialization gives *different aspects* to different agents and merges. Redundant Generation gives the *same task* and selects.

## Examples

TODO: Add concrete examples from real usage.

---

### Structured Reasoning (`structured-reasoning`)  `quality` `decisions`

*Make an agent''s reasoning process explicit and auditable by structuring it as a sequence of intermediate steps rather than producing answers in a single pass.*

**Tags:** `quality` `decisions`

Make an agent's reasoning process explicit and auditable by structuring it as a sequence of intermediate steps rather than producing answers in a single pass. The foundational technique that underpins many other quality patterns — when an agent "thinks step by step," it decomposes complex problems, catches errors, and produces more reliable outputs.

```
Single-pass:    Question → Answer (opaque)
Structured:     Question → Step 1 → Step 2 → ... → Step N → Answer (auditable)
```

**When to use:**
- Complex problems requiring multi-step logic, decomposition, or tool interaction
- When transparency of reasoning is as important as the final answer
- When you want self-correction opportunities between steps

**Tradeoffs:**
- **Pro:** Dramatically improves accuracy on complex tasks
- **Pro:** Transparent, auditable reasoning chains — you can see *where* it went wrong
- **Pro:** Enables self-correction at each step rather than only at the end
- **Con:** Higher token usage and latency (more generation per answer)
- **Con:** Reasoning steps can be confabulated — coherent-sounding but wrong
- **Con:** Requires compute budget allocation (more thinking = better results, but costs more)

**Variants:**
- **Chain-of-Thought (CoT)** — Linear sequence of reasoning steps. Can be few-shot (with worked examples) or zero-shot ("think step by step")
- **Tree-of-Thought (ToT)** — Explores multiple branching reasoning paths simultaneously, evaluates branches, and backtracks from dead ends. Richer than linear CoT but more expensive
- **ReAct** — Interleaved thought-action-observation loop: reason about what to do, execute a tool/action, observe the result, incorporate it into the next reasoning step. The core agentic operational loop

**Key decisions:**
- Reasoning depth: how many steps? Fixed or adaptive? (Scaling Inference Law: more compute at inference time = predictably better quality)
- Branching: linear chain sufficient, or does the problem require exploring alternatives (ToT)?
- Grounding: pure reasoning, or interleaved with tool use (ReAct)?

**Notes:** This is an enabling pattern — it makes other patterns more effective. **Reflection & Self-Critique** is structured reasoning applied to self-evaluation. **Adversarial Review** works better when agents show their reasoning chains. Pairs with **Budget-Aware Execution** (allocate reasoning budget proportional to task importance).

## Examples

TODO: Add concrete examples from real usage.

---

### TOC Index (`toc-index`)  `context`

*Instead of loading full content into an agent''s context, maintain a table of contents / index.*

**Tags:** `context`

Instead of loading full content into an agent's context, maintain a table of contents / index. The agent reads the index, identifies what it needs, then fetches just that section. Like a library card catalog vs. carrying every book.

```
Agent receives task → Reads TOC/index → Identifies relevant sections → Fetches only those → Produces output
```

**When to use:**
- The knowledge base is too large for any single context window
- Most tasks only need a small fraction of the total information
- The information is well-structured enough to index meaningfully

**Tradeoffs:**
- **Pro:** Dramatically reduces context size while preserving access to the full corpus
- **Pro:** Agent "knows what it doesn't know" — the TOC tells it what exists
- **Con:** Requires maintaining an accurate, up-to-date index
- **Con:** Agent must be good at identifying which sections are relevant from titles/summaries alone
- **Con:** Adds a lookup step — slower than having everything in context

**Key decisions:**
- Index granularity: section-level? paragraph-level? entity-level?
- Index format: flat list? hierarchical? tagged?
- Fetch mechanism: direct file read? API call? embedding search within section?

## Examples

TODO: Add concrete examples from real usage.

---

### Tool-Native Communication (`tool-native-communication`)  `communication`

*Agents output directly into the systems humans already use — ticketing (Linear), PRs (GitHub), chat (Slack), docs (Notion) — rather than creating parallel artifacts that require manual integration.*

**Tags:** `communication`

Agents output directly into the systems humans already use — ticketing (Linear), PRs (GitHub), chat (Slack), docs (Notion) — rather than creating parallel artifacts that require manual integration.

**The principle:** If an agent writes a plan to a markdown file that a human then copy-pastes into Linear, that's a manual integration step that defeats the purpose of automation.

**When to use:**
- The team already has established tools for tracking work, communication, and documentation
- Agent outputs need to be visible, commentable, and trackable by humans
- You want agents to participate in existing workflows, not create parallel ones

**Examples:**
- Write research plans directly to Linear tickets, not markdown files
- Add review comments directly on PRs, not in separate text files
- Post status updates to Slack channels, not log files
- Update Notion docs directly, not generate replacement text

**Tradeoffs:**
- **Pro:** Output is immediately visible in existing workflows — zero "last mile" friction
- **Pro:** Output is commentable, trackable, and integrated with existing processes
- **Pro:** Agents become participants in the team's process, not external tools
- **Con:** Each tool has its own formatting conventions, API quirks, and permission models
- **Con:** Tool outages or API changes can break agent output channels
- **Con:** Agents may produce output that doesn't match the team's conventions for that tool

**Key decisions:**
- Which tools to integrate with? (Start with the ones the team actually uses daily)
- Permission model: what can agents create vs. update vs. comment on?
- Formatting: agents must understand each tool's conventions (Linear markdown vs. GitHub markdown vs. Slack blocks)

## Examples

TODO: Add concrete examples from real usage.

---

### Tournament Selection (`tournament-selection`)  `convergent` `quality`

*Candidates evaluated in pairwise or bracket-style comparisons rather than absolute rankings.*

**Tags:** `convergent` `quality`

Candidates evaluated in pairwise or bracket-style comparisons rather than absolute rankings.

```
A vs B → winner₁ ─┐
                    ├→ winner₁ vs winner₂ → Final Winner
C vs D → winner₂ ─┘
```

**When to use:**
- Many candidates (10+) where absolute ranking is expensive
- Pairwise comparison is more reliable than absolute scoring
- You need O(n log n) comparisons instead of O(n²)

**Tradeoffs:**
- **Pro:** Pairwise is more reliable than "rate this 1-10"
- **Pro:** Scales well to large candidate pools
- **Con:** Strong candidates can be eliminated by slightly stronger ones early
- **Con:** Doesn't produce full ranking, just a winner

**Variants:** Double elimination, round-robin, Swiss system

## Examples

TODO: Add concrete examples from real usage.

---

### Verification Loop (`verification-loop`)  `convergent` `quality` `reliability`

*After output is produced, a separate verifier checks against defined criteria.*

**Tags:** `convergent` `quality` `reliability`

After output is produced, a separate verifier checks against defined criteria. If verification fails, output goes back with feedback for revision. Repeats until pass or retry limit.

```
Producer → Output → Verifier
              ↑         │
              └── fail ──┘ (with feedback)
              pass → Continue
```

**When to use:**
- Clear, checkable criteria for output quality
- Cost of bad output propagating downstream is high
- The producer can meaningfully improve given specific feedback

**Tradeoffs:**
- **Pro:** Catches errors before propagation
- **Pro:** Targeted feedback is more useful than "try again"
- **Con:** Can loop indefinitely without retry limits
- **Con:** Verifier has its own false positive/negative rate

**Variants:**
- **Multi-verifier** — different verifiers for different dimensions
- **Graduated** — cheap/fast first pass, expensive/thorough only if flagged

## Examples

TODO: Add concrete examples from real usage.

---

### Warm-up & Calibration (`warmup-calibration`)  `deployment` `quality`

*Before the system goes live, run it against known historical cases to verify it produces reasonable outputs.*

**Tags:** `deployment` `quality`

Before the system goes live, run it against known historical cases to verify it produces reasonable outputs. Like backtesting in finance or shadow deployment in ML.

**Process:**
1. Select historical cases with known outcomes
2. Run the system against those cases
3. Compare system outputs to known-good human outputs
4. Identify systematic biases or failure modes
5. Adjust prompts, parameters, or patterns before going live

**When to use:**
- Before deploying a new agent system or major revision
- When you have historical data to calibrate against (Swayable's 6,600+ studies)
- When the cost of a bad first impression with clients is high

**Key insight:** This is not just testing — it's calibrating. The system may need its priors adjusted, its confidence thresholds tuned, or its escalation triggers recalibrated based on how it performs on known cases.

## Examples

TODO: Add concrete examples from real usage.

---

### Watchdog & Circuit Breaker (`watchdog`)  `monitoring` `reliability`

*A monitoring agent observes system behavior in real time, watching for anomalies, runaway costs, or safety violations.*

**Tags:** `monitoring` `reliability`

A monitoring agent observes system behavior in real time, watching for anomalies, runaway costs, or safety violations. When a threshold is crossed, execution halts and a human is alerted.

```
System Running → Watchdog monitors (cost, time, quality, safety)
             → Normal → Continue
             → Anomaly → Circuit breaker → Halt + Alert Human
```

**When to use:**
- System runs autonomously for extended periods
- Hard constraints (budget, time) must not be exceeded
- Failure modes include runaway loops or cascading errors

**What to monitor:**
- Cost burn rate (are we spending faster than planned?)
- Output quality trends (are results degrading?)
- Agent error rates (is something failing repeatedly?)
- Time per step (is something hanging?)
- Safety signals (did the ethics agent flag something concerning?)

**Key decisions:**
- Threshold calibration: too sensitive = false alarms, too lax = missed problems
- Recovery: can the system resume after tripping, or must a human restart?

**Notes:** Pairs with **Notification Hooks** (alert humans on circuit break), **Configurable HITL** (human decides whether to resume), and **Provenance** (anomaly events feed the audit trail).


**Additional trigger types:**
- **Drift detection** — Monitor for degradation in agent performance over time due to changes in input data distribution or environmental shifts. Sustained quality decline triggers investigation, not just single anomalies
- **Before-tool callbacks** — Proactive parameter validation before tool execution (e.g., verifying user permissions, checking argument bounds). Prevents bad tool calls rather than detecting their aftermath
- **LLM-based overseer** — A separate, lightweight LLM monitors the primary agent's event stream and call graph for behavioral anomalies (loops, stagnation, off-task drift). More nuanced than threshold-based rules

## Examples

TODO: Add concrete examples from real usage.

---


## Modifiers

### Eager (`eager`)

*The agent invests in pre-computation, pre-fetching, or pre-validation before results are explicitly requested, trading compute cost for reduced latency later.*

When this modifier is applied, the agent invests in pre-computation, pre-fetching, or pre-validation before results are explicitly requested. It anticipates what will be needed and produces it now, trading compute cost for reduced latency later. The agent must distinguish what is *likely* needed from what is *certainly* needed — over-eagerness wastes resources.

## Examples

TODO: Add concrete examples from real usage.

---

### Exhaustive (`exhaustive`)

*The agent optimizes for coverage over speed, enumerating the full input space and using systematic search rather than heuristic sampling.*

When this modifier is applied, the agent optimizes for coverage over speed. It enumerates the full input space before acting, tracks what has been visited, and uses systematic search rather than heuristic sampling. When exhaustive coverage is infeasible, the agent must flag this and propose bounded alternatives rather than silently sampling.

## Examples

TODO: Add concrete examples from real usage.

---

### Incremental (`incremental`)

*The agent processes only what has changed since the last execution, computing a delta from a baseline and operating on that delta rather than the full corpus.*

When this modifier is applied, the agent processes only what has changed since the last execution. It must first establish a baseline (what was the prior state?), then compute a delta. All downstream logic operates on the delta, not the full corpus. The agent must reason about change detection, staleness, and whether partial updates preserve correctness of the whole.

## Decision Tree

```
Detect changes by **hash comparison**, **timestamp**, **diff against prior output**, or **explicit signal from caller**?
```

## Examples

TODO: Add concrete examples from real usage.

---

### Lazy (`lazy`)

*The agent defers all work until the result is actually needed, operating in just-in-time mode and actively resisting speculative work.*

When this modifier is applied, the agent defers all work until the result is actually needed by a downstream consumer. Instead of building everything upfront, it identifies the immediate need and produces only that. Downstream steps are planned but not executed — the agent operates in just-in-time mode and actively resists speculative work.

## Examples

TODO: Add concrete examples from real usage.

---

### Non-destructive (`non-destructive`)

*The agent keeps all source material intact and produces derived output alongside it rather than replacing it, maintaining clear lineage from source to output.*

When this modifier is applied, the agent keeps all source material intact and produces derived output alongside it rather than replacing it. Every transformation becomes a derivation step with provenance — the agent must plan for storage of both forms, maintain a clear lineage from source to output, and reason about which form to surface to the consumer.

## Examples

TODO: Add concrete examples from real usage.

---

### Publishable (`publishable`)

*The agent treats the output as audience-facing, applying a higher quality bar with mandatory review and verification steps.*

When this modifier is applied, the agent treats the output as audience-facing: it must be self-contained, properly formatted, and free of internal shorthand, TODOs, or draft markers. The agent applies a higher quality bar, reasons about the target audience and medium, and makes review and verification steps mandatory rather than optional.

## Decision Tree

```
Publish to **file**, **API**, **message channel**, or **external service**?
Audience: **technical peers**, **non-technical stakeholders**, or **general public**?
```

## Examples

TODO: Add concrete examples from real usage.

---

### Scoped (`scoped`)

*The agent establishes an explicit boundary before acting and constrains all subsequent reasoning to that boundary, actively rejecting drift beyond scope.*

When this modifier is applied, the agent establishes an explicit boundary before acting — what files, what time range, what subsystem — and constrains all subsequent reasoning to that boundary. The agent actively rejects drift beyond scope. Discovered dependencies outside the boundary are noted but not pursued; they become inputs for a future scoped pass.

## Examples

TODO: Add concrete examples from real usage.

---

### Speculative (`speculative`)

*The agent treats its output as explicitly provisional — a hypothesis to validate, not a final answer — making uncertainty visible and expecting downstream validation.*

When this modifier is applied, the agent treats its output as explicitly provisional — a hypothesis to validate, not a final answer. This frees the agent to explore broadly, generate multiple candidates, and tolerate lower individual confidence. Uncertainty must be made visible rather than hidden behind confident-sounding language; every speculative output expects a downstream validation step.

## Examples

TODO: Add concrete examples from real usage.

---

### Versionable (`versionable`)

*The agent treats every meaningful state of the artifact as a version that can be referenced, compared, or restored, reasoning about what constitutes a meaningful change worth versioning.*

When this modifier is applied, the agent treats every meaningful state of the artifact as a version that can be referenced, compared, or restored. It must decide on a versioning mechanism, assign version identifiers, and ensure that prior versions remain accessible. The agent reasons about what constitutes a "meaningful change" worth versioning versus noise, and maintains enough metadata to support diff, rollback, and audit.

## Decision Tree

```
Version via **git commits**, **filename suffixes**, **single file + metadata header**, **external system (API/DB)**, or **append-only log**?
Granularity: **every save**, **every meaningful change**, or **explicit checkpoints only**?
```

## Examples

TODO: Add concrete examples from real usage.

---



# Growing the Library

## When a Macro Earns Its Place

A concept becomes a macro when it meets all three criteria:

1. **Recurrence** — The same expansion keeps getting restated from scratch across different sessions or contexts
2. **Precision** — The concept has a specific enough expansion that two agents would behave similarly when invoking it
3. **Composability** — The concept combines meaningfully with existing macros

## How New Macros Are Added

1. Notice a recurring restatement — the agent keeps expanding the same concept ad-hoc
2. Draft the macro: name, shorthand, category, expansion, decision trees (if any)
3. Test composability: does it combine with at least 2-3 existing macros?
4. Add to `macros/` with frontmatter and full entry
5. Update `taxonomy/` if a new category or tag is needed

## What Doesn't Belong

- **One-off instructions** — if it only applies in one context, it's not a macro
- **Implementation details** — "use PostgreSQL" is a decision, not a macro
- **Vague aspirations** — if you can't write a precise expansion, it's not ready yet

## Open Questions

- How formal should composition rules become? Currently descriptive — could become a type system.
- Should macros have versioning? The expansion of `collapse` might evolve over time.
- What's the right threshold for "recurring enough" to earn a macro?
- How does this relate to the existing pattern catalog? Migration path or parallel systems?