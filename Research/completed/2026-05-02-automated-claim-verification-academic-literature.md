---
review_count: 2
title: "What automated claim verification approaches against scientific literature (arXiv) are used in research synthesis systems, and what is the minimum-viable verification workflow for an Artificial Intelligence (AI) research agent that must distinguish verified facts from inferences?"
added: 2026-05-02T06:11:10+00:00
status: completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, evaluation, workflow, agent-tooling, hallucinations]
started: 2026-05-03T04:20:12+00:00
completed: 2026-05-03T04:44:18+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-05-llm-hallucination-mechanisms, 2026-04-26-llm-verifiability-asymmetry-code-world-action, 2026-05-02-systematic-review-methodology-ai-synthesis]
related: [2026-05-02-adversarial-review-methods-ai-research-quality]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What automated claim verification approaches against scientific literature (arXiv) are used in research synthesis systems, and what is the minimum-viable verification workflow for an Artificial Intelligence (AI) research agent that must distinguish verified facts from inferences?

## Research Question

What automated claim verification approaches against scientific literature, specifically arXiv preprints, are used in research synthesis systems, what search strategies maximise recall and precision for claim-to-paper matching given a natural-language claim, and what is the minimum-viable verification workflow that an Artificial Intelligence (AI) research agent using the `arxiv_mcp_server` Model Context Protocol (MCP) tool can execute to verify that a support-critical claim, one a Key Finding directly depends on, is supported by a specific primary paper, and what should happen when verification fails (downgrading claim label from `[fact]` to `[inference]` with explanation)?

## Scope

**In scope:**
- Automated fact verification systems: Fact Extraction and VERification (FEVER), Fact or Fiction, the scientific-claim-verification benchmark commonly called SciFact, VerT5erini, a pretrained sequence-to-sequence scientific-claim verifier, and MultiVerS, a multitask verifier with full-document context, and how they retrieve candidate evidence papers and assess claim entailment
- arXiv search strategies: keyword search, embedding-based similarity search over paper text, author/title search, citation graph traversal, and which strategies maximise recall for support-critical claim verification
- Claim-to-paper matching: how to identify the specific paper that makes a given claim, title and abstract matching versus full-text search, and the false-positive risk for near-miss papers
- Large Language Model (LLM)-as-verifier patterns: using an LLM to check whether a retrieved paper supports, refutes, or is neutral to a claim, including reliability evidence and known failure modes
- `arxiv_mcp_server` tool capabilities: what search queries, paper ID lookups, abstract retrieval, full-text retrieval, and local embedding-based similarity-search features it supports
- Downgrade logic: what criteria justify downgrading a claim from `[fact]` to `[inference]`, what note format captures the failure, and whether partial support warrants a partial label
- Compute budget: how many verification steps are feasible per research item without exceeding session time budget

**Out of scope:**
- Real-time fact checking against live web sources (arXiv-only scope)
- Verification of non-scientific claims (policy, business, qualitative social science)
- Full automated scientific review systems
- Verification of all claims (only support-critical claims, those Key Findings directly depend on)

**Constraints:**
- Expand all acronyms on first use
- Must use the `arxiv_mcp_server` MCP tool as the search and retrieval mechanism
- Must fit within the existing §2 Investigation step of the research skill (not a new step)
- Verification overhead per item must be bounded to at most 5 support-critical claims

## Context

- [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.mcp.json] W-0042 proposes adding a support-critical-claim verification step to `research-prompt.md` section 2, and `.mcp.json` already configures `arxiv_mcp_server` as the intended arXiv access surface.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-llm-hallucination-mechanisms.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] Prior repository work already argues that claim extraction before synthesis, grounded retrieval, and explicit verifier boundaries reduce hallucination risk, so this item can focus on the arXiv-specific workflow rather than re-establishing those broader principles from scratch.

## Approach

1. **Automated fact verification systems survey**: Review FEVER, SciFact, VerT5erini, and MultiVerS, how they retrieve candidate evidence, assess claim entailment, and report confidence; extract patterns applicable to a single-agent workflow.
2. **arXiv search strategy evaluation**: Compare keyword search, semantic query, and author/title lookup for claim-to-paper matching on arXiv; assess recall and precision for each; identify when semantic query outperforms keyword search.
3. **LLM-as-verifier reliability assessment**: Review studies of LLM self-assessment and external claim verification; document known failure modes (hallucinated supporting papers, confirmation bias, abstract-level over-generalisation, and multiple-choice position bias).
4. **arxiv_mcp_server capabilities review**: Read tool documentation and examples; document what search queries, abstract retrieval, and full-text access it provides; assess suitability for verification use case.
5. **Support-critical claim identification heuristic**: Define what makes a claim support-critical (a Key Finding directly depends on it) versus supporting background; propose a practical identification heuristic for use in the research prompt.
6. **Verification workflow design**: Produce a concrete verification sub-workflow for §2 Investigation: (1) identify support-critical claims, (2) formulate an arXiv search query, (3) retrieve top-3 candidate papers, (4) check each for claim support, (5) record the arXiv identifier or downgrade to `[inference]` with note.

## Sources

- [x] [Thorne et al. (2018) FEVER: a Large-scale Dataset for Fact Extraction and VERification](https://arxiv.org/abs/1803.05355) - foundational fact-verification benchmark and retrieval-plus-entailment pipeline design
- [x] [Wadden et al. (2020) Fact or Fiction: Verifying Scientific Claims](https://arxiv.org/abs/2004.14974) - SciFact task definition, abstract retrieval, rationale selection, and support/refute labels for scientific claims
- [x] [Pradeep et al. (2021) Scientific Claim Verification with VerT5erini](https://aclanthology.org/2021.louhi-1.11/) - pretrained sequence-to-sequence retrieval, sentence selection, and label prediction on SciFact
- [x] [Wadden et al. (2022) MultiVerS: Improving scientific claim verification with weak supervision and full-document context](https://arxiv.org/abs/2112.01640) - full-document context and multitask rationale-plus-label prediction
- [x] [Vladika and Matthes (2024) Comparing Knowledge Sources for Open-Domain Scientific Claim Verification](https://aclanthology.org/2024.eacl-long.128/) - retrieval precision and recall trade-offs across Best Matching 25 (BM25) and semantic search
- [x] [Zheng et al. (2024) Evidence Retrieval is almost All You Need for Fact Verification](https://aclanthology.org/2024.findings-acl.551/) - hybrid retrieval evidence and the centrality of evidence selection to final verification quality
- [x] [Dmonte et al. (2024) Claim Verification in the Age of Large Language Models](https://arxiv.org/abs/2408.14317) - overview of Large Language Model-based verification pipelines and retrieval-augmented patterns
- [x] [Chelli et al. (2024) Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis](https://www.jmir.org/2024/1/e53164) - empirical evidence on hallucinated citations in academic literature search tasks
- [x] [Agrawal et al. (2024) Do Language Models Know When They're Hallucinating References?](https://aclanthology.org/2024.findings-eacl.62/) - consistency-check evidence for detecting fabricated references after generation
- [x] [Zheng et al. (2024) Large Language Models Are Not Robust Multiple Choice Selectors](https://arxiv.org/abs/2309.03882) - position-bias evidence against multiple-choice-only verifier prompts
- [x] [Huwiler et al. (2025) FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models](https://aclanthology.org/2025.naacl-long.534/) - robustness evidence for fact-verification brittleness under small perturbations
- [x] [de Vries et al. (2024) The perils and promises of fact-checking with large language models](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1341697/full) - retrieval-backed Large Language Model agent accuracy remains inconsistent
- [x] [blazickjp (2026) arxiv-mcp-server GitHub repository](https://github.com/blazickjp/arxiv-mcp-server) - tool documentation for search, download, local semantic search, and rate limits

## Related

- [LLM Hallucinations - Types, Causes, and Current Mitigation Approaches](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-llm-hallucination-mechanisms.md)
- [What is the precise technical distinction between code generation and other Large Language Model outputs in terms of external verifiability, and what does this asymmetry imply for safe deployment boundaries in a regulated financial institution?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md)
- [What systematic review methodologies and Artificial Intelligence-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine which scientific-claim-verification patterns transfer to arXiv-based support-critical-claim checking for this repository's research agent.
- Scope: retrieval strategy, claim-to-paper matching, Large Language Model verifier reliability, `arxiv_mcp_server` capabilities, support-critical-claim heuristics, downgrade logic, and bounded workflow design.
- Constraints: arXiv-only verification surface, at most five support-critical claims per item, all acronyms expanded on first use, and output must fit the existing investigation step rather than adding a new workflow phase.
- Output: one knowledge item that defines a minimum-viable verification workflow plus explicit downgrade rules.
- Prior completed items reviewed: [LLM Hallucinations - Types, Causes, and Current Mitigation Approaches](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-llm-hallucination-mechanisms.md), [What is the precise technical distinction between code generation and other Large Language Model outputs in terms of external verifiability, and what does this asymmetry imply for safe deployment boundaries in a regulated financial institution?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md), and [What systematic review methodologies and Artificial Intelligence-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md).

### §1 Question Decomposition

- **Root question:** what is the cheapest verification loop that still prevents a research agent from treating an unsupported scientific claim as a verified fact?
- **A. Scientific-claim-verification systems**
  - A1. What pipeline stages are shared across the core general and scientific claim-verification benchmarks and systems?
  - A2. What changes when the evidence corpus is scientific literature rather than Wikipedia?
  - A3. What does full-document context add beyond abstract-only pipelines?
- **B. Retrieval and matching**
  - B1. What retrieval method best balances precision and recall for claim-to-paper matching?
  - B2. When is lexical search better than semantic search?
  - B3. What is the practical role of title or author lookup?
- **C. Large Language Model verifier reliability**
  - C1. When do Large Language Models help as support or refute classifiers?
  - C2. What failure modes make them unsafe as sole paper finders?
  - C3. What prompt structures should be avoided?
- **D. Tool capabilities**
  - D1. What does `arxiv_mcp_server` support directly?
  - D2. Which capabilities require downloaded local papers first?
  - D3. What operational constraints shape the workflow?
- **E. Workflow design**
  - E1. Which claims should count as support-critical?
  - E2. What support threshold justifies keeping `[fact]`?
  - E3. When should the workflow stop and downgrade to `[inference]`?

### §2 Investigation

#### Source checks and terminology corrections

- [assumption; source: https://arxiv.org/abs/2408.14317; https://github.com/Cartus/Automated-Fact-Checking-Resources/] Search note: queries `VERA scientific claim verification`, `VERA natural language processing fact verification`, and `VERA SciFact` did not surface a distinct scientific-claim-verification system, so this item treats VerT5erini as the likely intended reference and records `VERA` as a naming gap rather than as an established system.
- [assumption; source: https://aclanthology.org/2024.eacl-long.128/; https://arxiv.org/abs/2408.14317] Failed primary-source search record: queries for a paper directly comparing author or title lookup against free-text claim search on arXiv did not locate a dedicated study, so any preference for author or title lookup is treated here as a precision-oriented workflow inference rather than a settled empirical result.

#### A. Shared architecture in scientific claim verification

- [fact; source: https://arxiv.org/abs/1803.05355] FEVER defines the now-standard support, refute, and not-enough-information framing, and the paper's baseline systems separate evidence retrieval from label prediction.
- [fact; source: https://arxiv.org/abs/2004.14974] SciFact adapts this pattern to scientific literature by asking systems to retrieve evidence-bearing abstracts, assign support or refute labels, and identify rationale sentences.
- [fact; source: https://github.com/allenai/scifact/blob/master/doc/model.md] The SciFact model documentation exposes an explicit three-stage pipeline, abstract retrieval, rationale selection, and label prediction, with lexical baselines and transformer-based components for later stages.
- [fact; source: https://aclanthology.org/2021.louhi-1.11/] VerT5erini uses a pretrained sequence-to-sequence model across abstract retrieval, sentence selection, and label prediction, and the paper reports gains over a strong SciFact baseline on all three sub-tasks.
- [fact; source: https://arxiv.org/abs/2112.01640; https://aclanthology.org/2022.findings-naacl.6/] MultiVerS predicts fact-checking labels and rationale sentences jointly from full-document context, which reduces information loss from extract-then-label pipelines and improves domain adaptation under weak supervision.
- [inference; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] The stable pattern across these systems is that finding candidate evidence and judging support are separate operations, so a repository workflow should not collapse paper discovery and support judgment into one opaque model call.

#### B. Retrieval strategy and claim-to-paper matching

- [fact; source: https://aclanthology.org/2024.eacl-long.128/; https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html#bm25-similarity] In open-domain scientific claim verification, changing only the document-retrieval method materially changes end-task performance, with Best Matching 25 (BM25) outperforming semantic search on retrieval precision and semantic search outperforming BM25 on recall of relevant evidence.
- [fact; source: https://aclanthology.org/2024.findings-acl.551/] The Retrieval-Augmented Verification (RAV) paper argues that evidence retrieval is a dominant determinant of final fact-verification quality and shows that hybrid retrieval outperforms heuristic semantic-similarity retrieval on FEVER.
- [fact; source: https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md] A reproducible SciFact retrieval comparison reports BM25 and a dense MiniLM retriever as effectively tied on top-10 ranking quality, while the dense retriever improves Recall@100 and the project documentation recommends hybrid retrieval for production systems.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md] For an arXiv workflow without global semantic search, the safest minimum-viable strategy is lexical retrieval first, because it preserves precision on exact technical terms and named entities, then limited candidate reranking by title and abstract fit.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/allenai/scifact/blob/master/doc/model.md] Claim-to-paper matching should treat title matches, exact domain terms, and abstract-level proposition overlap as positive signals, but should not accept a near-topic paper as evidence unless the abstract or full text states the same proposition or a materially equivalent one.

#### C. Large Language Model verifier reliability and failure modes

- [fact; source: https://arxiv.org/abs/2408.14317] The 2024 claim-verification survey shows that Large Language Model-based verification systems still rely on explicit retrieval, prompting, or fine-tuning pipelines rather than treating the model as a self-sufficient verifier.
- [fact; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1341697/full] Retrieval-backed Large Language Model fact-checking agents outperform no-context variants, but the study reports accuracy that still varies by language and claim type, which means retrieval improves but does not solve verifier reliability.
- [fact; source: https://aclanthology.org/2025.naacl-long.534/] FactEval shows that Large Language Models used for fact verification are brittle under small character-level and word-level perturbations, so apparently confident verification judgments are not robust enough to treat as sole acceptance criteria.
- [inference; source: https://www.jmir.org/2024/1/e53164] In a systematic-review retrieval task, Generative Pre-trained Transformer 4 (GPT-4) achieved only 13.4% precision and a 28.6% hallucination rate for references, which indicates that Large Language Models should not be trusted to invent or locate academic sources without external checking.
- [fact; source: https://aclanthology.org/2024.findings-eacl.62/] Agrawal et al. show that hallucinated references often reveal themselves through internal consistency checks, which supports using Large Language Model self-consistency as a post-retrieval sanity check, not as the primary paper-finding mechanism.
- [fact; source: https://arxiv.org/abs/2309.03882] Large Language Models exhibit option-position bias in multiple-choice selection tasks, so support or refute prompts that reduce paper verification to one multiple-choice label are vulnerable to a formatting artifact unrelated to the evidence.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://aclanthology.org/2025.naacl-long.534/; https://arxiv.org/abs/2309.03882] The right role for a Large Language Model in this workflow is constrained evidence interpretation across already retrieved candidate papers, not paper discovery, not citation generation, and not one-shot verdict selection without evidence extraction.

#### D. `arxiv_mcp_server` capabilities and limits

- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] The server's core workflow is `search_papers -> download_paper -> read_paper`, which means global search and local paper reading are separate steps by design.
- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] `search_papers` accepts free-text queries plus optional date and category filters, supports boolean-style query construction, and enforces arXiv's three-second rate limit automatically.
- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] `download_paper` retrieves a paper by arXiv identifier, prefers HyperText Markup Language (HTML) when available, and falls back to Portable Document Format (PDF) parsing for older papers.
- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] `semantic_search` is experimental and only operates over papers already downloaded into local storage, so it cannot replace the initial global search step.
- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] The server also exposes experimental `citation_graph` support and warns that paper content is untrusted input that can contain instructions attempting to redirect the model away from its assigned task.
- [inference; source: https://github.com/blazickjp/arxiv-mcp-server] These capabilities make the tool adequate for bounded support-critical-claim verification, but not for exhaustive literature review, because the workflow must spend search budget carefully and treat paper text as data rather than as instructions.

#### E. Anchor-claim heuristic, support threshold, and downgrade logic

- [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] A support-critical claim is the smallest proposition whose truth is necessary for a Key Finding to remain materially valid, typically a causal, comparative, quantified, or capability claim rather than background context.
- [inference; source: https://arxiv.org/abs/2408.14317; https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/] Support-critical claims should be capped at five per item, because verification cost rises with each additional search and read, while the marginal quality gain after the highest-dependency claims drops quickly.
- [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] A claim should remain `[fact]` only when a specific arXiv paper is identified and the abstract or full text explicitly supports the same or a materially equivalent proposition.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/] A claim should be downgraded to `[inference]` when no plausible candidate appears in the search results, when the best candidate is only topically related, when support is only partial or abstract-level, when multiple candidates conflict, or when the agent cannot confidently match the claim to one paper.
- [inference; source: https://arxiv.org/abs/2309.03882; https://aclanthology.org/2024.findings-eacl.62/] The downgrade note should record the query used, the best candidate examined, the reason support failed, and whether the failure was no match, partial match, contradictory evidence, or citation hallucination risk.

### §3 Reasoning

- [inference; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] Because the primary literature consistently separates retrieval from support judgment, a repository workflow should also separate search from verification rather than asking one model prompt to do both.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/blazickjp/arxiv-mcp-server] Because `arxiv_mcp_server` exposes strong lexical search but no global semantic index, lexical retrieval is the right first-stage choice for the minimum-viable workflow, even though an ideal production system would use hybrid retrieval.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/] Because Large Language Models are unreliable at generating or robustly selecting citations, they can only be trusted as constrained interpreters of already retrieved candidate papers.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] The conservative downgrade rule is justified because a weakly supported scientific claim is closer to an unverifiable world assertion than to a formally checkable code artifact, so false certainty is more dangerous than a labeled inference.

### §4 Consistency Check

- [fact; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md] Retrieval evidence is internally consistent: lexical methods improve precision, dense methods improve recall, and hybrid approaches are attractive when available.
- [fact; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://aclanthology.org/2025.naacl-long.534/] Reliability evidence is internally consistent: Large Language Models can help interpret evidence, but they remain too brittle and too hallucination-prone to serve as sole paper finders.
- [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.eacl-long.128/] The main unresolved tension is that the best-performing retrieval architecture in the literature is hybrid, while the available tool is lexical-first, which is why the proposed workflow stays minimum-viable rather than claiming state-of-the-art recall.
- [inference; source: https://arxiv.org/abs/2408.14317; https://github.com/blazickjp/arxiv-mcp-server] No contradiction was found between the broader survey literature and the tool documentation; the gap is capability breadth, not evidence conflict.

### §5 Depth and Breadth Expansion

- [inference; source: https://arxiv.org/abs/2112.01640; https://aclanthology.org/2021.louhi-1.11/] Technical lens: full-document context matters when support depends on qualifiers, caveats, or acronyms in the paper, so abstract-only verification is suitable for rejection and triage but weaker for positive fact retention.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/] Behavioural lens: the most dangerous verifier failure is not random error but plausible-source confabulation, because the output looks like scholarship while lacking a real paper match.
- [inference; source: https://github.com/blazickjp/arxiv-mcp-server] Security lens: paper text should be treated as untrusted input, so the verification sub-workflow should extract evidence passages and labels, not permit downloaded content to redirect tool use.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server] Operational lens: top-10 retrieval followed by top-3 inspection is a reasonable bound because search precision is good enough to surface plausible candidates near the top, while the tool's rate limit and per-paper reading cost make exhaustive inspection unattractive.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md; https://aclanthology.org/2024.findings-eacl.62/] Workflow-governance lens: a later self-review pass should challenge whether the chosen paper really makes the claim, because consistency checks and adversarial review are better at catching false positive matches than at generating new papers.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] A minimum-viable arXiv verification workflow should mirror scientific claim-verification systems by separating paper retrieval from support judgment, because the literature consistently treats those as different error surfaces.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server] For `arxiv_mcp_server`, that means lexical claim-to-paper retrieval first, then inspection of a small candidate set by title, abstract, and if necessary full-text fit, rather than relying on global semantic search that the tool does not provide.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2309.03882] Large Language Models are too hallucination-prone and too brittle to act as sole literature verifiers, so their role should be limited to structured support or refute assessment over already retrieved papers.
- [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] When no specific paper explicitly supports the support-critical claim, or support is only partial, the claim should be downgraded from `[fact]` to `[inference]` with a query-and-failure note rather than preserved as verified.

**Key findings:**

- [fact; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] Scientific claim-verification systems consistently decompose the task into retrieval, evidence selection, and support or refute judgment, even when later models integrate some stages more tightly.
- [fact; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md] Retrieval quality is a first-order determinant of final verification quality, with lexical methods favoring precision, dense methods favoring recall, and hybrid retrieval giving the strongest overall pattern where available.
- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] `arxiv_mcp_server` exposes global paper search, per-paper download, and paper reading, while its semantic search only works over locally downloaded papers.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2309.03882] Large Language Models should not be trusted as primary literature finders or single-shot verdict generators because fabricated references, perturbation brittleness, and multiple-choice position bias all remain live failure modes.
- [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] A support-critical claim should remain `[fact]` only when one identified arXiv paper states the same or materially equivalent proposition, and the workflow should otherwise preserve the claim only as `[inference]`.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] A bounded workflow that verifies only a small number of support-critical claims per item and inspects only a small top-ranked candidate set is the right minimum-viable compromise for this repository.

**Evidence map:**

- [fact; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] Shared architecture, retrieval plus evidence selection plus judgment, medium to high confidence, stable across general and scientific verification benchmarks.
- [fact; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md] Retrieval dominates quality and lexical precision should anchor the minimum-viable workflow, high confidence, recall trade-off explicitly documented.
- [fact; source: https://github.com/blazickjp/arxiv-mcp-server] Tool supports search-download-read and only local semantic search, high confidence, derived from current README and tool examples.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2309.03882] Large Language Models are best treated as unsafe as sole literature verifiers, medium confidence, multiple independent failure-mode studies support the conservative interpretation.
- [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] Exact-support threshold should gate `[fact]`, medium confidence, conservative design extrapolated from support or refute task structure.
- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] A bounded small-set workflow is the best minimum-viable compromise, medium confidence, combines evidence with repository time-budget constraints.

**Assumptions:**

- [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://arxiv.org/abs/2004.14974] A top-ten lexical arXiv search is usually wide enough to surface a plausible candidate paper for a well-phrased support-critical claim, because the tool exposes relevance-ranked search and scientific-claim benchmarks already operate on limited candidate sets.
- [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://arxiv.org/abs/2112.01640] Abstracts are sufficient for rejection and triage decisions, while positive retention of `[fact]` may require reading beyond the abstract when qualifiers or caveats matter.
- [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.eacl-long.128/] The repository can tolerate the search and read cost for at most five support-critical claims per item without distorting session time budgets.

**Analysis:**

- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/blazickjp/arxiv-mcp-server] The strongest retrieval result in the literature is hybrid retrieval, but the available tool makes lexical search the only global search primitive, so the recommended workflow optimizes precision rather than pretending to deliver best-possible recall.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://aclanthology.org/2025.naacl-long.534/] The reliability evidence weighs against letting the model propose papers from memory, because the academic-search failure mode is not merely wrong classification but fabricated citations that look legitimate.
- [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] The downgrade rule intentionally prefers false negatives over false positives, because a missed fact can survive as a labeled inference, while a mislabeled fact contaminates later synthesis as if it were verified ground truth.

**Risks, gaps, uncertainties:**

- [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://arxiv.org/abs/2408.14317] The empirical retrieval literature is strongest in biomedical or health-adjacent corpora, so generalization from PubMed-oriented benchmarks to all arXiv domains is plausible but not directly proven.
- [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.eacl-long.128/] No primary study directly measured author or title lookup against claim-keyword search on arXiv, so that precision claim remains a workflow heuristic rather than a benchmarked result.
- [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://arxiv.org/abs/2112.01640] Abstract-only verification can miss qualifiers that appear later in the paper, so any retained `[fact]` based only on abstract evidence should be treated as weaker than full-text-confirmed support.

**Open questions:**

- [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.eacl-long.128/] Would a later repository enhancement that downloads a larger candidate pool and then runs local semantic search improve recall enough to justify the added time and complexity?
- [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.findings-acl.551/] Should the workflow eventually exploit `citation_graph` or another citation-expansion surface when the top lexical hits are close but none makes the claim explicitly?
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/] What lightweight audit step best distinguishes a genuine verification failure from a prompt or query formulation failure before a support-critical claim is downgraded?

### §7 Recursive Review

- Acronym sweep: complete
- `VERA` naming gap: recorded
- Labels audit: sections 2 to 6 complete
- Remaining uncertainty: retrieval generalization beyond biomedical corpora; unbenchmarked title or author lookup heuristics

---

## Findings

### Executive Summary

A minimum-viable arXiv verification workflow should separate paper retrieval from support judgment and should leave a support-critical claim marked as `[fact]` only after one identified paper explicitly supports the same proposition. [inference; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] Scientific claim-verification systems consistently decompose the task into retrieval, evidence selection, and support or refute judgment, which implies that paper discovery and evidence interpretation are distinct failure surfaces in a research-agent workflow. [fact; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640] Because open-domain studies find that lexical retrieval tends to maximize precision while semantic retrieval improves recall, the current `arxiv_mcp_server` is best used as a lexical-first verifier surface with bounded candidate inspection rather than as a complete literature-search solution. [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server] Large Language Models remain too hallucination-prone and too brittle to invent papers or act as sole verifiers, so the safest role for the model is structured support or refute assessment over already retrieved candidate papers, with downgrade to `[inference]` whenever the paper match or support threshold fails. [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2309.03882]

### Key Findings

1. **Scientific claim-verification systems from FEVER through SciFact, VerT5erini, and MultiVerS consistently decompose verification into retrieval, evidence selection, and support or refute judgment, even when later models integrate some stages more tightly.** ([fact]; high confidence; source: https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640)
2. **Open-domain verification results show that retrieval quality materially changes final verification quality, with lexical methods favoring precision, semantic methods favoring recall, and hybrid retrieval giving the strongest overall pattern when the system can support it.** ([fact]; high confidence; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md)
3. **`arxiv_mcp_server` exposes global paper search, per-paper download, and paper reading, while its semantic search only works over locally downloaded papers and therefore cannot replace the initial global search step.** ([fact]; medium confidence; source: https://github.com/blazickjp/arxiv-mcp-server)
4. **Large Language Models are best treated as unsuitable primary literature finders or single-shot verdict generators, because fabricated references, perturbation brittleness, and multiple-choice position bias all remain well-documented failure modes in academic and fact-verification settings.** ([inference]; medium confidence; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2309.03882)
5. **A support-critical claim should remain `[fact]` only when one identified arXiv paper states the same or materially equivalent proposition, because topic-level similarity or partial support is not strong enough to preserve verified status in later synthesis.** ([inference]; medium confidence; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)
6. **A bounded workflow that verifies only a small number of support-critical claims per item and inspects only a small top-ranked candidate set is the right minimum-viable compromise for this repository.** ([inference]; medium confidence; source: https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)
7. **When no plausible paper match appears, when the best candidate is only topically related, or when support is partial or contradictory, the workflow should downgrade the claim to `[inference]` and record the query, candidate, and failure reason instead of preserving false certainty.** ([inference]; medium confidence; source: https://aclanthology.org/2024.eacl-long.128/; https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Scientific verification systems share a retrieval plus evidence plus judgment structure. | https://arxiv.org/abs/1803.05355; https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640 | high | Stable pattern across general and scientific benchmarks. |
| [fact] Retrieval quality is a first-order determinant of final verification quality. | https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/Jasonlingg/scifact-retrieval/blob/main/README.md | high | Precision versus recall trade-off is explicit in the evidence. |
| [fact] `arxiv_mcp_server` supports search, download, and reading, while semantic search is local-only. | https://github.com/blazickjp/arxiv-mcp-server | medium | Capability claim comes directly from current project documentation. |
| [inference] Large Language Models are best treated as unsafe as sole literature verifiers. | https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2309.03882 | medium | Independent studies document failure modes; the workflow recommendation is a conservative interpretation. |
| [inference] Exact-support threshold should gate retention of `[fact]`. | https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md | medium | Conservative design extrapolated from support or refute tasks and repository provenance rules. |
| [inference] A bounded small-set workflow is the best minimum-viable compromise. | https://aclanthology.org/2024.eacl-long.128/; https://github.com/blazickjp/arxiv-mcp-server; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md | medium | Practical bound combines literature with tool and session constraints. |
| [inference] Failed matches should become labeled inferences with an audit note. | https://aclanthology.org/2024.eacl-long.128/; https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/ | medium | Prevents paper-confabulation from entering later synthesis as fact. |

### Assumptions

- A top-ten lexical arXiv search is usually wide enough to surface a plausible candidate paper for a well-phrased support-critical claim. [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://arxiv.org/abs/2004.14974]
- Abstracts are sufficient for rejection and triage decisions, while positive retention of `[fact]` may require full-text reading when qualifiers matter. [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://arxiv.org/abs/2112.01640]
- The repository can tolerate the search and read cost for at most five support-critical claims per item without distorting session time budgets. [assumption; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.eacl-long.128]

### Analysis

A hybrid retrieval stack would be stronger than a lexical-only stack, but the available tool surface does not provide global semantic retrieval, so the practical recommendation optimizes precision and inspectability instead of claiming best-possible recall. [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://aclanthology.org/2024.findings-acl.551/; https://github.com/blazickjp/arxiv-mcp-server] The verification literature and the repository's prior synthesis work point in the same direction: retrieval alone is not enough, because later synthesis can still collapse near-miss papers into one overconfident claim unless support is checked at the paper and proposition level. [inference; source: https://arxiv.org/abs/2004.14974; https://arxiv.org/abs/2112.01640; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] The downgrade rule is intentionally conservative because a missed fact can survive as a labeled inference, while a mislabeled fact contaminates later reasoning as if it were verified ground truth. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2025.naacl-long.534/]

### Risks, Gaps, and Uncertainties

- The empirical retrieval evidence is strongest in biomedical or health-adjacent corpora, so generalization from PubMed-oriented benchmarks to every arXiv domain is plausible but not directly demonstrated here. [inference; source: https://aclanthology.org/2024.eacl-long.128/; https://arxiv.org/abs/2408.14317]
- No primary study directly measured author or title lookup against claim-keyword search on arXiv, so any claim that title or author lookup is best should be treated as a workflow heuristic rather than as benchmarked fact. [assumption; source: https://aclanthology.org/2024.eacl-long.128/; https://arxiv.org/abs/2408.14317]
- Abstract-only verification can miss qualifiers or boundary conditions that appear later in the paper, which means some retained `[fact]` judgments will remain weaker than full-text-confirmed support. [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://arxiv.org/abs/2112.01640]

### Open Questions

- Would downloading a larger candidate pool and then running local semantic search improve recall enough to justify the added time and complexity? [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.eacl-long.128/]
- Should a later version of the workflow use citation-graph expansion when the top lexical hits are close but none makes the claim explicitly? [inference; source: https://github.com/blazickjp/arxiv-mcp-server; https://aclanthology.org/2024.findings-acl.551/]
- What lightweight audit step best distinguishes a genuine verification failure from a poor query formulation before a support-critical claim is downgraded? [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/]

---

## Output

- Type: knowledge
- Description: This item defines a minimum-viable arXiv-based support-critical-claim verification workflow for research-loop items and a downgrade rule for claims that cannot be matched to explicit primary-paper support. [inference; source: https://arxiv.org/abs/2004.14974; https://aclanthology.org/2021.louhi-1.11/; https://arxiv.org/abs/2112.01640; https://github.com/blazickjp/arxiv-mcp-server]
- Links:
  - https://arxiv.org/abs/2004.14974
  - https://aclanthology.org/2024.eacl-long.128/
  - https://github.com/blazickjp/arxiv-mcp-server
