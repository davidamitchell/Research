# 2026-08-14 — Research completed (llm-consumption-maturity-ladder)

**Completed:**
- `Research/completed/2026-08-13-llm-consumption-maturity-ladder.md` — full research cycle (§0–§7 skill process, Findings, companion skill checks, two review passes) completed and moved from `in-progress/` to `completed/`. Answers how enterprise AI maturity frameworks (MIT CISR, AWS Prescriptive Guidance) map onto the empirical LLM consumption ladder (single-API, managed multi-model platform, dynamic routing, self-hosting, fine-tuning, owned-hardware inference). Key conclusion: maturity models measure organizational capability while the technical consumption rung is governed by a separate, largely orthogonal cost-benefit calculation (self-hosting/ownership economically rational primarily above ~50M tokens/month sustained volume or under strict data-residency mandates, per arXiv:2509.18101). Dynamic routing (Amazon Bedrock intelligent prompt routing, LiteLLM) functions as the bridging mechanism between managed platforms and self-hosting. `confidence: medium` (mixed primary-source and single-survey evidence).
- `learnings.md` — added a new evidence bullet to Thread 20 ("AI frameworks classify different objects, so teams need layered vocabulary") extending the layered-vocabulary claim to the cost-economics layer: maturity frameworks and the technical consumption ladder classify different objects (organizational capability vs. infrastructure cost economics).

**Sources consulted (primary, independently fetched/verified this session):**
- MIT CISR Enterprise AI Maturity Model (Weill, Woerner, Sebastian, Dec 2024) — mitsloan.mit.edu
- AWS Prescriptive Guidance generative AI maturity model — docs.aws.amazon.com
- arXiv:2509.18101 (Pan, Chodnekar, Roy & Wang, 2025) — On-premise LLM cost-benefit analysis, HTML full text
- arXiv:2603.04445 (Moslem & Kelleher, 2026) — Dynamic Model Routing and Cascading survey
- Amazon Bedrock intelligent prompt routing documentation
- LiteLLM Router documentation
- Menlo Ventures 2025 State of Generative AI in the Enterprise
- a16z 2025 Enterprise AI survey
- IDC FutureScape 2026 blog post (businesswire.com press release timed out; substituted accessible idc.com page)
- Gartner maturity model page (paywalled — treated as unverified, excluded from Key Findings)
- 5 prior completed repository items cross-referenced and cited with URL-backed links

## Mini-Retro

1. **Did the process work?** Yes. The full §0–§7 research skill process, Findings seeding, and companion skill checks produced an item that needed only two automated review passes (both minor violations, no issue raised) before auto-passing at `review_count: 2`.

2. **What slowed down or went wrong?**
   - The `.github/skills/` submodule was not initialized at session start and required `git submodule update --init` before the skill file was readable.
   - The automated review workflow's own commit on pass 1 raced with a concurrent `docs: rebuild site` commit and never landed on `main` (the documented "research-review.yml commit race" pattern) — required manually verifying `git log` to confirm the pass didn't count before treating the violations as still-open.
   - Two review passes surfaced violations that manual self-review missed: (a) a four-sentence §6 Synthesis paragraph where only the first sentence carried a source label; (b) two Key Findings that appended an unlabelled evaluative generalization ("market-wide shift", "modal practice") to a correctly-labelled statistic under one `[fact]` tag; (c) single-source Key Findings incorrectly marked `high confidence`; (d) a `related:` frontmatter item (AgentCore) never mentioned in the body; (e) an unsupported "peer-reviewed" characterization of an arXiv preprint.

3. **What single change would prevent this next time?** Add an explicit self-review step that greps every Key Finding and Evidence Map "high confidence" claim for citation count and organizational independence *before* triggering the first automated review — this session's self-review checked label presence and source-URL presence but not source-count/independence per confidence tier, which is exactly the gap the `peer-reviewer` skill caught on pass 1.

4. **Is this a pattern?** Yes — three of the five pass-1/pass-2 violations (multi-sentence paragraph with one leading label, fact+evaluative-generalization merge, single-source high-confidence) match patterns already documented in `.github/copilot-instructions.md`'s Known Recurring Failure Patterns table, confirming those patterns are still live risks even when the self-review checklist is followed carefully. The `related:`-frontmatter-item-never-mentioned-in-body violation is a new pattern not yet in that table.

5. **Does any documentation need updating?** Yes — see the new Known Recurring Failure Patterns row added to `.github/copilot-instructions.md` in this same commit (frontmatter `related:`/`cites:` items must be mentioned in body prose, not just listed).

6. **Do the default instructions need updating?** Added the new failure-pattern row (see above). No other convention changes identified.
