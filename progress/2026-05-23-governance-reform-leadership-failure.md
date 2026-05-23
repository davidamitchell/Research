# 2026-05-23 -- Research Loop (governance-reform-leadership-failure)

**Completed:**

Research item:
- `Research/completed/2026-05-23-governance-reform-leadership-failure.md` -- completed; the item finds that governance reform in regulated enterprises usually stalls because accountability diffuses, information is filtered upward, and inherited control structures are politically easier to keep than to remove. It also finds that durable reform usually needs a forcing event, clearer ownership, stronger challenge rights, and external validation that simplification changed outcomes rather than only documentation.

Sources consulted:
- https://www.apra.gov.au/news-and-publications/apra-releases-cba-prudential-inquiry-final-report-and-accepts-enforceable (official banking governance failure and remediation case)
- https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/279124/0947.pdf (official Mid Staffordshire inquiry report on board and system failure)
- https://www.govinfo.gov/content/pkg/GPO-OILCOMMISSION/pdf/GPO-OILCOMMISSION.pdf (official Deepwater Horizon commission report on leadership, culture, and oversight failure)

## Mini-Retro

1. **Did the process work?** Yes, but only after a first review pass exposed a few claim-label and definition-first-use errors that were easy to fix once the log was read closely.
2. **What slowed down or went wrong?** The review workflow auto-passed on the second run even though the log still contained real violations, and bullet-style audit notes in `§4` and `§7` were treated as unsupported claims.
3. **What single change would prevent this next time?** Tell future runs to render `§4 Consistency Check` and `§7 Recursive Review` as fenced plain-text metadata blocks by default instead of bullet sentences.
4. **Is this a pattern?** Yes, it matches the broader recurring pattern that review metadata and shorthand definitions get interpreted as claim-bearing prose unless the prompt forces a stricter format.

## Applied improvements

- Updated `research-prompt.md` so `§4 Consistency Check` and `§7 Recursive Review` default to fenced plain-text metadata blocks, and so the `§7 review-metadata check` explicitly prefers that format over bullet sentences.

## Pending skill improvements

- Mirror the same fenced-metadata guidance into `.github/skills/research/SKILL.md` for `§4 Consistency Check` and `§7 Recursive Review` once the skills submodule can be updated in the `davidamitchell/Skills` repository.
