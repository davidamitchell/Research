---
date: 2025-07-15
slug: fix-taxonomy-expansion-violations
---

# Session: Fix research review violations in failure-mode-taxonomy-expansion

## What was done

Fixed all violations flagged by the research review for `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md`.

### citation-discipline fixes
1. **OPA** expanded at first use (line 69): `Open Policy Agent (OPA)`
2. **CVSS** expanded at first use (line 193): `Common Vulnerability Scoring System (CVSS)`
3. **ICLR** expanded at first use (line 234): `International Conference on Learning Representations (ICLR)`
4. **OWASP primary source**: Added `owasp.org/www-project-top-10-for-large-language-model-applications/` alongside invicti.com at both claims (lines 180 and 265)

### speculation-control fixes
5. Added `[inference]` to unlabeled Goodhart's Law causal chain paragraph (line 261)
6. Added `[inference]` to each "most dangerous cascades" evaluative bullet (lines 345–347)
7. Added `[inference]` to "OWASP's security mandate over-represents adversarial failures" (line 631)
8. Added `[inference]` to "This makes Layer 5 → Layer 1 the highest-priority unmonitored risk" (line 635)

## Outcome

All 8 violations resolved with minimum-change edits. No facts, findings, or evidence altered.
