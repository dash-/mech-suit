---
name: Agent Discovery
shorthand: agent-discovery
category: pattern
tags: [setup, coordination]
summary: 'Enable agents to discover each other''s capabilities at runtime rather than hardcoding agent references.'
composes_with: [contract-interface, skill-delegation]
opposes: []
---

# Agent Discovery (`agent-discovery`)

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
