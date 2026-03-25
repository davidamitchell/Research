# 2026-03-24 — add-colour-and-svg-icons

## Task
Implement issue "A letter little bit of colour" — add subtle colour accents and
inline SVG icons to the static research site, inspired by Maggie Appleton's dark-mode site.

## Changes made

All changes are in `scripts/build_site.py` (the site generator). Rebuilt `docs/`
from scratch after each change.

### CSS additions
- Added `--link: #E8006F` (warm pink) — WCAG AA contrast 4.56:1 on `#0d0d0d` background ✓
- Added `--teal: #2DD4BF` (teal accent)
- `.item-content a { color: var(--link) }` — content links are now warm pink
- `.nav-links a.active { color: var(--teal) }` — active nav item is teal
- `.nav-brand` and `.nav-links a` updated to `display: inline-flex; align-items: center; gap` for icon alignment
- `.featured-label` updated to flex for icon alignment

### SVG icons (16×16, stroke-based, teal #2DD4BF, aria-hidden)
Five hardcoded inline SVG constants added:
- `ICON_NOTE` — document with corner fold (used on "Research" nav brand)
- `ICON_THREAD` — chain-link arcs (used on "Threads" nav link + homepage "threads" label)
- `ICON_TAG` — price-tag shape with dot (used on "Tags" nav link + homepage "topics" label)
- `ICON_SEARCH` — magnifying glass (used on "Search" nav link)
- `ICON_GITHUB` — simplified octocat outline (used on "GitHub" nav link)

### Active nav bug fix
- `html_nav()` signature changed from `html_nav()` → `html_nav(active: str = "")`
- Emits `class="active"` on the matching `<a>` element
- All 8 call sites updated: threads/tags/search pages pass their page key;
  landing/browse/item/thread-item pages pass `""` (no active item, correct)

## Verification
- `make check` (ruff) — passes ✓
- `make test` — 190/191 pass; 1 pre-existing failure (`TAVILY_API_KEY` not set, unrelated) ✓
- `python scripts/build_site.py` — 301 pages written ✓
- Browser screenshots confirmed:
  - Homepage: teal icons in nav and section labels, correct layout
  - Threads page: "Threads" nav link highlighted in teal (active state working)
  - Item page: no active nav item (correct)

## Security
No new attack surface. SVG icons are hardcoded constants. All user-supplied data
(titles, tags) continues to pass through the existing `escape()` function.
