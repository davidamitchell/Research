# 2026-04-27 — W-0050: Research backlog page

## What was done

- Added `docs/backlog.html` to the static site. Lists all items in `Research/backlog/` as non-linkable cards showing title, date, priority badge, tags, and research question excerpt.
- Added `load_backlog_items()` to `scripts/build_site.py` — reads `Research/backlog/*.md`, parses frontmatter and `## Research Question` section, sorts newest-first.
- Added `render_backlog_card()` — outputs `<div class="card">` (non-linkable; no individual backlog item pages exist) with a colour-coded priority badge.
- Added `build_backlog_page()` — matches `build_all_items_page` structure.
- Added `"Backlog"` nav link to `html_nav()` using key `"backlog"`, positioned after "All Items".
- Added `BACKLOG_DIR` constant to `scripts/build_site.py`.
- Updated module docstring in `scripts/build_site.py` to list `docs/backlog.html`.
- Updated `.github/workflows/build_site.yml` push trigger to include `Research/backlog/**` so the page regenerates when backlog items change.
- Marked W-0050 done in `BACKLOG.md`.

## Verification steps

```bash
python scripts/build_site.py
# Should print: Building backlog.html…
# docs/backlog.html should exist and be valid HTML
```

## Mini-retro

1. **Did the process work?** Yes. The existing page/card patterns made implementation straightforward — `render_card` and `build_all_items_page` provided a clear template.
2. **What slowed down or went wrong?** Nothing significant. The step numbering in `main()` had a duplicate that was fixed as part of the update.
3. **What single change would prevent this next time?** No change needed.
4. **Is this a pattern?** No.
5. **Does any documentation need updating?** Module docstring updated as part of this change.
6. **Do the default instructions need updating?** No.
