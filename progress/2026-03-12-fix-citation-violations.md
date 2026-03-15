# Session: Fix Citation & Speculation Violations in volume-vs-correctness

**Date:** 2026-03-12
**Slug:** fix-citation-violations

## Task

Fix review violations in `Research/completed/2026-03-12-volume-vs-correctness-ai-era.md`.

## Changes Made

1. **Line 182** — Changed `[fact]` → `[inference — secondary source]` for philippdubach.com citation of DORA 2025 quotation (blog is a secondary source; primary DORA report not directly accessed).

2. **Line 327** — Added `[URL NEEDED]` after reference to the Harvard Business Review publication of the underlying UC Berkeley research (no URL was present).

3. **Line 498** — Moved `[inference — derived from Dell'Acqua et al. 2025 treatment arm comparisons]` label to appear directly after the first sentence ("A critical distinction emerges from the P&G study: AI substitutes for average peer collaboration, not peak collaborative quality.") — the claim was previously unlabeled at the sentence level.

## Violations Already Fixed in File

Violations #3–7 and #10–11 (Microsoft Research URL, CNBC/debevoisedatablog URLs, medium.com/@tobrien URL, medium.com/@ignatovich.dm URLs, paddo.dev/Amdahl's Law URLs, and the "decisive differentiator" / "implication for team composition" speculation-control issues) were already addressed in the file prior to this session.

## Commit

`f2c115c` — fix: address citation-discipline and speculation-control violations
