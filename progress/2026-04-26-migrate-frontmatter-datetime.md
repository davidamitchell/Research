# 2026-04-26 -- Migrate frontmatter dates to full ISO 8601 datetime

**Completed:**
- `src/research/cli.py` — replaced `date.today().isoformat()` with `datetime.now(UTC).isoformat(timespec="seconds")` for `added`, `started`, and `completed` stamps; filename prefix still uses the date component only
- `src/research/item.py` — updated `added` field type to `date | datetime` union; added fallback parsing for ISO 8601 datetime strings returned as raw strings by PyYAML
- `Research/_template.md` — updated placeholder from `YYYY-MM-DD` to `YYYY-MM-DDTHH:MM:SS+00:00`
- `scripts/migrate_datetime.py` — new migration script that uses `git log --follow` to backfill exact git commit timestamps for all existing research items
- `tests/test_research_cli.py` — updated `test_cmd_start_sets_started_date` and `test_cmd_complete_sets_completed_date` to verify ISO datetime regex pattern; added `re` import
- `tests/test_research_item.py` — added `test_from_file_loads_added_datetime` for datetime parsing; updated imports
- 173 research item files in `Research/` migrated with accurate git commit timestamps

## Mini-Retro

1. **Did the process work?** Yes. The approach — query `git log --follow` per file to find the commit where each field was first set — correctly recovered accurate timestamps for all 173 files.

2. **What slowed down or went wrong?** The migration script's `_find_commit_when_field_set` runs a `git show` for every commit of every file, which is O(commits × files). For a repo with deep history this would be slow, but the Research repo is shallow enough that 173 files ran in under 2 minutes.

3. **What single change would prevent this next time?** Nothing to prevent — this is a one-time migration. Going forward, all new items use datetimes from the CLI.

4. **Is this a pattern?** No new recurring pattern. The one code-review note (filename date vs `added` date off by one day for one file) is a pre-existing inconsistency, not introduced by this change.

5. **Does any documentation need updating?** The `Research/completed/README.md` still mentions setting the `completed:` date. Minor — not urgent.

6. **Do the default instructions need updating?** No — the instructions already use `YYYY-MM-DD` as a generic placeholder which is correct for human-written items. The tooling now stamps full datetimes automatically.
