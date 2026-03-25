# 2026-03-25 — threads-overhaul

## What was done

Overhauled the threads listing page and thread detection logic in `scripts/build_site.py`. 309 pages regenerated.

### Changes made

**Thread detection (`detect_threads`)**:
- Lowered implicit cluster threshold: items sharing **2+ tags** (was 3+) now group together
- Result: 16 threads (was 10), covering 62 items (was 38), 54 fewer orphans

**New threads surfaced**:
- `interface / delivery / output` — 5 items on surfacing research outputs
- `team-size / ai / coordination-overhead` — 4 items on small-team AI amplification
- `agents / skills / orchestration` — 3 items on agent skill frameworks
- `architecture / agents / governance` — 3 items
- `evaluation / agents / research-loop` — 3 items
- `delivery / interface / slack` — 3 items

**Thread cards (threads listing page)**:
- Each thread is now a full card (`<a class="thread-card-link">`) with soft-black background, teal-hover
- Shows: title (bold), item count + date range (`YYYY-MM-DD → YYYY-MM-DD`), tag cluster pills, first-item question excerpt
- Cards separated by DUSK (`#E8A1A8`) HR rules (`<hr class="thread-card-hr">`)

**New CSS**:
- `.thread-card-link`, `.thread-card`, `.thread-card-title`, `.thread-card-meta`, `.thread-card-tags`, `.thread-card-excerpt`, `.thread-card-hr`
- Replaced the old merged-border `.thread-entry` list

**New helper**: `_thread_date_range(items)` — returns ISO date range string for display

## Mini-Retro

1. **Did the process work?** Yes — analysed tag distribution with a quick Python script, found the 3-tag threshold was excluding 89/127 items, lowered to 2 and got a much healthier 16-thread corpus.

2. **What slowed down or went wrong?** Nothing. The data exploration step (running the detection simulation locally before touching the code) made the right threshold obvious.

3. **What single change would prevent this next time?** The thread-title naming is still purely mechanical (top-3 tag names joined with ` / `). A future improvement: allow an optional `thread_title` override field in frontmatter, or derive a better human-readable title from the cluster.

4. **Is this a pattern?** First threads-page overhaul. The detection logic is still greedy first-match — a proper clustering algorithm (e.g. single-linkage) would be more principled for overlapping themes.

## Related

- Branch: `claude/fix-gh-pages-styling-1gT5R`
- `scripts/build_site.py` — `detect_threads`, `build_threads_listing`, CSS
- `docs/threads/` — 16 thread pages (6 new, several renamed due to slug changes)
