#!/usr/bin/env python3
"""Build a static GitHub Pages site from Research/completed/*.md files.

Generates:
  docs/index.html            — landing page with stats, threads, tags, search preview
  docs/browse.html           — filterable research card grid
  docs/research/<slug>.html  — individual item pages with related items
  docs/tags/<tag>.html       — one page per unique tag
  docs/threads.html          — threads listing
  docs/threads/<slug>.html   — individual thread pages
  docs/search.html           — standalone search page
  docs/search-index.json     — search index for client-side JS
  docs/threads-index.json    — thread data for JS

Usage:
  python scripts/build_site.py

Requires: mistune, PyYAML
"""

from __future__ import annotations

import json
import re
import shutil
import textwrap
from collections import Counter
from datetime import date
from pathlib import Path

import mistune
import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
COMPLETED_DIR = REPO_ROOT / "Research" / "completed"
DOCS_DIR = REPO_ROOT / "docs"
RESEARCH_DIR = DOCS_DIR / "research"
TAGS_DIR = DOCS_DIR / "tags"
THREADS_DIR = DOCS_DIR / "threads"

CUTOFF_DATE = date(2026, 2, 28)
GITHUB_BASE = "https://github.com/davidamitchell/Research/blob/main/Research/completed/"

# Section names to extract, in display order
SECTIONS_ORDERED = [
    "Research Question",
    "Findings",
    "Methodology",
    "Technical Architecture",
    "Implementation Logic",
    "Strategic Choice",
    "Decision Log",
    "Schema",
]

# All section names that the extractor looks for (includes alias)
SECTION_PATTERNS = SECTIONS_ORDERED + ["Question / Hypothesis"]

# Regex to remove stray HTML closing tags that can appear from malformed URLs in source
# markdown. These tags are bare (appearing after a quote or another closing tag) rather
# than properly closing a block element. Pattern matches </p>, </li>, </td>, </div>
# only when immediately followed by a quote character or >.
_STRAY_CLOSE_TAGS_RE = re.compile(r"</(?:p|li|td|div)>(?=[\"'>])")

# ---------------------------------------------------------------------------
# CSS / Design system
# ---------------------------------------------------------------------------

CSS = """
:root {
  --bg:              #0d0d0d;
  --surface:         #141414;
  --surface-2:       #1c1c1c;
  --border:          #2a2a2a;
  --text:            #e8e8e8;
  --text-muted:      #666;
  --accent:          #e8e8e8;
  --accent-dim:      #333;
  --tag-bg:          #1e1e1e;
  --tag-text:        #999;
  --tag-active-bg:   #e8e8e8;
  --tag-active-text: #0d0d0d;

  --text-xs:   0.7rem;
  --text-sm:   0.8rem;
  --text-base: 0.9rem;
  --text-lg:   1.1rem;
  --text-xl:   1.4rem;
  --text-2xl:  2rem;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { font-size: 16px; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'IBM Plex Mono', monospace;
  font-size: var(--text-base);
  line-height: 1.6;
  letter-spacing: 0.02em;
}

a { color: var(--text); text-decoration: none; }
a:hover { text-decoration: underline; }

/* Nav */
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 48px;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  z-index: 100;
  display: flex;
  align-items: center;
  padding: 0 2rem;
}
.nav-inner {
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.nav-brand {
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text);
  letter-spacing: 0.05em;
}
.nav-links {
  display: flex;
  gap: 1.5rem;
}
.nav-links a {
  font-size: var(--text-sm);
  color: var(--text-muted);
  letter-spacing: 0.05em;
}
.nav-links a:hover { color: var(--text); text-decoration: none; }

/* Main content */
main {
  max-width: 960px;
  margin: 0 auto;
  padding: 80px 2rem 4rem;
}

/* Page header */
.page-header {
  margin-bottom: 2rem;
}
.page-header h1 {
  font-size: var(--text-2xl);
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: 0.02em;
}
.page-subtitle {
  font-size: var(--text-sm);
  color: var(--text-muted);
  margin-top: 0.5rem;
}

/* Search input */
.search-wrap {
  margin-bottom: 1.5rem;
}
.search-input {
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text);
  font-family: 'IBM Plex Mono', monospace;
  font-size: var(--text-sm);
  padding: 0.6rem 0.8rem;
  outline: none;
  border-radius: 0;
  letter-spacing: 0.02em;
}
.search-input:focus { border-color: var(--accent); }
.search-input::placeholder { color: var(--text-muted); }

/* Tag filter bar */
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.5rem;
  align-items: center;
}
.filter-label {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  margin-right: 0.25rem;
}
.clear-filters {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  cursor: pointer;
  margin-left: 0.5rem;
  text-decoration: underline;
}
.clear-filters:hover { color: var(--text); }

/* Tag pills */
.tag {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  background: var(--tag-bg);
  color: var(--tag-text);
  font-size: var(--text-xs);
  letter-spacing: 0.05em;
  text-transform: lowercase;
  cursor: pointer;
  border: 1px solid transparent;
  font-family: 'IBM Plex Mono', monospace;
  text-decoration: none;
}
.tag:hover { color: var(--text); text-decoration: none; }
.tag.active {
  background: var(--tag-active-bg);
  color: var(--tag-active-text);
}

/* Card grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

/* Card */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 1.25rem;
  border-radius: 0;
  transition: border-color 200ms ease;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  text-decoration: none;
  color: var(--text);
}
.card:hover { border-color: var(--accent); text-decoration: none; }
.card-title {
  font-size: var(--text-base);
  font-weight: 500;
  line-height: 1.3;
  letter-spacing: 0.02em;
}
.card-meta {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
}
.card-excerpt {
  font-size: var(--text-xs);
  color: var(--text-muted);
  line-height: 1.5;
  flex: 1;
}
.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-top: 0.25rem;
}
.card .tag { cursor: default; }

/* No results */
.no-results {
  font-size: var(--text-sm);
  color: var(--text-muted);
  padding: 2rem 0;
}

/* Item page */
.breadcrumb {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  margin-bottom: 1.5rem;
}
.breadcrumb a { color: var(--text-muted); }
.breadcrumb a:hover { color: var(--text); }
.breadcrumb span { margin: 0 0.4em; }

.item-title {
  font-size: var(--text-xl);
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: 0.02em;
  margin-bottom: 1rem;
}

.meta-bar {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 2rem;
}
.meta-sep { margin: 0 0.2em; }
.source-link {
  font-size: var(--text-xs);
  color: var(--text-muted);
  text-decoration: none;
}
.source-link:hover { text-decoration: underline; }

.item-content h2 {
  font-size: var(--text-sm);
  text-transform: lowercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-top: 2.5rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.5rem;
  font-weight: 500;
}
.item-content h3 {
  font-size: var(--text-base);
  font-weight: 500;
  margin-top: 1.5rem;
  letter-spacing: 0.02em;
}
.item-content h4, .item-content h5, .item-content h6 {
  font-size: var(--text-sm);
  font-weight: 500;
  margin-top: 1.2rem;
  letter-spacing: 0.02em;
}
.item-content p { margin-top: 0.8rem; }
.item-content ul, .item-content ol {
  margin-top: 0.8rem;
  padding-left: 1.5rem;
}
.item-content li { margin-top: 0.3rem; }
.item-content table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  font-size: var(--text-xs);
}
.item-content th, .item-content td {
  border: 1px solid var(--border);
  padding: 0.4rem 0.6rem;
  text-align: left;
}
.item-content th {
  background: var(--surface-2);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-size: var(--text-xs);
}
.item-content code {
  background: var(--surface-2);
  padding: 0.1em 0.3em;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.9em;
}
.item-content pre {
  background: var(--surface-2);
  border: 1px solid var(--border);
  padding: 1rem;
  overflow-x: auto;
  margin-top: 1rem;
}
.item-content pre code { background: none; padding: 0; }
.item-content blockquote {
  border-left: 2px solid var(--border);
  padding-left: 1rem;
  color: var(--text-muted);
  margin-top: 0.8rem;
}
.item-content a { color: var(--text); text-decoration: underline; }
.item-content a:hover { color: var(--text-muted); }
.item-content strong { font-weight: 600; }
.item-content em { font-style: italic; }
.item-content hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 2rem 0;
}

/* Prev / Next navigation */
.item-nav {
  display: flex;
  justify-content: space-between;
  border-top: 1px solid var(--border);
  padding-top: 1rem;
  margin-top: 3rem;
  font-size: var(--text-sm);
  gap: 1rem;
}
.item-nav a { color: var(--text-muted); }
.item-nav a:hover { color: var(--text); text-decoration: none; }
.item-nav-prev { text-align: left; }
.item-nav-next { text-align: right; }
.item-nav-label {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  display: block;
  margin-bottom: 0.2rem;
}

/* Tag page */
.tag-page-header {
  margin-bottom: 2rem;
}
.tag-page-header h1 {
  font-size: var(--text-xl);
  font-weight: 500;
  letter-spacing: 0.02em;
}
.back-link {
  font-size: var(--text-sm);
  color: var(--text-muted);
  display: inline-block;
  margin-top: 1rem;
}
.back-link:hover { color: var(--text); }

/* Search page */
.search-page-header {
  margin-bottom: 1.5rem;
}
.search-page-header h1 {
  font-size: var(--text-xl);
  font-weight: 500;
  letter-spacing: 0.02em;
}
.search-results-count {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
  min-height: 1.2em;
}

/* Tags list (all tags index) */
.tags-list {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}
.tags-list li {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.tag-count {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.05em;
}

/* Responsive */
@media (max-width: 640px) {
  :root {
    --text-xs: 0.75rem;
    --text-sm: 0.85rem;
    --text-base: 1rem;
    --text-lg: 1.15rem;
    --text-xl: 1.3rem;
    --text-2xl: 1.6rem;
  }
  nav {
    position: sticky;
    height: auto;
    padding: 0.75rem 1rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  .container {
    padding: 0 1rem;
  }
  main {
    padding: 0 1rem;
    padding-top: 64px;
  }
  .card-grid {
    grid-template-columns: 1fr;
  }
  .stats-block {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border: 1px solid var(--border);
  }
  .stat-item {
    border-right: none !important;
    border-bottom: 1px solid var(--border);
  }
  .stat-item:nth-child(odd) {
    border-right: 1px solid var(--border) !important;
  }
  .stat-item:nth-child(3),
  .stat-item:nth-child(4) {
    border-bottom: none;
  }
  .meta-bar {
    flex-wrap: wrap;
    gap: 0.4rem;
    font-size: var(--text-sm);
  }
  .key-claims {
    padding: 0.75rem 1rem;
    font-size: var(--text-base);
  }
  .item-content h2 {
    margin-top: 2rem;
  }
  .item-nav {
    flex-direction: column;
    gap: 0.75rem;
  }
  .breadcrumb {
    font-size: var(--text-sm);
  }
  .card {
    padding: 1rem;
  }
  .tag {
    padding: 0.2rem 0.6rem;
  }
  .search-input {
    padding: 0.75rem 1rem;
    font-size: var(--text-base);
  }
  .full-title-subtitle {
    font-size: var(--text-sm);
    color: var(--text-muted);
    margin-top: 0.25rem;
    margin-bottom: 1rem;
  }
}

.full-title-subtitle {
  font-size: var(--text-sm);
  color: var(--text-muted);
  margin-top: 0.25rem;
  margin-bottom: 1.5rem;
  line-height: 1.4;
}

/* Stats block */
.stats-block { display: flex; border: 1px solid var(--border); margin: 2rem 0; }
.stat-item { flex: 1; padding: 1.25rem; text-align: center; border-right: 1px solid var(--border); }
.stat-item:last-child { border-right: none; }
.stat-number { font-size: var(--text-2xl); color: var(--text); display: block; line-height: 1.2; }
.stat-label { font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.05em; display: block; margin-top: 0.25rem; }

/* Key claims block */
.key-claims { background: var(--surface-2); border-left: 2px solid var(--border); padding: 1rem 1.25rem; margin-bottom: 2rem; }
.key-claims-label { font-size: var(--text-xs); text-transform: lowercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 0.75rem; }
.key-claims ol { list-style: none; padding: 0; margin: 0; }
.key-claims li { font-size: var(--text-sm); line-height: 1.6; padding: 0.3rem 0; border-bottom: 1px solid var(--border); }
.key-claims li:last-child { border-bottom: none; }

/* Relationship type pill */
.rel-pill { display: inline-block; padding: 0.15rem 0.5rem; background: transparent; border: 1px solid var(--border); color: var(--text-muted); font-size: var(--text-xs); letter-spacing: 0.05em; text-transform: lowercase; font-family: 'IBM Plex Mono', monospace; }

/* Related items */
.related-section { margin-top: 2.5rem; }
.related-group { margin-top: 1rem; }
.related-group-label { font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.05em; text-transform: lowercase; margin-bottom: 0.5rem; }
.related-entry { display: flex; align-items: baseline; gap: 0.6rem; padding: 0.4rem 0; border-bottom: 1px solid var(--border); font-size: var(--text-sm); }
.related-entry:last-child { border-bottom: none; }
.related-note { color: var(--text-muted); font-size: var(--text-xs); }

/* Thread connector */
.thread-connector { text-align: center; font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.05em; padding: 0.5rem 0; }

/* Thread card variant */
.thread-card-excerpt { font-size: var(--text-xs); color: var(--text-muted); line-height: 1.5; flex: 1; }

/* Featured sections on landing page */
.landing-desc { font-size: var(--text-sm); color: var(--text-muted); margin: 1.5rem 0; line-height: 1.6; }
.featured-section { margin: 2rem 0; }
.featured-label { font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.1em; text-transform: lowercase; margin-bottom: 0.75rem; }
.featured-pills { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.thread-pill { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.3rem 0.75rem; background: var(--surface); border: 1px solid var(--border); color: var(--text); font-size: var(--text-xs); letter-spacing: 0.05em; text-decoration: none; }
.thread-pill:hover { border-color: var(--text); text-decoration: none; }
.thread-pill-count { color: var(--text-muted); }
.tag-pill-link { display: inline-block; padding: 0.15rem 0.5rem; background: var(--tag-bg); color: var(--tag-text); font-size: var(--text-xs); letter-spacing: 0.05em; text-transform: lowercase; text-decoration: none; font-family: 'IBM Plex Mono', monospace; }
.tag-pill-link:hover { color: var(--text); text-decoration: none; }

/* Search preview on landing */
.search-preview-wrap { position: relative; margin-bottom: 2rem; }
.search-preview-results { background: var(--surface); border: 1px solid var(--border); border-top: none; display: none; }
.search-preview-item { display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0.8rem; border-bottom: 1px solid var(--border); text-decoration: none; color: var(--text); font-size: var(--text-sm); gap: 1rem; }
.search-preview-item:last-child { border-bottom: none; }
.search-preview-item:hover { background: var(--surface-2); text-decoration: none; }
.search-preview-date { font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.05em; flex-shrink: 0; }
.search-see-all { display: block; text-align: right; padding: 0.4rem 0.8rem; font-size: var(--text-xs); color: var(--text-muted); border-top: 1px solid var(--border); text-decoration: none; }
.search-see-all:hover { color: var(--text); text-decoration: none; }

/* Thread filter row */
.thread-filter-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1rem; align-items: center; }
.thread-filter-btn { display: inline-block; padding: 0.15rem 0.5rem; background: transparent; border: 1px solid var(--border); color: var(--text-muted); font-size: var(--text-xs); letter-spacing: 0.05em; cursor: pointer; font-family: 'IBM Plex Mono', monospace; text-transform: lowercase; }
.thread-filter-btn.active { background: var(--surface-2); border-color: var(--text); color: var(--text); }

/* Threads listing */
.thread-list { display: flex; flex-direction: column; gap: 0; }
.thread-entry { padding: 1rem; border: 1px solid var(--border); border-bottom: none; text-decoration: none; color: var(--text); display: block; }
.thread-entry:last-child { border-bottom: 1px solid var(--border); }
.thread-entry:hover { background: var(--surface); text-decoration: none; }
.thread-entry-title { font-size: var(--text-base); font-weight: 500; }
.thread-entry-meta { font-size: var(--text-xs); color: var(--text-muted); margin-top: 0.25rem; letter-spacing: 0.05em; }
"""

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

GOOGLE_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n'
)


def html_head(title: str, extra_head: str = "") -> str:
    return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{title}</title>
          {GOOGLE_FONTS}  <style>{CSS}</style>
          {extra_head}
        </head>
        <body>
        """)


def html_nav() -> str:
    return textwrap.dedent("""\
        <nav>
          <div class="nav-inner">
            <a class="nav-brand" href="/Research/">Research</a>
            <div class="nav-links">
              <a href="/Research/threads.html">Threads</a>
              <a href="/Research/tags/">Tags</a>
              <a href="/Research/search.html">Search</a>
              <a href="https://github.com/davidamitchell/Research" target="_blank" rel="noopener">GitHub</a>
            </div>
          </div>
        </nav>
        """)


def html_foot() -> str:
    return "</body>\n</html>\n"


def escape(text: str) -> str:
    """Minimal HTML escaping."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


# ---------------------------------------------------------------------------
# Title helpers
# ---------------------------------------------------------------------------


def make_display_title(title: str) -> str:
    """Shorten title for display: collapse acronym expansions, colon-truncate, length limit."""
    result = title
    abbr_pattern = re.compile(r"[A-Z][a-zA-Z\-]*(?:\s+[A-Za-z][a-zA-Z\-]*)*\s+\(([A-Z]{2,8})\)")
    prev = None
    while prev != result:
        prev = result
        result = abbr_pattern.sub(lambda m: m.group(1), result)
    if ":" in result:
        before_colon = result.split(":", 1)[0].strip()
        if len(before_colon) < 80:
            result = before_colon
    if len(result) > 80:
        truncated = result[:80]
        last_space = truncated.rfind(" ")
        if last_space > 0:
            truncated = truncated[:last_space]
        result = truncated + "…"
    return result


# ---------------------------------------------------------------------------
# Singleton tag filtering
# ---------------------------------------------------------------------------


def filter_singleton_tags(items: list[dict]) -> tuple[set[str], int, int]:
    """Return (tags_to_drop, n_dropped, n_retained_sole).

    For each tag T where count == 1:
      - If the single item carrying T has at least one other tag with count > 1: drop T
      - If ALL of that item's tags have count == 1: retain T (sole tag for navigation)
    """
    tag_counts: Counter[str] = Counter(t for item in items for t in item["tags"])
    singleton_tags = {t for t, c in tag_counts.items() if c == 1}

    tags_to_drop: set[str] = set()
    tags_to_retain: set[str] = set()
    for tag in singleton_tags:
        items_with_tag = [i for i in items if tag in i["tags"]]
        if not items_with_tag:
            continue
        single_item = items_with_tag[0]
        has_non_singleton = any(tag_counts[t] > 1 for t in single_item["tags"] if t != tag)
        if has_non_singleton:
            tags_to_drop.add(tag)
        else:
            tags_to_retain.add(tag)

    return tags_to_drop, len(tags_to_drop), len(tags_to_retain)


# ---------------------------------------------------------------------------
# Source reference parsing and autolinking
# ---------------------------------------------------------------------------


def parse_source_refs(sources_text: str) -> dict[str, str]:
    """Parse Sources section markdown into {display_name: url} dict."""
    refs: dict[str, str] = {}
    if not sources_text:
        return refs
    for m in re.finditer(r"\[([^\]]+)\]\((https://[^)]+)\)", sources_text):
        refs[m.group(1)] = m.group(2)
    for m in re.finditer(r"^[*\-]?\s*(.+?):\s+(https://\S+)", sources_text, re.MULTILINE):
        name = m.group(1).strip("*- []")
        if len(name) < 100 and name:
            refs[name] = m.group(2).rstrip(".,;)")
    return refs


def autolink_html(html: str, source_refs: dict[str, str]) -> str:
    """Replace first unlinked occurrence of each ref name; autolink bare https:// URLs."""
    link_pattern = re.compile(r"<a\b[^>]*>.*?</a>", re.DOTALL | re.IGNORECASE)

    def replace_first_outside_links(html_text: str, search: str, replacement: str) -> str:
        result = []
        last_end = 0
        replaced = False
        for m in link_pattern.finditer(html_text):
            segment = html_text[last_end : m.start()]
            if not replaced:
                idx = segment.find(search)
                if idx >= 0:
                    result.append(segment[:idx] + replacement + segment[idx + len(search) :])
                    replaced = True
                else:
                    result.append(segment)
            else:
                result.append(segment)
            result.append(m.group(0))
            last_end = m.end()
        segment = html_text[last_end:]
        if not replaced:
            idx = segment.find(search)
            if idx >= 0:
                result.append(segment[:idx] + replacement + segment[idx + len(search) :])
            else:
                result.append(segment)
        else:
            result.append(segment)
        return "".join(result)

    for name, url in source_refs.items():
        if not name or not url:
            continue
        escaped_url = url.replace('"', "&quot;")
        link_html = f'<a href="{escaped_url}">{escape(name)}</a>'
        html = replace_first_outside_links(html, name, link_html)

    def get_display_domain(url: str) -> str:
        if "arxiv.org" in url:
            arxiv_m = re.search(r"arxiv\.org/abs/(\S+?)(?:\s|$|[,;)])", url)
            if arxiv_m:
                return f"arxiv.org/abs/{arxiv_m.group(1)}"
        m = re.match(r"https?://([^/]+)", url)
        return m.group(1) if m else url

    def autolink_bare_urls(html_text: str) -> str:
        url_pattern = re.compile(r"https://\S+")

        def replace_url(um: re.Match) -> str:
            url = um.group(0).rstrip(".,;)")
            return f'<a href="{url}">{get_display_domain(url)}</a>'

        result = []
        last_end = 0
        for m in link_pattern.finditer(html_text):
            segment = html_text[last_end : m.start()]
            result.append(url_pattern.sub(replace_url, segment))
            result.append(m.group(0))
            last_end = m.end()
        segment = html_text[last_end:]
        result.append(url_pattern.sub(replace_url, segment))
        return "".join(result)

    html = autolink_bare_urls(html)
    return html


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML front matter and body. Returns (meta, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_src = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    try:
        meta = yaml.safe_load(yaml_src) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, body


def normalise_tags(raw: object) -> list[str]:
    """Normalise tags field to a list of lowercase strings."""
    if isinstance(raw, list):
        return [str(t).strip().lower() for t in raw if t]
    if isinstance(raw, str):
        return [t.strip().lower() for t in re.split(r"[,\s]+", raw) if t.strip()]
    return []


def slugify(name: str) -> str:
    """Convert a filename stem to a URL slug."""
    s = name.lower()
    s = re.sub(r"[\s\.]+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def extract_section(body: str, section_name: str) -> str:
    """Extract content of a named ## section from markdown body."""
    lines = body.split("\n")
    in_section = False
    result: list[str] = []
    for line in lines:
        if re.match(r"^##\s+" + re.escape(section_name) + r"\s*$", line):
            in_section = True
            continue
        if in_section:
            if re.match(r"^##\s+", line):
                break
            result.append(line)
    return "\n".join(result).strip()


def extract_sections(body: str) -> dict[str, str]:
    """Extract all tracked sections from the markdown body."""
    sections: dict[str, str] = {}
    # "Research Question" and "Question / Hypothesis" map to the same key
    for name in SECTION_PATTERNS:
        content = extract_section(body, name)
        if content:
            key = "Research Question" if name == "Question / Hypothesis" else name
            if key not in sections:
                sections[key] = content
    return sections


def strip_evidence_map(text: str) -> str:
    """Remove an Evidence Map section appended by tooling."""
    lines = text.split("\n")
    result: list[str] = []
    skip = False
    for line in lines:
        if re.match(r"^##\s+Evidence Map\s*$", line, re.IGNORECASE):
            skip = True
            continue
        if skip and re.match(r"^##\s+", line):
            skip = False
        if not skip:
            result.append(line)
    return "\n".join(result)


def strip_evidence_map_table(text: str) -> str:
    """Strip markdown table that follows a line containing 'Evidence Map'.

    Used before rendering section content so inline Evidence Map tables
    (e.g. inside ## Findings) do not appear as HTML tables on item pages.
    Strips from the Evidence Map heading line through to the last
    consecutive line starting with '|'. Blank lines between the heading
    and the table are also consumed.
    """
    lines = text.split("\n")
    result: list[str] = []
    skip = False
    found_table = False
    for line in lines:
        if not skip and re.search(r"\bEvidence Map\b", line, re.IGNORECASE):
            skip = True
            found_table = False
            continue
        if skip:
            stripped = line.strip()
            if stripped.startswith("|"):
                found_table = True
                continue
            if not stripped and not found_table:
                # Blank line before any table row: keep skipping
                continue
            # Non-blank, non-table line ends the skip
            skip = False
            found_table = False
        result.append(line)
    return "\n".join(result)


def get_findings_excerpt(item: dict, max_chars: int = 200) -> str:
    """Return a short plain-text excerpt from the Findings section."""
    findings = item["sections"].get("Findings", "")
    if not findings:
        return ""
    findings = strip_evidence_map_table(findings)
    # Strip markdown syntax for plain-text preview
    text = re.sub(r"#{1,6}\s+", "", findings)
    text = re.sub(r"\*{1,2}([^*]+)\*{1,2}", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_chars:
        return text[:max_chars].rstrip() + "…"
    return text


def load_items() -> tuple[list[dict], dict[str, int]]:
    """Load and filter all completed research items.

    Returns (items, exclusion_stats) where exclusion_stats has keys
    'meta_infra' and 'date' with counts of excluded files.
    """
    items = []
    excl_meta = 0
    excl_date = 0
    for path in sorted(COMPLETED_DIR.glob("*.md"), reverse=True):
        name = path.name
        if name.lower() == "readme.md":
            continue
        if re.search(r"meta|infra", name, re.IGNORECASE):
            excl_meta += 1
            continue
        try:
            text = path.read_text(encoding="utf-8")
            text = strip_evidence_map(text)
            meta, body = parse_frontmatter(text)
        except Exception as exc:
            print(f"ERROR: failed to parse {path}: {exc}")
            raise SystemExit(1) from exc
        added_raw = meta.get("added")
        if not added_raw:
            excl_date += 1
            continue
        try:
            if isinstance(added_raw, str):
                added = date.fromisoformat(added_raw)
            else:
                added = date(added_raw.year, added_raw.month, added_raw.day)
        except (ValueError, AttributeError):
            excl_date += 1
            continue
        if added < CUTOFF_DATE:
            excl_date += 1
            continue
        title = str(meta.get("title", path.stem))
        tags = normalise_tags(meta.get("tags", []))
        slug = slugify(path.stem)
        sections = extract_sections(body)
        sources_text = extract_section(body, "Sources")
        question = sections.get("Research Question", "")
        thread_field = meta.get("thread", "")
        items.append(
            {
                "slug": slug,
                "filename": name,
                "title": title,
                "display_title": make_display_title(title),
                "added": added,
                "added_str": added.isoformat(),
                "tags": tags,
                "sections": sections,
                "_sources_text": sources_text,
                "question": question,
                "question_excerpt": question[:200].strip(),
                "github_url": GITHUB_BASE + name,
                "thread": str(thread_field).strip() if thread_field else "",
            }
        )
    items.sort(key=lambda x: x["added"], reverse=True)
    return items, {"meta_infra": excl_meta, "date": excl_date}


def load_metadata() -> dict:
    """Load state/content_metadata.json if present, else return empty dict."""
    path = REPO_ROOT / "state" / "content_metadata.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_links(items: list[dict]) -> dict[str, list[dict]]:
    """Build a map of slug -> list of related items (by shared tags, >= 2 tags)."""
    links: dict[str, list[dict]] = {item["slug"]: [] for item in items}
    for item in items:
        item_tags = set(item["tags"])
        if len(item_tags) < 2:
            continue
        for other in items:
            if other["slug"] == item["slug"]:
                continue
            shared = item_tags & set(other["tags"])
            if len(shared) >= 2:
                links[item["slug"]].append(
                    {"item": other, "shared_tags": sorted(shared), "rel": "related"}
                )
    # Deduplicate and keep top 5 by shared tag count
    for slug in links:
        seen: set[str] = set()
        deduped = []
        for entry in sorted(links[slug], key=lambda e: -len(e["shared_tags"])):
            if entry["item"]["slug"] not in seen:
                seen.add(entry["item"]["slug"])
                deduped.append(entry)
        links[slug] = deduped[:5]
    return links


def detect_threads(items: list[dict]) -> list[dict]:
    """Group items into threads.

    Priority:
    1. Items with a matching ``thread`` frontmatter field are grouped together.
    2. Items sharing 3+ tags form implicit threads (tag cluster).

    Returns a list of thread dicts, each with keys:
      slug, title, items, kind ('explicit' or 'implicit'), tag_cluster (list)
    """
    threads: list[dict] = []

    # Explicit threads via frontmatter
    explicit: dict[str, list[dict]] = {}
    for item in items:
        if item["thread"]:
            explicit.setdefault(item["thread"], []).append(item)
    for name, thread_items in explicit.items():
        if len(thread_items) < 2:
            continue
        thread_items_sorted = sorted(thread_items, key=lambda x: x["added"])
        threads.append(
            {
                "slug": slugify(name),
                "title": name,
                "items": thread_items_sorted,
                "kind": "explicit",
                "tag_cluster": [],
            }
        )

    # Implicit threads: items sharing 3+ tags
    explicit_slugs = {item["slug"] for t in threads for item in t["items"]}
    remaining = [item for item in items if item["slug"] not in explicit_slugs]

    # Find dense tag clusters
    processed: set[str] = set()
    for item in remaining:
        if item["slug"] in processed or len(item["tags"]) < 3:
            continue
        item_tags = set(item["tags"])
        cluster = [item]
        for other in remaining:
            if other["slug"] == item["slug"] or other["slug"] in processed:
                continue
            shared = item_tags & set(other["tags"])
            if len(shared) >= 3:
                cluster.append(other)
        if len(cluster) >= 3:
            for c in cluster:
                processed.add(c["slug"])
            cluster_sorted = sorted(cluster, key=lambda x: x["added"])
            # Title from most frequent tags
            all_tags: list[str] = []
            for c in cluster:
                all_tags.extend(c["tags"])
            top_tags = [t for t, _ in Counter(all_tags).most_common(3)]
            thread_title = " / ".join(top_tags)
            threads.append(
                {
                    "slug": slugify(thread_title),
                    "title": thread_title,
                    "items": cluster_sorted,
                    "kind": "implicit",
                    "tag_cluster": top_tags,
                }
            )

    threads.sort(key=lambda t: -len(t["items"]))
    return threads


def detect_shared_sources(items: list[dict]) -> dict[str, list[dict]]:
    """Group items that cite the same GitHub source URL (by filename stem)."""
    source_map: dict[str, list[dict]] = {}
    for item in items:
        stem = Path(item["filename"]).stem
        source_map.setdefault(stem, []).append(item)
    return {k: v for k, v in source_map.items() if len(v) > 1}


# ---------------------------------------------------------------------------
# Card HTML component
# ---------------------------------------------------------------------------


def render_card(item: dict, link_prefix: str = "/Research/research/") -> str:
    tags_html = "".join(f'<span class="tag">{escape(t)}</span>' for t in item["tags"])
    excerpt = item["question_excerpt"]
    if len(item["question"]) > 200:
        excerpt = excerpt.rstrip() + "…"
    return (
        f'<a class="card" href="{link_prefix}{item["slug"]}.html"'
        f' data-title="{escape(item["display_title"].lower())}"'
        f' data-question="{escape(item["question_excerpt"].lower())}"'
        f' data-tags="{escape(",".join(item["tags"]))}">\n'
        f'  <div class="card-title">{escape(item["display_title"])}</div>\n'
        f'  <div class="card-meta">{item["added_str"]}</div>\n'
        f'  <div class="card-tags">{tags_html}</div>\n'
        f'  <div class="card-excerpt">{escape(excerpt)}</div>\n'
        f"</a>\n"
    )


# ---------------------------------------------------------------------------
# Shared JS snippets
# ---------------------------------------------------------------------------

BROWSE_JS = """
(function() {
  var cards = Array.from(document.querySelectorAll('.card'));
  var tagBtns = Array.from(document.querySelectorAll('.filter-bar .tag'));
  var searchInput = document.getElementById('search-input');
  var clearBtn = document.getElementById('clear-filters');
  var noResults = document.getElementById('no-results');
  var activeTags = new Set();

  function getParams() {
    var params = new URLSearchParams(window.location.search);
    var t = params.get('tags');
    var q = params.get('q') || '';
    return { tags: t ? t.split(',').filter(Boolean) : [], q: q };
  }

  function setParams() {
    var params = new URLSearchParams();
    if (activeTags.size > 0) params.set('tags', Array.from(activeTags).join(','));
    var q = searchInput.value.trim();
    if (q) params.set('q', q);
    var str = params.toString();
    var url = window.location.pathname + (str ? '?' + str : '');
    history.replaceState(null, '', url);
  }

  function applyFilters() {
    var q = searchInput.value.trim().toLowerCase();
    var anyVisible = false;
    cards.forEach(function(card) {
      var cardTags = card.dataset.tags ? card.dataset.tags.split(',') : [];
      var tagMatch = activeTags.size === 0 || Array.from(activeTags).some(function(t) {
        return cardTags.indexOf(t) !== -1;
      });
      var textMatch = !q ||
        card.dataset.title.indexOf(q) !== -1 ||
        card.dataset.question.indexOf(q) !== -1;
      var visible = tagMatch && textMatch;
      card.style.display = visible ? '' : 'none';
      if (visible) anyVisible = true;
    });
    var filtersActive = activeTags.size > 0 || q.length > 0;
    if (noResults) noResults.style.display = (filtersActive && !anyVisible) ? '' : 'none';
    if (clearBtn) clearBtn.style.display = activeTags.size > 0 ? '' : 'none';
    tagBtns.forEach(function(btn) {
      btn.classList.toggle('active', activeTags.has(btn.dataset.tag));
    });
    setParams();
  }

  var init = getParams();
  init.tags.forEach(function(t) { activeTags.add(t); });
  searchInput.value = init.q;

  tagBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var t = btn.dataset.tag;
      if (activeTags.has(t)) activeTags.delete(t);
      else activeTags.add(t);
      applyFilters();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', function() {
      activeTags.clear();
      applyFilters();
    });
  }

  searchInput.addEventListener('input', applyFilters);
  applyFilters();
})();
"""

SEARCH_JS = """
(function() {
  var input = document.getElementById('search-input');
  var resultsEl = document.getElementById('search-results');
  var countEl = document.getElementById('results-count');
  var index = null;

  function fetchIndex() {
    fetch('/Research/search-index.json')
      .then(function(r) { return r.json(); })
      .then(function(data) { index = data; runSearch(); })
      .catch(function() {
        if (countEl) countEl.textContent = 'Search index unavailable.';
      });
  }

  function escapeHtml(s) {
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
            .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  }

  function renderCard(item) {
    var tags = item.tags.map(function(t) {
      return '<span class="tag">' + escapeHtml(t) + '</span>';
    }).join('');
    return '<a class="card" href="/Research/research/' + item.slug + '.html">'
      + '<div class="card-title">' + escapeHtml(item.title) + '</div>'
      + '<div class="card-meta">' + escapeHtml(item.added) + '</div>'
      + '<div class="card-tags">' + tags + '</div>'
      + '<div class="card-excerpt">' + escapeHtml(item.findings_excerpt || item.question_excerpt || '') + '</div>'
      + '</a>';
  }

  function runSearch() {
    if (!index) return;
    var q = input.value.trim().toLowerCase();
    var results = !q ? [] : index.filter(function(item) {
      return (item.full_text || item.title + ' ' + item.question_excerpt).toLowerCase().indexOf(q) !== -1;
    });
    resultsEl.innerHTML = results.map(renderCard).join('');
    if (countEl) {
      if (!q) {
        countEl.textContent = '';
      } else if (results.length === 0) {
        countEl.textContent = 'No results found.';
      } else {
        countEl.textContent = results.length + ' result' + (results.length === 1 ? '' : 's');
      }
    }
    var params = new URLSearchParams();
    if (q) params.set('q', q);
    var str = params.toString();
    history.replaceState(null, '', window.location.pathname + (str ? '?' + str : ''));
  }

  var params = new URLSearchParams(window.location.search);
  var initQ = params.get('q') || '';
  input.value = initQ;

  input.addEventListener('input', runSearch);
  fetchIndex();
})();
"""

LANDING_SEARCH_JS = """
(function() {
  var input = document.getElementById('landing-search');
  var resultsEl = document.getElementById('landing-search-results');
  var index = null;

  function fetchIndex() {
    fetch('/Research/search-index.json')
      .then(function(r) { return r.json(); })
      .then(function(data) { index = data; })
      .catch(function() {});
  }

  function escapeHtml(s) {
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
            .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  }

  function runPreview() {
    if (!index || !resultsEl) return;
    var q = input.value.trim().toLowerCase();
    if (!q) { resultsEl.style.display = 'none'; resultsEl.innerHTML = ''; return; }
    var results = index.filter(function(item) {
      return item.title.toLowerCase().indexOf(q) !== -1
          || item.question_excerpt.toLowerCase().indexOf(q) !== -1
          || item.tags.join(' ').indexOf(q) !== -1;
    }).slice(0, 6);
    if (!results.length) { resultsEl.style.display = 'none'; return; }
    resultsEl.innerHTML = results.map(function(item) {
      return '<a class="search-preview-item" href="/Research/research/' + item.slug + '.html">'
        + '<span>' + escapeHtml(item.title) + '</span>'
        + '<span class="search-preview-date">' + escapeHtml(item.added) + '</span>'
        + '</a>';
    }).join('') + '<a class="search-see-all" href="/Research/search.html?q=' + encodeURIComponent(input.value.trim()) + '">see all results →</a>';
    resultsEl.style.display = '';
  }

  if (input) {
    input.addEventListener('input', runPreview);
    document.addEventListener('click', function(e) {
      if (!input.contains(e.target) && !resultsEl.contains(e.target)) {
        resultsEl.style.display = 'none';
      }
    });
  }

  fetchIndex();
})();
"""

# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------


def build_landing(items: list[dict], threads: list[dict]) -> str:
    """Generate docs/index.html — landing page."""
    count = len(items)
    all_tags_flat: list[str] = []
    for item in items:
        all_tags_flat.extend(item["tags"])
    tag_count = len(set(all_tags_flat))
    all_tags: Counter[str] = Counter(all_tags_flat)
    thread_count = len(threads)

    # Stats block
    stats_html = (
        f'<div class="stats-block">'
        f'<div class="stat-item"><span class="stat-number">{count}</span>'
        f'<span class="stat-label">items</span></div>'
        f'<div class="stat-item"><span class="stat-number">{tag_count}</span>'
        f'<span class="stat-label">tags</span></div>'
        f'<div class="stat-item"><span class="stat-number">{thread_count}</span>'
        f'<span class="stat-label">threads</span></div>'
        f"</div>"
    )

    # Thread pills (top 8 by size)
    thread_pills = ""
    for t in threads[:8]:
        thread_pills += (
            f'<a class="thread-pill" href="/Research/threads/{t["slug"]}.html">'
            f"{escape(t['title'])}"
            f' <span class="thread-pill-count">{len(t["items"])}</span>'
            f"</a>"
        )

    # Tag pills (top 20 by frequency)
    tag_pills = ""
    for tag, _ in all_tags.most_common(20):
        tag_pills += (
            f'<a class="tag-pill-link tag" href="/Research/tags/{escape(tag)}.html">'
            f"{escape(tag)}</a>"
        )

    return (
        html_head("Research", extra_head="")
        + html_nav()
        + f"""\
<main>
  <div class="page-header">
    <h1>Research</h1>
    <p class="page-subtitle">notes, findings, and threads</p>
  </div>
  {stats_html}
  <div class="search-preview-wrap">
    <input id="landing-search" class="search-input" type="text"
           placeholder="search research items…" autocomplete="off">
    <div id="landing-search-results" class="search-preview-results"></div>
  </div>
  <div class="featured-section">
    <div class="featured-label">threads</div>
    <div class="featured-pills">{thread_pills}</div>
  </div>
  <div class="featured-section">
    <div class="featured-label">topics</div>
    <div class="featured-pills">{tag_pills}</div>
  </div>
</main>
<script>{LANDING_SEARCH_JS}</script>
"""
        + html_foot()
    )


def build_browse(items: list[dict]) -> str:
    """Generate docs/browse.html — filterable research card grid."""
    all_tags: set[str] = set()
    for item in items:
        all_tags.update(item["tags"])
    sorted_tags = sorted(all_tags)

    tag_btns = "".join(
        f'<button class="tag" data-tag="{escape(t)}">{escape(t)}</button>' for t in sorted_tags
    )
    cards_html = "".join(render_card(item) for item in items)
    count = len(items)

    return (
        html_head("Browse — Research")
        + html_nav()
        + f"""\
<main>
  <div class="page-header">
    <h1>Browse</h1>
    <p class="page-subtitle">{count} items</p>
  </div>
  <div class="search-wrap">
    <input id="search-input" class="search-input" type="text"
           placeholder="search by title or question…" autocomplete="off">
  </div>
  <div class="filter-bar">
    <span class="filter-label">tags:</span>
    {tag_btns}
    <span id="clear-filters" class="clear-filters" style="display:none">clear</span>
  </div>
  <div class="card-grid">
    {cards_html}
  </div>
  <div id="no-results" class="no-results" style="display:none">No matching items.</div>
</main>
<script>{BROWSE_JS}</script>
"""
        + html_foot()
    )


def _render_key_claims(meta_claims: list[str]) -> str:
    """Render key claims block from pre-extracted, clean claim sentences."""
    if not meta_claims:
        return ""
    items_html = "".join(f"<li>{escape(c)}</li>\n" for c in meta_claims)
    return (
        '<div class="key-claims">'
        '<div class="key-claims-label">key claims</div>'
        f"<ol>{items_html}</ol>"
        "</div>\n"
    )


def _render_related(related: list[dict]) -> str:
    """Render related items section."""
    if not related:
        return ""
    entries_html = ""
    for entry in related:
        other = entry["item"]
        shared = ", ".join(entry["shared_tags"])
        entries_html += (
            f'<div class="related-entry">'
            f'<a href="/Research/research/{other["slug"]}.html">{escape(other["title"])}</a>'
            f' <span class="related-note">via {escape(shared)}</span>'
            f"</div>\n"
        )
    return (
        '<div class="related-section">'
        '<div class="related-group-label">related items</div>'
        f'<div class="related-group">{entries_html}</div>'
        "</div>\n"
    )


def build_item_page(
    item: dict,
    prev_item: dict | None,
    next_item: dict | None,
    related: list[dict] | None = None,
    meta_claims: list[str] | None = None,
) -> str:
    """Generate docs/research/<slug>.html."""
    md = mistune.create_markdown(plugins=["table", "strikethrough"])

    display_title = item["display_title"]
    full_title = item["title"]
    wiki_slug = item["slug"]

    tags_html = "".join(
        f'<a class="tag" href="/Research/tags/{escape(t)}.html">{escape(t)}</a> '
        for t in item["tags"]
    )

    # Key claims from pre-extracted metadata (clean, source-URL-free sentences)
    key_claims_html = _render_key_claims(meta_claims or [])

    # Build source refs for autolinking
    source_refs = parse_source_refs(item.get("_sources_text", ""))

    sections_html = ""
    for section_name in SECTIONS_ORDERED:
        content = item["sections"].get(section_name, "")
        if not content:
            continue
        content = strip_evidence_map_table(content)
        rendered = md(content)
        rendered = autolink_html(rendered, source_refs)
        rendered = _STRAY_CLOSE_TAGS_RE.sub("", rendered)
        sections_html += f"<h2>{escape(section_name)}</h2>\n{rendered}\n"

    related_html = _render_related(related or [])

    # Subtitle line shown when display_title has been shortened
    subtitle_html = ""
    if display_title != full_title:
        subtitle_html = f'<p class="full-title-subtitle">{escape(full_title)}</p>\n'

    # Prev / Next
    prev_html = ""
    next_html = ""
    if prev_item:
        prev_html = (
            f'<div class="item-nav-prev">'
            f'<span class="item-nav-label">← newer</span>'
            f'<a href="/Research/research/{prev_item["slug"]}.html">'
            f"{escape(prev_item['display_title'])}</a>"
            f"</div>"
        )
    if next_item:
        next_html = (
            f'<div class="item-nav-next">'
            f'<span class="item-nav-label">older →</span>'
            f'<a href="/Research/research/{next_item["slug"]}.html">'
            f"{escape(next_item['display_title'])}</a>"
            f"</div>"
        )

    return (
        html_head(f"{escape(display_title)} — Research")
        + html_nav()
        + f"""\
<main>
  <div class="breadcrumb">
    <a href="/Research/">Research</a>
    <span>/</span>
    <span>{escape(display_title)}</span>
  </div>
  <h1 class="item-title">{escape(display_title)}</h1>
  {subtitle_html}  <div class="meta-bar">
    <span>{item["added_str"]}</span>
    <span class="meta-sep">·</span>
    {tags_html}
    <span class="meta-sep">·</span>
    <a class="source-link" href="{item["github_url"]}" target="_blank" rel="noopener">source →</a>
    <span class="meta-sep">·</span>
    <a class="source-link" href="https://github.com/davidamitchell/Research/wiki/{wiki_slug}" target="_blank" rel="noopener">wiki →</a>
  </div>
  {key_claims_html}
  <div class="item-content">
    {sections_html}
  </div>
  {related_html}
  <div class="item-nav">
    {prev_html}
    {next_html}
  </div>
</main>
"""
        + html_foot()
    )


def build_tag_page(tag: str, tag_items: list[dict]) -> str:
    """Generate docs/tags/<tag>.html."""
    cards_html = "".join(render_card(item) for item in tag_items)
    count = len(tag_items)
    return (
        html_head(f"Tagged: {escape(tag)} — Research")
        + html_nav()
        + f"""\
<main>
  <div class="tag-page-header">
    <h1>Tagged: {escape(tag)}</h1>
    <p class="page-subtitle">{count} item{"s" if count != 1 else ""}</p>
    <a class="back-link" href="/Research/tags/">← all tags</a>
  </div>
  <div class="card-grid">
    {cards_html}
  </div>
</main>
"""
        + html_foot()
    )


def build_tags_index(tags_map: dict[str, list[dict]]) -> str:
    """Generate docs/tags/index.html — all tags listed alphabetically."""
    sorted_tags = sorted(tags_map.keys())
    rows = "".join(
        f'<li data-tag="{escape(t)}">'
        f'<a class="tag" href="/Research/tags/{escape(t)}.html">{escape(t)}</a>'
        f' <span class="tag-count">({len(tags_map[t])})</span></li>\n'
        for t in sorted_tags
    )
    tags_filter_js = """
(function() {
  var input = document.getElementById('tag-filter');
  var items = document.querySelectorAll('#tags-list li');
  if (!input) return;
  input.addEventListener('input', function() {
    var q = input.value.trim().toLowerCase();
    items.forEach(function(li) {
      var tag = li.getAttribute('data-tag') || '';
      li.style.display = (!q || tag.indexOf(q) !== -1) ? '' : 'none';
    });
  });
})();
"""
    return (
        html_head("Tags — Research")
        + html_nav()
        + f"""\
<main>
  <div class="tag-page-header">
    <h1>Tags</h1>
    <p class="page-subtitle">{len(sorted_tags)} tags</p>
  </div>
  <div class="search-wrap" style="margin-bottom:1.5rem">
    <input id="tag-filter" class="search-input" type="text"
           placeholder="filter tags…" autocomplete="off">
  </div>
  <ul id="tags-list" class="tags-list">
    {rows}
  </ul>
</main>
<script>{tags_filter_js}</script>
"""
        + html_foot()
    )


def build_threads_listing(threads: list[dict]) -> str:
    """Generate docs/threads.html — all threads."""
    entries_html = ""
    for t in threads:
        kind_label = "explicit" if t["kind"] == "explicit" else "tag cluster"
        entries_html += (
            f'<a class="thread-entry" href="/Research/threads/{t["slug"]}.html">'
            f'<div class="thread-entry-title">{escape(t["title"])}</div>'
            f'<div class="thread-entry-meta">{len(t["items"])} items · {kind_label}</div>'
            f"</a>\n"
        )
    count = len(threads)
    return (
        html_head("Threads — Research")
        + html_nav()
        + f"""\
<main>
  <div class="page-header">
    <h1>Threads</h1>
    <p class="page-subtitle">{count} thread{"s" if count != 1 else ""}</p>
  </div>
  <div class="thread-list">
    {entries_html}
  </div>
</main>
"""
        + html_foot()
    )


def build_thread_page(thread: dict) -> str:
    """Generate docs/threads/<slug>.html — single thread."""
    items = thread["items"]
    cards_html = ""
    for idx, item in enumerate(items):
        cards_html += render_card(item)
        if idx < len(items) - 1:
            cards_html += '<div class="thread-connector">↓</div>\n'

    tag_cluster_html = ""
    if thread["tag_cluster"]:
        pills = "".join(
            f'<a class="tag-pill-link tag" href="/Research/tags/{escape(t)}.html">{escape(t)}</a>'
            for t in thread["tag_cluster"]
        )
        tag_cluster_html = f'<div class="featured-pills" style="margin-bottom:1.5rem">{pills}</div>'

    return (
        html_head(f"{escape(thread['title'])} — Threads — Research")
        + html_nav()
        + f"""\
<main>
  <div class="breadcrumb">
    <a href="/Research/">Research</a>
    <span>/</span>
    <a href="/Research/threads.html">Threads</a>
    <span>/</span>
    <span>{escape(thread["title"])}</span>
  </div>
  <h1 class="item-title">{escape(thread["title"])}</h1>
  <p class="page-subtitle" style="margin-bottom:1.5rem">{len(items)} items</p>
  {tag_cluster_html}
  <div class="card-grid">
    {cards_html}
  </div>
  <a class="back-link" href="/Research/threads.html">← all threads</a>
</main>
"""
        + html_foot()
    )


def build_search_page() -> str:
    """Generate docs/search.html."""
    return (
        html_head("Search — Research")
        + html_nav()
        + f"""\
<main>
  <div class="search-page-header">
    <h1>Search</h1>
  </div>
  <div class="search-wrap">
    <input id="search-input" class="search-input" type="text"
           placeholder="search research items…" autocomplete="off" autofocus>
  </div>
  <div id="results-count" class="search-results-count"></div>
  <div id="search-results" class="card-grid"></div>
</main>
<script>{SEARCH_JS}</script>
"""
        + html_foot()
    )


def build_search_index(
    items: list[dict],
    metadata: dict,
    slug_to_threads: dict[str, list[str]],
) -> str:
    """Generate docs/search-index.json."""
    meta_items = metadata.get("items", {})
    index = []
    for item in items:
        slug = item["slug"]
        item_meta = meta_items.get(slug, {})
        named_concepts = item_meta.get("named_concepts", [])
        all_text_parts = [item["title"]] + list(item["sections"].values()) + named_concepts
        full_text = " ".join(all_text_parts)
        index.append(
            {
                "slug": slug,
                "title": item["display_title"],
                "full_title": item["title"],
                "tags": item["tags"],
                "added": item["added_str"],
                "question_excerpt": item["question_excerpt"],
                "findings_excerpt": get_findings_excerpt(item, 400),
                "full_text": full_text,
                "thread_slugs": slug_to_threads.get(slug, []),
                "url": f"/Research/research/{slug}.html",
            }
        )
    return json.dumps(index, ensure_ascii=False, indent=2)


def build_threads_index_json(threads: list[dict]) -> str:
    """Generate docs/threads-index.json."""
    data = [
        {
            "slug": t["slug"],
            "title": t["title"],
            "kind": t["kind"],
            "tag_cluster": t["tag_cluster"],
            "item_count": len(t["items"]),
            "items": [
                {"slug": item["slug"], "title": item["title"], "added": item["added_str"]}
                for item in t["items"]
            ],
            "url": f"/Research/threads/{t['slug']}.html",
        }
        for t in threads
    ]
    return json.dumps(data, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("Loading research items…")
    items, excl_stats = load_items()
    print(f"  {len(items)} items loaded")
    print(
        f"  {excl_stats['meta_infra'] + excl_stats['date']} items excluded"
        f" (meta/infra: {excl_stats['meta_infra']}, date: {excl_stats['date']})"
    )

    # Singleton tag filtering
    tags_to_drop, n_dropped, n_retained = filter_singleton_tags(items)
    for item in items:
        item["tags"] = [t for t in item["tags"] if t not in tags_to_drop]
    print(f"  {n_dropped} singleton tags dropped, {n_retained} retained (sole tag for item)")

    metadata = load_metadata()

    print("Building relationship graph…")
    links = load_links(items)
    total_edges = sum(len(v) for v in links.values())

    print("Detecting threads…")
    threads = detect_threads(items)
    n_explicit = sum(1 for t in threads if t["kind"] == "explicit")
    n_implicit = len(threads) - n_explicit
    print(f"  {len(threads)} threads detected ({n_explicit} chain, {n_implicit} tag)")

    # Shared-source relationships
    shared = detect_shared_sources(items)
    n_shared = sum(len(v) for v in shared.values())

    # Build slug -> thread slugs mapping
    slug_to_threads: dict[str, list[str]] = {}
    for thread in threads:
        for item in thread["items"]:
            slug_to_threads.setdefault(item["slug"], []).append(thread["slug"])

    # Ensure owned output directories are clean (removes stale pages)
    DOCS_DIR.mkdir(exist_ok=True)
    for owned_dir in (RESEARCH_DIR, TAGS_DIR, THREADS_DIR):
        if owned_dir.exists():
            shutil.rmtree(owned_dir)
        owned_dir.mkdir()

    pages_written = 0

    # 1. index.html (landing)
    print("Building index.html…")
    (DOCS_DIR / "index.html").write_text(build_landing(items, threads), encoding="utf-8")
    pages_written += 1

    # 2. browse.html (filterable grid)
    print("Building browse.html…")
    (DOCS_DIR / "browse.html").write_text(build_browse(items), encoding="utf-8")
    pages_written += 1

    # 3. Individual item pages
    print(f"Building {len(items)} item pages…")
    for i, item in enumerate(items):
        prev_item = items[i - 1] if i > 0 else None
        next_item = items[i + 1] if i < len(items) - 1 else None
        related = links.get(item["slug"], [])
        meta_claims = metadata.get("items", {}).get(item["slug"], {}).get("key_claims", [])
        html = build_item_page(item, prev_item, next_item, related, meta_claims)
        (RESEARCH_DIR / f"{item['slug']}.html").write_text(html, encoding="utf-8")
        pages_written += 1

    # 4. Tag pages
    tags_map: dict[str, list[dict]] = {}
    for item in items:
        for tag in item["tags"]:
            tags_map.setdefault(tag, []).append(item)
    print(f"Building tags index + {len(tags_map)} tag pages…")
    (TAGS_DIR / "index.html").write_text(build_tags_index(tags_map), encoding="utf-8")
    pages_written += 1
    for tag, tag_items in tags_map.items():
        html = build_tag_page(tag, tag_items)
        (TAGS_DIR / f"{tag}.html").write_text(html, encoding="utf-8")
        pages_written += 1

    # 5. Thread pages
    print(f"Building threads.html + {len(threads)} thread pages…")
    (DOCS_DIR / "threads.html").write_text(build_threads_listing(threads), encoding="utf-8")
    pages_written += 1
    for thread in threads:
        html = build_thread_page(thread)
        (THREADS_DIR / f"{thread['slug']}.html").write_text(html, encoding="utf-8")
        pages_written += 1

    # 6. search.html
    print("Building search.html…")
    (DOCS_DIR / "search.html").write_text(build_search_page(), encoding="utf-8")
    pages_written += 1

    # 7. search-index.json
    print("Building search-index.json…")
    (DOCS_DIR / "search-index.json").write_text(
        build_search_index(items, metadata, slug_to_threads), encoding="utf-8"
    )

    # 8. threads-index.json
    print("Building threads-index.json…")
    (DOCS_DIR / "threads-index.json").write_text(
        build_threads_index_json(threads), encoding="utf-8"
    )

    # 9. .nojekyll
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")

    unique_tags = len({t for item in items for t in item["tags"]})
    n_with_claims = sum(
        1 for item in items if metadata.get("items", {}).get(item["slug"], {}).get("key_claims")
    )

    print("\nBuild complete.")
    print(f"  {len(items)} items processed")
    print(
        f"  {excl_stats['meta_infra'] + excl_stats['date']} items excluded"
        f" (meta/infra: {excl_stats['meta_infra']}, date: {excl_stats['date']})"
    )
    print(f"  {pages_written} pages written")
    print(f"  {unique_tags} unique tags (after singleton filtering)")
    print(f"  {n_dropped} singleton tags dropped / {n_retained} retained")
    print(f"  {len(threads)} threads ({n_explicit} chain, {n_implicit} tag)")
    print(f"  {total_edges} edges loaded")
    print(f"  {n_shared} shared-source relationships added")
    print(f"  {n_with_claims} items with key claims")


if __name__ == "__main__":
    main()
