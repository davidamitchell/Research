---
date: 2025-07-18
slug: fix-ai-force-multiplier-violations
type: fix
---

# Fix: citation-discipline and speculation-control violations in ai-force-multiplier item

## What was done

Fixed 9 violations identified by research review in
`Research/completed/2026-03-12-ai-force-multiplier-ambition-expansion.md`.

### citation-discipline fixes

| # | Violation | Fix applied |
|---|---|---|
| 1 | VC not expanded at first use | Already compliant — "venture capital (VC)" precedes "VC capital" in the same bullet; no change needed |
| 2 | NZ not expanded | "New Zealand (NZ)" at first use in Open Questions Q3 |
| 3 | RBNZ/FSC not expanded | "Reserve Bank of New Zealand (RBNZ)" and "Financial Services Council (FSC)" at first use |
| 4 | Apple $2.4M figure unsourced | Added `[SOURCE NEEDED]` in Key Finding 4 |
| 5 | xpromx.me citation missing URL | Added `[URL NEEDED]` after DEV Community citation in §2 D1 |
| 6 | UCLA Anderson/JSV citation insufficient | Added `[URL NEEDED — full title and URL required]` in §2 B |
| 7 | McKinsey/LinkedIn RIF claim labelled [fact] | Changed to `[inference]` — source is secondary LinkedIn post citing unnamed studies |
| 8 | SaaS <$500K benchmark unsourced | Added `[SOURCE NEEDED]` in Context section |

### speculation-control fixes

| # | Violation | Fix applied |
|---|---|---|
| 1 | "AI layer acts as multiplier" causal claim unlabelled | Added `[inference]` in §5 Technical lens |
| 2 | March 1991 extended to AI adoption budgets | Added `[inference]` before that sentence in §5 Behavioural lens |

## Commit

`2b6348c` — research: fix citation-discipline and speculation-control violations in ai-force-multiplier item
