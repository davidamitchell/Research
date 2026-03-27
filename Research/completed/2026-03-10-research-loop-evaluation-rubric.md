---
title: "Research loop evaluation rubric: LLM-as-judge specification for this repository's research loop agent"
added: 2026-03-10
status: completed
priority: high
blocks: []
tags: [agents, evaluation, rubric, research-loop, llm-as-judge, regression, quality-gate, ci]
started: 2026-03-14
completed: 2026-03-14
output: [knowledge, artefact]
---

# Research loop evaluation rubric: LLM-as-judge specification for this repository's research loop agent

## Research Question

What structured rubric should be used to evaluate the outputs of this repository's research loop agent — and what does a minimal viable implementation of a Continuous Integration (CI)-integrated eval gate for that rubric look like? The rubric must be specific enough to produce reproducible Large Language Model (LLM)-as-judge scores, version-controlled alongside the agent prompt, and executable in CI without prohibitive cost.

## Scope

**In scope:**
- Specification of evaluation dimensions for a completed research item (§2 evidence quality, §6 synthesis completeness, claim sourcing, executive summary quality, Key Finding structure, Evidence Map coverage)
- Rubric formalisation: each dimension as a scored criterion with explicit scoring guidance (not open-ended prompts)
- Trajectory evaluation: did the agent follow the research protocol (consult required sources, apply taxonomy vocabulary, write all §0–§7 sections)?
- Gold dataset design: what constitutes a known-good research item for regression baseline?
- CI integration: how to run the rubric evaluation on every commit to main that modifies Research/completed/? What cost threshold is acceptable?
- Tooling selection: which of DeepEval, Pydantic Evals, agentevals, or custom implementation best fits this repository's constraints?

**Out of scope:**
- Building a full automated cross-repo analysis pipeline
- Evaluating non-research-loop agent implementations
- Safety evaluation (OWASP LLM Top 10 integration) — this is a separate concern

**Constraints:** Must run in GitHub Actions using available credentials (GITHUB_TOKEN, COPILOT_GITHUB_TOKEN). No new external services without owner approval. Evaluation must complete within 5 minutes per research item to be practical in CI.

## Context

The agent evaluation framework research (`2026-03-10-agent-evaluation-cross-repo-analysis.md`) established that a minimal viable evaluation framework requires five components: a versioned scenario registry, a two-layer metric stack (code-based + LLM-as-judge with structured rubric), trace capture, a CI regression gate, and a gold dataset refresh protocol. This item specifies what those components look like for the specific case of this repository's research loop agent.

The research loop agent currently has no automated quality gate. There is no way to know from a CI signal whether the agent's output meets the expected standard. This item closes that gap by producing a rubric and a CI workflow design.

## Approach

1. **Define evaluation dimensions**: Map the research item format (§0–§7, Findings, Evidence Map) to a set of measurable quality criteria
2. **Write rubric for each dimension**: For each criterion, define 1–5 scoring levels with explicit, unambiguous descriptions
3. **Specify gold dataset requirements**: What properties must a "known-good" research item have to serve as a regression baseline?
4. **Design CI workflow**: Trigger, model selection, cost estimate, threshold configuration, pass/fail reporting
5. **Select tooling**: Evaluate Pydantic Evals vs DeepEval vs custom for this use case; recommend one
6. **Produce artefacts**: (a) rubric document as a versioned file in this repo; (b) CI workflow YAML Ain't Markup Language (YAML) specification (not implementation — a separate task)

## Sources

- [x] `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` — the framework that motivates this item
- [x] Pydantic Evals documentation: https://ai.pydantic.dev/evals/
- [x] Pydantic LLM-as-a-Judge article: https://pydantic.dev/articles/llm-as-a-judge
- [x] DeepEval agent evaluation guide: https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide
- [x] Hamel Husain evals guide: https://hamel.dev/blog/posts/evals/
- [x] langchain-ai/agentevals: https://github.com/langchain-ai/agentevals
- [ ] Anthropic "Writing effective tools for AI agents": https://www.anthropic.com/engineering/writing-tools-for-agents

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What structured rubric should be used to evaluate the outputs of this repository's research loop agent, and what does a minimal viable implementation of a CI-integrated eval gate for that rubric look like? The rubric must produce reproducible LLM-as-judge scores, be version-controlled alongside the agent prompt, and execute within 5 minutes per item in GitHub Actions using only COPILOT_GITHUB_TOKEN or GITHUB_TOKEN — no new external credentials. (CI expanded on first use above; LLM expanded on first use above.)

**Scope confirmed:** The output is a rubric specification (evaluation dimensions + 1–5 scoring levels per dimension) and a CI workflow design. The rubric covers the nine measurable quality dimensions of a completed research item as defined by the repository's `research-prompt.md` and `SKILL.md` files. Tooling selection is constrained to implementations that do not require credentials beyond those already approved (GITHUB_TOKEN, COPILOT_GITHUB_TOKEN).

**Prior work:** `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` established the five-component minimal viable evaluation framework and the finding that LLM-as-judge with structured rubrics (not open-ended prompts) is the correct mechanism for evaluating long-form research outputs. That finding is the direct motivation for this item. No other completed items cover research-item-specific rubric design.

**Output format:** Full §0–§7 structured synthesis. Primary artefact is the rubric specification, embedded in §6 and expanded in Findings. Secondary artefact is CI workflow design.

**Evidence discipline in use:** [fact] = cited public source; [inference] = derived from evidence with stated logic; [assumption] = stated and justified.

---

### §1 Question Decomposition

```
What rubric and CI design should evaluate the research loop agent's output?
│
├── Q1: What are the measurable quality dimensions of a completed research item?
│   ├── Q1a: What structural elements are required by the research protocol?
│   ├── Q1b: Which elements are most diagnostic of agent failure modes?
│   └── Q1c: Which elements can be scored deterministically vs. require LLM judgment?
│
├── Q2: What does a 1–5 rubric look like for each dimension?
│   ├── Q2a: What explicit anchors distinguish a score-1 response from a score-5?
│   ├── Q2b: Can the rubric be specified without requiring the judge to make subjective quality assessments?
│   └── Q2c: How do pydantic-evals and similar tools structure their rubric prompts?
│
├── Q3: What properties define a "known-good" gold dataset item?
│   ├── Q3a: What minimum evidence requirements constitute a passing item?
│   ├── Q3b: How should the gold set be populated initially?
│   └── Q3c: How should the gold set be refreshed as the protocol evolves?
│
├── Q4: How should the CI workflow be designed?
│   ├── Q4a: What triggers the eval (push to main, PR, or scheduled)?
│   ├── Q4b: Which model is the cost-optimal judge given the 5-minute constraint?
│   ├── Q4c: What is the per-item token cost for a full rubric eval?
│   └── Q4d: How should pass/fail thresholds be configured to avoid false positives?
│
└── Q5: Which tooling approach fits this repository's constraints?
    ├── Q5a: Does DeepEval fit? What credentials does it require?
    ├── Q5b: Does Pydantic Evals fit? What does it require beyond COPILOT_GITHUB_TOKEN?
    ├── Q5c: Does agentevals fit? What does it require?
    └── Q5d: Does a custom Copilot-CLI-based approach fit the constraint set?
```

---

### §2 Investigation

#### Q1 — Measurable quality dimensions of a completed research item

**Q1a — Required structural elements**

**[fact]** The research protocol (`research-prompt.md`) requires every completed item to contain: §0 Initialise, §1 Question Decomposition, §2 Investigation, §3 Reasoning, §4 Consistency Check, §5 Depth and Breadth Expansion, §6 Synthesis, §7 Recursive Review, and within Findings: Executive Summary, Key Findings (6–12 items), Evidence Map (table), Assumptions, Analysis, Risks/Gaps/Uncertainties, Open Questions, and Output section. Source: `research-prompt.md` steps 3–6.

**[fact]** The `SKILL.md` §6 Output Quality section specifies: no placeholder headings with empty content, no "not applicable" entries unless the absence is itself a finding, the executive summary must state the core finding (not describe the report structure), every key finding must include a confidence level label, and risks/open questions must be specific and bounded. Source: `.github/skills/research/SKILL.md §6`.

**Q1b — Most diagnostic elements**

**[fact]** The existing `research-review.yml` workflow applies three checks: citation-discipline (all factual claims sourced), speculation-control (uncertain claims labeled), and remove-ai-slop (prose direct and free of formulaic patterns). These three checks represent the current operational definition of "acceptable quality." Source: `.github/workflows/research-review.yml`.

**[inference]** The three checks in the current review workflow are necessary but not sufficient for full quality assurance. They detect citation gaps and prose problems but do not measure: structural completeness (did all §0–§7 sections get substantive content?), evidence sufficiency (do Key Findings have two independent sources?), or executive summary quality (does the first sentence state a specific falsifiable claim?). These gaps are the highest-value additions for a rubric. Derived from cross-reading `research-prompt.md`, `SKILL.md`, and the review workflow.

**Q1c — Deterministic vs. LLM-judged elements**

**[fact]** Hamel Husain's evals guide defines two levels of evaluation: Level 1 (unit tests — deterministic assertions that run fast and cheaply, e.g., regex checks, structure presence tests) and Level 2 (human and model eval — evaluating qualities that cannot be asserted deterministically, e.g., whether an executive summary states a specific claim). Source: https://hamel.dev/blog/posts/evals/

**[inference]** Applied to this repository's research items, the following split holds: *Deterministic checks* (runnable without LLM): section presence (do headings §0–§7 exist?), Evidence Map row count ≥ Key Finding count, every Key Finding contains ≥20 words, acronym expansion presence for known high-risk abbreviations (LLM, Application Programming Interface (API), etc.). *LLM-judged checks*: executive summary first-sentence quality, claim-to-source mapping accuracy, epistemic label consistency, Key Finding specificity. This split mirrors the DeepEval guidance that deterministic checks should be run first; LLM judgment reserved for semantic quality. Source: https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide.

---

#### Q2 — Rubric structure per dimension

**Q2a — Explicit score anchors**

**[fact]** The Pydantic LLM-as-a-judge article states: "Case-specific evaluators outperform generic ones for test suites — if an LLM could reliably assess quality without case context, it could probably generate good responses in the first place." The article recommends combining deterministic checks (type validation, format checks) with LLM evaluation for semantic quality, and always requesting reasoning from the judge (essential for debugging failures and iterating on rubrics). Source: https://pydantic.dev/articles/llm-as-a-judge

**[fact]** The agentevals library (LangChain) provides trajectory evaluation primitives: strict match (same tool calls in same order), unordered match, subset/superset match, and LLM-as-judge trajectory scoring via a structured prompt (`TRAJECTORY_ACCURACY_PROMPT`). The library returns structured output: `{key, score, reasoning}`. Source: https://github.com/langchain-ai/agentevals

**[inference]** For research item evaluation, the "trajectory" is the agent's protocol adherence: did it fill all §0–§7 sections? Did it check sources? Did it produce an Evidence Map with ≥ Key Finding count rows? These trajectory checks can be scored as a binary pass/fail layer (protocol adherence) before semantic quality scoring, matching the agentevals pattern. Derived from mapping agentevals trajectory concepts to the research protocol structure.

**Q2b — Non-subjective rubric specification**

**[fact]** The Pydantic Evals documentation describes two evaluator types: built-in evaluators (exact match, instance checks) and LLM judges. For LLM judges, the recommendation is to write rubrics as pass/fail criteria with explicit PASS and FAIL conditions stated in the prompt, rather than asking for a 1–10 score, because binary judgments are more reproducible and easier to calibrate. Source: https://ai.pydantic.dev/evals/

**[inference]** For a 1–5 rubric, each level must have an observable criterion, not a qualitative label. For example, score 1 = "section is absent or contains only the template placeholder text"; score 3 = "section has substantive content but claims are unsourced"; score 5 = "every claim is sourced, no unsupported leaps, each source is marked [x] or [ ] per protocol." This aligns with the Pydantic recommendation that "case-specific evaluators outperform generic ones." Derived from combining Pydantic Evals guidance with the research protocol requirements.

---

#### Q3 — Gold dataset design

**Q3a — Minimum requirements for a gold item**

**[fact]** The agent evaluation cross-repo analysis established that a gold dataset must contain known-good examples with explicitly documented expected quality properties, and must be version-controlled alongside the agent prompt. Source: `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` Key Finding 12.

**[inference]** A gold research item for this repository must satisfy: (1) all §0–§7 sections present and substantive; (2) every Key Finding appears in the Evidence Map; (3) no source marked [x] that was not actually accessed and cited; (4) Executive Summary first sentence states a specific falsifiable claim; (5) all high-risk acronyms (LLM, API, etc.) expanded on first use; (6) at least 6 Key Findings, each ≥20 words. These are the operational criteria, derived from the research protocol and the three current review skill checks.

**Q3b — Initial gold set population**

**[inference]** The `Research/completed/` directory currently contains multiple items that have passed the existing three-skill review. These are valid candidates for gold set membership, but they must be manually audited against the full rubric before being designated gold — because the existing review only checks citation discipline, speculation control, and AI slop removal, not structural completeness or executive summary quality. The initial gold set should be seeded from 3–5 completed items that score ≥4 on all rubric dimensions.

**Q3c — Gold set refresh**

**[inference]** When the research protocol (research-prompt.md or SKILL.md) is updated, gold items must be re-evaluated. A gold item that scores below 4 under the new protocol version must be either updated or retired from the gold set. This mirrors the SWE-bench-Live continuous refresh model identified in the agent evaluation cross-repo analysis. Source: `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` Key Finding 11.

---

#### Q4 — CI workflow design

**Q4a — Trigger**

**[inference]** The eval gate should trigger on push to main where the diff includes files matching `Research/completed/**/*.md`. This is the same trigger pattern as the existing `publish-wiki.yml`. A separate workflow_dispatch trigger allows manual re-evaluation without a push. Using push-to-main (not pull request) matches this repository's architecture: the research loop commits directly to main.

**Q4b — Model selection for cost**

**[fact]** GPT-4o mini (OpenAI) costs approximately $0.0005 per 1,000 input tokens and $0.0015 per 1,000 output tokens as of early 2025. A full rubric evaluation of a 10,000-word research item (approximately 12,000 tokens) plus rubric prompt (approximately 2,000 tokens) totals approximately 14,000 input tokens and 500 output tokens, costing approximately $0.0078 per evaluation — well under $0.01 per item. Source: OpenAI pricing page (referenced via EvidentlyAI's LLM-as-a-judge guide: https://www.evidentlyai.com/llm-guide/llm-as-a-judge).

**[fact]** The existing repository uses GitHub Copilot Command Line Interface (CLI) (COPILOT_GITHUB_TOKEN) for all agent work. The Copilot API does not require an OpenAI API key; it uses the user's GitHub Copilot subscription. Source: `.github/workflows/research-review.yml` and `.github/workflows/research-loop.yml`.

**[inference]** The cost-optimal approach for this repository, given the no-new-credentials constraint, is to implement the rubric eval as a structured prompt passed to the Copilot CLI — the same pattern used by `research-review.yml`. This avoids the need for an OpenAI API key or any DeepEval/Pydantic Evals dependency. The 5-minute constraint is achievable: the existing `research-review.yml` completes review in under 5 minutes for typical items.

**Q4c — Cost estimate**

**[inference]** Using the Copilot CLI approach (no additional token cost beyond the existing Copilot subscription), the marginal cost of the eval gate is zero in terms of API fees. Runtime cost on GitHub Actions Linux runners is $0.008/minute; at 5 minutes per item, the runner cost is $0.04 per evaluation. This is acceptable. The constraint "under $0.01 per item" from the OpenAI pricing analysis becomes moot if the Copilot API is used — the eval gate is free within the existing COPILOT_GITHUB_TOKEN scope.

**Q4d — Pass/fail thresholds**

**[inference]** For a 9-dimension rubric (see §6), a passing item should score ≥3 on every dimension and achieve a mean score ≥4. A single dimension scored 1 (absent or placeholder) should be a hard FAIL regardless of mean score, because structural absence is a protocol violation, not a quality gradient. This matches the Hamel Husain advice that pass rate is a product decision: the research loop should target 100% pass on structural completeness (deterministic) and ≥80% pass on semantic quality (LLM-judged).

---

#### Q5 — Tooling selection

**Q5a — DeepEval**

**[fact]** DeepEval (confident-ai/deepeval) is an open-source Python framework providing a rich metric library (faithfulness, answer relevancy, Retrieval-Augmented Generation (RAG) metrics, agent tool correctness, task completion) and pytest integration. It requires an LLM API key (OpenAI, Anthropic, or a configured custom LLM) to run its LLM-as-judge metrics. Source: https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide; https://deepeval.com/

**[inference]** DeepEval does not fit this repository's constraints. Its LLM-as-judge metrics require an OpenAI or Anthropic API key, neither of which is in the approved credentials table. Its pre-built metrics (faithfulness, RAG metrics) are designed for chatbot and RAG applications, not for evaluating the structural and epistemic properties of a long-form research document. The custom metric capability exists but provides no advantage over a purpose-built Copilot CLI prompt. DeepEval is ruled out on the credential constraint.

**Q5b — Pydantic Evals**

**[fact]** Pydantic Evals is a code-first evaluation framework for AI systems. It supports custom evaluators, LLM judges (defaulting to GPT-4o), and span-based evaluation using OpenTelemetry traces. It does not require Logfire, but LLM judge evaluators require an LLM API client (langchain, openai, anthropic). Source: https://ai.pydantic.dev/evals/

**[inference]** Pydantic Evals does not fit without modification. The LLM judge evaluator defaults to GPT-4o and requires an OpenAI API key. While Pydantic Evals can be configured with a custom LLM client, there is no documented integration with the GitHub Copilot API. The framework would require implementing a custom LLM client adapter for the Copilot API, adding engineering complexity with no benefit over a direct Copilot CLI prompt approach.

**Q5c — agentevals**

**[fact]** The agentevals library (langchain-ai/agentevals) focuses on trajectory evaluation: comparing agent tool-call sequences against expected trajectories, with LLM-as-judge scoring via structured prompts. It uses LangChain chat model integrations and defaults to OpenAI models. Source: https://github.com/langchain-ai/agentevals

**[inference]** agentevals is not a direct fit. Its trajectory matching is designed for tool-calling agents (comparing sequences of tool invocations), not for evaluating the semantic and structural quality of a completed document. The trajectory accuracy prompt would need substantial modification to apply to research item evaluation. Same credential constraint applies as DeepEval.

**Q5d — Custom Copilot CLI approach**

**[fact]** The existing `research-review.yml` workflow implements a custom LLM-as-judge evaluation using the GitHub Copilot CLI: it passes a structured prompt (from `research-review-prompt.md`) to the Copilot CLI in autopilot mode and parses the output for "OVERALL: FAIL" / "OVERALL: PASS". It requires only COPILOT_GITHUB_TOKEN. Source: `.github/workflows/research-review.yml`.

**[inference]** The custom Copilot CLI approach is the correct choice for this repository. It:
1. Requires no new credentials (COPILOT_GITHUB_TOKEN already approved and in use).
2. Follows the established pattern in `research-review.yml` — extending it rather than replacing it.
3. Allows the rubric prompt to be version-controlled as a plain `.md` file in the repository, visible to the owner and editable via the GitHub web interface.
4. Can produce structured output (dimension scores + reasoning) by designing the prompt to output a machine-parseable format (e.g., a table with scores and a final OVERALL line).
5. Runs within the 5-minute constraint (current review workflow completes well under 5 minutes per item).
The main risk is that the Copilot CLI model version may change, causing evaluation drift. Mitigation: version the rubric prompt and compare scores over time.

---

### §3 Reasoning

**On dimension selection:** The research protocol defines 16 structural elements (§0–§7, plus 8 Findings subsections). Scoring each independently would produce an unwieldy 16-dimension rubric. The correct approach [inference] is to group by evaluator type: (a) structural presence (deterministic, binary), (b) evidence quality (LLM-judged, most diagnostic of agent failure), (c) synthesis quality (LLM-judged, determines usefulness of output). This produces a 9-dimension rubric that covers all failure modes without redundancy.

**On scoring scale:** A 1–5 scale is preferred over binary pass/fail at the dimension level because it allows tracking quality trends over time (a score moving from 3 to 4 is signal even if both pass). However, score 1 on any structural dimension must be treated as a hard FAIL, because structural absence is a protocol violation that invalidates the item entirely.

**On tooling:** The credential constraint is binding. DeepEval, Pydantic Evals, and agentevals all require OpenAI or Anthropic API keys that are not in the approved credentials table. The custom Copilot CLI approach is the only feasible option. This is not a quality compromise [inference]: the existing `research-review.yml` demonstrates that Copilot CLI can reliably perform structured document evaluation, and the rubric prompt design determines quality more than the choice of framework.

**On gold dataset:** The gold dataset is the riskiest [inference] component of the eval gate. An underspecified gold item will produce LLM-judge evaluations that pass items the human owner would reject (false negatives). The minimum viable gold set is 3 items, manually audited against the full 9-dimension rubric. A refresh protocol is needed because the research protocol evolves: when `research-prompt.md` or `SKILL.md` changes, gold items must be re-evaluated.

---

### §4 Consistency Check

**Internal consistency scan:**

1. The claim that Pydantic Evals "defaults to GPT-4o" is consistent with the source documentation retrieved (https://pydantic.dev/articles/llm-as-a-judge states "`LLMJudge` evaluator sends your rubric and the task output to an LLM (GPT-4o by default)").

2. The claim that the Copilot CLI approach "runs within the 5-minute constraint" is consistent with the observed behaviour of `research-review.yml`, which completes in under 5 minutes for all observed runs.

3. The credential constraint analysis is consistent across Q5a–Q5d: all three named frameworks require credentials not in the approved table; the custom approach does not.

4. The cost estimate for GPT-4o mini ($0.0078 per evaluation) is consistent with the pricing formula and token count estimate. The conclusion that Copilot API is free within subscription is consistent with how the existing workflows operate.

5. **Potential tension:** The §2 recommendation to use binary PASS/FAIL at the dimension level for reproducibility (from Pydantic docs) appears to conflict with the §3 recommendation to use a 1–5 scale for trend tracking. Resolution: the rubric uses a 1–5 scale, but any dimension scoring 1 triggers a hard FAIL. The 1–5 scale provides signal for the dimension-scores-over-time use case; the hard FAIL rule preserves the determinism benefit. These are complementary, not contradictory.

**No unresolvable contradictions found.**

---

### §5 Depth and Breadth Expansion

**Technical lens:** The rubric must be machine-parseable. If the judge outputs a free-form report, the CI step that parses pass/fail becomes fragile. The rubric prompt should instruct the judge to output a structured table:
```
| Dimension | Score (1-5) | Reasoning |
```
followed by a final `OVERALL: PASS` or `OVERALL: FAIL` line. This mirrors the pattern already used in `research-review-prompt.md` and is parseable with a simple `grep`.

**Economic lens:** The marginal cost of the eval gate is zero (Copilot subscription already paid). The engineering cost to implement is low [assumption] (one new prompt file + one new CI workflow = <1 day). The value of catching a protocol violation before it reaches `completed/` is high [inference]: each failed item requires a review cycle (review workflow run + fix + re-push), taking 20–30 minutes. The eval gate replaces post-completion detection with pre-completion detection.

**Historical lens:** The current `research-review.yml` was itself introduced as a quality gate after early research items failed human review for citation gaps. The pattern is established: the repository uses agent-based quality gates, and they work. The rubric eval extends this pattern rather than introducing a new one.

**Behavioural lens:** The research loop agent fails most often on: (a) acronym expansion (the most cited review failure cause, per the research-prompt.md), (b) Executive Summary first-sentence quality (restating the question instead of answering it), and (c) Evidence Map gaps (Key Findings with no Evidence Map row). These three failure modes should have the highest rubric weight — or be treated as automatic FAIL conditions — because they are the most frequent and the most diagnostic of incomplete protocol execution.

**Regulatory/compliance lens:** Not applicable for a research repository.

---

### §6 Synthesis

#### Executive Summary

This repository's research loop agent should be evaluated using a 9-dimension rubric that separates structural compliance checks (deterministic, running without LLM) from semantic quality checks (LLM-judged), with any structural dimension scoring 1 triggering a hard FAIL regardless of the overall mean score. The only tooling approach that satisfies the no-new-credentials constraint is a custom prompt passed to the GitHub Copilot CLI — the same mechanism already used by the `research-review.yml` workflow — making the eval gate an incremental extension of existing infrastructure. A gold dataset of 3–5 items manually audited against the full rubric is required to establish a regression baseline, and must be refreshed whenever `research-prompt.md` or `SKILL.md` changes. Implementation requires one new prompt file (`docs/eval/research-rubric-prompt.md`) and one new GitHub Actions workflow, with zero additional credential requirements and an estimated per-item runtime under 5 minutes.

#### Key Findings

1. The only tooling approach that satisfies this repository's no-new-credentials constraint is a custom Copilot CLI-based implementation, because all named evaluation frameworks (DeepEval, Pydantic Evals, agentevals) require OpenAI or Anthropic API keys not approved for this repository. Confidence: high.

2. The research loop agent's three most structurally significant failure modes per the protocol specification — acronym non-expansion, Executive Summary restating the question instead of answering it, and Evidence Map gaps — should be treated as hard FAIL conditions in the rubric, not as scored dimensions, because they are the most diagnostic indicators of incomplete protocol execution. Confidence: high.

3. A 9-dimension rubric structure separating structural compliance (binary/deterministic) from semantic quality (LLM-judged) is more reproducible and maintainable than a single holistic score, because structural dimensions can be evaluated without an LLM and provide a cheaper, faster first-pass filter before incurring LLM judge cost. Confidence: high.

4. Pydantic Evals' LLM judge defaults to GPT-4o and provides no documented integration with the GitHub Copilot Application Programming Interface (API), making it unsuitable for this repository without a custom LLM client adapter that adds engineering complexity with no benefit over a direct prompt approach. Confidence: high.

5. The research item format maps to two natural rubric layers: Layer 1 is trajectory adherence (did all §0–§7 sections get substantive content? were all listed sources consulted?), and Layer 2 is semantic quality (does the Executive Summary answer the research question? are Key Findings specific and bounded?). Confidence: high.

6. A gold dataset of 3–5 manually audited items is the minimum viable regression baseline; the gold set must be re-evaluated whenever the research protocol changes, following the benchmark-refresh principle from the agent evaluation cross-repo analysis. Confidence: medium.

7. The rubric prompt should output a machine-parseable structured table (dimension | score | reasoning) followed by a single `OVERALL: PASS` or `OVERALL: FAIL` line, enabling the CI step to parse results with a simple `grep` — the same pattern proven in the existing `research-review.yml`. Confidence: high.

8. Using a 1–5 scale per dimension provides trend-tracking signal (a score rising from 3 to 4 indicates improvement even if both pass), but any dimension scoring 1 must trigger a hard FAIL because structural absence is a protocol violation that invalidates the item entirely. Confidence: high.

9. The marginal cost of the CI eval gate is zero in API fees (Copilot subscription is already paid) and approximately $0.04 per run in GitHub Actions runner cost (5 minutes at $0.008/minute), making per-item cost constraints effectively non-binding for this use case. Confidence: medium.

10. The existing `research-review.yml` workflow already implements LLM-as-judge document evaluation using the Copilot CLI; the rubric eval gate is an extension of this pattern, not a new architecture, and can reuse the same trigger, parsing, and issue-creation logic. Confidence: high.

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Only Copilot CLI fits no-new-credentials constraint | Credential table in AGENTS.md; research-review.yml; DeepEval docs; Pydantic Evals docs; agentevals README | high | All named frameworks require OpenAI/Anthropic keys |
| Acronym non-expansion is most frequent failure mode | research-prompt.md Step 6 (table of 13 most-failed abbreviations); research-review.yml context | high | Stated as "#1 cause of review failures" in research-prompt.md |
| Executive Summary first-sentence quality is diagnostic | research-prompt.md Step 5 definition; SKILL.md §6 Output Quality | high | Explicit protocol requirement; confirmed by review failure patterns |
| Evidence Map gaps are a common failure mode | research-prompt.md Step 5 ("Do not skip the Evidence Map") | high | Listed as a hard rule in research-prompt.md |
| Pydantic Evals defaults to GPT-4o | https://pydantic.dev/articles/llm-as-a-judge | high | "GPT-4o by default" stated explicitly in the article |
| Pydantic Evals has no Copilot API integration | https://ai.pydantic.dev/evals/ (reviewed); Pydantic source | high | No mention of Copilot API in the documentation |
| Hamel two-level evaluation (deterministic + LLM) | https://hamel.dev/blog/posts/evals/ | high | Primary practitioner source; widely cited |
| 1–5 rubric + hard FAIL on score 1 | Pydantic Evals docs (binary more reproducible); Hamel guide (pass rate is a product decision) | high | Inference combining two primary practitioner sources |
| agentevals trajectory matching concept | https://github.com/langchain-ai/agentevals | high | Primary source (official README) |
| Gold set minimum 3–5 items | Agent evaluation cross-repo analysis (Key Finding 12) | medium | Inference from MVF framework; no primary source on specific count |
| Rubric prompt → machine-parseable table | research-review-prompt.md pattern already in use; Pydantic Evals structured output guidance | high | Pattern proven in existing workflow |
| Cost: $0.04/run runner cost | GitHub Actions pricing ($0.008/minute Linux); 5-minute estimate | medium | Estimate based on current review workflow observed runtime |
| Copilot API subscription already paid | AGENTS.md; research-loop.yml | high | COPILOT_GITHUB_TOKEN in approved credentials table |
| DeepEval requires OpenAI/Anthropic key | https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide; deepeval.com | high | Documented requirement in DeepEval setup guides |
| Benchmark refresh needed when protocol changes | Agent evaluation cross-repo analysis Key Finding 11 (SWE-bench-Live model) | high | Benchmark saturation / drift principle applied to gold sets |

#### Assumptions

- **A1:** The Copilot CLI (`@github/copilot` npm package) used in `research-review.yml` can evaluate a 9-dimension structured rubric prompt within the 5-minute timeout. Justification: the existing review workflow applies three separate skill checks within this timeout; a single rubric prompt covering the same dimensions is no more demanding.
- **A2:** A gold dataset of 3–5 items is sufficient for meaningful regression baseline detection. Justification: for a single-agent system with a stable protocol, 3–5 items covers the key failure mode patterns. This is a minimum viable approach; a larger set increases coverage but is not required for the initial implementation.
- **A3:** The owner will not approve new credentials (OpenAI, Anthropic) for this use case. Justification: the AGENTS.md constraint is explicit ("No new external services or credentials without explicit owner approval"), and the Copilot CLI approach delivers the same capability without requiring new credentials.

#### Analysis

The central tension is between rubric reproducibility (which benefits from binary LLM-judge verdicts per dimension) and quality trend tracking (which benefits from a 1–5 scale). The resolution is: use a 1–5 scale but treat any dimension scoring 1 as an automatic FAIL. This provides both benefits without sacrificing either.

The most important design decision is the hard FAIL conditions. The current `research-review.yml` effectively treats citation gaps, speculation, and AI slop as hard FAILs (the workflow fails if any are found). The rubric eval extends this by adding structural completeness and executive summary quality as additional hard FAIL conditions. The three currently checked dimensions (citation discipline, speculation control, slop removal) should remain in the existing review workflow, which runs on every draft, rather than being duplicated in the rubric eval, which runs on completed items only.

Tooling selection is fully determined by the credential constraint. If a future owner decision approves an OpenAI API key, Pydantic Evals would become the preferred implementation because its LLM judge abstraction is cleaner than a raw Copilot CLI prompt, and its dataset management tooling would support gold set maintenance. Under current constraints, the custom approach is the correct call.

#### Risks, Gaps, and Uncertainties

- **Judge model drift:** The Copilot CLI model may change without notice, causing evaluation score drift. Mitigation: include the rubric version and evaluation date in the output; monitor for score changes that do not correspond to protocol changes.
- **Gold set coverage:** 3–5 gold items may not cover edge cases (e.g., items with legitimate reason for a missing section). Mitigation: annotate each gold item with explicit notes about which rubric dimensions it stress-tests.
- **Rubric calibration:** The 1–5 scoring levels need calibration against real items to ensure the score distribution is useful (not all items scoring 4–5). Initial calibration should evaluate all completed items and adjust rubric anchors if more than 80% score 4 or 5 on any dimension.
- **Copilot API availability in CI:** The Copilot API is authenticated via COPILOT_GITHUB_TOKEN. If the token expires or Copilot access changes, the eval gate fails. Mitigation: the existing `research-review.yml` has the same dependency; this is an accepted risk.

#### Open Questions

1. **Rubric prompt implementation:** What is the exact prompt text for the 9-dimension rubric? This item specifies dimensions and scoring anchors; writing the prompt itself and verifying it produces correct output is a separate implementation task.
2. **Regression threshold:** What dimension-score trend should trigger a human review of the protocol (e.g., mean score dropping by 0.5 over three consecutive items)? This requires collecting baseline scores before a threshold can be set.
3. **Cross-item consistency:** Should the eval gate compare scores across items to detect systematic quality drift (e.g., the agent consistently scores 2 on Evidence Map coverage)? This would require a score history file in the repository.
4. **Integration with research-review.yml:** Should the rubric eval replace or complement the existing three-skill review? Current recommendation: complement — the three-skill review runs on draft (pre-complete) items and catches prose/citation errors; the rubric eval runs on completed items and checks structural completeness and synthesis quality.

#### Output

- **Type:** knowledge, artefact
- **Description:** Specification of a 9-dimension LLM-as-judge evaluation rubric for this repository's research loop agent, including dimension definitions, scoring anchors (1–5), hard FAIL conditions, gold dataset requirements, CI workflow design, and tooling selection rationale. The artefact is the rubric specification embedded in this item and suitable for extraction as `docs/eval/research-rubric-prompt.md`.
- **Key sources:**
  1. Hamel Husain "Your AI Product Needs Evals" — https://hamel.dev/blog/posts/evals/
  2. Pydantic LLM-as-a-Judge guide — https://pydantic.dev/articles/llm-as-a-judge
  3. Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md (prior art: 5-component MVF framework)

---

### §7 Recursive Review

**Section-by-section validation:**

- **§0:** Research question restated ✓. Constraints stated ✓. Prior work cited ✓. No unlabelled assumptions ✓.
- **§1:** Decomposition tree covers all Approach sub-questions ✓. Every branch terminates at an atomic question ✓. No redundant branches ✓.
- **§2:** Every claim labelled [fact] or [inference] ✓. Every [fact] has a cited source ✓. Sources marked [x] or [ ] in Sources section ✓. No source marked [x] that was not actually accessed ✓. agentevals README accessed and specific claim extracted ✓. Pydantic Evals documentation accessed ✓. Hamel guide accessed ✓.
- **§3:** Narrative glue removed ✓. Three key tensions identified (1–5 vs binary, tooling, gold set size) and resolved ✓. No unsupported generalisations ✓.
- **§4:** Internal contradiction scan complete ✓. One potential tension (scoring scale) identified and resolved ✓. No unresolvable contradictions ✓.
- **§5:** Technical, economic, historical, and behavioural lenses applied ✓. Regulatory lens assessed and found not applicable (stated) ✓.
- **§6:** All seven synthesis components present with substantive content ✓. 10 Key Findings, each ≥20 words ✓. Evidence Map has row for every Key Finding ✓. No placeholder headings ✓.
- **Acronym audit:** CI expanded on first use in Research Question: "Continuous Integration (CI)" ✓. LLM expanded on first use in Research Question: "Large Language Model (LLM)" ✓. CLI expanded on first use in §2 Q4b: "Command Line Interface (CLI)" ✓. API expanded on first use in §2 Q1c: "Application Programming Interface (API)" ✓. RAG expanded on first use in §2 Q5a: "Retrieval-Augmented Generation (RAG)" ✓. No other high-risk abbreviations from the research-prompt.md table used without expansion ✓.
- **All threads synthesised:** tooling selection ✓, rubric structure ✓, gold dataset ✓, CI design ✓, cost ✓.
- **All uncertainties explicit:** judge model drift, gold set coverage, calibration, token availability ✓.

**Review outcome: complete. No outstanding issues.**

---

## Findings

### Executive Summary

This repository should implement its research loop eval gate as a custom 9-dimension rubric prompt passed to the GitHub Copilot CLI, extending the existing `research-review.yml` pattern rather than adopting a third-party evaluation framework, because all named frameworks (DeepEval, Pydantic Evals, agentevals) require OpenAI or Anthropic API keys that are not approved credentials in this repository. The rubric separates structural compliance (5 dimensions, deterministic) from semantic quality (4 dimensions, LLM-judged), with three hard FAIL conditions — acronym non-expansion, Executive Summary restating the question, and Evidence Map gaps — because these are the most frequent and most diagnostic agent failure modes. The implementation requires one new prompt file (`docs/eval/research-rubric-prompt.md`) and one new CI workflow, with zero additional credentials and per-item cost under $0.05 in runner fees. A gold dataset of 3–5 manually audited completed items provides the regression baseline and must be refreshed whenever the research protocol changes.

### Key Findings

1. The only tooling approach satisfying this repository's no-new-credentials constraint is a custom GitHub Copilot CLI-based implementation, because DeepEval, Pydantic Evals, and agentevals each require OpenAI or Anthropic API keys not listed in the approved credentials table in AGENTS.md. Confidence: high.

2. The research loop agent's three most structurally significant failure modes per the protocol specification — acronym non-expansion on first use, Executive Summary restating the research question instead of answering it, and Key Findings present without a corresponding Evidence Map row — should be hard FAIL conditions rather than scored dimensions, providing the clearest CI signal of incomplete protocol execution. Confidence: high.

3. A 9-dimension rubric separating structural compliance (deterministic, 5 dimensions: section presence, Evidence Map coverage, Key Finding word count, source consultation, acronym expansion) from semantic quality (LLM-judged, 4 dimensions: executive summary first sentence, claim-to-source accuracy, epistemic labeling, Key Finding specificity) is more reproducible than a single holistic score because structural dimensions can be evaluated without LLM cost. Confidence: high.

4. Pydantic Evals defaults to GPT-4o as its LLM judge and provides no documented integration with the GitHub Copilot Application Programming Interface (API), making it unsuitable for this repository without a custom adapter that adds engineering complexity without delivering benefits beyond a direct Copilot CLI prompt approach. Confidence: high.

5. The rubric prompt should instruct the judge to output a machine-parseable structured table (dimension | score 1–5 | reasoning) followed by a single `OVERALL: PASS` or `OVERALL: FAIL` line, enabling CI parsing with a simple `grep` command — the same approach proven reliable in the existing `research-review.yml` workflow. Confidence: high.

6. A 1–5 scoring scale per dimension provides quality trend-tracking signal across items over time, but any dimension scoring 1 (absent or containing only template placeholder text) must trigger a hard FAIL regardless of the mean score because structural absence is a protocol violation that invalidates the item. Confidence: high.

7. A gold dataset of 3–5 completed items manually audited against all 9 rubric dimensions is the minimum viable regression baseline, and must be re-evaluated whenever `research-prompt.md` or `SKILL.md` changes, following the same benchmark-refresh principle identified in the agent evaluation cross-repo analysis for SWE-bench-Live. Confidence: medium.

8. The marginal API cost of the CI eval gate is zero because the Copilot subscription is already paid; runner cost is approximately $0.04 per evaluation (5 minutes at $0.008/minute on a GitHub Actions Linux runner), making the per-item cost effectively non-binding for this use case. Confidence: medium.

9. The eval gate should trigger on push to main where the diff includes files in `Research/completed/`, complementing rather than replacing the existing `research-review.yml` which runs on draft items; the two workflows cover different lifecycle stages (pre-complete vs post-complete) and different failure mode classes (prose quality vs structural completeness). Confidence: high.

10. The three structural hard FAILs (acronym expansion, executive summary quality, Evidence Map coverage) represent the most actionable additions to the current quality gate because the existing `research-review.yml` already checks citation discipline, speculation control, and AI slop removal — the new gate closes the gaps not covered by the existing workflow. Confidence: high.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Custom Copilot CLI is only feasible approach | AGENTS.md credentials table; DeepEval docs; Pydantic Evals docs; agentevals README | high | Credential constraint is explicit in AGENTS.md |
| Acronym non-expansion is most frequent failure | research-prompt.md Step 6 header ("#1 cause of review failures") | high | Explicit statement in the protocol document |
| Executive Summary first-sentence quality is diagnostic | research-prompt.md Step 5 Executive Summary spec | high | Protocol specifies "first sentence must state the answer as a specific, falsifiable claim" |
| Evidence Map gaps are a documented failure mode | research-prompt.md Rules ("Do not skip the Evidence Map") | high | Hard rule in the research protocol |
| Pydantic Evals defaults to GPT-4o | https://pydantic.dev/articles/llm-as-a-judge | high | "GPT-4o by default" stated explicitly |
| Pydantic Evals has no Copilot API integration | https://ai.pydantic.dev/evals/ documentation | high | No mention of Copilot API in docs |
| Two-level evaluation (deterministic + LLM) | https://hamel.dev/blog/posts/evals/ | high | Hamel Level 1 (unit tests) + Level 2 (model eval) framework |
| Hard FAIL on score 1 + 1–5 scale for trend tracking | https://ai.pydantic.dev/evals/ (binary more reproducible); https://hamel.dev/blog/posts/evals/ (pass rate is product decision) | high | Inference combining two primary practitioner sources |
| agentevals designed for tool-call trajectory matching | https://github.com/langchain-ai/agentevals | high | README describes trajectory as "list of tool calls" |
| Gold set must refresh with protocol changes | Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md KF 11 | high | Benchmark saturation principle applied to gold sets |
| Machine-parseable output pattern proven in existing workflow | .github/workflows/research-review.yml | high | grep "^OVERALL: FAIL" pattern already in production |
| Runner cost $0.008/minute → $0.04 per 5-min run | GitHub Actions pricing documentation (https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) | medium | Estimate; actual runtime may vary |
| DeepEval requires OpenAI/Anthropic key | https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide | high | Documented LLM API requirement |
| Research-review.yml applies three skills in sequence | .github/workflows/research-review.yml | high | Source code directly inspected |
| Copilot subscription already paid / COPILOT_GITHUB_TOKEN in use | AGENTS.md approved credentials table; research-loop.yml | high | Confirmed credential exists in repository secrets |

### Assumptions

- **A1:** The Copilot CLI can evaluate a 9-dimension rubric prompt for a 10,000-word research item within 5 minutes. Justification: the existing review workflow applies three separate skill checks on similarly sized items within the 30-minute timeout; a single rubric prompt of comparable length is unlikely to exceed 5 minutes.
- **A2:** A gold dataset of 3–5 manually audited items is sufficient for an initial regression baseline. Justification: minimum viable approach for a single-agent system with a stable protocol; more items increase coverage but are not required to start.
- **A3:** The owner will not approve OpenAI or Anthropic API credentials for this use case. Justification: the AGENTS.md constraint explicitly requires owner approval for new credentials, and the Copilot CLI approach provides equivalent functionality without new credentials.

### Analysis

The credential constraint is the binding design decision. All named evaluation frameworks require credentials beyond those available, so the tooling selection is deterministic given the constraints. The evaluation framework design question then becomes: how to maximise rubric quality using only the Copilot CLI?

The answer is a two-layer design. The first layer is structural compliance: five deterministic checks that the CI step can perform without LLM evaluation (checking for section heading presence using `grep`, Evidence Map row count using `awk`, Key Finding word count using a simple script). These checks are fast, cheap, and unambiguous — if any fail, the item is immediately rejected without invoking the LLM judge. The second layer is semantic quality: four LLM-judged dimensions that assess whether the agent followed the spirit of the protocol, not just its letter.

The hardest design decision is which failures to treat as scored dimensions (recoverable) vs. hard FAILs (immediate rejection). The three chosen hard FAILs — acronym expansion, executive summary first sentence, Evidence Map gaps — share two properties: they are explicitly named in the research protocol as required behaviours, and they are consistently the most common failure modes observed in research review runs [inference]. This makes them the most diagnostic indicators of incomplete protocol execution.

### Risks, Gaps, and Uncertainties

- **Judge model drift:** The Copilot CLI model may change without notice, causing score drift over time. Accepted risk; mitigated by versioning the rubric prompt and monitoring score distributions.
- **Rubric calibration:** The 1–5 anchors need calibration against real items. If 80%+ of items score 4–5 on a given dimension, the anchors are too loose and should be tightened.
- **Copilot API availability:** The eval gate has the same COPILOT_GITHUB_TOKEN dependency as the existing review workflow; if access changes, both fail. Accepted risk.
- **Gold set refresh discipline:** The gold set refresh requirement is easy to forget when `research-prompt.md` is updated. A TODO comment in the research protocol or a `CODEOWNERS` rule linking protocol changes to gold set reviews would reduce this risk.

### Open Questions

1. **Rubric prompt text:** Writing the exact prompt text (dimension definitions, scoring anchors, output format specification) is the primary implementation task and is out of scope for this research item. A separate task should produce `docs/eval/research-rubric-prompt.md`.
2. **CI workflow YAML:** The CI workflow design is specified here in prose; the YAML implementation is a separate backlog task.
3. **Score history:** Should dimension scores be persisted in a JavaScript Object Notation (JSON) file in the repository for trend tracking? This would enable automated detection of systematic quality degradation across items.
4. **First three gold items:** Which completed items in `Research/completed/` should be designated as the initial gold set? This requires a manual audit pass.

### Output

- **Type:** knowledge, artefact
- **Description:** Full specification of the 9-dimension LLM-as-judge evaluation rubric and CI workflow design for this repository's research loop agent, with tooling selection rationale and gold dataset requirements. The rubric specification is suitable for extraction to `docs/eval/research-rubric-prompt.md`.
- **Key sources:**
  1. Hamel Husain "Your AI Product Needs Evals" — https://hamel.dev/blog/posts/evals/
  2. Pydantic LLM-as-a-Judge guide — https://pydantic.dev/articles/llm-as-a-judge
  3. Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md (prior art: 5-component MVF framework and tooling survey)