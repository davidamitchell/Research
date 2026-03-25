# 2026-03-25 — fix-gh-pages-styling

## What was done

Overhauled the GitHub Pages static site styling in `scripts/build_site.py`. All 303 HTML pages regenerated and committed. PR #304 raised.

### Changes made

**Colour palette** (from owner-supplied spec image):
- `--surface`: `#141414` → `#0f1115` (SOFT BLACK — card backgrounds)
- `--surface-2`: `#1c1c1c` → `#161b22`
- `--border`: `#2a2a2a` → `#252b33` (subtle card border)
- `--text`: `#e8e8e8` → `#e6e6e6` (OFF-WHITE)
- `--link`: `#E8006F` → `#00C3A5` (KIWIBANK TEAL)
- `--teal`: `#2DD4BF` → `#00C3A5` (KIWIBANK TEAL)
- Added `--dusk: #E8A1A8` for HRs only

**Links:**
- Item content `<a>` tags render in teal with underline
- Sources section now rendered on item pages — `[Title](url)` markdown becomes real clickable links
- Bare URL autolinking now uses source-ref title when the URL matches a known source
- Key claims: replaced `escape(c)` with `_render_claim(c)` which parses inline markdown links so `[Publisher Name](url)` renders as a teal link and stays within the container

**Icons:**
- Refactored from hardcoded `_SVG_ATTRS` strings to `_make_svg(paths, size)` helper
- All icon stroke colour updated: `#2DD4BF` → `#00C3A5`
- Page h1 headers: 20px icons (Browse, Search, Threads, Tags, item title, thread page title)
- Section h2 headers: 12px icons (Research Question → search icon, others → note/tag icon)

**Header size consistency:**
- `item-title`, `tag-page-header h1`, `search-page-header h1` updated from `--text-xl` to `--text-2xl`
- All h1 headers now use `display: inline-flex; align-items: center; gap: 0.4em` for icon layout

**Mobile:**
- Nav stacks vertically on ≤640px: brand row + links row (links wrap)
- `main` padding-top reduced (sticky nav, no fixed offset needed)
- `overflow-x: clip` on body prevents horizontal scroll without breaking sticky
- Tables and `<pre>` blocks: `overflow-x: auto; max-width: 100%`
- `word-break: break-word; overflow-wrap: break-word` on p, li, card text
- Key claims: `overflow: hidden` + `word-break: break-all` on links

**Nav spacing:**
- Icon-to-text gap: `0.35em` → `0.5em`
- Inter-item gap: `1.5rem` → `1.75rem`

## Mini-Retro

1. **Did the process work?** Yes — read the full generator, planned all changes, implemented in one pass, regenerated, committed. No rework needed.

2. **What slowed down or went wrong?** The build_site.py CSS block is a single large string constant (~566 lines). Replacing it required careful old/new matching with the Edit tool. No failures, but it's a fragile pattern.

3. **What single change would prevent this next time?** Extract the CSS into a separate `_styles.css` file that `build_site.py` reads at build time — would make future style-only changes much simpler and avoid the "replace a 566-line string" problem.

4. **Is this a pattern?** First occurrence of a large CSS-in-Python-string edit. Worth adding a backlog item to extract CSS.

## Related

- PR #304: https://github.com/davidamitchell/Research/pull/304
- `scripts/build_site.py` — source of truth for all site HTML/CSS
- `docs/` — auto-generated output (303 pages)
