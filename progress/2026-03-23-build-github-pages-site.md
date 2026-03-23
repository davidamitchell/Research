---
date: 2026-03-23
slug: build-github-pages-site
---

# Session: Build GitHub Pages Site

## Goal

Build a self-contained static GitHub Pages site for the Research repository, as specified in the GitHub issue.

## What was done

### `scripts/build_site.py`

Python build script that:
- Reads `Research/completed/*.md`, parses YAML front matter with PyYAML
- Applies exclusion rules: skips filenames containing "meta" or "infra", skips items with `added` before 2026-02-28
- Extracts sections: Research Question (also accepts "Question / Hypothesis"), Findings, Methodology, Technical Architecture, Implementation Logic, Strategic Choice, Decision Log, Schema
- Generates:
  - `docs/index.html` — filterable card grid with live search and tag filter (URL-reflected state)
  - `docs/research/<slug>.html` — individual item pages with breadcrumb, meta bar, sections, prev/next nav
  - `docs/tags/index.html` — all tags index
  - `docs/tags/<tag>.html` — per-tag filtered card pages
  - `docs/search.html` — standalone search with client-side JS over search-index.json
  - `docs/search-index.json` — search index array
  - `docs/.nojekyll` — prevents GitHub Pages Jekyll processing
- Uses mistune for markdown-to-HTML, PyYAML for front matter
- All HTML generated via Python string templates — no Jinja2 or other templating
- CSS inlined; IBM Plex Mono from Google Fonts; dark mode only; monochromatic palette

### `.github/workflows/build_site.yml`

GitHub Actions workflow that:
- Triggers on push to main touching `Research/completed/**` and `workflow_dispatch`
- Checks out repo, sets up Python from `.python-version`, installs mistune + PyYAML
- Runs `python scripts/build_site.py`
- Commits generated `docs/` back to main with `[skip ci]`

## Design system

- Dark mode only; no light mode toggle
- Palette: `--bg: #0d0d0d`, `--surface: #141414`, strictly monochromatic
- Font: IBM Plex Mono throughout
- No rounded corners, no box shadows, borders only
- CSS variables for all design tokens

## Items generated

- 112 research items (after exclusions)
- 564 unique tags
- All pages idempotent — running twice produces identical output
