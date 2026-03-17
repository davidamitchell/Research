# Session: Clean Up Research Review Issues

**Date:** 2026-03-17
**Slug:** clean-up-research-review-issues
**PR:** #220 (closes #161, #162, #163, #164, #179, #180, #181, #182, #183, #184, #185, #186, #187, #188, #189, #190, #198, #199, #202, #203, #207, #208, #209, #210, #211, #212, #213, #214, #215)

## Work Done

Fixed all research review violations across 7 completed research items and removed all em-dashes from each.

### Files Modified

1. `Research/completed/2026-03-14-reliable-software-llm-era.md` (issues #179–190, #199)
   - Added [fact]/[inference] labels to all 10 Findings Key Findings
   - Fixed unsourced reddit claim: [fact] → [inference] + [SOURCE NEEDED]
   - Added [SOURCE NEEDED] to unsourced model-based testing claim
   - Fixed KF2 wording to match source ("more familiar to working engineers")
   - Condensed near-verbatim duplicate Findings Executive Summary
   - Condensed Findings KF4 to avoid AI slop repetition of §6 KF4
   - Added authoritative links for TLA, Language Server Protocol on first use
   - Expanded "Visual Studio Code (VS Code)" at first use
   - Added ROI expansion at first use in §5
   - Added FM (Formal Methods) expansion at first use
   - Fixed "historical context" placeholder → [SOURCE NEEDED]
   - Removed 95 em-dashes

2. `Research/completed/2026-03-15-adam-smith-org-design-desire-paths-ai.md` (issues #202–214)
   - Expanded "User Experience (UX)" at first use
   - Expanded "Human Resources (HR)" at first use
   - Added [full citation NEEDED] to all three incomplete Springer citations
   - Relabelled Wikipedia-sourced [fact] claims → [inference]
   - Added [URL NEEDED] to Mises Institute citations
   - Removed 98 em-dashes

3. `Research/completed/2026-03-08-chatgpt-actions-memory-integration.md` (issue #164)
   - Expanded RAG at first use
   - Removed em-dashes

4. `Research/completed/2026-03-12-swat-technique-loop-fresh-context.md` (issues #161, #162)
   - Expanded SWOT, BM25, AMPS at first use
   - Expanded AIES, CHI, SLA, NeurIPS, EMNLP at first use
   - Fixed epistemic label mismatch: [fact] Recency bias → [inference]
   - Removed em-dashes

5. `Research/completed/2026-03-14-ricardian-contract-model.md` (issue #163)
   - Verified IEEE, IPFS, PGP, SQL expansions present
   - Removed em-dashes

6. `Research/completed/2026-03-15-context-compression-rag-enterprise-knowledge.md` (issue #198)
   - Expanded RULER, ICLR, EMNLP, ACL, GSM8K at first use
   - Removed em-dashes

7. `Research/completed/2026-03-15-latent-concept-extraction-confluence.md` (issue #215)
   - Expanded SPLADE at first use
   - Moved SBERT expansion to first use
   - Added [SOURCE NEEDED] to unsourced historical KMS claim
   - Added [SOURCE NEEDED] to unsourced cost claim
   - Removed 58 em-dashes

## Pattern Observed

Research review failures are predominantly: (1) acronym not expanded at first use, (2) factual claims without citations or with Wikipedia as sole source, (3) near-verbatim repetition between §6 and Findings sections. The research-review skill checks these systematically.
