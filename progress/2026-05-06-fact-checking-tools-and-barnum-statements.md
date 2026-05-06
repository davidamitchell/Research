# 2026-05-06 -- Add backlog items (fact-checking-tools-and-barnum-statements)

**Completed:**
- `Research/backlog/2026-05-06-openfactcheck-automated-fact-verification.md` — added from issue; asks what OpenFactCheck provides for automated fact verification and how applicable it is to this repository's AI-generated research review process.
- `Research/backlog/2026-05-06-loki-fact-checking-journalists-ai-content.md` — added from issue; asks what the Loki fact-checking tool does for journalists and content moderators and what relevance it has for verifying claims in AI-generated research items.
- `Research/backlog/2026-05-06-factscore-atomic-claim-precision-scoring.md` — added from issue; asks how FActScore (Factuality Assessment at Claim Granularity) computes precision scores for atomic factual claims and what the implications are for automated quality scoring of research items in this repository.
- `Research/backlog/2026-05-06-open-weight-policy-enforcement-research-review.md` — added from issue; asks how open-weight policy enforcement models (such as gpt-oss-safeguard) classify text against customizable policies and whether they can implement this repository's research review rules as a machine-checkable policy.
- `Research/backlog/2026-05-06-barnum-statements-ai-response-detection-removal.md` — added from issue; asks what Barnum statements (Forer effect) are, how LLMs produce them, and what systematic methods exist to detect and remove them from AI-generated research outputs.

## Mini-Retro

1. **Did the process work?** Yes. All five topics from the issue were well-defined enough to scope into specific, answerable research questions. The research-question skill was applied manually (submodule not initialised in sandbox). Each item's question passed all five quality tests: Specific, Answerable, Scoped, Motivated, Decomposable.

2. **What slowed down or went wrong?** The Loki tool required a note in the item to confirm the correct GitHub repository URL during research — the exact repository location was not definitively known from the issue description alone. This is the correct handling: flag the uncertainty, do not guess.

3. **What single change would prevent this next time?** Nothing structural. The one uncertainty (Loki's exact repository) is inherent to the issue description and is correctly flagged in the item's Sources section with a note to confirm during research.

4. **Is this a pattern?** No — the uncertainty is specific to Loki's description in the issue. The broader pattern of the submodule not being initialised is already a known, documented constraint.

5. **Does any documentation need updating?** No. Five new backlog items were created; no existing documentation references these topics. No user-facing behaviour changed.

6. **Do the default instructions need updating?** No new convention emerged. The manual fallback for the `research-question` skill is already documented in `.github/copilot-instructions.md`.
