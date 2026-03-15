---
date: 2026-03-14
slug: fix-hosting-options-review-violations
---

# Session: Fix Research Review Violations — hosting-options-for-the-research-repo

## What was done

Fixed all violations flagged by the research review in `Research/completed/2026-03-12-hosting-options-for-the-research-repo.md`.

### citation-discipline fixes
- Expanded 6 acronyms at first use: YAML (§1 Q2a), SSL (§2 Q1a table), JSON (§2 Q3a), REST+gRPC (§2 Q4a), CORS (Open Questions §6)
- Added `[SOURCE NEEDED]` to uncited Jekyll claims ("Ruby SSG native to GitHub Pages", "Limited plugin support in branch-deploy mode"), Docusaurus claim ("Optimised for versioned documentation"), MkDocs Material "hundreds of major open-source documentation sites" claim, "covers 80% of the filtering use case" statistic, and Jekyll+Lunr.js historical claim
- Added `[URL NEEDED]` to the Techzine AuraDB Free launch citation and MkDocs Material tags docs citation
- Added `[PRIMARY SOURCE NEEDED]` note to Cloudflare Pages limits sourced from netlify.com (a competitor)

### speculation-control fixes
- Added `[inference]` to: "Pagefind is superior to lunr", "Technical risk is low", "This is a known, solved problem", "current state of the art for static search"

### §7 acronym audit
- Added all 6 newly expanded acronyms (YAML, SSL, JSON, REST, gRPC, CORS) to the §7 audit checklist

## Outcome

All 13 citation-discipline violations and 4 speculation-control violations resolved. File committed on branch `copilot/fix-research-review-issues`.
