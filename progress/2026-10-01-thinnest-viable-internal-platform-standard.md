# 2026-10-01 — Add backlog item (thinnest-viable-internal-platform-standard)

**Completed:**
- `Research/backlog/2026-10-01-thinnest-viable-internal-platform-standard.md` — added from issue #665; formulates a ready-to-investigate question about the thinnest viable internal platform and a practical product-management standard for platform teams.

The candidate passed the research-question skill's Specific, Answerable, Scoped, Motivated, and Decomposable tests. The expected output is knowledge. Research itself was not conducted.

**Validation:**
- 28 targeted research-item and theme tests passed.
- Full suite: 620 passed, 2 skipped, 1 failed because `TAVILY_API_KEY` is unavailable in this sandbox.
- `make check`: lint passed; format check found four pre-existing violations in unrelated completed research items.
- Manual checks confirmed item metadata, URL-linked sources, internal links, empty research placeholders, and the six-part Mini-Retro.

## Mini-Retro

1. **Did the process work?** Yes. Applying the research-question skill resulted in clear scope boundaries and a decomposed path from first-principles criteria to an assessable standard.
2. **What slowed down or went wrong?** The skills submodule was initially unpopulated. Repository-wide validation also found four formatting violations in unrelated completed items and a missing `TAVILY_API_KEY` for one integration test.
3. **What single change would prevent this next time?** Initialize the skills submodule before intake work; address the unrelated formatting baseline and configure the integration-test secret through their own maintenance tasks.
4. **Is this a pattern?** The submodule setup is already documented; the validation blockers predate and are outside this intake change.
5. **Does any documentation need updating?** No. This intake adds a backlog item, not research findings or a change to repository behavior.
6. **Do the default instructions need updating?** No new convention or constraint emerged.

## Related

- [First-principles taxonomy of modern technology platforms](https://davidamitchell.github.io/Research/research/2026-09-14-modern-technology-platform-taxonomy.html)
- [Platform engineering, InnerSource, and standard-core plus local-extension operating models](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [Local optimisation of team- and role-level tooling in knowledge work](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
