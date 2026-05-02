---
title: "What automated claim verification approaches against scientific literature (arXiv) are used in research synthesis systems, and what is the minimum-viable verification workflow for an AI research agent that must distinguish verified facts from inferences?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, evaluation, research-tooling, workflow]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What automated claim verification approaches against scientific literature (arXiv) are used in research synthesis systems, and what is the minimum-viable verification workflow for an AI research agent that must distinguish verified facts from inferences?

## Research Question

What automated claim verification approaches against scientific literature — specifically arXiv preprints — are used in research synthesis systems, what search strategies maximise recall and precision for claim-to-paper matching given a natural-language claim, and what is the minimum-viable verification workflow that an AI research agent using the `arxiv_mcp_server` MCP (Model Context Protocol) tool can execute to verify that an "anchor claim" (a claim that a Key Finding directly depends on) is supported by a specific primary paper — and what should happen when verification fails (downgrading claim label from `[fact]` to `[inference]` with explanation)?

## Scope

**In scope:**
- Automated fact verification systems: FEVER (Fact Extraction and VERification), SciFact, MultiVerS, and VERA — how they retrieve candidate evidence papers and assess claim entailment
- arXiv search strategies: keyword search, semantic search, author/title search, citation graph traversal; which strategies maximise recall for anchor claim verification
- Claim-to-paper matching: how to identify the specific paper that makes a given claim; title and abstract matching vs full-text search; false positive rate for near-miss papers
- LLM-as-verifier patterns: using an LLM to check whether a retrieved paper supports, refutes, or is neutral to a claim; reliability evidence and known failure modes
- `arxiv_mcp_server` tool capabilities: what search queries, paper ID lookups, and abstract/full-text retrieval it supports
- Downgrade logic: what criteria justify downgrading a claim from `[fact]` to `[inference]`, what note format captures the failure, and whether partial support warrants a partial label
- Compute budget: how many verification steps are feasible per research item without exceeding session time budget

**Out of scope:**
- Real-time fact checking against live web sources (arXiv-only scope)
- Verification of non-scientific claims (policy, business, qualitative social science)
- Full automated scientific review systems
- Verification of all claims (anchor claims only — those Key Findings directly depend on)

**Constraints:**
- Expand all acronyms on first use
- Must use the `arxiv_mcp_server` MCP tool as the search and retrieval mechanism
- Must fit within the existing §2 Investigation step of the research skill (not a new step)
- Verification overhead per item must be bounded to at most 5 anchor claims

## Context

W-0042 in `BACKLOG.md` proposes adding a claim verification step to `research-prompt.md` §2 Investigation: for anchor claims (those Key Findings directly depend on), search arXiv to locate the primary paper, verify the paper supports the claim, and downgrade `[fact]` to `[inference]` when verification fails. The `arxiv_mcp_server` is already configured in `.mcp.json`. Before implementing, the verification approach must be evidence-based — specifically: what search strategy finds the right paper, how an LLM should assess whether a paper supports a claim, and when the cost of verification is justified. This research item answers those questions.

## Approach

1. **Automated fact verification systems survey**: Review FEVER, SciFact, MultiVerS, and VERA — how they retrieve candidate evidence, assess claim entailment, and report confidence; extract patterns applicable to a single-agent workflow.
2. **arXiv search strategy evaluation**: Compare keyword search, semantic query, and author/title lookup for claim-to-paper matching on arXiv; assess recall and precision for each; identify when semantic query outperforms keyword search.
3. **LLM-as-verifier reliability assessment**: Review studies of LLM self-assessment and external claim verification; document known failure modes (hallucinated supporting papers, confirmation bias, abstract-level over-generalisation).
4. **arxiv_mcp_server capabilities review**: Read tool documentation and examples; document what search queries, abstract retrieval, and full-text access it provides; assess suitability for verification use case.
5. **Anchor claim identification heuristic**: Define what makes a claim "anchor" (Key Finding directly depends on it) vs supporting (context or background); propose a practical identification heuristic for use in the research prompt.
6. **Verification workflow design**: Produce a concrete verification sub-workflow for §2 Investigation: (1) identify anchor claims, (2) formulate arXiv search query, (3) retrieve top-3 candidate papers, (4) check each for claim support, (5) record arXiv ID or downgrade to `[inference]` with note.

## Sources

- [ ] [Thorne et al. (2018) FEVER: a Large-scale Dataset for Fact Extraction and VERification](https://arxiv.org/abs/1803.05355) — foundational fact verification benchmark and retrieval-plus-entailment pipeline design
- [ ] [Wadden et al. (2020) Fact or Fiction: Verifying Scientific Claims (SciFact)](https://arxiv.org/abs/2004.14974) — scientific claim verification against abstracts; precision/recall for arXiv-style retrieval
- [ ] [Zheng et al. (2023) Large Language Models Are Not Robust Multiple Choice Selectors](https://arxiv.org/abs/2309.03882) — LLM verification reliability failure modes; confirmation bias and position effects
- [ ] [arxiv-mcp-server GitHub repository](https://github.com/blazickjp/arxiv-mcp-server) — tool documentation for arXiv search, paper ID lookup, and abstract retrieval
- [ ] [OpenAI (2023) GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) — LLM fact verification capability benchmarks on FEVER and related tasks

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
