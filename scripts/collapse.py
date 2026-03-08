#!/usr/bin/env python3
"""
Collapse the macro library into a single publishable markdown document.

Usage:
    python scripts/collapse.py                  # outputs to stdout
    python scripts/collapse.py -o dist/mech-suit.md  # outputs to file
    python scripts/collapse.py --format json    # outputs JSON catalog
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACROS_DIR = ROOT / "macros"
TAXONOMY_DIR = ROOT / "taxonomy"

CATEGORY_ORDER = ["principle", "strategy", "pattern", "modifier"]

TAXONOMY_ORDER = ["principle", "strategy", "pattern", "modifier", "skill"]


def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file. Returns (metadata_dict, body_str)."""
    text = filepath.read_text()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
    if not m:
        return {}, text

    fm_text, body = m.group(1), m.group(2)
    meta = {}
    for line in fm_text.split('\n'):
        if ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()

        # Parse YAML lists: [a, b, c] or [principle, modifier]
        if val.startswith('[') and val.endswith(']'):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(',') if v.strip()]
            meta[key] = items
        else:
            # Strip surrounding quotes
            val = val.strip("'\"")
            meta[key] = val

    return meta, body


def primary_category(meta):
    """Get the primary category for sorting. Handles both string and list."""
    cat = meta.get('category', 'pattern')
    if isinstance(cat, list):
        # Use the first category that's in our order
        for c in CATEGORY_ORDER:
            if c in cat:
                return c
        return cat[0]
    return cat


def load_macros():
    """Load all macro files, return list of (metadata, body) tuples."""
    macros = []
    for f in sorted(MACROS_DIR.glob("*.md")):
        meta, body = parse_frontmatter(f)
        if meta:
            macros.append((meta, body))
    return macros


def load_taxonomy():
    """Load taxonomy files in order."""
    sections = []
    for name in TAXONOMY_ORDER:
        f = TAXONOMY_DIR / f"{name}.md"
        if f.exists():
            _, body = parse_frontmatter(f)
            sections.append(body.strip())
    return sections


def group_macros(macros):
    """Group macros by primary category."""
    groups = {cat: [] for cat in CATEGORY_ORDER}
    for meta, body in macros:
        cat = primary_category(meta)
        if cat not in groups:
            groups[cat] = []
        groups[cat].append((meta, body))

    # Sort each group alphabetically by shorthand
    for cat in groups:
        groups[cat].sort(key=lambda x: x[0].get('shorthand', ''))

    return groups


def render_tags(tags):
    """Render tags as inline badges."""
    if not tags:
        return ""
    return " ".join(f"`{t}`" for t in tags)


def collapse_markdown(macros):
    """Produce a single markdown document."""
    lines = []

    # Intro
    intro_path = ROOT / "intro.md"
    if intro_path.exists():
        lines.append(intro_path.read_text().strip())
        lines.append("\n\n---\n")

    # Taxonomy
    lines.append("\n# Categories\n")
    for section in load_taxonomy():
        lines.append(section)
        lines.append("\n---\n")

    # Macro catalog
    lines.append("\n# Macro Catalog\n")
    groups = group_macros(macros)

    for cat in CATEGORY_ORDER:
        if cat not in groups or not groups[cat]:
            continue

        PLURALS = {"principle": "Principles", "strategy": "Strategies", "pattern": "Patterns", "modifier": "Modifiers"}
        cat_title = PLURALS.get(cat, cat.replace('-', ' ').title() + "s")
        lines.append(f"\n## {cat_title}\n")

        for meta, body in groups[cat]:
            name = meta.get('name', 'Unknown')
            shorthand = meta.get('shorthand', '')
            tags = meta.get('tags', [])
            summary = meta.get('summary', '')

            # Heading with tags
            tag_str = f"  {render_tags(tags)}" if tags else ""
            lines.append(f"### {name} (`{shorthand}`){tag_str}\n")

            if summary:
                lines.append(f"*{summary}*\n")

            # Body (strip the heading since we already rendered it)
            cleaned = re.sub(r'^#[^\n]*\n', '', body.strip(), count=1).strip()
            lines.append(cleaned)
            lines.append("\n---\n")

    # Outro
    outro_path = ROOT / "outro.md"
    if outro_path.exists():
        lines.append("\n")
        lines.append(outro_path.read_text().strip())

    return "\n".join(lines)


def collapse_json(macros):
    """Produce a JSON catalog."""
    entries = []
    for meta, body in macros:
        # Clean body: remove frontmatter heading, trim
        cleaned = re.sub(r'^#[^\n]*\n', '', body.strip(), count=1).strip()

        entry = {
            "name": meta.get("name", ""),
            "shorthand": meta.get("shorthand", ""),
            "category": meta.get("category", ""),
            "tags": meta.get("tags", []),
            "summary": meta.get("summary", ""),
            "composes_with": meta.get("composes_with", []),
            "opposes": meta.get("opposes", []),
            "body": cleaned,
        }
        entries.append(entry)

    return json.dumps({"macros": entries}, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Collapse macro library into a single document")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output format (default: markdown)")
    args = parser.parse_args()

    macros = load_macros()

    if args.format == "json":
        result = collapse_json(macros)
    else:
        result = collapse_markdown(macros)

    if args.output:
        outpath = Path(args.output)
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(result)
        print(f"Written to {outpath} ({len(macros)} macros)", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
