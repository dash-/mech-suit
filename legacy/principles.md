# Principles

Principles are the sharpest tools in the arsenal — they cut across every domain. Invoking a principle macro causes the agent to scan the current context through that lens and surface violations or opportunities. Principles don't tell an agent *what to build*; they tell it *what to catch*.

---

### Don't Repeat Yourself (`DRY`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent identifies every instance where the same knowledge exists in more than one place. It flags duplicated logic, copy-pasted text, parallel structures that will drift, and any spot where a change in one location demands a corresponding change elsewhere. The agent then proposes how to collapse each duplication to a single authoritative source.

**Decision tree:**
```
How should the duplication be eliminated?
  A. Abstraction (extract shared logic into a function, module, or component)
  B. Configuration (single config source referenced by all consumers)
  C. Generation (one source template that produces the variants)
  D. Reference (replace copies with pointers to a canonical location)
```

**Composes with:** `composable`, `SoC`, `collapse`

**Opposes:** `generate` (which deliberately creates redundancy for quality)

---

### Separation of Concerns (`SoC`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent examines each unit — function, file, agent, document — and identifies any that serve multiple masters. It flags functions that both compute and format, configs that mix deployment and business logic, prompts that conflate instruction with context. For each violation, the agent proposes a split such that each resulting piece changes for exactly one reason.

**Composes with:** `DRY`, `composable`, `least-priv`, `delegate`

**Opposes:** `collapse` (which deliberately merges separated sources into one artifact)

---

### Principle of Least Surprise (`least-surprise`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent audits naming, return values, defaults, and side effects for anything that would confuse a person or system encountering them for the first time without documentation. It flags misleading names, return values that violate convention, side effects hidden behind innocent-looking interfaces, and defaults no one would guess. The test: "If someone encountered this cold, what would they expect?"

**Composes with:** `explicit`, `transparent`

---

### Fail Fast (`fail-fast`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent traces every error path and identifies where bad state can travel far from its origin before detection. It flags silent failures, bare exception handlers that swallow errors, functions returning ambiguous sentinel values, and late validation of input that was available earlier. For each finding, the agent proposes moving detection to the earliest possible moment.

**Decision tree:**
```
How should the early failure surface?
  A. Throw/raise (halt execution with a clear error)
  B. Return typed error (let the caller decide)
  C. Validate at boundary (reject bad input before it enters the system)
  D. Assert invariant (crash on impossible state in development)
```

**Composes with:** `explicit`, `transparent`, `verify`

**Opposes:** `lazy` (which defers work — tension: defer execution but surface errors early)

---

### Least Privilege (`least-priv`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent audits every permission grant, scope, and capability in the current context. It flags overly broad permissions, god-objects that can touch everything, API tokens with unnecessary scopes, agents with write access when they only need read, and any situation where the blast radius of a mistake is larger than necessary. For each finding, it proposes the minimum viable permission.

**Composes with:** `SoC`, `scoped`, `delegate`

---

### Idempotent (`idempotent`)

**Category:** principle, modifier

**Expansion:** When this macro is invoked, the agent examines every operation and asks: "What happens if this runs again right now?" It flags operations that accumulate side effects on re-run — duplicate records, appended-not-replaced content, repeated notifications, migrations that break if executed twice. For each violation, the agent proposes a guard or restructuring that makes repeated execution safe.

**Decision tree:**
```
How should idempotency be achieved?
  A. Check-before-write (skip if already applied)
  B. Upsert (insert or update, never duplicate)
  C. Deterministic key (same input always maps to same identity)
  D. Replace-not-append (overwrite the whole target each time)
```

**Composes with:** `fail-fast`, `reversible`, `non-destructive`

---

### Transparent (`transparent`)

**Category:** principle, modifier

**Expansion:** When this macro is invoked, the agent identifies every black box in the current context — processes whose intermediate state is invisible, decisions made without recorded rationale, error messages that hide root causes, agents that produce output without showing their work. For each, it proposes a way to make the internal state, reasoning, or decision point visible to observers. The test: "If this fails, can someone reconstruct *why* from what's visible?"

**Composes with:** `explicit`, `emit`, `verify`

**Opposes:** `minimal` (transparency adds visible structure; tension: be observable without being noisy)

---

### Reversible (`reversible`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent identifies every point of no return in the current context — destructive operations without backup, one-way deployments, writes that overwrite without preserving the original. For each, it proposes an alternative that preserves a recovery path: soft deletes, backup-before-write, staged rollouts, or undo mechanisms. The test: "If this turns out to be wrong, what's the recovery path?"

**Composes with:** `non-destructive`, `idempotent`, `incremental`

---

### Explicit over Implicit (`explicit`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent hunts for anything that requires "you just have to know" to understand. It flags magic values, hidden coupling between modules, behavior that depends on execution order or ambient state, and undocumented prerequisites. For each finding, it proposes stating the intention, dependency, or assumption directly — accepting verbosity as the price of eliminating mystery.

**Composes with:** `transparent`, `least-surprise`, `fail-fast`

**Opposes:** `composable` (in edge cases — explicit wiring can reduce plug-and-play flexibility)

---

### Minimal Footprint (`minimal`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent challenges every piece of structure, dependency, and scope in the current context. It flags premature abstractions, unused parameters, speculative features, dependencies pulled in for a single function, and framework choices that outweigh the problem. For each, it asks: "What is the simplest thing that could work here, and is what we have meaningfully better or just bigger?" It proposes removals or simplifications.

**Decision tree:**
```
What kind of excess is being removed?
  A. Unused code/structure (dead code, empty abstractions)
  B. Premature abstraction (generalized before needed — inline it)
  C. Heavyweight dependency (replace with focused alternative or hand-roll)
  D. Speculative scope (features/parameters for futures that haven't arrived)
```

**Composes with:** `DRY`, `SoC`, `lazy`

**Opposes:** `transparent` (observability adds structure), `composable` (composability adds interface surface)

---

### Composable (`composable`)

**Category:** principle

**Expansion:** When this macro is invoked, the agent examines every component and asks: "Can this be used in a context its author didn't anticipate?" It flags components that work only in their original context, outputs that require transformation before the next step can consume them, tightly coupled pairs that cannot be recombined, and interfaces that demand knowledge of internal implementation. For each, it proposes interface changes that enable free connection through simple, consistent contracts.

**Composes with:** `SoC`, `DRY`, `explicit`

**Opposes:** `minimal` (in edge cases — composable interfaces add surface area beyond the immediate need)
