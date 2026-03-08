---
name: Memory & Retrieval Augmentation
shorthand: memory-retrieval
category: pattern
tags: [context, learning]
summary: Agents query a knowledge base to inform decisions.
composes_with: []
opposes: []
---

# Memory & Retrieval Augmentation (`memory-retrieval`)

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
