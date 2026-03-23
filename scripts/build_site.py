#!/usr/bin/env python3
"""Build a static GitHub Pages site from Research/completed/*.md files.

Generates:
  docs/index.html            — filterable research card grid
  docs/research/<slug>.html  — individual item pages
  docs/tags/<tag>.html       — one page per unique tag
  docs/search.html           — standalone search page
  docs/search-index.json     — search index for client-side JS

Usage:
  python scripts/build_site.py

Requires: mistune, PyYAML
"""

from __future__ import annotations

import json
import re
import textwrap
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
  text-transform: uppercase;
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
@media (max-width: 600px) {
  main { padding: 72px 1rem 3rem; }
  nav { padding: 0 1rem; }
}
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
              <a href="/Research/tags/">Tags</a>
              <a href="/Research/search.html">Search</a>
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
# Data loading
# ---------------------------------------------------------------------------


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


def load_items() -> list[dict]:
    """Load and filter all completed research items."""
    items = []
    for path in sorted(COMPLETED_DIR.glob("*.md"), reverse=True):
        name = path.name
        # Skip README and non-research files
        if name.lower() == "readme.md":
            continue
        # Exclusion: meta or infra in filename (case-insensitive)
        if re.search(r"meta|infra", name, re.IGNORECASE):
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        # Exclusion: missing or pre-cutoff added date
        added_raw = meta.get("added")
        if not added_raw:
            continue
        try:
            if isinstance(added_raw, str):
                added = date.fromisoformat(added_raw)
            else:
                added = date(added_raw.year, added_raw.month, added_raw.day)
        except (ValueError, AttributeError):
            continue
        if added < CUTOFF_DATE:
            continue
        title = str(meta.get("title", path.stem))
        tags = normalise_tags(meta.get("tags", []))
        slug = slugify(path.stem)
        sections = extract_sections(body)
        question = sections.get("Research Question", "")
        items.append(
            {
                "slug": slug,
                "filename": name,
                "title": title,
                "added": added,
                "added_str": added.isoformat(),
                "tags": tags,
                "sections": sections,
                "question": question,
                "question_excerpt": question[:200].strip(),
                "github_url": GITHUB_BASE + name,
            }
        )
    # Sort newest-first
    items.sort(key=lambda x: x["added"], reverse=True)
    return items


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
        f' data-title="{escape(item["title"].lower())}"'
        f' data-question="{escape(item["question_excerpt"].lower())}"'
        f' data-tags="{escape(",".join(item["tags"]))}">\n'
        f'  <div class="card-title">{escape(item["title"])}</div>\n'
        f'  <div class="card-meta">{item["added_str"]}</div>\n'
        f'  <div class="card-tags">{tags_html}</div>\n'
        f'  <div class="card-excerpt">{escape(excerpt)}</div>\n'
        f"</a>\n"
    )


# ---------------------------------------------------------------------------
# Index JS (filter + search + URL params)
# ---------------------------------------------------------------------------

INDEX_JS = """
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
    if (noResults) noResults.style.display = anyVisible ? 'none' : '';
    if (clearBtn) clearBtn.style.display = activeTags.size > 0 ? '' : 'none';
    tagBtns.forEach(function(btn) {
      btn.classList.toggle('active', activeTags.has(btn.dataset.tag));
    });
    setParams();
  }

  // Restore state from URL
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

# ---------------------------------------------------------------------------
# Search page JS
# ---------------------------------------------------------------------------

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
      + '<div class="card-excerpt">' + escapeHtml(item.question_excerpt) + '</div>'
      + '</a>';
  }

  function runSearch() {
    if (!index) return;
    var q = input.value.trim().toLowerCase();
    var results = !q ? [] : index.filter(function(item) {
      return item.title.toLowerCase().indexOf(q) !== -1
          || item.question_excerpt.toLowerCase().indexOf(q) !== -1
          || item.tags.join(' ').indexOf(q) !== -1;
    });
    resultsEl.innerHTML = results.map(renderCard).join('');
    if (countEl) {
      countEl.textContent = q
        ? results.length + ' result' + (results.length === 1 ? '' : 's')
        : '';
    }
    // Restore URL param
    var params = new URLSearchParams();
    if (q) params.set('q', q);
    var str = params.toString();
    history.replaceState(null, '', window.location.pathname + (str ? '?' + str : ''));
  }

  // Restore from URL
  var params = new URLSearchParams(window.location.search);
  var initQ = params.get('q') || '';
  input.value = initQ;

  input.addEventListener('input', runSearch);
  fetchIndex();
})();
"""

# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------


def build_index(items: list[dict]) -> str:
    """Generate docs/index.html."""
    # Collect all tags sorted alphabetically
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
        html_head("Research")
        + html_nav()
        + f"""\
<main>
  <div class="page-header">
    <h1>Research</h1>
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
<script>{INDEX_JS}</script>
"""
        + html_foot()
    )


def build_item_page(item: dict, prev_item: dict | None, next_item: dict | None) -> str:
    """Generate docs/research/<slug>.html."""
    md = mistune.create_markdown(plugins=["table", "strikethrough"])

    tags_html = "".join(
        f'<a class="tag" href="/Research/tags/{escape(t)}.html">{escape(t)}</a> '
        for t in item["tags"]
    )

    sections_html = ""
    for section_name in SECTIONS_ORDERED:
        content = item["sections"].get(section_name, "")
        if not content:
            continue
        rendered = md(content)
        sections_html += f"<h2>{escape(section_name)}</h2>\n{rendered}\n"

    # Prev / Next
    prev_html = ""
    next_html = ""
    if prev_item:
        prev_html = (
            f'<div class="item-nav-prev">'
            f'<span class="item-nav-label">← newer</span>'
            f'<a href="/Research/research/{prev_item["slug"]}.html">{escape(prev_item["title"])}</a>'
            f"</div>"
        )
    if next_item:
        next_html = (
            f'<div class="item-nav-next">'
            f'<span class="item-nav-label">older →</span>'
            f'<a href="/Research/research/{next_item["slug"]}.html">{escape(next_item["title"])}</a>'
            f"</div>"
        )

    return (
        html_head(f"{escape(item['title'])} — Research")
        + html_nav()
        + f"""\
<main>
  <div class="breadcrumb">
    <a href="/Research/">Research</a>
    <span>/</span>
    <span>{escape(item["title"])}</span>
  </div>
  <h1 class="item-title">{escape(item["title"])}</h1>
  <div class="meta-bar">
    <span>{item["added_str"]}</span>
    <span class="meta-sep">·</span>
    {tags_html}
    <span class="meta-sep">·</span>
    <a class="source-link" href="{item["github_url"]}" target="_blank" rel="noopener">source →</a>
  </div>
  <div class="item-content">
    {sections_html}
  </div>
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
    <a class="back-link" href="/Research/">← all research</a>
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
        f'<li><a class="tag" href="/Research/tags/{escape(t)}.html">{escape(t)}</a>'
        f' <span class="tag-count">({len(tags_map[t])})</span></li>\n'
        for t in sorted_tags
    )
    return (
        html_head("Tags — Research")
        + html_nav()
        + f"""\
<main>
  <div class="tag-page-header">
    <h1>Tags</h1>
    <p class="page-subtitle">{len(sorted_tags)} tags</p>
    <a class="back-link" href="/Research/">← all research</a>
  </div>
  <ul class="tags-list">
    {rows}
  </ul>
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


def build_search_index(items: list[dict]) -> str:
    """Generate docs/search-index.json."""
    index = [
        {
            "slug": item["slug"],
            "title": item["title"],
            "tags": item["tags"],
            "added": item["added_str"],
            "question_excerpt": item["question_excerpt"],
            "url": f"/Research/research/{item['slug']}.html",
        }
        for item in items
    ]
    return json.dumps(index, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("Loading research items…")
    items = load_items()
    print(f"  {len(items)} items loaded")

    # Create output directories
    DOCS_DIR.mkdir(exist_ok=True)
    RESEARCH_DIR.mkdir(exist_ok=True)
    TAGS_DIR.mkdir(exist_ok=True)

    # 1. index.html
    print("Building index.html…")
    (DOCS_DIR / "index.html").write_text(build_index(items), encoding="utf-8")

    # 2. Individual item pages
    print(f"Building {len(items)} item pages…")
    for i, item in enumerate(items):
        prev_item = items[i - 1] if i > 0 else None
        next_item = items[i + 1] if i < len(items) - 1 else None
        html = build_item_page(item, prev_item, next_item)
        (RESEARCH_DIR / f"{item['slug']}.html").write_text(html, encoding="utf-8")

    # 3. Tag pages
    tags_map: dict[str, list[dict]] = {}
    for item in items:
        for tag in item["tags"]:
            tags_map.setdefault(tag, []).append(item)
    print(f"Building tags index + {len(tags_map)} tag pages…")
    (TAGS_DIR / "index.html").write_text(build_tags_index(tags_map), encoding="utf-8")
    for tag, tag_items in tags_map.items():
        html = build_tag_page(tag, tag_items)
        (TAGS_DIR / f"{tag}.html").write_text(html, encoding="utf-8")

    # 4. search.html
    print("Building search.html…")
    (DOCS_DIR / "search.html").write_text(build_search_page(), encoding="utf-8")

    # 5. search-index.json
    print("Building search-index.json…")
    (DOCS_DIR / "search-index.json").write_text(build_search_index(items), encoding="utf-8")

    # 6. .nojekyll (prevents GitHub Pages from running Jekyll)
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print("Done.")


if __name__ == "__main__":
    main()
