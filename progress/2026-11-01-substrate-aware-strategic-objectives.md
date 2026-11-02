# 2026-11-01 -- Add backlog item (substrate-aware-strategic-objectives)

**Completed:**
- Added [the research backlog item](../Research/backlog/2026-11-01-substrate-aware-strategic-objectives.md) from [issue #686](https://github.com/davidamitchell/Research/issues/686), asking whether enterprise objectives must account for delivery constraints and which criteria support feasible autonomy and coordination without technical or capability debt.
- Applied the research-question skill: all five quality tests pass; readiness is READY. Preserved counterexamples, enterprise-level scope, capacity models, and the distinction between fixed commitments and funded substrate change.
- Retained each supplied bibliographic seed as an unconsulted lead and linked six existing local research items. Left research output and findings as template placeholders.
- Used available GitHub, filesystem, and fetch equivalents; dedicated research servers are not exposed. Initialised the read-only skills submodule without changing its pointer or contents.

**Validation:**
- Parsed the item with the existing research-item loader; checked canonical themes, all six local references, source URLs, unique headings, and unchanged research-output and findings placeholders.
- Focused research-item tests: 16 passed. Full suite: 620 passed, 2 skipped, 1 failed because this sandbox has no `TAVILY_API_KEY`.
- Installed the declared development dependencies. `make check`: lint passed; Ruff 0.17.3 flagged formatting in four untouched completed research files. No unrelated files were changed.
- Inspected [the current Continuous Integration (CI) run](https://github.com/davidamitchell/Research/actions/runs/41299421045): `action_required`, with zero jobs and no failed-job logs. CI supplies the Tavily secret, but no clean run is available to confirm here.
- Applied remove-ai-slop to the authored prose while preserving the required template. No code, generated site, or dependency configuration changes.

## Related

- [Satisfiable internal platforms](../Research/completed/2026-10-01-thinnest-viable-internal-platform-standard.md)
- [Dependency properties and coordination mechanisms](../Research/completed/2026-10-23-dependency-properties-coordination-mechanisms.md)
- [Strategic intent to scoped delivery objectives](../Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md)

## Mini-Retro

1. **Did the process work?** Yes. Question formulation produced a bounded backlog item without conducting research.
2. **What slowed down or went wrong?** The skills submodule and development dependencies needed installation; the shell lacked ripgrep, so the available search tool replaced it. A metadata memory described an outdated fallback. Full validation is blocked by a missing sandbox credential, unrelated formatting failures, and CI awaiting approval.
3. **What single change would prevent this next time?** Check the live template and vocabulary before assigning metadata; corrected the stored fallback note against the cited files.
4. **Is this a pattern?** No new recurring failure pattern was established in this session.
5. **Does any documentation need updating?** The backlog item and this log capture the scope and handoff; no architecture or user-interface change requires further documentation.
6. **Do the default instructions need updating?** No new convention emerged. The live template already specifies the current metadata field.
