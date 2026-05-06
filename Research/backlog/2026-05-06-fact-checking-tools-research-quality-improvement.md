---
title: "How can findings from OpenFactCheck, Loki, FActScore, gpt-oss-safeguard, and Barnum statement research be synthesised into concrete improvements to the automated review process in this research repository?"
added: 2026-05-06T09:49:53+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [research-methodology, quality-assurance, evaluation, research-loop, fact-checking, llm, workflow]
started: ~
completed: ~
output: [backlog-item, knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-openfactcheck-ai-fact-checking-pipeline, 2026-05-06-loki-fact-checking-journalists-moderation, 2026-05-06-factscore-precision-scoring-atomic-claims, 2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight, 2026-05-06-barnum-statements-ai-responses-theory-practice]
related: [2026-05-06-openfactcheck-ai-fact-checking-pipeline, 2026-05-06-loki-fact-checking-journalists-moderation, 2026-05-06-factscore-precision-scoring-atomic-claims, 2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight, 2026-05-06-barnum-statements-ai-responses-theory-practice]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: synthesis # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How can findings from OpenFactCheck, Loki, FActScore, gpt-oss-safeguard, and Barnum statement research be synthesised into concrete improvements to the automated review process in this research repository?

## Research Question

How can the findings from research into OpenFactCheck, Loki, FActScore, gpt-oss-safeguard, and Barnum statement identification techniques be synthesised into concrete, actionable improvements to the automated review process (`research-review-prompt.md`) in this repository — specifically targeting factual precision, policy compliance, and output quality?

## Scope

**In scope:**
- Synthesis of findings from the five prerequisite items: capabilities, limitations, and deployment feasibility of each tool
- Gap analysis between the current `research-review-prompt.md` review criteria and what automated claim-level verification could additionally check
- Actionable recommendations for each of three intervention points: (1) the research agent prompt (`research-prompt.md`), (2) the review workflow prompt (`research-review-prompt.md`), and (3) a new automated pre-review tooling step
- Assessment of which quality improvements can be made with no new tooling (prompt changes only) versus which require new tooling integration
- Priority ordering of recommendations by effort-to-impact ratio
- Proposed candidate rubric additions to `research-review-prompt.md` for: atomic claim labelling completeness, Barnum statement absence, and source URL coverage
- Identification of W-XXXX backlog items to capture any tooling changes required

**Out of scope:**
- Implementation of any tooling changes (these are scoped to separate backlog items produced as output)
- Re-researching the individual tools (these are covered in the five prerequisite items and should be read as inputs to this synthesis)
- General LLM evaluation methodology beyond what is directly applicable to this repository's research outputs

**Constraints:**
- This item must not start until all five prerequisite items are completed: `2026-05-06-openfactcheck-ai-fact-checking-pipeline`, `2026-05-06-loki-fact-checking-journalists-moderation`, `2026-05-06-factscore-precision-scoring-atomic-claims`, `2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight`, and `2026-05-06-barnum-statements-ai-responses-theory-practice`
- Recommendations must be specific and actionable: each must identify the exact file and section to be changed, the nature of the change, and the expected quality improvement
- The synthesis must distinguish between prompt-level fixes (zero infrastructure cost) and tooling fixes (require new dependencies or workflow steps)

## Context

This repository runs an autonomous research loop that produces structured research items. The quality of those items is enforced by an automated review workflow (`research-review.yml`) that evaluates each completed item against criteria in `research-review-prompt.md`. The current review criteria are largely structural (source URL presence, epistemic labelling, section completeness) but do not assess factual precision at the claim level, do not detect policy-class content violations, and do not explicitly flag Barnum-style hollow assertions. Five preceding research items investigate specific tools that could address each of these gaps. This synthesis item reads the findings from all five and translates them into prioritised, actionable improvements to the review process. It is the culmination of the fact-checking and output-quality research series.

## Approach

1. **Read prerequisite findings:** Summarise the key findings from each of the five prerequisite items in a structured comparison table covering: capability, accuracy, deployment feasibility (GitHub Actions compatible?), cost, and primary failure mode.

2. **Gap analysis against current review criteria:** Read `research-review-prompt.md` in full. Map each current review criterion to the quality dimension it addresses. Identify the quality dimensions not currently covered: factual precision at claim level, Barnum statement density, policy compliance, and source recency.

3. **Prompt-only improvements (no new tooling):** Identify the additions to `research-review-prompt.md` that require no new tooling — for example, explicit Barnum statement criteria, atomic claim labelling completeness checks, and a prohibition on hollow hedging phrases. Draft the proposed criterion text for each.

4. **Tooling-assisted improvements:** For improvements that would benefit from automated tooling (FActScore integration, OpenFactCheck pipeline, gpt-oss-safeguard policy check), assess: (a) integration effort, (b) false positive risk, (c) impact on review latency, and (d) whether the improvement could be approximated with a prompt-only approach first.

5. **Priority matrix:** Rank all proposed improvements on a two-axis matrix: implementation effort (low/medium/high) vs. expected quality uplift (low/medium/high). Identify the top three highest-impact, lowest-effort changes.

6. **Backlog item drafting:** For each improvement that requires a new backlog item (tooling integration, skill update, prompt rewrite), draft the item title and one-sentence scope so the output can immediately populate `BACKLOG.md` and/or `Research/backlog/`.

7. **Research prompt improvements:** Assess whether any improvements should be applied to `research-prompt.md` rather than `research-review-prompt.md` — i.e., whether the research agent should be instructed to avoid Barnum statements at generation time, not just catch them at review time.

## Sources

- [ ] [research-review-prompt.md in this repository](https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md) — primary target document; the current automated review criteria that this synthesis item is designed to improve
- [ ] [research-prompt.md in this repository](https://github.com/davidamitchell/Research/blob/main/research-prompt.md) — secondary target document; the research agent prompt where upstream quality improvements can be applied
- [ ] [Wang et al. (2024) OpenFactCheck: A Unified Framework for Factuality Evaluation of LLMs](https://arxiv.org/abs/2405.05583) — OpenFactCheck findings from prerequisite item `2026-05-06-openfactcheck-ai-fact-checking-pipeline`
- [ ] [Min et al. (2023) FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) — FActScore findings from prerequisite item `2026-05-06-factscore-precision-scoring-atomic-claims`
- [ ] [Inan et al. (2023) Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) — policy enforcement architecture findings from prerequisite item `2026-05-06-gpt-oss-safeguard-policy-enforcement-open-weight`
- [ ] [Sharma et al. (2023) Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) — Barnum/sycophancy findings from prerequisite item `2026-05-06-barnum-statements-ai-responses-theory-practice`
- [ ] [Augenstein et al. (2023) Factuality Challenges in the Era of Large Language Models and Opportunities for Fact-Checking](https://arxiv.org/abs/2310.05189) — survey contextualising all five tool categories within the broader LLM factuality landscape

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
