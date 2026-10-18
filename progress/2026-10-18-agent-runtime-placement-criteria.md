# 2026-10-18 -- Research complete (agent-runtime-placement-criteria)

**Completed:**
- `Research/completed/2026-10-17-agent-runtime-placement-criteria.md`: researched placement of software-engineering agents across local, vendor-hosted, and organisation-owned runtimes from primary vendor documentation. Output is a placement matrix of proposed decision rules, measurable criteria, and documented gaps (credential lifetime and revocation undocumented for Copilot cloud agent; no published numeric thresholds; scaffolding effect not isolated from model capability).
- `learnings.md`: added evidence to Thread 16.
- Review passed on pass 3 after two remediation commits (em-dashes in template Sources text; bare "AI" in internal link titles).

## Mini-Retro

1. **Did the process work?** Yes. Primary-doc fetching and per-sentence labelling produced a pass on the citation and speculation checks at the first review.
2. **What slowed down or went wrong?** The `.github/skills/` submodule was empty, so rules came from the prompt. Two review passes were spent on slop violations in pre-existing template text (Sources list em-dashes) and bare acronyms in internal link titles.
3. **What single change would prevent this next time?** Run an em-dash and bare-acronym grep over the whole file, including frontmatter-adjacent Sources and Related link titles, before the first draft.
4. **Is this a pattern?** Yes for bare acronyms in internal item-title link text, already in the Known Recurring Failure Patterns table. The em-dash source was template-seeded text written at backlog creation.
5. **Does any documentation need updating?** No further updates beyond `learnings.md`.
6. **Do the default instructions need updating?** Suggest that backlog-item creation avoid em-dashes in seeded Sources annotations; not changed here.
