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
