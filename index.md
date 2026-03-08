# Publishing Index

Instructions for assembling the macro library into a single publishable document.

## Assembly Order

1. `intro.md` — Purpose, audience, how to use
2. **Taxonomy section** — assembled from `taxonomy/*.md`, sorted by: principle, strategy, pattern, modifier, skill, anti-pattern
3. **Macro catalog** — assembled from `macros/*.md`, grouped by primary category, alphabetical within group
4. `outro.md` — Growth model, contribution guidelines, open questions

## Assembly Rules

- Each macro file's frontmatter drives grouping and sorting
- Within each category group, macros are sorted alphabetically by shorthand
- Cross-references between macros become hyperlinks in the published form
- Decision trees render as indented lists
- `composes_with` and `opposes` render as inline links to other macro entries
- Tags from frontmatter render as badges/pills after the macro name

## Formats

The assembled document can be rendered to:
- **Markdown** — single `.md` file (default)
- **HTML** — static site with anchor links between macros
- **JSON** — machine-readable catalog for agent consumption via API/MCP

## Collapse Script

To produce a single collapsed markdown file:

```bash
# TODO: implement assembly script
# Should read index.md for order, parse frontmatter for grouping,
# and produce a single self-contained document.
```
