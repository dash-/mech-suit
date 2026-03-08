# Strategies

Strategies are action macros. Each one is a named verb that expands into a precise agent behavior contract — invoke the name, get the behavior. They are domain-agnostic: they apply equally to code, processes, and communication. Strategies compose with each other (a pipeline might `normalize` then `decompose` then `delegate`) and oppose each other where tension is real (`generate` vs. `refine`, `defer` vs. `collapse`). When you invoke a strategy, you are telling an agent *what kind of action to take*, not how to structure the result.

---

### Compose (`compose`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent builds a whole from existing, well-defined parts. It inventories available sub-components, wires them together through explicit seams, and prefers reuse over reinvention. The agent makes the assembly structure visible — which parts were combined and how they connect.

**Composes with:** `decompose`, `normalize`, `cache`

**Opposes:** `generate` (compose reuses; generate creates new)

---

### Decompose (`decompose`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent splits a complex input or task along natural boundaries into independent, addressable parts. Each part can be understood, acted on, or delegated without reference to the others. The agent ensures loose coupling — changing one part must not require changing another.

**Decision tree:**
- Split by responsibility, by data shape, or by lifecycle stage?
- Flat decomposition (all parts peer-level) or hierarchical (parts contain sub-parts)?

**Composes with:** `compose`, `delegate`, `isolate`

---

### Collapse (`collapse`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent walks all dependency chains, inlines referenced content, and resolves variables or lookups, producing a flat, self-contained artifact that requires no further resolution. The consumer never performs lookups or chases references. If a reference cannot be resolved, the agent fails immediately rather than emitting a broken link.

**Decision tree:**
- Resolve via inlining (embed content), compilation (transform to target), or snapshot (freeze current state)?

**Composes with:** `normalize`, `verify`, `cache`

**Opposes:** `defer` (collapse resolves eagerly; defer postpones resolution)

---

### Cache (`cache`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent checks for a valid prior result before performing an expensive operation. If one exists, it returns the cached value. If not, it performs the operation and stores the result. The agent maintains cache validity — when inputs change, it invalidates stale entries rather than serving outdated results.

**Decision tree:**
- Cache in memory, filesystem, or external store?
- Invalidate by TTL, content hash, or explicit signal?

**Composes with:** `collapse`, `normalize`, `verify`

---

### Delegate (`delegate`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent identifies work that falls outside its core responsibility or optimal scope and passes it to a specialist with only the authority and context needed for that sub-task. It defines the interface clearly — inputs, expected outputs, constraints — and reclaims control when the delegate returns.

**Decision tree:**
- Delegate to subagent, external service, or human?
- Pass full context or minimal context (need-to-know)?

**Composes with:** `decompose`, `isolate`, `gate`

**Opposes:** `escalate` (delegate passes work down or sideways; escalate passes it up)

---

### Escalate (`escalate`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent surfaces a problem or decision to a higher authority with full context: what was attempted, why it was insufficient, and what information or permission is needed to proceed. The agent does not guess or silently degrade — it halts its current path and makes the blocker explicit.

**Composes with:** `gate`, `verify`, `emit`

**Opposes:** `delegate` (escalate goes up; delegate goes down or sideways)

---

### Gate (`gate`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent evaluates a precondition and either allows progress (pass) or blocks it (halt). There is no middle ground — gates are binary. The agent does not attempt workarounds for unmet requirements. Gates enforce invariants at transition points, not after the fact.

**Composes with:** `verify`, `isolate`, `escalate`

---

### Verify (`verify`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent checks produced output against defined criteria — correctness, completeness, format, or constraints — before passing it downstream. Verification happens before handoff, never after. When verification fails, the agent either rejects the output with a clear explanation or routes it to `refine`.

**Composes with:** `gate`, `refine`, `emit`

---

### Refine (`refine`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent takes a prior output and applies targeted modifications — fixing defects, tightening language, improving structure — while preserving what already works. Each refinement pass has a diminishing scope of changes. The agent does not regenerate wholesale when a scalpel will do.

**Decision tree:**
- Refine for correctness, clarity, or performance?
- Single pass or iterate until a quality threshold is met?

**Composes with:** `verify`, `generate`, `emit`

**Opposes:** `generate` (refine converges; generate diverges)

---

### Generate (`generate`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent produces multiple distinct outputs — ideas, drafts, solutions — intentionally favoring breadth over efficiency. Redundancy is the point: overlapping candidates increase the chance of finding high-quality results. The agent does not self-filter during generation; convergence happens in a subsequent `verify` or `refine` pass.

**Decision tree:**
- Generate N candidates with variation in what dimension (approach, style, scope)?
- Constrained generation (within guardrails) or unconstrained (maximize diversity)?

**Composes with:** `verify`, `refine`, `decompose`

**Opposes:** `refine` (generate diverges; refine converges), `compose` (generate creates new; compose reuses existing)

---

### Isolate (`isolate`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent sets up boundaries — sandboxes, scoped permissions, or working copies — so that a risky or uncertain operation cannot affect anything outside its designated area. Isolation is applied before the risky action, not as cleanup after. If the operation fails, damage is contained to the isolated scope.

**Decision tree:**
- Isolate by process boundary, filesystem copy, or permission scope?

**Composes with:** `delegate`, `gate`, `defer`

---

### Normalize (`normalize`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent maps diverse representations — formats, naming conventions, structures — to a single canonical form early in the pipeline. All downstream logic handles only one shape, eliminating branching and surprise. The agent preserves the original when the transformation is lossy, but all processing operates on the normalized version.

**Composes with:** `compose`, `collapse`, `cache`

---

### Emit (`emit`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent produces structured, observable signals about internal state or progress — logs, progress indicators, intermediate results — as a side channel. Emission is non-blocking: it does not wait for acknowledgment and does not alter control flow. It makes the agent's reasoning or progress legible to supervisors without requiring interruption.

**Composes with:** `verify`, `escalate`, `refine`

---

### Defer (`defer`)

**Category:** strategy

**Expansion:** When this macro is invoked, the agent registers that work could be done but postpones execution until a consumer actually demands the result. This avoids wasted computation on paths that may never be taken. The agent ensures preconditions are still valid at execution time, not just at registration time — a deferred action that fires against stale state is a bug.

**Decision tree:**
- Defer until first access (lazy), until explicit trigger (event-driven), or until a batch boundary (bulk)?

**Composes with:** `isolate`, `gate`, `cache`

**Opposes:** `collapse` (defer postpones resolution; collapse resolves eagerly)
