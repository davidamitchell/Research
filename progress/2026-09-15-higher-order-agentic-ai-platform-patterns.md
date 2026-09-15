# 2026-09-15 -- Complete research item (higher-order-agentic-ai-platform-patterns)

**Completed:**
- `Research/completed/2026-09-14-higher-order-agentic-ai-platform-patterns.md` -- ran the full research skill (§0-§7) and populated Findings for the research question "What higher-order operational patterns recur across production agentic AI systems, what underlying operational problems do they address, and which patterns generalise across applications and execution environments?"
- Identified three recurring higher-order patterns: a mandatory policy-gated governance-and-tool-registry layer, an event-driven multi-agent coordination substrate, and a shift from episodic to continuous production-traffic evaluation.
- Sourced from 7 external sources (arXiv papers, an MDPI paper via an accessible mirror after a 403, a Confluent engineering article, a Microsoft AI Red Team taxonomy, and a substituted arXiv systematic literature review after a ResearchGate 403) plus 7 prior completed items cross-referenced in `cites:`.
- Updated `learnings.md` with Thread 30, connecting this item's governance/HITL-bypass/inter-agent-trust findings to the machine-identity precondition established in three prior completed items.

## Review cycle

The item went through 2 real review cycles before hitting the workflow's review cap (2) and auto-passing:
- **Pass 1** (2 attempts, first attempt's own commit failed to push and did not count): flagged SLR used bare with no expansion, "confused-deputy problem" cited without an authoritative primary source, an unaddressed alternative explanation (testing-selection bias) for the HITL-bypass governance-lag inference, and three materially overlapping completed items not cross-referenced (control-plane architecture, agent identity/access management, multi-agent identity attribution). All four fixed: expanded SLR, added Hardy (1988) "The Confused Deputy" as a primary source, added the rival-explanation paragraph to Analysis and both mirrored Executive Summary sentences, and added the three items to `cites:` plus a substantive cited §0 paragraph.
- **Pass 2**: flagged CSIRO and HTTP used bare with no expansion, and two paragraphs in Findings Risks/Gaps with no epistemic label or citation. Fixed both.
- **Pass 2 (second attempt)**: flagged that the §6 Synthesis condensed mini-summary paragraphs (Assumptions, Analysis, Risks/Gaps) asserted claims, including a comparative "strongest, most independently corroborated" judgment, without their own labels or citations, even though the expanded Findings versions were fully labeled. Fixed by adding per-sentence labels and sources to the §6 mini-summaries.
- Third review trigger auto-passed at the review cap (`review_count: 2`).

## Mini-Retro

1. **Did the process work?** Yes. The self-review checks caught most violations before the first review run (30 em-dashes, bracket formatting, acronym ordering), and the external review caught real gaps the self-review missed: a condensed-summary section (§6) that is easy to treat as "just a pointer to Findings" but is itself claim-bearing prose in scope for citation-discipline.
2. **What slowed down or went wrong?** The first review trigger's own commit-and-push step failed (a known race with a concurrent commit landing on `main`), so that pass did not count toward the review budget and had to be re-triggered. Also, condensed/mirrored content (§6 Synthesis mini-summaries) was treated as exempt from full citation-discipline during self-review, when it is not; every condensed sentence needs its own label and source even if the sentence is a compressed restatement of an already-labeled Findings sentence.
3. **What single change would prevent this next time?** Add an explicit self-review sub-check for condensed/compressed synthesis text: any sentence in a "mini-summary" or "condensed version" block, not just full-length Findings prose, must carry its own epistemic label and source, even when it summarises already-labeled content elsewhere in the document.
4. **Is this a pattern?** Yes -- this is a variant of the already-documented "paragraph-opening sentence left unlabeled" class of failure, extended to condensed/compressed summary sections specifically. Adding this to the Known Recurring Failure Patterns table below.
5. **Does any documentation need updating?** Yes -- adding a new row to the Known Recurring Failure Patterns table in `.github/copilot-instructions.md` for the condensed-summary labeling gap.
6. **Do the default instructions need updating?** Same as above; see the added table row.
