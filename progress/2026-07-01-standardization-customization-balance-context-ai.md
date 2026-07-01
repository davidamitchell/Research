# 2026-07-01 -- Research Loop (standardization-customization-balance-context-ai)

**Completed:**

Research item:
- `Research/completed/2026-06-13-standardization-customization-balance-context-ai.md` -- completed; synthesises four companion repository items into a two-axis framework (governance-infrastructure standardization versus task-execution standardization) that resolves an apparent contradiction between banking evidence (favouring centralised governance infrastructure) and healthcare evidence (favouring less standardization of frontline task execution). Finds that Artificial Intelligence (AI) agent adoption amplifies existing platform maturity on productivity outcomes (per the DORA 2025 report) while independently raising the minimum required standardization of the AI-specific control plane because agentic, tool-calling failure modes are harder to detect and contain than earlier non-agentic local tooling.

Sources consulted:
- https://www.annfammed.org/content/19/2/171 (Sinsky et al. 2021 healthcare standardization-versus-customization framework, peer-reviewed)
- https://cmr.berkeley.edu/1988/11/31-1-organizing-for-worldwide-effectiveness-the-transnational-solution/ (Bartlett and Ghoshal 1988 transnational organisational-design framework)
- https://dora.dev/research/2025/dora-report/ (DORA 2025 State of AI-assisted Software Development report, resolved URL after redirect from the seeded dora.dev/report/2025 link)
- Four companion repository items completed 2026-06-13 on local-global throughput dynamics, fragmentation-threshold measurement, platform-engineering/InnerSource hybrid patterns, and shadow-IT governance transition
- Three earlier repository items on banking agent governance (2026-05-20), shadow AI behavioural drivers (2026-05-08), and AI/low-code SDLC platform-engineering integration (2026-04-26)
- https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf (bank model-risk-management guidance, cited via the banking companion item)
- https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/ (CNCF Platform Engineering Maturity Model)
- https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem (Spotify golden path case study)

## Mini-Retro

1. **Did the process work?** Yes. This was a synthesis item with all four companion items and the three cited items already completed, so the research consisted of cross-item integration plus verification of three additional seed sources (Sinsky et al., Bartlett and Ghoshal, DORA 2025). The two-round review cycle worked as designed: pass 1 caught real acronym-ordering and claim-labelling errors, pass 2 caught more subtle epistemic-boundary issues (an interpretive "weighs against" sentence mislabeled as fact, an unlabeled superlative opening sentence), and pass 2's auto-pass rule let the item complete without a third cycle.
2. **What slowed down or went wrong?** The first review workflow run (28507495514) reported "FAIL... no issue raised" but did not appear to commit a `review_count` update before a second workflow run was triggered; the visible `review_count` progression (0 to 1 to 2) suggests the two workflow-triggered runs correspond to the two allowed passes even though the first run's commit was not independently visible in `git log` before the second run's commit landed. This did not block completion but made mid-loop diagnosis slightly harder than expected.
3. **What single change would prevent this next time?** Before re-triggering a review after a fix commit, explicitly check `git log --oneline -- <item path>` for a `review: pass N/M` commit from the prior run, not just the `review_count` frontmatter field, to confirm the previous pass's result actually landed before triggering the next one.
4. **Is this a pattern?** Two of the four review violations found (Key Finding full-sentence bold; acronym expansion order errors such as "SDLC (Software Development Lifecycle)" reversed order) match existing entries in the Known Recurring Patterns table in `.github/copilot-instructions.md`. A new pattern surfaced: **interpretive reasoning sentences that follow a `[fact]`-labeled sentence and draw an inference from it (e.g., "X weighs against Y because...") must carry their own `[inference]` label even when the preceding sentence is `[fact]`** -- the fact label does not transfer to derived reasoning about what that fact implies for a rival explanation. This is closely related to the existing "mid-paragraph evaluative/comparative claims" and "closing-sentence" patterns already documented, but is distinct enough (a reasoning connective built on a `[fact]` premise, not a bare evaluative adjective) that it warrants its own entry.

## Applied improvements

Added a new row to the Known Recurring Failure Patterns table in `.github/copilot-instructions.md`: "Inferential reasoning sentences built on a `[fact]`-labeled premise inherit no label of their own" -- covering the specific case where a sentence draws an interpretive conclusion ("weighs against", "would not be expected if", "is inconsistent with") from a preceding fact-labeled claim and must carry its own `[inference]` label rather than being read as part of the fact.
