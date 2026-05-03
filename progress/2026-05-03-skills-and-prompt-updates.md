# 2026-05-03 -- Skills submodule update and backlog execution

**Completed:**
- `.github/skills` submodule — advanced to `f8c5471` (adds `backlog-worker`, `inline-citation`, `skill-author`, updated `tdd`/`swe`/`code-review`/`strategy-author`/`research-reviewer`)
- `.github/copilot-instructions.md` — Quick Reference item #10 updated to mention `backlog-worker`; new "Skill Chains" section added before "Agent Skills"; skills table expanded with 8 new entries (`backlog-worker`, `feedback`, `inline-citation`, `peer-reviewer`, `plain-language`, `research-reviewer`, `skill-author`, `technical-writer`) in alphabetical order; `depends_on` vs `blocks` semantics documented
- `research-prompt.md` — added §0.5 Memory Graph Query, §2 Anchor Claim Verification (arXiv), §4.4 Memory Graph Write, and §4.5 Adversarial Challenge blocks covering W-0039, W-0041, W-0042; added §6.5 Extract Gaps and session-start gap registry check for W-0040
- `Research/_template.md` — added `gaps: []` field (W-0040) and `depends_on: []` field (W-0054)
- `src/research/item.py` — `ResearchItem` extended with `depends_on: list[str]` (W-0054)
- `src/research/cli.py` — `cmd_pick` now gates on `depends_on` against `Research/completed/` slugs (W-0054)
- `scripts/aggregate_gaps.py` — new script: reads `gaps:` from completed items, writes `state/gap_registry.json` with count/items/promote (W-0040)
- `scripts/build_site.py` — added `normalize_source_display_name()` utility function (W-0057)
- `scripts/migrate_source_display_names.py` — new idempotent migration script for source display names (W-0057)
- `tests/test_aggregate_gaps.py` — 18 unit tests for gaps aggregation (W-0040)
- `tests/test_research_cli.py` — 4 new tests for `depends_on` picker gating (W-0054)
- `docs-adr/0014-research-item-depends-on-picker-gating.md` — ADR for W-0054 picker behavior change
- `docs-adr/README.md` — indexed ADR-0014
- `BACKLOG.md` — W-0039, W-0040, W-0041, W-0042, W-0054, W-0057 marked done

## Mini-Retro

1. **Did the process work?** Yes — all items were decomposed, implemented, tested, and verified clean in a single session. Delegating complex multi-file work to sub-agents while running tests in parallel was effective.
2. **What slowed down or went wrong?** Nothing significant. The submodule update needed an explicit `--remote` flag to pull latest.
3. **What single change would prevent this next time?** The skill table in copilot-instructions.md falls behind when new skills are added to the submodule. The `sync-skills.yml` workflow could auto-update the table as part of the pointer advance.
4. **Is this a pattern?** The skill table lag is recurring — skills are added to `davidamitchell/Skills` but the instructions here are only updated manually. Candidate for automation.
5. **Does any documentation need updating?** ADR-0014 written for W-0054. All other changes are self-documenting in code.
6. **Do the default instructions need updating?** Quick Reference #10 and the Agent Skills table updated in this session. The `backlog-worker` skill chain is now documented.
