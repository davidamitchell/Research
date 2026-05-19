# 2026-05-19 -- Break interdisciplinary prompt into multiple research questions

**Completed:**
- Added 9 backlog items in `Research/backlog/` from the issue prompt, splitting the thermodynamic + transaction-cost + institutional framing into 8 primary questions plus 1 synthesis question.
- Assigned descriptive titles and scoped each item with in-scope/out-of-scope constraints, approaches, and URL-backed source seeds.
- Added explicit dependency links by making the synthesis question block on the 8 primary questions.

## Mini-Retro

1. **Did the process work?** Yes. The issue content already contained strong thematic clusters, so converting each cluster into a separately scoped backlog item was straightforward.
2. **What slowed down or went wrong?** The initial auto-generated slugs for two long titles were truncated, which reduced readability and required manual rename.
3. **What single change would prevent this next time?** Use shorter titles when running `python -m src.main research add` so generated slugs stay descriptive without truncation.
4. **Is this a pattern?** No clear pattern yet; this session had only two long-title truncations and was quickly corrected.
5. **Does any documentation need updating?** No documentation change is required for this issue; the existing research-item workflow already covers this pattern.
6. **Do the default instructions need updating?** Not at this stage. The current instructions already emphasise descriptive filenames and scoped questions.
