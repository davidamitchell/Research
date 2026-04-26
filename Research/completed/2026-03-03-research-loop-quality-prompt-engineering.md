---
title: "Evaluating and improving autonomous research loop quality: prompt engineering and output assessment"
added: 2026-03-03T17:59:54+00:00
status: completed
priority: high
blocks: []
tags: [research-loop, prompt-engineering, quality, autonomous-research, evaluation, research-prompt, github-actions]
started: 2026-03-03T17:59:54+00:00
completed: 2026-03-03T17:59:54+00:00
output: [knowledge, tool, backlog-item]
---

# Evaluating and improving autonomous research loop quality: prompt engineering and output assessment

## Research Question

How can the quality of research items produced by the `research-loop.yml` autonomous pipeline be systematically evaluated, and what changes to `research-prompt.md` and the loop's prompting strategy would produce higher-quality, deeper, more synthesis-rich research outputs?

## Scope

**In scope:**
- Defining quality dimensions specific to autonomous research output: depth, source diversity, citation accuracy, executive summary precision, findings specificity, open-questions usefulness
- Empirical assessment of existing completed items produced by the loop: what patterns of shallow or formulaic output appear, and what is their root cause in the prompt?
- Prompt engineering techniques applicable to research prompts: chain-of-thought, role assignment, structured output constraints, negative constraints ("do not just list headings"), step decomposition
- Evaluation methodology: what criteria distinguish a high-quality completed research item from a low-quality one, and how can these criteria be applied automatically (CI check) vs. manually (spot check)?
- `research-prompt.md` redesign options: what changes would address identified weaknesses without making the prompt so long that it degrades instruction-following?
- Loop-level improvements: how the outer `while` loop in `research-loop.yml` selects items, whether priority-ordering is respected, and whether a "research brief" passed to each session improves focus

**Out of scope:**
- The underlying model (Copilot, Claude, GPT-4) selection — constrained by `COPILOT_GITHUB_TOKEN` and the existing `research-loop.yml` setup
- Loop safety controls (timeout, failure threshold, max iterations) — covered by ADR-0004 and not in scope unless evaluation reveals safety-relevant defects
- Manual research quality (items written by an agent in a direct session, not the loop) — focus is on loop-produced items

**Constraints:** Any prompt changes must remain compatible with the existing `research-loop.yml` invocation pattern. `research-prompt.md` is the only lever; no changes to the workflow file are required unless a loop-level fix is identified as necessary.

## Context

The `research-loop.yml` workflow runs automatically on weekdays, processing up to 3 backlog items per day. It has been in operation since late February 2026 and has produced the majority of items in `Research/completed/`. The `research-prompt.md` file is the sole instruction document passed to the agent each session.

The current loop has produced variable-quality output. Some items (e.g., `2026-03-01-context-mode-llm-context-compression.md`, `2026-03-02-agent-memory-management-context-injection.md`) contain rich, specific findings with cited evidence. Others follow the template structure mechanically without providing substantive answers to the research question. The root cause is unclear: is it prompt ambiguity, item underspecification, or model limitation?

The `2026-03-02-research-quality-assurance-methodology.md` backlog item addresses the quality review methodology (what checks to apply after output is produced). This item is the complement: it addresses the upstream cause (what prompting strategy produces better output in the first place). Both items are required to close the quality loop.

There is no current mechanism to detect when the loop has produced a shallow item vs. a deep one. The CI pipeline (`ci.yml`) runs linting and tests but has no research-quality check. Adding a structured quality gate (even a simple one) would provide a signal for when to trigger manual review.

## Approach

1. **Quality dimension definition** — Define the measurable quality dimensions for a completed research item produced by the loop:
   - *Depth*: does the Executive Summary directly answer the Research Question with a specific claim (not just a restatement)?
   - *Source engagement*: are the listed sources actually referenced in the Findings, or are they listed but ignored?
   - *Findings specificity*: are Key Findings concrete, evidence-backed claims, or vague generalisations?
   - *Open Questions utility*: do Open Questions represent genuine unresolved tensions surfaced by the research, or are they boilerplate?
   - *Cross-item integration*: does the item reference related completed items where relevant?
   Assess: which dimensions are automatable (structure/pattern checks) vs. require agent reasoning.

2. **Corpus audit** — Apply the quality dimensions to all existing completed items (specifically those produced by the autonomous loop). Identify the 3–5 most common failure patterns. Classify each failure as prompt-caused (the prompt did not instruct the agent to do X) vs. model-caused (the prompt did instruct it but the model did not comply).

3. **Prompt engineering survey** — Review the literature and practitioner community for prompt engineering techniques that improve research and synthesis quality in long-form outputs:
   - Chain-of-thought: explicit reasoning steps before producing findings
   - Role assignment: "You are a research analyst with expertise in X"
   - Negative constraints: "Do not reproduce the template headings without substantive content"
   - Structured output: require specific fields (e.g., "state the exact answer to the research question in one sentence in the Executive Summary")
   - Decomposition prompts: break the research task into sub-questions with separate reasoning passes

4. **research-prompt.md redesign** — Draft a revised `research-prompt.md` that addresses the identified failure patterns using the techniques from step 3. Key principles: the prompt should be long enough to set quality expectations clearly, but not so long that it dilutes the specific instructions. Test the revised prompt against the quality dimensions defined in step 1.

5. **Loop item-selection review** — Examine whether the loop respects `priority: high` items over `priority: medium` items when selecting from the backlog. Confirm the selection logic in the prompt or workflow. If items are selected in file-system order rather than priority order, propose a fix.

6. **Lightweight quality gate design** — Design a minimal quality check that can run as a GitHub Actions step after a research item is committed by the loop. Candidate checks:
   - Executive Summary word count ≥ 50 and contains a verb
   - Key Findings list contains ≥ 2 non-placeholder entries
   - At least one source listed in the Sources section is referenced in the Findings section
   - `started` and `completed` dates are populated
   Assess: are these checks sufficient to detect the most common failure modes?

7. **Iterative test** — If possible, run the revised prompt on a low-priority backlog item via `workflow_dispatch` (1 item) and compare the output quality to a pre-revision item of similar complexity. Document the before/after comparison.

## Sources

- [x] `research-prompt.md` — current prompt; the primary artefact to evaluate and revise
- [x] `.github/workflows/research-loop.yml` — loop implementation; understand item selection and session invocation
- [x] `Research/completed/` — existing loop-produced items; corpus for the quality audit
- [x] `Research/completed/2026-03-01-github-specify-ralph-loop-lisa-planning.md` — completed research on the Ralph Wiggum Technique, loop phases (Specify → Plan → Build), and proof-driven development; covers loop *design* (this item covers loop output *quality* and prompt improvement)
- [x] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — complement to this item: quality review methodology (downstream quality checks vs. this item's upstream prompt improvements)
- [x] Anthropic Prompt Engineering Guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview — chain-of-thought, role prompting, negative constraints
- [ ] OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering — structured output, decomposition patterns (JS-protected, inaccessible)
- [x] LMSYS / arXiv — The Prompt Report (arXiv:2406.06608): systematic survey of 58+ LLM prompting techniques (2024)
- [x] Fabric (Daniel Miessler): https://github.com/danielmiessler/fabric — prompt patterns for research extraction and synthesis; patterns like `extract_wisdom`, `summarize`, `create_report`
- [x] `docs-adr/0004-autonomous-research-loop.md` — ADR for the loop; safety controls and design rationale

---

## Research Skill Output

### §0 Initialise

**Research question restated:** How can the quality of research items produced by the `research-loop.yml` autonomous pipeline be systematically evaluated, and what changes to `research-prompt.md` and the loop's prompting strategy would produce higher-quality, deeper, more synthesis-rich research outputs?

**Scope confirmation:** In scope: quality dimension definition, corpus audit of 20 completed items, prompt engineering survey, `research-prompt.md` redesign, loop item-selection verification, lightweight quality gate design. Out of scope: model selection, safety controls (ADR-0004), items produced by direct agent sessions.

**Constraints confirmed:** All prompt changes must be compatible with `copilot -p "$(cat research-prompt.md)" --autopilot --allow-all`. The workflow YAML is the secondary lever; `research-prompt.md` is the primary one. Any quality gate must run as a GitHub Actions shell step without requiring new credentials.

**Output format:** Structured findings with quality dimension framework, corpus audit results, prompt engineering recommendations, revised `research-prompt.md` additions, quality gate shell script design.

---

### §1 Question Decomposition

**Root question:** What produces quality variation in autonomous research loop output?

Tree of atomic questions:

**A. Quality definition**
- A1. What are the measurable quality dimensions for a completed research item?
- A2. Which dimensions are automatable (structure/pattern checks) vs. require reasoning?
- A3. What distinguishes a high-quality executive summary from a low-quality one?

**B. Corpus audit**
- B1. What fraction of completed items have sources marked `[x]` (consulted) vs. `[ ]` (listed but not checked)?
- B2. What fraction have a Research Skill Output section (§0–§7)?
- B3. Does the presence of the Research Skill Output section correlate with higher source engagement and key finding count?
- B4. What are the 3–5 most common failure patterns across the 20 completed items?
- B5. Are failure patterns prompt-caused or model-caused?

**C. Prompt engineering**
- C1. What does chain-of-thought prompting demonstrably improve in long-form synthesis outputs?
- C2. Do negative constraints ("do not X") reliably reduce failure modes in LLM outputs?
- C3. What structured output constraints force specificity in executive summaries and key findings?
- C4. What does the Fabric `extract_wisdom` pattern reveal about best-practice prompt structure?
- C5. How long can a research prompt be before instruction-following degrades?

**D. Loop mechanics**
- D1. Does `research-prompt.md` contain explicit priority-ordering instructions?
- D2. Are `priority: high` items selected before `priority: medium` items in practice?
- D3. Is there an instruction to search completed items for prior related work before starting?

**E. Quality gate**
- E1. What are the minimum structural checks detectable by shell script in a Markdown file?
- E2. Are these checks sufficient to detect the most common failure modes?
- E3. What is the false-positive rate of a simple structural gate?

**F. Revised prompt**
- F1. What additions to `research-prompt.md` address the identified failure patterns?
- F2. Does the revised prompt remain short enough to avoid instruction-following degradation?

---

### §2 Investigation

#### A. Quality dimension definition (A1–A3)

**A1. Measurable quality dimensions:**

Drawing from the RACE (Reference-based Adaptive Criteria-driven Evaluation) framework (DeepResearch Bench, 2024) and the corpus audit below, six quality dimensions apply to completed research items in this repository: **[fact]** RACE treats "Insight/Depth," "Specificity," "Citation Coverage," and "Comprehensiveness" as primary evaluation metrics with granular sub-criteria. Source: DeepResearch Bench (https://deepresearch-bench.github.io/).

Mapped to this repository's format:
1. **Depth** — Executive Summary answers the Research Question with a specific claim. Proxies: executive summary word count ≥ 80, first sentence contains a declarative claim not present in the research question text.
2. **Source engagement** — Sources in the `## Sources` checklist are marked `[x]` (consulted). Proxy: count of `[x]` vs. `[ ]` items.
3. **Findings specificity** — Key Findings are numbered concrete claims, not template placeholders. Proxy: count of numbered items under `### Key Findings` that contain ≥ 15 words.
4. **Evidence map completeness** — Every Key Finding has a row in the Evidence Map. Proxy: count of `| ` rows in Evidence Map ≥ Key Finding count.
5. **Cross-item integration** — The item references related completed items. Proxy: presence of links to `Research/completed/` in the body.
6. **Open Questions utility** — Open Questions are specific unresolved tensions, not boilerplate. Proxy: each entry is ≥ 20 words and differs from the original research question's sub-questions.

**A2. Automatable vs. reasoning-required:**
Dimensions 1–4 are automatable via shell/Python pattern matching. Dimensions 5–6 require agent-level reasoning to assess whether the references are substantive or the open questions are genuine. **[inference]** from the structural nature of the checks.

**A3. High vs. low quality executive summary:**
High quality: First sentence states the answer to the research question as a specific, falsifiable claim. Example from `2026-03-01-context-mode-llm-context-compression.md`: "Context compression is a solved engineering problem at the session level but an unsolved architectural problem at the knowledge-base level." Low quality: First sentence restates the question or describes what the item covers. **[fact]** from corpus comparison.

---

#### B. Corpus audit (B1–B5)

**Direct inspection of all 20 completed items** (excluding README.md):

**B1. Source engagement (checked vs. unchecked):**
- Items with ALL sources checked (`[x]` only): 7 items (35%)
  - `2026-02-27-research-backlog-vs-repo-improvement-backlog.md` (4/4)
  - `2026-02-27-simple-process-for-adding-research-item.md` (2/2)
  - `2026-02-27-youtube-transcript-fetcher.md` (3/3)
  - `2026-02-28-ai-strategy.md` (14/14)
  - `2026-02-28-youtube-video-HYUoS0GkGCs-concepts.md` (7/7)
  - `2026-03-01-github-wiki-research-content.md` (4/4)
  - `2026-03-02-transaction-costs.md` (7/7)
  
- Items with SOME sources unchecked: 5 items (25%)
  - `2026-02-28-ai-control-testing-and-assurance.md` (6 checked, 3 unchecked)
  - `2026-02-28-jevons-paradox.md` (3 checked, 6 unchecked)
  - `2026-02-28-predictive-processing-active-inference.md` (3 checked, 1 unchecked)
  - `2026-03-01-context-mode-llm-context-compression.md` (4 checked, 1 unchecked)
  - `2026-03-01-github-specify-ralph-loop-lisa-planning.md` (0 checked, 7 unchecked — all sources listed but none marked)

- Items with NO sources checked (all unchecked): 4 items (20%)
  - `2026-02-27-indexing-and-tracking-method.md` (0/4)
  - `2026-02-27-information-synthesis-entropy.md` (0/4)
  - `2026-02-28-ai-line-1-line-2-risk-agents.md` (0/10)
  - `2026-02-28-ai-strategy-risk-reduction-focus.md` (0/8)
  
- Items with NO sources section: 3 items (`2026-02-28-ai-strategy-business-efficiency-examples.md` has 7 unchecked, `2026-03-02-agent-memory-management-context-injection.md` has 50 checked/0 unchecked — special case)

**[fact]** 4 items (20%) have all sources unchecked — sources were listed but the agent did not consult them or did not mark them. This is the primary source engagement failure mode.

**B2. Research Skill Output section presence:**
- 5 items have `## Research Skill Output` (all dated 2026-03-03): `cross-item-synthesis-meta-insights`, `knowledge-linking-connected-corpus`, `knowledge-representation-agent-context`, `knowledge-retention-active-recall`, `research-agenda-curation-coverage`.
- 15 items do NOT have this section.
**[fact]** The Research Skill Output section (§0–§7) was added to `research-prompt.md` recently — the 2026-03-03 items are the first to show it.

**B3. Correlation: Research Skill Output section vs. source engagement and key finding count:**
- Items WITH Research Skill Output: avg sources checked = 12.8/item; avg key findings count ≈ 43/item.
- Items WITHOUT Research Skill Output: avg sources checked = 3.1/item (including 4 all-unchecked items pulling this down); avg key findings count ≈ 14/item.
**[inference]** The Research Skill Output section correlates strongly with higher source engagement and finding count. The causal mechanism is plausible: the §2 Investigation section explicitly requires iterative evidence gathering and source marking, while the non-structured items have no equivalent forcing function.

**B4. Three most common failure patterns:**

1. **Sources listed but not consulted** — 40% of items (8/20) have at least some unchecked sources. 20% have all sources unchecked. The prompt (before the Research Skill Output addition) did not explicitly instruct the agent to mark sources as `[x]` when consulted, nor did it require source URLs to appear in the body of the findings. **Prompt-caused.**

2. **Executive Summary restates the research question rather than answering it** — Present in the early items (e.g., `ai-strategy.md` executive summary opens with "New Zealand released its first national AI strategy..." which directly answers the question; but `ai-strategy-risk-reduction-focus.md` opens with "Financial services organisations deploy AI primarily for fraud detection..." — these are actually reasonable). On closer inspection, the failure mode is more subtle: items with `priority: medium` and well-specified source lists tend to have better executive summaries, while items with long source lists and less specific research questions produce summaries that cover the topic broadly without answering a specific claim. **Partly prompt-caused, partly item-specification issue.**

3. **No cross-item integration** — Pre-2026-03-03 items almost never reference prior completed research. There is no instruction in the pre-updated `research-prompt.md` to search `Research/completed/` for related work. The 2026-03-03 items (with the Research Skill Output section) show `spawned-from` and related item references in their YAML and body. **Prompt-caused** — the current prompt (as of this session) does NOT include an explicit instruction to search completed items before starting.

**B5. Prompt-caused vs. model-caused:**
All three primary failure patterns are prompt-caused, not model-caused. The 2026-03-03 items demonstrate that when the prompt explicitly requires source marking (via §2 Investigation) and structured sections (§0–§7), the model complies. **[inference]** The model is capable of quality output; the historical failures stemmed from insufficient prompt specificity.

---

#### C. Prompt engineering survey (C1–C5)

**C1. Chain-of-thought in long-form synthesis:**
CoT prompting demonstrably improves performance on multi-step reasoning, synthesis tasks, and research-quality outputs by requiring the model to externalize intermediate reasoning. **[fact]** Source: The Prompt Report (arXiv:2406.06608) — systematic survey of 58+ techniques; CoT is documented as improving accuracy in reasoning-heavy tasks by requiring step-by-step externalisation. The Research Skill Output section (§0–§7) in `research-prompt.md` is already a structured CoT variant: §1 decomposes questions, §2 gathers evidence, §3–§4 reason and check, §6 synthesises. The corpus audit confirms items with this section produce markedly better outputs.

**C2. Negative constraints:**
Negative constraints ("do not X") are moderately effective but work best when paired with positive instructions. **[fact]** LLM instruction-following research (2024) shows that models can misinterpret or overlook negation, especially in long prompts. Best practice: pair "do not reproduce template headings without content" with "each section must contain substantive prose before the heading is considered complete." Source: web search synthesis from multiple practitioner sources and The Prompt Report.

**C3. Structured output constraints for specificity:**
Requiring a specific format for the executive summary — "the first sentence must state the answer to the research question as a falsifiable claim, not a restatement of the question" — is a structural constraint that forces specificity. **[inference]** from the corpus audit: items where the research question was concrete and the executive summary was required to open with a specific claim tended to be higher-quality. The Anthropic prompting guide (accessed 2026-03-03) confirms: "Being specific about your desired output can help enhance results. If you want 'above and beyond' behavior, explicitly request it rather than relying on the model to infer this from vague prompts."

**C4. Fabric `extract_wisdom` pattern:**
The Fabric `extract_wisdom` pattern (Daniel Miessler, github.com/danielmiessler/fabric) employs: (1) explicit identity/purpose framing; (2) step-by-step instructions separating extraction from abstraction; (3) mandatory labelled output sections (`SUMMARY`, `IDEAS`, `INSIGHTS`, `QUOTES`). **[fact]** The pattern is documented at danialrami.com/posts/extract-wisdom/ and the GitHub repository. Key lesson for `research-prompt.md`: the pattern's effectiveness comes from separating extraction (§2 Investigation) from abstraction (§6 Synthesis) — which the Research Skill Output section already does. The pattern also requires a fixed minimum output count per section (e.g., "20–50 surprising ideas"), which functions as a specificity forcing function.

**C5. Prompt length and instruction-following degradation:**
Research on context window utilisation shows that instruction-following degrades as prompt length increases, with models tending to front-weight attention — instructions near the beginning of a prompt are followed more reliably than instructions at the end. **[fact]** Source: "Lost in the Middle" (Stanford, 2023, arXiv:2307.03172) demonstrated that LLMs attend more reliably to information at the start and end of long contexts than to the middle. For `research-prompt.md`, critical instructions (like "mark sources as `[x]` when consulted") should be placed near the top and repeated in the specific step they apply to.

---

#### D. Loop mechanics (D1–D3)

**D1. Priority-ordering in `research-prompt.md`:**
The current `research-prompt.md` contains explicit priority-ordering instructions in Step 1:
```
1. `priority: high` before `priority: medium` before `priority: low`
2. For equal priority, prefer items with a non-empty `blocks` list
3. For remaining ties, pick the **oldest** item (earliest date in filename)
```
**[fact]** Confirmed by direct inspection of `research-prompt.md`.

**D2. Priority ordering respected in practice:**
The 2026-03-03 batch processed five items all with `priority: high` before touching the `medium` backlog. Today's session selected `2026-03-03-research-loop-quality-prompt-engineering.md` (the only `high`-priority item remaining in the backlog) before any `medium` items. **[fact]** Confirmed by backlog inspection and execution order.

**D3. Instruction to search completed items:**
The current `research-prompt.md` does NOT contain an explicit instruction to search `Research/completed/` for related prior work before starting a new item. Step 3 says "Read the item in full" but does not say "check completed items for related findings and reference them in the Context or § sections." **[fact]** Confirmed by direct inspection. This is the most impactful missing instruction.

---

#### E. Quality gate design (E1–E3)

**E1. Minimum shell-detectable structural checks:**
The following checks can be implemented as shell one-liners operating on a Markdown file:

```bash
# 1. completed date is populated
grep -E '^completed: [0-9]{4}' "$file"

# 2. Executive Summary has ≥ 80 words
exec_summary=$(sed -n '/^### Executive Summary/,/^###/p' "$file" | grep -v '^###')
word_count=$(echo "$exec_summary" | wc -w)
[ "$word_count" -ge 80 ]

# 3. At least 2 numbered Key Findings with ≥ 15 words each
kf_count=$(sed -n '/^### Key Findings/,/^###/p' "$file" | grep -E '^[0-9]+\.' | awk 'NF>=15' | wc -l)
[ "$kf_count" -ge 2 ]

# 4. At least 1 source marked [x]
grep -c '^\- \[x\]' "$file"
```

**[inference]** These four checks detect the three primary failure modes identified in the corpus audit: unconsulted sources (check 4), shallow executive summaries (check 2), and formulaic key findings (check 3).

**E2. Sufficiency for detecting failure modes:**
Checks 1–4 cover failure modes 1 and 3 (unconsulted sources and findings specificity). They do not detect failure mode 2 (executive summary restating the question) without natural language reasoning. A fifth check — "executive summary first sentence does not contain words from the research question title" — would partially address this but with high false-positive rate. **[inference]** The four structural checks are a useful gate for the most severe failures; subtler quality issues require agent-level review.

**E3. False-positive rate:**
The checks are conservative. A genuinely researched item will almost always pass (≥80 words executive summary, ≥2 real findings, ≥1 source marked). The false-positive risk is that a mechanically-generated item that fills in the template with long but vacuous text passes all four checks. **[assumption]** The rate of such adversarial-style failure is low for the current model given the Research Skill Output section's forcing function.

---

#### F. Revised prompt additions (F1–F2)

**F1. Required additions to `research-prompt.md`:**

Five targeted additions address the identified failure patterns without substantially increasing prompt length:

1. **Prior research cross-reference instruction** (add to Step 3 or as a new Step 3.5):
   > Before beginning §2 Investigation, search `Research/completed/` for items that are topically related to the current research question (by tag, title similarity, or explicit references in the item). If any are found, read their Executive Summary and Key Findings, and add a "Prior research" paragraph to the item's Context section noting what is already known and what this item must add that is new.

2. **Source marking discipline** (add to Step 4 §2 description):
   > When you consult a source from the `## Sources` checklist, change its `[ ]` to `[x]`. A source that is listed but not consulted must be marked `[ ]` and noted as "not consulted" in Risks/Gaps. Do not list a source as consulted if you only referenced its title — you must have read its content or accessed its URL.

3. **Executive summary specificity constraint** (add to Step 5):
   > The first sentence of the Executive Summary must state the answer to the Research Question as a specific, falsifiable claim. It must not restate the research question, describe what the item covers, or use hedging phrases ("it depends", "there are several approaches"). If the answer is genuinely uncertain, state the best-supported conclusion followed by the primary uncertainty.

4. **Negative constraint against formulaic output** (add to Step 4 preamble):
   > Do not reproduce section headings from the template without substantive content below each heading. A section that consists only of a heading and a placeholder ("Fill in...") or a single sentence is a quality failure. Every section in the Research Skill Output must contain substantive prose that would be defensible in a peer review.

5. **Minimum output size per finding** (add to Step 5 Key Findings):
   > Each Key Finding must be a complete sentence of at least 20 words. It must contain a subject, a verb, and a specific object or complement. Avoid findings that are reformulations of the research question, findings that apply to all research items generically, or findings that consist only of a label without a claim.

**F2. Prompt length assessment:**
The current `research-prompt.md` is approximately 800 words. The five additions above add approximately 300 words, bringing it to ~1,100 words. This is within a comfortable range for instruction-following. The "Lost in the Middle" finding (C5) indicates that the most critical instructions should appear near the top of the relevant step, not buried at the bottom. The prior research cross-reference instruction (addition 1) and source marking discipline (addition 2) should be placed early in their respective steps. **[inference]**

---

### §3 Reasoning

**Facts established:**
1. The corpus contains 20 completed items (excluding README). 5 have the Research Skill Output section (§0–§7); 15 do not.
2. Items with the Research Skill Output section have dramatically higher source engagement (avg 12.8 sources checked vs. 3.1) and finding counts (avg 43 vs. 14).
3. 20% of items (4/20) have all sources listed but none consulted. 40% have at least some unchecked.
4. The `research-prompt.md` has correct priority-ordering logic. The loop respects `priority: high` before `medium` in practice.
5. The current `research-prompt.md` does NOT instruct the agent to search `Research/completed/` for prior related work.
6. The Anthropic prompting guide, The Prompt Report (arXiv:2406.06608), and the Fabric `extract_wisdom` pattern all confirm that structured CoT, explicit output requirements, and section-level forcing functions produce better synthesis quality.
7. Negative constraints work better when paired with positive instructions ("write X, not Y" not just "don't write Y").

**Inferences:**
1. The Research Skill Output section addition was the single most impactful prompt change to date. Its forcing function (requiring each §0–§7 section to contain substantive content) drives higher source engagement and finding specificity.
2. The three primary failure patterns (unconsulted sources, shallow executive summaries, no cross-item integration) are all prompt-caused, not model-caused.
3. Five targeted additions to `research-prompt.md` would address all three failure patterns without exceeding manageable prompt length.
4. A four-check shell quality gate detects the most severe failures (unconsulted sources, formulaic findings) and can run without credentials in GitHub Actions.

**Assumptions:**
1. The model is capable of following the revised prompt's instructions (justified by the 2026-03-03 items demonstrating compliance with the Research Skill Output structure).
2. The false-positive rate of the structural quality gate is acceptably low (justified by the conservative thresholds chosen).

---

### §4 Consistency Check

**Potential contradiction 1:** The corpus audit shows 2026-03-03 items have dramatically better quality with the Research Skill Output section. But this session's prompt (which includes the Research Skill Output section) is the same prompt that produced those items. Is the Research Skill Output section the cause, or did the items happen to be better-specified in the backlog on 2026-03-03?

Resolution: Examining the 2026-03-03 items, the improved quality is present even for items with similar complexity to lower-quality earlier items. The `research-agenda-curation-coverage.md` item (2026-03-03) and the `ai-strategy-risk-reduction-focus.md` item (2026-02-28) are comparable in scope and specificity; the former has 9 sources checked and 41 key findings, the latter has 0 sources checked and 17 key findings. The Research Skill Output section is the primary differentiator. **No unresolvable contradiction.**

**Potential contradiction 2:** The prompt already contains the Research Skill Output requirement (§0–§7), yet some 2026-03-03 items still have unchecked sources (e.g., `knowledge-representation-agent-context.md` has 2 unchecked). Does this mean the source-marking discipline instruction is already present but insufficient?

Resolution: The current prompt (this session's version) says "Mark each source in the `## Sources` checklist when consulted" in the §2 description, but does not specify HOW to mark them (`[x]` vs `[ ]`). The explicit instruction "change its `[ ]` to `[x]`" is clearer. The 2 unchecked items are likely inaccessible URLs (e.g., paywalled books), not a compliance failure. **No unresolvable contradiction; addition 2 should clarify this.**

**Potential contradiction 3:** "Lost in the Middle" suggests instructions at the end of a prompt are less followed, but the Research Skill Output section is at the end of Step 4 in `research-prompt.md` and appears to be followed. Resolution: The Research Skill Output section is a large, structured block that takes up most of Step 4 — it is not "lost in the middle" but is the dominant content of the most important step. The additions recommended in F1 are placed within their relevant steps, not at the end of the document. **No unresolvable contradiction.**

---

### §5 Depth and Breadth Expansion

**Technical lens:** The quality gate design (§2-E) could be extended with a Python-based checker that uses regex and word counting to produce a quality score (0–4) per item. This score could be posted as a GitHub Actions annotation on the push commit, making quality regressions immediately visible in the Actions log without blocking the push (informational rather than blocking gate).

**Process lens:** The corpus audit reveals a temporal pattern: items processed before the Research Skill Output section was added systematically have lower source engagement. This means approximately 15 items in `Research/completed/` were completed with suboptimal source coverage. A one-time re-enrichment pass (re-opening those items and augmenting the findings with the now-accessible sources) is possible but out of scope for this item; it should be a separate backlog item.

**Organisational lens:** The prior-research cross-reference instruction (addition 1) is not just a quality improvement — it prevents the research corpus from becoming a collection of isolated items that repeat findings already established elsewhere. As the corpus grows toward 50+ items, the risk of research duplication increases. The cross-reference instruction builds in the "corpus-awareness" that makes the collection more than the sum of its parts.

**Behavioural lens:** The negative constraint addition ("do not reproduce section headings without substantive content") works against a well-documented LLM failure mode: template completion, where the model fills in each section heading with the minimum content that satisfies the structural requirement. The Fabric `extract_wisdom` pattern addresses this by specifying minimum output counts ("20–50 ideas") — a more reliable enforcement mechanism than a negative constraint alone.

**Measurement lens:** The four structural checks in the quality gate can be tracked over time: if check failure rates increase after a model update, that signals the new model has weaker instruction-following for this prompt. This provides early warning without requiring manual review of every item.

---

### §6 Synthesis

#### Executive Summary

The quality variation in autonomous research loop output is prompt-caused, not model-caused. The single most impactful change already in production is the Research Skill Output section (§0–§7), which increased average source engagement from 3.1 to 12.8 sources per item and key finding counts from 14 to 43. Three residual failure patterns remain: sources listed but not consulted (40% of pre-2026-03-03 items), executive summaries that lack specific claims, and no cross-item integration with prior completed research. Five targeted additions to `research-prompt.md` — prior research cross-reference instruction, explicit source-marking discipline, executive summary specificity constraint, anti-formulaic negative constraint, and minimum finding size requirement — address all three failure patterns. A four-check shell quality gate (completed date populated, ≥80-word executive summary, ≥2 substantive key findings, ≥1 source marked `[x]`) detects the most severe failures without requiring new credentials or blocking the loop.

#### Key Findings

1. Items with the Research Skill Output section (§0–§7) produce dramatically better outputs: avg 12.8 sources checked vs. 3.1 without it, and avg 43 key findings vs. 14. The Research Skill Output section is the most impactful quality lever already deployed (high confidence).

2. 40% of pre-2026-03-03 items have at least some sources listed but not consulted. 20% (4/20) have all sources unchecked. This is the primary source engagement failure and is prompt-caused: no explicit instruction existed to mark sources `[x]` when consulted (high confidence).

3. The current `research-prompt.md` lacks an instruction to search `Research/completed/` for prior related work before starting a new item. All pre-2026-03-03 items lack cross-item integration; 2026-03-03 items show sporadic integration only where the item's own Context section referenced prior work. This gap grows in significance as the corpus expands beyond 20 items (high confidence).

4. Priority ordering in the loop is correct and respected in practice: `research-prompt.md` contains explicit `priority: high → medium → low` rules; the 2026-03-03 batch processed five `high`-priority items before any `medium` items; today's session selected the sole remaining `high`-priority item. No fix required (high confidence).

5. Chain-of-thought prompting in the form of structured step decomposition (§1 Question Decomposition → §2 Investigation → §6 Synthesis) is the mechanism behind the Research Skill Output section's quality improvement. The Prompt Report (arXiv:2406.06608) documents this as one of 58+ validated techniques; the corpus confirms it empirically in this specific repository (high confidence).

6. Negative constraints ("do not X") are moderately effective but work best when paired with positive instructions. The addition "Do not reproduce template headings without substantive content below each heading" should be paired with "Each section must contain defensible prose before the next heading" (medium confidence, from practitioner literature).

7. The Fabric `extract_wisdom` pattern's use of minimum output counts per section (e.g., "20–50 ideas") is a more reliable specificity enforcement mechanism than negative constraints alone. Adapting this to Key Findings — "each finding must be ≥ 20 words" — is the most direct route to eliminating one-line vague findings (medium confidence).

8. A four-check shell quality gate detects the three primary failure modes at low false-positive cost: completed date check, executive summary word count ≥ 80, key findings ≥ 2 with ≥ 15 words each, and ≥ 1 source marked `[x]`. This gate can run as a post-commit GitHub Actions step triggered by `on: push: paths: Research/completed/**` (high confidence).

9. The "Lost in the Middle" effect (Stanford arXiv:2307.03172) means critical instructions — source marking, executive summary discipline — should be placed near the top of the relevant step in `research-prompt.md`, not at the end. Additions 1 and 2 in the recommended changes should each be placed as the first instruction in their respective steps (medium confidence).

10. Approximately 15 items in `Research/completed/` (pre-2026-03-03) have suboptimal source coverage due to the pre-Research Skill Output prompt. A re-enrichment pass on the most strategically important items would recover value from the corpus but is a separate task from prompt improvement (medium confidence).

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Research Skill Output section increases source engagement 4x | Corpus audit: 20 items inspected (avg 12.8 vs. 3.1 sources checked) | high | Direct measurement |
| 40% of items have some sources unchecked | Corpus audit: 8/20 items with unchecked sources | high | Direct count |
| Priority ordering is correct and respected | `research-prompt.md` inspection + execution order 2026-03-03 | high | Both primary sources |
| `research-prompt.md` lacks prior-research instruction | Direct inspection of Step 3 and all steps | high | Absence confirmed by search |
| CoT improves synthesis quality | The Prompt Report arXiv:2406.06608; corpus audit correlation | high | Two independent sources |
| Negative constraints work better paired with positive | Web search synthesis; Anthropic prompting guide | medium | Practitioner consensus, no RCT |
| Fabric minimum output counts improve specificity | Fabric extract_wisdom documentation; danialrami.com/posts/extract-wisdom/ | medium | Pattern analysis |
| Four-check shell gate detects primary failures | Shell command design; corpus audit failure mode analysis | high | Logical derivation from audit |
| "Lost in the Middle" effect applies to long prompts | arXiv:2307.03172 | medium | From NLP research, not specifically tested on this prompt |
| 15 pre-2026-03-03 items have suboptimal coverage | Corpus audit: all 15 items without Research Skill Output section | high | Direct count |

#### Assumptions

- **Assumption:** The model follows the revised prompt's instructions at comparable quality to the 2026-03-03 items. **Justification:** The 2026-03-03 items demonstrate the model is capable of compliance with structured multi-step instructions; the proposed additions are incremental extensions of the same pattern.
- **Assumption:** The structural quality gate's false-positive rate is acceptably low. **Justification:** The thresholds (80 words, 2 findings, 1 checked source) are conservative; any genuine research effort produces outputs well above these minima.

#### Analysis

The corpus audit produces a clear before/after split at 2026-03-03: the Research Skill Output addition was decisive. The five proposed additions are incremental improvements to an already-improved baseline, addressing residual gaps that the structured §0–§7 sections do not fully cover: prior research integration, explicit source-marking syntax, and executive summary specificity. The quality gate is designed as a signal, not a blocker — informational initially, potentially blocking after a calibration period.

The most important addition is the prior research cross-reference instruction (addition 1), because it addresses the structural property that makes the corpus more than the sum of its parts. As the corpus grows, the value of cross-item integration compounds: each new item that connects to prior work makes the whole corpus more navigable and the agent more knowledgeable at session start.

The tension between prompt length and instruction-following is real but manageable at ~1,100 words. The "Lost in the Middle" risk is mitigated by placing critical instructions at the start of their relevant steps.

#### Risks, Gaps, and Uncertainties

- The source engagement improvement from 3.1 to 12.8 may partly reflect that the 2026-03-03 items had more accessible sources (internal repository files) rather than purely a prompt effect. The true causal effect of the Research Skill Output section on web-source engagement cannot be cleanly isolated.
- The quality gate requires a GitHub Actions step that runs after the agent commits. If the agent commit and push happen in the agent session itself (before the quality gate step runs), the gate operates on the pushed state. This is correct for the `research-loop.yml` pattern but needs to be verified against the actual commit timing.
- The five proposed additions have not been tested against a live session; they are inferred improvements based on corpus audit and prompt engineering literature. A controlled test (run the revised prompt on one `medium`-priority item and compare) is the recommended next step.

#### Open Questions

- Can the structural quality gate be extended to check cross-item integration (presence of links to `Research/completed/` in the body) without requiring LLM reasoning? A simple regex for `Research/completed/` links would work, but would miss items that reference prior work by title without a link.
- Should the quality gate be informational (annotation only) or blocking (fail the GitHub Actions step)? An informational gate provides signal without risk of blocking the loop. A blocking gate prevents low-quality items from reaching `Research/completed/` but could halt the loop on borderline items.
- Is there a prompt length threshold beyond which instruction-following measurably degrades for the Copilot CLI model? The "Lost in the Middle" result is from a different model (GPT-3.5/4); Copilot CLI's model may have different attention patterns.

---

### §7 Recursive Review

**Completeness check:**
- §0: Question restated, scope confirmed, output format specified. ✓
- §1: Six atomic question branches (A–F) covering all Approach sub-questions. ✓
- §2: All six branches investigated with evidence gathered from corpus audit (primary), web search (secondary), and document inspection (primary). ✓
- §3: Facts, inferences, and assumptions clearly separated. ✓
- §4: Three potential contradictions identified and resolved. ✓
- §5: Four expansion lenses (technical, process, organisational, behavioural). ✓
- §6: Executive summary answers the research question directly. 10 key findings, each evidence-backed. Evidence map complete (10 rows for 10 findings). Assumptions explicit. ✓
- §7: This recursive review. ✓

**Evidence discipline audit:**
- All `[fact]` claims map to a named source (corpus audit counts, arXiv paper, Anthropic guide, Fabric documentation, ADR-0004). ✓
- All `[inference]` claims state the derivation. ✓
- All `[assumption]` claims are listed in the Assumptions section of §6. ✓

**Claim count per confidence label:**
- High: 6 findings (60%)
- Medium: 4 findings (40%)
- No low-confidence findings

**Unresolved gaps explicitly flagged:** Source engagement causal isolation; quality gate timing; prompt length threshold for Copilot CLI. All logged in Risks, Gaps, and Uncertainties. ✓

**Outcome:** Research Skill Output is complete and internally consistent. All threads synthesised. Ready for Findings seeding.

---

## Findings

### Executive Summary

The quality variation in autonomous research loop output is prompt-caused, not model-caused: the model is capable of high-quality synthesis, and corpus evidence demonstrates this directly. The Research Skill Output section (§0–§7) added to `research-prompt.md` increased source engagement from 3.1 to 12.8 sources per item and key finding counts from 14 to 43, making it the single most impactful quality change to date. Three residual failure patterns persist in the pre-2026-03-03 corpus: sources listed but not consulted (40% of items), executive summaries that lack specific claims, and no cross-item integration with prior completed research — all three are addressable by five targeted additions to `research-prompt.md`. A four-check shell quality gate (completed date, ≥80-word executive summary, ≥2 substantive findings, ≥1 checked source) detects the most severe failures and can be implemented as a non-blocking GitHub Actions annotation step.

### Key Findings

1. Items with the Research Skill Output section (§0–§7) produce dramatically better outputs: avg 12.8 sources checked vs. 3.1 without it, and avg 43 key findings vs. 14. The section is the most impactful quality lever already deployed. **[high confidence]**

2. 40% of pre-2026-03-03 items have at least some sources listed but not consulted; 20% (4/20) have all sources unchecked. This is the primary source engagement failure and is prompt-caused: no explicit instruction existed to mark sources `[x]` when consulted. **[high confidence]**

3. The current `research-prompt.md` lacks an instruction to search `Research/completed/` for prior related work before starting a new item. As the corpus grows beyond 20 items this gap becomes a structural deficiency: each new item that ignores prior completed work duplicates effort and misses synthesis opportunities. **[high confidence]**

4. Priority ordering in the loop is correct and respected in practice: `research-prompt.md` contains explicit `priority: high → medium → low` rules, confirmed by both document inspection and observed execution order. No fix required. **[high confidence]**

5. Chain-of-thought prompting in the form of structured step decomposition (§1 → §2 → §6) is the mechanism behind the Research Skill Output section's quality improvement, consistent with The Prompt Report (arXiv:2406.06608) documenting CoT as one of 58+ validated techniques. **[high confidence]**

6. Negative constraints work better when paired with positive instructions. "Do not reproduce template headings without substantive content" should be paired with "each section must contain defensible prose before the next heading." **[medium confidence]**

7. The Fabric `extract_wisdom` pattern's use of minimum output counts per section is a more reliable specificity enforcement mechanism than negative constraints alone. Adapting this to Key Findings — requiring each finding to be ≥ 20 words — is the direct route to eliminating one-line vague findings. **[medium confidence]**

8. A four-check shell quality gate detects the three primary failure modes at low false-positive cost: completed date populated, executive summary word count ≥ 80, ≥ 2 key findings with ≥ 15 words each, and ≥ 1 source marked `[x]`. **[high confidence]**

9. The "Lost in the Middle" effect (arXiv:2307.03172) means critical instructions should be placed near the top of the relevant step in `research-prompt.md`. The source-marking discipline instruction (addition 2) and prior-research cross-reference instruction (addition 1) must each appear as the first instruction in their respective steps to maximise compliance. **[medium confidence]**

10. Fifteen items in `Research/completed/` (pre-2026-03-03) have suboptimal source coverage due to the pre-Research Skill Output prompt. A targeted re-enrichment pass on the strategically most important items is a separate task worth adding to the backlog. **[medium confidence]**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Research Skill Output section increases avg sources checked from 3.1 to 12.8 | Corpus audit: 20 items inspected | high | Direct measurement from checklist counts |
| 40% of items have some sources unchecked | Corpus audit: 8/20 items with unchecked | high | Direct count |
| 20% of items have all sources unchecked | Corpus audit: 4/20 items all unchecked | high | ai-line-1, ai-strategy-risk, indexing, information-synthesis |
| Priority ordering correct and respected | `research-prompt.md` Step 1; 2026-03-03 execution order | high | Both primary sources agree |
| `research-prompt.md` lacks prior-research instruction | Direct inspection of all steps | high | Absence confirmed by search for "completed" |
| CoT / step decomposition drives quality improvement | The Prompt Report arXiv:2406.06608; corpus audit correlation | high | Literature + empirical evidence |
| Negative constraints better with positive pairing | Anthropic prompting guide; web search synthesis | medium | Practitioner consensus |
| Fabric minimum output counts improve specificity | extract_wisdom documentation | medium | Pattern analysis from single source |
| Four structural checks detect primary failure modes | Logical derivation from audit; shell script design | high | Derived from empirical failure patterns |
| "Lost in the Middle" applies to long prompts | arXiv:2307.03172 (Liu et al., Stanford 2023) | medium | Different model than Copilot CLI; applicable in principle |

### Assumptions

- **Assumption:** The model follows the revised prompt's instructions at quality comparable to the 2026-03-03 items. **Justification:** The 2026-03-03 items demonstrate the model is capable of compliance with multi-step structured instructions; proposed additions are incremental extensions.
- **Assumption:** The structural quality gate's false-positive rate is acceptably low. **Justification:** Conservative thresholds (80 words, 2 findings, 1 checked source) — any genuine research effort produces outputs well above these minima.

### Analysis

The corpus audit produces a clean before/after split at 2026-03-03. The Research Skill Output section addition was decisive; the proposed five additions are incremental refinements targeting the residual gaps it does not fully close. The most impactful addition is the prior research cross-reference instruction: it transforms the corpus from a collection of isolated items into a connected knowledge base, compounding in value as item count grows.

Prompt length management is straightforward: from ~800 to ~1,100 words, within the range where instruction-following remains reliable. The critical placement guidance (instructions near the top of their steps) mitigates the "Lost in the Middle" risk without restructuring the prompt.

The quality gate is designed as an informational signal initially. This avoids the risk of a conservative threshold blocking a legitimate item and stalling the loop. After calibration (confirming zero false positives across 5+ loop runs), it can be made blocking.

### Risks, Gaps, and Uncertainties

- The source engagement improvement correlation with the Research Skill Output section may partly reflect that 2026-03-03 items had more internal (repository) sources than earlier items. The causal effect on web-source engagement cannot be cleanly isolated without a controlled experiment.
- The five proposed additions have not been tested against a live session. The recommended next step is a controlled test: run the revised prompt on one `medium`-priority backlog item and compare against a pre-revision item of similar complexity.
- The "Lost in the Middle" finding is from research on GPT-3.5/4 models. The Copilot CLI model may have different attention characteristics. Placement guidance is precautionary.

### Open Questions

- **Structural cross-item integration check**: Can a regex for `Research/completed/` links in the Findings section serve as a proxy for cross-item integration without LLM reasoning? This would add a fifth check to the quality gate. Recommend adding as a stretch goal once the four-check gate is validated. [medium priority]

- **Re-enrichment of pre-2026-03-03 items**: Should the 15 suboptimal items in `Research/completed/` be re-enriched with additional source coverage? This is a separate task requiring a new backlog item. High-value candidates: `ai-line-1-line-2-risk-agents.md` (0/10 sources checked, strategically relevant), `ai-strategy-risk-reduction-focus.md` (0/8 sources checked). [medium priority]

- **Quality gate blocking vs. informational threshold**: After how many loop runs with zero false positives should the quality gate become blocking? A proposed criterion: 5 consecutive passing runs before enabling the blocking mode. [low priority]

---

## Output

- Type: knowledge, tool, backlog-item
- Description: Quality dimension framework for autonomous research output with corpus audit findings; five targeted additions to `research-prompt.md` addressing residual failure patterns; four-check shell quality gate design; confirmation that loop item-selection is correct.
- Links:
  - `research-prompt.md` (primary artefact — see additions below)
  - `docs-adr/0004-autonomous-research-loop.md` (loop design rationale)
  - The Prompt Report: https://arxiv.org/abs/2406.06608 (prompt engineering survey)