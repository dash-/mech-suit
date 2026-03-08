---
description: Invoke macros from the mech-suit library by name, tag, or need
---

# Macro Lookup and Expansion

The macro library lives at `~/src/mech-suit/macros/`. Each macro is a markdown file with YAML frontmatter.

## Step 1 — Resolve the argument

The user's argument tells you what to look up. It may be:

- **One or more macro names** — e.g., `/with caching` or `/with caching, incremental, publishable` → fetch each macro file by shorthand
- **A category** — e.g., `/with strategy` or `/with modifier` → list all macros in that category with one-line summaries
- **A tag** — e.g., `/with quality` or `/with coordination` → list all macros with that tag
- **A need** — e.g., `/with how do I make this resumable?` → search summaries and tags for relevant macros, then fetch them
- **No argument** — list all macros grouped by category with one-line summaries

To build the index, scan frontmatter from all macro files:

```bash
for f in ~/src/mech-suit/macros/*.md; do grep -m1 "^shorthand:" "$f" | sed 's/shorthand: //'; grep -m1 "^category:" "$f" | sed 's/category: //'; grep -m1 "^summary:" "$f" | sed 's/summary: //'; echo "---"; done
```

## Step 2 — Fetch and expand

Read the macro file(s) from `~/src/mech-suit/macros/{shorthand}.md`.

For each macro:
1. Read the full file
2. Extract the expansion (the main description text after the heading)
3. If it has a decision tree, note the choices

## Step 3 — Restate in context

This is the critical step. Do NOT just dump the macro text. Instead:

1. **Restate** each macro's expansion applied to the user's current task. Be specific — replace generic language with concrete details from the context.
2. If multiple macros are composed, **synthesize** them into a single coherent plan. Note any tensions between macros and propose resolutions.
3. If a macro has a **decision tree**, present the choices with a recommendation based on context.
4. **Ask for confirmation** before executing. This is a contract negotiation: "Here's what I'll do: [specific restatement]. Does that match your intent?"

## Step 4 — On confirmation, execute

Once the user confirms (or adjusts), proceed with the agreed plan. The macro expansion is now the contract.

## Notes

- Macro names accept both human form ("Adversarial Review") and shorthand (`adversarial-review`)
- Multiple macros can be composed in one invocation: `/with caching, incremental` means "apply both"
- If a macro's `opposes` field lists another macro in the same invocation, surface the tension explicitly
- Keep output focused — present the restatement, not the raw macro file
