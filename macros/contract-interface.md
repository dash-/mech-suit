---
name: Contract Interface
shorthand: contract-interface
category: pattern
tags: [coordination, reliability]
summary: Define strict input/output schemas between agents.
composes_with: []
opposes: []
---

# Contract Interface (`contract-interface`)

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
