---
name: TOC Index
shorthand: toc-index
category: pattern
tags: [context]
summary: 'Instead of loading full content into an agent''s context, maintain a table of contents / index.'
composes_with: []
opposes: []
---

# TOC Index (`toc-index`)

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
