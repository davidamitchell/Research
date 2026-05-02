---
title: "What structured approaches and AI agent workflow patterns exist for converting synthesised research findings into polished papers and practical frameworks, and what are the critical failure modes of research-to-publication pipelines?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: [2026-05-02-systematic-review-methodology-ai-synthesis]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, workflow, research-tooling, strategy-author]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-05-02-systematic-review-methodology-ai-synthesis, 2026-04-27-uelgf-synthesis-complete-framework]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What structured approaches and AI agent workflow patterns exist for converting synthesised research findings into polished papers and practical frameworks, and what are the critical failure modes of research-to-publication pipelines?

## Research Question

What structured approaches — from academic writing pedagogy, AI-assisted writing tools, and agentic workflow design — exist for converting synthesised research findings into polished papers and practical decision frameworks, what Data-Information-Knowledge-Wisdom (DIKW) chain steps are typically skipped or corrupted in AI-assisted research-to-publication pipelines, and what `authoring-prompt.md` design and `authoring-loop.yml` workflow structure best support producing a finished paper or framework artifact from specified synthesis and primary research items while avoiding the most critical failure modes?

## Scope

**In scope:**
- Academic writing structure: standard paper templates (IMRaD — Introduction, Methods, Results, and Discussion; argument essay; policy brief) and practical framework templates (decision framework, maturity model, capability map) — their structural differences and when each is appropriate
- AI-assisted writing tools: Elicit, Consensus, Semantic Scholar Research Assistant, Paperpal, and GPT-4-based writing assistants — how they structure the research-to-draft pipeline and what quality controls they apply
- DIKW chain gap analysis: where AI-assisted pipelines typically skip from data/information directly to wisdom-level output without sufficient knowledge synthesis; what artefacts are most commonly missing
- Failure mode survey: hallucinated citations in generated papers, loss of nuance from synthesis items, unsupported generalisations, inappropriate certainty, and loss of provenance in the generation step
- Authoring agent prompt design: how to instruct an AI agent to draw on specified synthesis and primary items faithfully, apply the `strategy-author` and `strategic-persuasion` skills, and produce a draft that cites sources by item slug
- `authoring-loop.yml` workflow design: `workflow_dispatch` trigger, input parameters (`output_type`: paper | framework, `title`, `source_items`), and output directory structure (`Outputs/papers/`, `Outputs/frameworks/`)
- Quality assurance: what post-generation review steps are needed to catch the most critical failure modes before an authored output is committed

**Out of scope:**
- Academic submission and peer review processes
- Copyright and intellectual property considerations for AI-generated papers
- Marketing, distribution, or publication channels for authored outputs
- Synthesis workflow (covered by W-0051)

**Constraints:**
- Expand all acronyms on first use
- The authoring workflow must be manual-trigger-only (`workflow_dispatch`) — never scheduled
- Authored outputs must cite source items by slug; the references section must be generated from `cites:` fields
- Blocked on W-0051 (synthesis workflow must exist before authoring draws on synthesis items)

## Context

W-0052 in `BACKLOG.md` proposes an authoring workflow to produce finished papers and frameworks from synthesis and primary research items. This closes the last gap in the DIKW chain: the research corpus produces information (primary items) and knowledge (synthesis items) but has no workflow to produce wisdom-level outputs (papers, frameworks). Before implementing, the design must be grounded in evidence about what makes AI-assisted authoring succeed or fail: what templates work for papers vs frameworks, what the critical failure modes are, and how the `authoring-prompt.md` and workflow should be structured to avoid them. This item is blocked on W-0051 (synthesis workflow) because the authoring workflow draws on synthesis items as its primary inputs.

## Approach

1. **Academic writing structure survey**: Review IMRaD structure, argument essay structure, policy brief format, decision framework template, and capability maturity model format; identify the structural differences and when each output type is appropriate given the source material.
2. **AI-assisted writing tool architecture review**: Study Elicit, Consensus, Paperpal, and GPT-4 writing assistants; document how each structures the research-to-draft pipeline, what quality controls they apply, and what failure modes each is known for.
3. **DIKW chain gap analysis**: Review DIKW chain theory and identify the most common gaps in AI-assisted research-to-publication pipelines — where information is promoted to wisdom-level output without adequate knowledge synthesis; document the artefacts that bridge each gap.
4. **Failure mode survey**: Systematically catalogue known failure modes of AI-generated academic papers and frameworks: hallucinated citations, loss of nuance, unsupported generalisations, inappropriate certainty, provenance loss; assess which are most damaging and most preventable.
5. **Authoring prompt design**: Design an `authoring-prompt.md` structure that: (a) instructs the agent to read all source items via `filesystem` MCP before drafting, (b) applies the `strategy-author` skill for structure, (c) applies the `strategic-persuasion` skill for audience targeting, (d) generates a references section from `cites:` slugs, (e) includes a post-generation quality check step for the most critical failure modes.
6. **Workflow design**: Propose `authoring-loop.yml` trigger, input parameters, output structure, and any post-generation review steps that run automatically before the output is committed.

## Sources

- [ ] [Swales and Feak (2012) Academic Writing for Graduate Students: Essential Tasks and Skills](https://www.press.umich.edu/57293/academic_writing_for_graduate_students) — IMRaD and academic paper structure pedagogy
- [ ] [Elicit AI — Research Workflow](https://elicit.com/how-it-works) — AI-assisted paper writing pipeline from literature to draft
- [ ] [Floridi et al. (2020) GPT-3: Its Nature, Scope, Limits, and Consequences](https://link.springer.com/article/10.1007/s11023-020-09548-1) — AI-generated text quality, failure modes, and DIKW chain implications
- [ ] [Atkinson and Claxton (2000) The Intuitive Practitioner: On the Value of Not Always Knowing What One is Doing](https://www.mheducation.co.uk/the-intuitive-practitioner-9780335203543-emea-group) — DIKW chain theory: information to knowledge to wisdom gaps
- [ ] [Bang et al. (2023) A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity](https://arxiv.org/abs/2302.04023) — hallucination and factual error rates in AI-generated text; applicable to authoring failure mode survey

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
