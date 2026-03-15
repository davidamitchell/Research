# Session: fix-rubric-review-violations

**Date:** 2025-01-31
**Slug:** fix-rubric-review-violations

## What was done

Fixed all violations flagged by research review in `Research/completed/2026-03-10-research-loop-evaluation-rubric.md`.

### citation-discipline fixes
1. Expanded YAML at first use (line 49): "YAML Ain't Markup Language (YAML)"
2. Expanded JSON at first use (line 459): "JavaScript Object Notation (JSON)"
3. Fixed factual error in Evidence Map (line 429): `$0.08/minute` → `$0.008/minute` (consistent with body at lines 190, 304, 408)
4. Added missing URL for GitHub Actions pricing documentation at Evidence Map citation
5. Replaced "highest-frequency failure modes" (lines 290, 396) with "most structurally significant failure modes per the protocol specification"; added `[inference]` to "most common failure modes" claim (line 446)

### speculation-control fixes
1. Added `[inference]` to "The correct approach is to group by evaluator type" (line 234)
2. Added `[inference]` to "This is not a quality compromise" (line 238)
3. Added `[inference]` to "The gold dataset is the riskiest component" (line 240)
4. Added `[assumption]` to engineering cost estimate `<1 day` (line 270)
5. Added `[inference]` to "The value of catching a protocol violation is high" (line 270)

## Outcome

All 10 violations resolved with minimum necessary changes. No facts, findings, or evidence altered.
