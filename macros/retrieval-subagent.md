---
name: Retrieval Subagent
shorthand: retrieval-subagent
category: pattern
tags: [context, coordination]
summary: One step beyond **TOC Index**.
composes_with: [session-forking]
opposes: []
---

# Retrieval Subagent (`retrieval-subagent`)

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
