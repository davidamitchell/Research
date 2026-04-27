#!/usr/bin/env python3
"""Build a static GitHub Pages site from Research/completed/*.md files.

Generates:
  docs/index.html            — landing page with stats, threads, tags, search preview
  docs/browse.html           — filterable research card grid
  docs/all-items.html        — complete list of all completed items (newest first)
  docs/research/<slug>.html  — individual item pages with related items
  docs/tags/<tag>.html       — one page per unique tag
  docs/threads.html          — threads listing
  docs/threads/<slug>.html   — individual thread pages
  docs/search.html           — standalone search page
  docs/research-master.html  — rendered Research_Master.md with valid HTML anchors
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
from datetime import UTC, date, datetime
from pathlib import Path

import yaml
from markdown_it import MarkdownIt

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
COMPLETED_DIR = REPO_ROOT / "Research" / "completed"
RESEARCH_MASTER_MD = REPO_ROOT / "Research" / "Research_Master.md"
DOCS_DIR = REPO_ROOT / "docs"
RESEARCH_DIR = DOCS_DIR / "research"
TAGS_DIR = DOCS_DIR / "tags"
THREADS_DIR = DOCS_DIR / "threads"

GITHUB_BASE = "https://github.com/davidamitchell/Research/blob/main/Research/completed/"
RESEARCH_MASTER_GITHUB_URL = (
    "https://github.com/davidamitchell/Research/blob/main/Research/Research_Master.md"
)

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
  --surface:         #0f1115;
  --surface-2:       #161b22;
  --border:          #252b33;
  --text:            #e6e6e6;
  --text-muted:      #666;
  --accent:          #e6e6e6;
  --accent-dim:      #333;
  --tag-bg:          #161b22;
  --tag-text:        #999;
  --tag-active-bg:   #e6e6e6;
  --tag-active-text: #0f1115;
  --link:            #00C3A5;
  --teal:            #00C3A5;
  --dusk:            #E8A1A8;

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
  overflow-x: clip;
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
  display: inline-flex;
  align-items: center;
  gap: 0.5em;
}
.nav-links {
  display: flex;
  gap: 1.75rem;
}
.nav-links a {
  font-size: var(--text-sm);
  color: var(--text-muted);
  letter-spacing: 0.05em;
  display: inline-flex;
  align-items: center;
  gap: 0.5em;
}
.nav-links a:hover { color: var(--text); text-decoration: none; }
.nav-links a.active { color: var(--teal); }

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
  display: inline-flex;
  align-items: center;
  gap: 0.4em;
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
.search-input:focus { border-color: var(--teal); }
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
  min-width: 0;
}
.card:hover { border-color: var(--teal); text-decoration: none; }
.card-title {
  font-size: var(--text-base);
  font-weight: 500;
  line-height: 1.3;
  letter-spacing: 0.02em;
  word-break: break-word;
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
  word-break: break-word;
  overflow-wrap: break-word;
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
  font-size: var(--text-2xl);
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: 0.02em;
  margin-bottom: 1rem;
  display: flex;
  align-items: flex-start;
  gap: 0.4em;
  word-break: break-word;
  overflow-wrap: break-word;
}
.item-title svg { flex-shrink: 0; margin-top: 0.2em; }

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
  display: flex;
  align-items: center;
  gap: 0.4em;
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
.item-content p { margin-top: 0.8rem; word-break: break-word; overflow-wrap: break-word; }
.item-content ul, .item-content ol {
  margin-top: 0.8rem;
  padding-left: 1.5rem;
}
.item-content li { margin-top: 0.3rem; word-break: break-word; overflow-wrap: break-word; }
.item-content table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  font-size: var(--text-xs);
  display: block;
  overflow-x: auto;
  max-width: 100%;
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
  word-break: break-all;
}
.item-content pre {
  background: var(--surface-2);
  border: 1px solid var(--border);
  padding: 1rem;
  overflow-x: auto;
  margin-top: 1rem;
  max-width: 100%;
}
.item-content pre code { background: none; padding: 0; word-break: normal; }
.item-content blockquote {
  border-left: 2px solid var(--border);
  padding-left: 1rem;
  color: var(--text-muted);
  margin-top: 0.8rem;
}
.item-content a { color: var(--teal); text-decoration: underline; }
.item-content a:hover { color: var(--text); text-decoration: underline; }
.item-content strong { font-weight: 600; }
.item-content em { font-style: italic; }
.item-content hr {
  border: none;
  border-top: 1px solid var(--dusk);
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
  font-size: var(--text-2xl);
  font-weight: 500;
  letter-spacing: 0.02em;
  display: inline-flex;
  align-items: center;
  gap: 0.4em;
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
  font-size: var(--text-2xl);
  font-weight: 500;
  letter-spacing: 0.02em;
  display: inline-flex;
  align-items: center;
  gap: 0.4em;
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
    top: 0;
    height: auto;
    padding: 0.5rem 1rem;
  }
  .nav-inner {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  .nav-links {
    width: 100%;
    gap: 0.75rem;
    flex-wrap: wrap;
  }
  main {
    padding: 1.5rem 1rem 4rem;
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
.key-claims { background: var(--surface-2); border-left: 2px solid var(--border); padding: 1rem 1.25rem; margin-bottom: 2rem; overflow: hidden; }
.key-claims-label { font-size: var(--text-xs); text-transform: lowercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 0.75rem; }
.key-claims ol { list-style: none; padding: 0; margin: 0; }
.key-claims li { font-size: var(--text-sm); line-height: 1.6; padding: 0.3rem 0; border-bottom: 1px solid var(--border); word-break: break-word; overflow-wrap: break-word; }
.key-claims li:last-child { border-bottom: none; }
.key-claims a { color: var(--teal); text-decoration: underline; word-break: break-all; }
.key-claims a:hover { color: var(--text); }

/* Relationship type pill */
.rel-pill { display: inline-block; padding: 0.15rem 0.5rem; background: transparent; border: 1px solid var(--border); color: var(--text-muted); font-size: var(--text-xs); letter-spacing: 0.05em; text-transform: lowercase; font-family: 'IBM Plex Mono', monospace; }

/* Related items */
.related-section { margin-top: 2.5rem; }
.related-group { margin-top: 1rem; }
.related-group-label { font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.05em; text-transform: lowercase; margin-bottom: 0.5rem; }
.related-entry { display: flex; align-items: baseline; gap: 0.6rem; padding: 0.4rem 0; border-bottom: 1px solid var(--border); font-size: var(--text-sm); flex-wrap: wrap; }
.related-entry:last-child { border-bottom: none; }
.related-entry a { color: var(--teal); word-break: break-word; }
.related-note { color: var(--text-muted); font-size: var(--text-xs); }

/* Thread connector */
.thread-connector { text-align: center; font-size: var(--text-xs); color: var(--dusk); letter-spacing: 0.05em; padding: 0.5rem 0; }

/* Thread card variant */
.thread-card-excerpt { font-size: var(--text-xs); color: var(--text-muted); line-height: 1.5; flex: 1; }

/* Featured sections on landing page */
.landing-desc { font-size: var(--text-sm); color: var(--text-muted); margin: 1.5rem 0; line-height: 1.6; }
.featured-section { margin: 2rem 0; }
.featured-label { font-size: var(--text-xs); color: var(--text-muted); letter-spacing: 0.1em; text-transform: lowercase; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.4em; }
.featured-pills { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.thread-pill { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.3rem 0.75rem; background: var(--surface); border: 1px solid var(--border); color: var(--text); font-size: var(--text-xs); letter-spacing: 0.05em; text-decoration: none; }
.thread-pill:hover { border-color: var(--teal); text-decoration: none; }
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
.thread-card-link { text-decoration: none; color: var(--text); display: block; }
.thread-card-link:hover .thread-card { background: var(--surface-2); }
.thread-card { background: var(--surface); border: 1px solid var(--border); padding: 1.5rem 1.75rem 1.75rem; }
.thread-card-title { font-size: var(--text-base); font-weight: 600; margin-bottom: 0.5rem; }
.thread-card-meta { font-size: var(--text-xs); color: var(--text-muted); margin-bottom: 0.75rem; letter-spacing: 0.05em; }
.thread-card-tags { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.75rem; }
.thread-card-excerpt { font-size: var(--text-xs); color: var(--text-muted); line-height: 1.6; }
.thread-card-hr { border: none; border-top: 1px solid var(--dusk); opacity: 0.4; margin: 1rem 0; }
"""

# ---------------------------------------------------------------------------
# SVG icons — stroke-based, teal (#00C3A5), multiple size variants
# ---------------------------------------------------------------------------

# SVG path data for each icon
_ICON_NOTE_PATHS = (
    '<path d="M9 2H4a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V6z"/><path d="M9 2v4h4"/>'
)
_ICON_THREAD_PATHS = (
    '<path d="M6 8a3.5 3.5 0 0 0 5 0l2-2a3.5 3.5 0 0 0-5-5L7 2"/>'
    '<path d="M10 8a3.5 3.5 0 0 0-5 0L3 10a3.5 3.5 0 0 0 5 5l1-1"/>'
)
_ICON_TAG_PATHS = '<path d="M2 2h5.5l6.5 6.5-5.5 5.5L2 7.5V2z"/><circle cx="6" cy="6" r="1"/>'
_ICON_SEARCH_PATHS = '<circle cx="7" cy="7" r="4.5"/><path d="m10.5 10.5 3 3"/>'
_ICON_GITHUB_PATHS = (
    '<path d="M8 1.5C4.41 1.5 1.5 4.41 1.5 8c0 2.87 1.86 5.3 4.44 6.16.32.06.44-.14.44-.31'
    "v-1.09c-1.8.39-2.18-.87-2.18-.87-.3-.75-.72-.95-.72-.95-.59-.4.04-.4.04-.4.65.05 1 .67"
    " 1 .67.58 1 1.53.71 1.9.54.06-.42.23-.71.41-.87-1.44-.16-2.95-.72-2.95-3.2 0-.71.25-1.28"
    ".67-1.74-.07-.16-.29-.82.06-1.71 0 0 .55-.18 1.8.67a6.27 6.27 0 0 1 3.28 0c1.25-.85"
    " 1.8-.67 1.8-.67.35.89.13 1.55.06 1.71.42.46.67 1.03.67 1.74 0 2.49-1.51 3.04-2.96"
    ' 3.2.23.2.44.6.44 1.21v1.8c0 .17.12.37.44.31A6.5 6.5 0 0 0 14.5 8 6.5 6.5 0 0 0 8 1.5z"/>'
)


def _make_svg(paths: str, size: int = 16) -> str:
    """Generate a teal SVG icon at the given pixel size."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 16 16" fill="none" stroke="#00C3A5" stroke-width="1.5" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
        f'style="flex-shrink:0">{paths}</svg>'
    )


# Nav icons (16px)
ICON_NOTE = _make_svg(_ICON_NOTE_PATHS)
ICON_THREAD = _make_svg(_ICON_THREAD_PATHS)
ICON_TAG = _make_svg(_ICON_TAG_PATHS)
ICON_SEARCH = _make_svg(_ICON_SEARCH_PATHS)
ICON_GITHUB = _make_svg(_ICON_GITHUB_PATHS)

# Page h1 icons (20px)
ICON_NOTE_H1 = _make_svg(_ICON_NOTE_PATHS, 20)
ICON_THREAD_H1 = _make_svg(_ICON_THREAD_PATHS, 20)
ICON_TAG_H1 = _make_svg(_ICON_TAG_PATHS, 20)
ICON_SEARCH_H1 = _make_svg(_ICON_SEARCH_PATHS, 20)

# Section h2 icons (12px)
ICON_NOTE_H2 = _make_svg(_ICON_NOTE_PATHS, 12)
ICON_TAG_H2 = _make_svg(_ICON_TAG_PATHS, 12)
ICON_SEARCH_H2 = _make_svg(_ICON_SEARCH_PATHS, 12)

# Section name → icon mapping for h2 headers
_SECTION_ICONS: dict[str, str] = {
    "Research Question": ICON_SEARCH_H2,
    "Findings": ICON_NOTE_H2,
    "Methodology": ICON_NOTE_H2,
    "Technical Architecture": ICON_NOTE_H2,
    "Implementation Logic": ICON_NOTE_H2,
    "Strategic Choice": ICON_NOTE_H2,
    "Decision Log": ICON_NOTE_H2,
    "Schema": ICON_NOTE_H2,
    "Sources": ICON_TAG_H2,
}

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


def html_nav(active: str = "") -> str:
    def _cls(page: str) -> str:
        return ' class="active"' if active == page else ""

    return (
        "<nav>\n"
        '  <div class="nav-inner">\n'
        f'    <a class="nav-brand" href="/Research/">{ICON_NOTE}Research</a>\n'
        '    <div class="nav-links">\n'
        f'      <a href="/Research/threads.html"{_cls("threads")}>{ICON_THREAD}Threads</a>\n'
        f'      <a href="/Research/tags/"{_cls("tags")}>{ICON_TAG}Tags</a>\n'
        f'      <a href="/Research/search.html"{_cls("search")}>{ICON_SEARCH}Search</a>\n'
        '      <a href="https://github.com/davidamitchell/Research"'
        f' target="_blank" rel="noopener">{ICON_GITHUB}GitHub</a>\n'
        "    </div>\n"
        "  </div>\n"
        "</nav>\n"
    )


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

    # Build reverse URL→name map so bare URLs can display their source title
    url_to_name = {url: name for name, url in source_refs.items() if name and url}

    def autolink_bare_urls(html_text: str) -> str:
        url_pattern = re.compile(r"https://[^\s<>\"']+")

        def replace_url(um: re.Match) -> str:
            url = um.group(0).rstrip(".,;)")
            display = escape(url_to_name[url]) if url in url_to_name else get_display_domain(url)
            return f'<a href="{url}">{display}</a>'

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

    Returns (items, exclusion_stats) where exclusion_stats has key
    'meta_infra' with count of excluded files.
    """
    items = []
    excl_meta = 0
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
            continue
        try:
            if isinstance(added_raw, datetime):
                # YAML parsed an ISO 8601 datetime string (e.g. 2026-04-26T06:03:17+00:00)
                added_dt = added_raw if added_raw.tzinfo else added_raw.replace(tzinfo=UTC)
            elif isinstance(added_raw, date):
                # YAML parsed a plain date (legacy format, pre-PR#403)
                added_dt = datetime(added_raw.year, added_raw.month, added_raw.day, tzinfo=UTC)
            elif isinstance(added_raw, str):
                parsed = datetime.fromisoformat(added_raw)
                added_dt = parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
            else:
                continue
        except (ValueError, AttributeError):
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
                "added": added_dt,
                "added_str": added_dt.date().isoformat(),
                "tags": tags,
                "sections": sections,
                "_sources_text": sources_text,
                "question": question,
                "question_excerpt": question[:200].strip(),
                "github_url": GITHUB_BASE + name,
                "thread": str(thread_field).strip() if thread_field else "",
            }
        )
    # Sort newest-first by full datetime; within the same second the filename
    # provides a stable deterministic tiebreaker.
    items.sort(key=lambda x: (x["added"], x["filename"]), reverse=True)
    return items, {"meta_infra": excl_meta}


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


def _cluster_overlap(slugs_a: set[str], slugs_b: set[str]) -> float:
    """Overlap ratio: |A∩B| / min(|A|, |B|).  Returns 0 when either set is empty."""
    if not slugs_a or not slugs_b:
        return 0.0
    return len(slugs_a & slugs_b) / min(len(slugs_a), len(slugs_b))


def detect_threads(items: list[dict], metadata: dict | None = None) -> list[dict]:
    """Group items into threads.

    Priority:
    1. Items with a matching ``thread`` frontmatter field are grouped together.
    2. Items sharing 2+ tags form implicit threads (tag cluster).  Items may
       appear in more than one thread if they genuinely belong to multiple
       distinct clusters.
    3. Items sharing 3+ named concepts (from content_metadata.json) form
       concept threads as a fallback for items not reached by tags alone.

    Returns a list of thread dicts, each with keys:
      slug, title, items, kind ('explicit', 'implicit', or 'concept'),
      tag_cluster (list), concept_cluster (list)
    """
    threads: list[dict] = []

    # ------------------------------------------------------------------
    # 1. Explicit threads via frontmatter ``thread:`` field
    # ------------------------------------------------------------------
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
                "concept_cluster": [],
            }
        )

    # ------------------------------------------------------------------
    # 2. Implicit tag-based threads
    # Generate all candidate clusters (every item as seed, no exclusion),
    # then deduplicate clusters with >= 75% item overlap.
    # This allows items to appear in multiple genuinely different threads.
    # ------------------------------------------------------------------
    candidate_clusters: list[list[dict]] = []
    for item in items:
        if len(item["tags"]) < 2:
            continue
        item_tags = set(item["tags"])
        cluster = [item]
        for other in items:
            if other["slug"] == item["slug"]:
                continue
            if len(item_tags & set(other["tags"])) >= 2:
                cluster.append(other)
        if len(cluster) >= 3:
            candidate_clusters.append(cluster)

    # Largest clusters first; skip any that are 75%+ covered by an already-accepted one
    candidate_clusters.sort(key=lambda c: -len(c))
    accepted_slugsets: list[set[str]] = []
    for cluster in candidate_clusters:
        cluster_slugs = {c["slug"] for c in cluster}
        if any(_cluster_overlap(cluster_slugs, a) >= 0.75 for a in accepted_slugsets):
            continue
        accepted_slugsets.append(cluster_slugs)
        cluster_sorted = sorted(cluster, key=lambda x: x["added"])
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
                "concept_cluster": [],
            }
        )

    # ------------------------------------------------------------------
    # 3. Concept-based threads (secondary pass)
    # ------------------------------------------------------------------
    if metadata:
        threads.extend(detect_concept_threads(items, metadata, threads))

    threads.sort(key=lambda t: -len(t["items"]))
    return threads


def detect_concept_threads(
    items: list[dict],
    metadata: dict,
    existing_threads: list[dict],
) -> list[dict]:
    """Detect threads based on shared named concepts from content_metadata.json.

    Clusters items that share >= 3 named concepts, after filtering out
    high-frequency concepts (appearing in > 25% of items).  Skips clusters
    that are >= 75% covered by an already-accepted thread.
    """
    meta_items = metadata.get("items", {})
    n_items = max(len(items), 1)
    high_freq_threshold = max(3, int(n_items * 0.25))

    # Concepts that are structural/boilerplate artifacts rather than topical signals
    _blocklist: frozenset[str] = frozenset(
        {
            "et al",
            "executive summary",
            "key findings",
            "current corpus",
            "research question",
            "github actions",
        }
    )

    # Collect concept frequency across the corpus
    all_concept_counts: Counter = Counter()
    item_concepts_raw: dict[str, list[str]] = {}
    for item in items:
        slug = item["slug"]
        concepts = [
            c for c in meta_items.get(slug, {}).get("named_concepts", []) if c not in _blocklist
        ]
        item_concepts_raw[slug] = concepts
        all_concept_counts.update(concepts)

    # Retain only concepts appearing rarely enough to be distinctive
    distinctive: set[str] = {
        c for c, cnt in all_concept_counts.items() if cnt <= high_freq_threshold
    }

    # Build filtered concept sets per item
    item_filtered: dict[str, set[str]] = {
        item["slug"]: set(item_concepts_raw[item["slug"]]) & distinctive for item in items
    }

    # Only consider items that have at least 3 distinctive concepts
    candidates = [item for item in items if len(item_filtered[item["slug"]]) >= 3]

    # Generate candidate clusters (seed-based, same logic as tag threads)
    candidate_clusters: list[list[dict]] = []
    for item in candidates:
        seed_concepts = item_filtered[item["slug"]]
        cluster = [item]
        for other in candidates:
            if other["slug"] == item["slug"]:
                continue
            if len(seed_concepts & item_filtered[other["slug"]]) >= 3:
                cluster.append(other)
        if len(cluster) >= 3:
            candidate_clusters.append(cluster)

    # Build slug-sets for existing threads to avoid duplication
    existing_slugsets: list[set[str]] = [
        {it["slug"] for it in t["items"]} for t in existing_threads
    ]

    # Deduplicate: skip if 75%+ overlap with existing thread or already-accepted concept cluster
    candidate_clusters.sort(key=lambda c: -len(c))
    accepted_slugsets: list[set[str]] = []
    accepted_clusters: list[list[dict]] = []
    for cluster in candidate_clusters:
        cluster_slugs = {c["slug"] for c in cluster}
        if any(_cluster_overlap(cluster_slugs, e) >= 0.75 for e in existing_slugsets):
            continue
        if any(_cluster_overlap(cluster_slugs, a) >= 0.75 for a in accepted_slugsets):
            continue
        accepted_clusters.append(cluster)
        accepted_slugsets.append(cluster_slugs)

    # Build thread dicts
    concept_threads: list[dict] = []
    for cluster in accepted_clusters:
        cluster_sorted = sorted(cluster, key=lambda x: x["added"])
        all_concepts_in_cluster: list[str] = []
        for c in cluster:
            all_concepts_in_cluster.extend(item_filtered[c["slug"]])
        top_concepts = [c for c, _ in Counter(all_concepts_in_cluster).most_common(3)]
        thread_title = " / ".join(top_concepts)
        concept_threads.append(
            {
                "slug": slugify(thread_title),
                "title": thread_title,
                "items": cluster_sorted,
                "kind": "concept",
                "tag_cluster": [],
                "concept_cluster": top_concepts,
            }
        )

    return concept_threads


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
      .then(function(data) { index = data; runPreview(); })
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
    resultsEl.style.display = 'block';
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
    <h1>{ICON_NOTE_H1}Research</h1>
    <p class="page-subtitle">notes, findings, and threads</p>
  </div>
  {stats_html}
  <div class="search-preview-wrap">
    <input id="landing-search" class="search-input" type="text"
           placeholder="search research items…" autocomplete="off">
    <div id="landing-search-results" class="search-preview-results"></div>
  </div>
  <div class="featured-section">
    <div class="featured-label">{ICON_THREAD}threads</div>
    <div class="featured-pills">{thread_pills}</div>
  </div>
  <div class="featured-section">
    <div class="featured-label">{ICON_TAG}topics</div>
    <div class="featured-pills">{tag_pills}</div>
  </div>
  <div class="featured-section" style="margin-top:2.5rem;border-top:1px solid var(--border);padding-top:2rem">
    <div class="featured-label">{ICON_NOTE}more</div>
    <div class="featured-pills">
      <a class="thread-pill" href="/Research/all-items.html">{ICON_NOTE}All Items
        <span class="thread-pill-count">{count}</span></a>
      <a class="thread-pill" href="/Research/research-master.html">{ICON_NOTE}Research Master</a>
    </div>
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
    <h1>{ICON_NOTE_H1}Browse</h1>
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


def build_all_items_page(items: list[dict]) -> str:
    """Generate docs/all-items.html — complete list of all items.

    Args:
        items: Research items already sorted newest-first (as returned by load_items).
               This function does not perform any sorting.
    """
    cards_html = "".join(render_card(item) for item in items)
    count = len(items)

    return (
        html_head("All Items — Research")
        + html_nav()
        + f"""\
<main>
  <div class="page-header">
    <h1>{ICON_NOTE_H1}All Items</h1>
    <p class="page-subtitle">{count} completed research items, newest first</p>
  </div>
  <div class="search-wrap">
    <input id="search-input" class="search-input" type="text"
           placeholder="search by title or question…" autocomplete="off">
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


def build_research_master_page() -> str:
    """Generate docs/research-master.html from Research/Research_Master.md.

    Reads RESEARCH_MASTER_MD from the filesystem and renders it as HTML.
    The Table of Contents section is stripped before rendering to reduce page
    size and DOM element count.  Deprecated ``<a name="...">`` anchors are
    converted to the HTML5 ``<a id="...">`` form.  No JavaScript is emitted.
    """
    md_text = RESEARCH_MASTER_MD.read_text(encoding="utf-8")

    # Strip the TOC section (## Table of Contents ... --- separator) to reduce
    # page size and DOM element count.
    md_text = re.sub(
        r"## Table of Contents\n\n(?:\* [^\n]+\n)+\n---\n\n",
        "",
        md_text,
    )

    # Convert deprecated <a name="..."> anchors to HTML5 <a id="..."> form.
    md_text = md_text.replace('<a name="', '<a id="')

    md = MarkdownIt().enable("table").enable("strikethrough")
    body_html = md.render(md_text)
    return (
        html_head(
            "Research Master — Research",
            extra_head=(
                "<style>"
                ".research-master-content { max-width: 860px; }"
                ".research-master-content h2 { font-size: var(--text-xl); font-weight: 500;"
                " margin-top: 2.5rem; margin-bottom: 0.75rem; padding-top: 0.5rem; }"
                ".research-master-content h3 { font-size: var(--text-lg); font-weight: 500;"
                " margin-top: 1.5rem; margin-bottom: 0.5rem; }"
                ".research-master-content ul { list-style: disc; padding-left: 1.5rem;"
                " margin-top: 0.5rem; }"
                ".research-master-content ul li { margin-bottom: 0.2rem;"
                " font-size: var(--text-sm); }"
                ".research-master-content a { color: var(--teal); text-decoration: underline; }"
                ".research-master-content a:hover { color: var(--text); }"
                ".research-master-content p { margin-top: 0.75rem; font-size: var(--text-sm); }"
                ".research-master-content hr { border: none; border-top: 1px solid var(--border);"
                " margin: 2rem 0; }"
                ".research-master-content table { border-collapse: collapse; width: 100%;"
                " margin-top: 1rem; font-size: var(--text-xs); }"
                ".research-master-content th, .research-master-content td"
                " { border: 1px solid var(--border); padding: 0.4rem 0.6rem;"
                " text-align: left; }"
                ".research-master-content strong { font-weight: 600; }"
                ".research-master-content code { background: var(--surface-2);"
                " padding: 0.1em 0.3em; font-family: 'IBM Plex Mono', monospace;"
                " font-size: 0.9em; }"
                "</style>"
            ),
        )
        + html_nav()
        + f"""\
<main>
  <div class="page-header">
    <h1>{ICON_NOTE_H1}Research Master</h1>
    <p class="page-subtitle">complete research index with findings —
      <a href="{RESEARCH_MASTER_GITHUB_URL}" target="_blank" rel="noopener"
         style="color:var(--teal);text-decoration:underline">view source on GitHub →</a>
    </p>
  </div>
  <div class="research-master-content item-content">
    {body_html}
  </div>
</main>
"""
        + html_foot()
    )


def _render_claim(text: str) -> str:
    """Render a single claim string, converting markdown links to <a> tags."""

    # Convert [title](url) markdown links to anchor tags without a full md parse
    def _link_repl(m: re.Match) -> str:
        title = m.group(1)
        url = m.group(2)
        return f'<a href="{url.replace(chr(34), "&quot;")}">{escape(title)}</a>'

    # First escape HTML entities in the plain text portions, then apply links
    # We do this by splitting on link patterns, escaping non-link parts
    parts = []
    last = 0
    for m in re.finditer(r"\[([^\]]+)\]\((https?://(?:[^()]+|\([^()]*\))*)\)", text):
        parts.append(escape(text[last : m.start()]))
        parts.append(_link_repl(m))
        last = m.end()
    parts.append(escape(text[last:]))
    return "".join(parts)


def _render_key_claims(meta_claims: list[str]) -> str:
    """Render key claims block from pre-extracted, clean claim sentences."""
    if not meta_claims:
        return ""
    items_html = "".join(f"<li>{_render_claim(c)}</li>\n" for c in meta_claims)
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
    md = MarkdownIt().enable("table").enable("strikethrough")

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
        rendered = md.render(content)
        rendered = autolink_html(rendered, source_refs)
        rendered = _STRAY_CLOSE_TAGS_RE.sub("", rendered)
        icon = _SECTION_ICONS.get(section_name, ICON_NOTE_H2)
        sections_html += f"<h2>{icon}{escape(section_name)}</h2>\n{rendered}\n"

    # Render Sources section so links appear as proper <a> tags on the page
    sources_text = item.get("_sources_text", "")
    if sources_text:
        rendered_sources = md.render(sources_text)
        rendered_sources = autolink_html(rendered_sources, source_refs)
        rendered_sources = _STRAY_CLOSE_TAGS_RE.sub("", rendered_sources)
        sections_html += f"<h2>{ICON_TAG_H2}sources</h2>\n{rendered_sources}\n"

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
  <h1 class="item-title">{ICON_NOTE_H1}{escape(display_title)}</h1>
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
        + html_nav("tags")
        + f"""\
<main>
  <div class="tag-page-header">
    <h1>{ICON_TAG_H1}Tagged: {escape(tag)}</h1>
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
        + html_nav("tags")
        + f"""\
<main>
  <div class="tag-page-header">
    <h1>{ICON_TAG_H1}Tags</h1>
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


def _thread_date_range(items: list[dict]) -> str:
    """Return 'YYYY-MM-DD → YYYY-MM-DD' or single date if all the same."""
    dates = sorted(item["added"] for item in items)
    first = dates[0].date().isoformat()
    last = dates[-1].date().isoformat()
    if first == last:
        return first
    return f"{first} → {last}"


def build_threads_listing(threads: list[dict]) -> str:
    """Generate docs/threads.html — all threads."""
    entries_html = ""
    for idx, t in enumerate(threads):
        n = len(t["items"])
        date_range = _thread_date_range(t["items"])
        meta = f"{n} item{'s' if n != 1 else ''} · {date_range}"
        cluster_labels = t["tag_cluster"] or t.get("concept_cluster", [])
        tag_pills = "".join(f'<span class="tag">{escape(label)}</span>' for label in cluster_labels)
        excerpt = t["items"][0]["question_excerpt"]
        if len(t["items"][0]["question"]) > 200:
            excerpt = excerpt.rstrip() + "…"
        entries_html += (
            f'<a class="thread-card-link" href="/Research/threads/{t["slug"]}.html">'
            f'<div class="thread-card">'
            f'<div class="thread-card-title">{escape(t["title"])}</div>'
            f'<div class="thread-card-meta">{escape(meta)}</div>'
            + (f'<div class="thread-card-tags">{tag_pills}</div>' if tag_pills else "")
            + (f'<div class="thread-card-excerpt">{escape(excerpt)}</div>' if excerpt else "")
            + "</div></a>\n"
        )
        if idx < len(threads) - 1:
            entries_html += '<hr class="thread-card-hr">\n'
    count = len(threads)
    return (
        html_head("Threads — Research")
        + html_nav("threads")
        + f"""\
<main>
  <div class="page-header">
    <h1>{ICON_THREAD_H1}Threads</h1>
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
    elif thread.get("concept_cluster"):
        pills = "".join(f'<span class="tag">{escape(c)}</span>' for c in thread["concept_cluster"])
        tag_cluster_html = f'<div class="featured-pills" style="margin-bottom:1.5rem">{pills}</div>'

    return (
        html_head(f"{escape(thread['title'])} — Threads — Research")
        + html_nav("threads")
        + f"""\
<main>
  <div class="breadcrumb">
    <a href="/Research/">Research</a>
    <span>/</span>
    <a href="/Research/threads.html">Threads</a>
    <span>/</span>
    <span>{escape(thread["title"])}</span>
  </div>
  <h1 class="item-title">{ICON_THREAD_H1}{escape(thread["title"])}</h1>
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
        + html_nav("search")
        + f"""\
<main>
  <div class="search-page-header">
    <h1>{ICON_SEARCH_H1}Search</h1>
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
            "concept_cluster": t.get("concept_cluster", []),
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
    print(f"  {excl_stats['meta_infra']} items excluded (meta/infra)")

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
    threads = detect_threads(items, metadata)
    n_explicit = sum(1 for t in threads if t["kind"] == "explicit")
    n_implicit = sum(1 for t in threads if t["kind"] == "implicit")
    n_concept = sum(1 for t in threads if t["kind"] == "concept")
    print(
        f"  {len(threads)} threads detected "
        f"({n_explicit} explicit, {n_implicit} tag, {n_concept} concept)"
    )

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

    # 3. all-items.html (complete list, newest first)
    print("Building all-items.html…")
    (DOCS_DIR / "all-items.html").write_text(build_all_items_page(items), encoding="utf-8")
    pages_written += 1

    # 4. research-master.html
    print("Building research-master.html…")
    (DOCS_DIR / "research-master.html").write_text(build_research_master_page(), encoding="utf-8")
    pages_written += 1

    # 5. Individual item pages
    print(f"Building {len(items)} item pages…")
    for i, item in enumerate(items):
        prev_item = items[i - 1] if i > 0 else None
        next_item = items[i + 1] if i < len(items) - 1 else None
        related = links.get(item["slug"], [])
        meta_claims = metadata.get("items", {}).get(item["slug"], {}).get("key_claims", [])
        html = build_item_page(item, prev_item, next_item, related, meta_claims)
        (RESEARCH_DIR / f"{item['slug']}.html").write_text(html, encoding="utf-8")
        pages_written += 1

    # 6. Tag pages
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

    # 7. Thread pages
    print(f"Building threads.html + {len(threads)} thread pages…")
    (DOCS_DIR / "threads.html").write_text(build_threads_listing(threads), encoding="utf-8")
    pages_written += 1
    for thread in threads:
        html = build_thread_page(thread)
        (THREADS_DIR / f"{thread['slug']}.html").write_text(html, encoding="utf-8")
        pages_written += 1

    # 8. search.html
    print("Building search.html…")
    (DOCS_DIR / "search.html").write_text(build_search_page(), encoding="utf-8")
    pages_written += 1

    # 9. search-index.json
    print("Building search-index.json…")
    (DOCS_DIR / "search-index.json").write_text(
        build_search_index(items, metadata, slug_to_threads), encoding="utf-8"
    )

    # 10. threads-index.json
    print("Building threads-index.json…")
    (DOCS_DIR / "threads-index.json").write_text(
        build_threads_index_json(threads), encoding="utf-8"
    )

    # 11. .nojekyll
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")

    unique_tags = len({t for item in items for t in item["tags"]})
    n_with_claims = sum(
        1 for item in items if metadata.get("items", {}).get(item["slug"], {}).get("key_claims")
    )

    print("\nBuild complete.")
    print(f"  {len(items)} items processed")
    print(f"  {excl_stats['meta_infra']} items excluded (meta/infra)")
    print(f"  {pages_written} pages written")
    print(f"  {unique_tags} unique tags (after singleton filtering)")
    print(f"  {n_dropped} singleton tags dropped / {n_retained} retained")
    print(
        f"  {len(threads)} threads ({n_explicit} explicit, {n_implicit} tag, {n_concept} concept)"
    )
    print(f"  {total_edges} edges loaded")
    print(f"  {n_shared} shared-source relationships added")
    print(f"  {n_with_claims} items with key claims")


if __name__ == "__main__":
    main()
