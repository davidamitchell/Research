# 2026-05-29 -- AI-First Software Ecology Developer Ecosystems

**Completed:**
- `Research/completed/2026-05-27-ai-first-software-ecology-developer-ecosystems.md` — completed from issue; research question: what operating model, architecture strategy, and governance approach should large software organisations adopt to build AI-assisted developer productivity sustainably by 2030?

## Work Done

- Read item in full; identified 8 related completed items for cross-reference
- Conducted evidence gathering across 19+ sources: METR RCT, Google Research RCT, MIT/Microsoft MIT Sloan RCT, Faros AI telemetry (10,000+ devs), DORA 2025, Microsoft Work Trend Index (WTI) 2026, Anthropic Economic Index, OWASP LLM Top 10, Team Topologies, SPACE framework, McKinsey three-horizon model, Wardley Maps
- Wrote complete §§0-7 Research Skill Output
- Seeded full Findings: Executive Summary, 12 Key Findings, Evidence Map, Assumptions, Analysis (with cross-item references), Risks/Gaps, Open Questions, Output
- Marked as draft; triggered `research-review.yml` (MAX_REVIEWS=2)
- Review pass 1/2: FAIL — fixed ROI/UX/SPACE acronym expansions, §5 inference labels, em-dashes, Faros alternative explanation, cross-item integration for `ai-coding-harnesses-agent-philosophy` and `it-throughput-constraint`
- Review pass 2/2: FAIL — fixed SPACE expansion at §1 first use, §5 Technical/Behavioural labels, automation bias authoritative source, KF bold format (removed full-sentence bold from KF1-12)
- Review pass 3 auto-passed (MAX_REVIEWS=2 reached); moved item to `Research/completed/`
- Updated `learnings.md`: Thread 11 (volume-correctness inversion) and Thread 8 (force multiplication) extended with Acceleration Whiplash pattern, METR RCT finding, and conditional amplification evidence

## Key Findings Summary

1. AI is an amplifier of existing organisational conditions, not a transformer of them
2. Faros "Acceleration Whiplash": individual throughput up, organisational DORA metrics flat or degrading
3. METR RCT: experienced engineers 19% slower on complex tasks with AI assistance
4. DORA 2025: seven capability prerequisites; organisational factors = 2× the impact of individual tools
5. Platform engineering (developer portals, automated quality gates, pipelines) is the prerequisite
6. Google/MIT RCT confirms developer experience level mediates productivity effects
7. Automation bias from AI code review and AI-generated tests creates governance risk
8. Only 19% of organisations at Frontier Firm operating model level by late 2025
9. 3-5 year adoption timeline for full AI-first operating model
10. OWASP LLM Top 10 and access-scoped agent identities as security requirements

## Mini-Retro

1. **Did the process work?** Mostly yes. The research evidence-gathering phase was thorough and the §§0-7 structure guided the investigation well. The review workflow surfaced real violations each pass.

2. **What slowed down or went wrong?** Three review passes were required (one beyond MAX_REVIEWS auto-pass). The recurring failures were: (a) SPACE acronym not expanded at the first prose occurrence in §1 - expanded only in §2.B but §7 incorrectly reported §2.B as first use; (b) §5 Depth/Breadth lens paragraphs missing `[inference]` labels - these are consistently treated as exempt from claim-labelling but are not; (c) full-sentence bold on Key Findings (inline-header list pattern) - this is listed in Known Recurring Patterns but was still initially applied.

3. **What single change would prevent this next time?** Add an explicit §5 claim-labelling check to the self-review step before draft commit. The §5 paragraphs must be treated as claim-bearing prose on every pass.

4. **Is this a pattern?** Yes. SPACE acronym first-use tracking failed twice in this item. §5 unlabelled claims have appeared in at least two prior sessions. Full-sentence bold on Key Findings is listed in Known Recurring Patterns but recurs. All three are recurring class problems.

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should note that §5 Depth/Breadth lens paragraphs require explicit `[fact]`/`[inference]`/`[assumption]` labels on every claim - this is distinct from the SPACE acronym issue but equally common. The §7 acronym audit instruction should explicitly state that the audit must identify the first _prose_ use, not the first occurrence in any section header or sub-question label.

6. **Do the default instructions need updating?** The Known Recurring Patterns table entry for SPACE/acronym should be sharpened: the §7 audit result must confirm first _narrative prose_ use (not first occurrence anywhere in the document). Consider adding a new row: "§5 Depth/Breadth lens claims missing epistemic labels - check every paragraph in §5 for unlabelled factual or inferential claims before triggering review."
