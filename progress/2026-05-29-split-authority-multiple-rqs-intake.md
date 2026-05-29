# 2026-05-29 -- Break split-authority issue into multiple interdependent research questions

**Completed:**
- Added 7 backlog items in `Research/backlog/` from the issue prompt: 6 supporting questions (Q1-Q6) plus 1 synthesis question (P1).
- Encoded the dependency graph directly in each item's `blocks` field so prerequisites are explicit and executable.
- Kept all items in `status: backlog` with empty findings, consistent with intake-only workflow.

## Mini-Retro

1. **Did the process work?** Yes. The issue already provided a clear dependency map (`Depends on` and `Enables`), so decomposition into separate backlog items was straightforward.
2. **What slowed down or went wrong?** The only friction was translating question IDs into stable slug names while preserving readable file names.
3. **What single change would prevent this next time?** Add canonical slug hints in issue templates when submitters provide multi-question dependency graphs.
4. **Is this a pattern?** Yes. Structured issue prompts with explicit dependencies consistently produce high-quality backlog decomposition.
5. **Does any documentation need updating?** No. Existing intake instructions were sufficient.
6. **Do the default instructions need updating?** No. Current guidance already fits multi-question dependency intake.
