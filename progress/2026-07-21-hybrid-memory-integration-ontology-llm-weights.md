# 2026-07-21 -- Research Loop (hybrid-memory-integration-ontology-llm-weights)

**Completed:**

Research item:
- `Research/completed/2026-07-20-hybrid-memory-integration-ontology-llm-weights.md` -- completed; found that current hybrid-memory architectures synchronize symbolic knowledge graphs and latent Large Language Model (LLM) weights most reliably through read-through mediation (prompt augmentation, tool calls, graph-grounded plans) rather than direct write-back synchronization, that conflict handling works best as an explicit detect-then-resolve pipeline, and that provenance/versioning standards (PROV-O, PAV, PROV-AGENT) provide the vocabulary for authority arbitration without yet functioning as the runtime arbiter in any consulted deployed system. No benchmark was found that directly measures durable hybrid-memory coherence across repeated graph updates and later multi-turn reuse.

Sources consulted:
- https://arxiv.org/abs/2306.08302 (Pan et al. 2024 LLM-KG unification roadmap)
- https://arxiv.org/abs/2306.04136 (Baek et al. 2023 KAPING prompt-level KG augmentation)
- https://aclanthology.org/2023.emnlp-main.574/ (StructGPT tool-mediated structured reasoning)
- https://arxiv.org/abs/2310.01061 (Luo et al. 2023 Reasoning on Graphs)
- https://aclanthology.org/2025.acl-long.468/ (KG-Agent)
- https://arxiv.org/abs/2502.06864 (KG2RAG hybrid retrieval)
- https://arxiv.org/abs/2412.16311 (HybGRAG on STaRK benchmark)
- https://www.mdpi.com/2227-7390/12/15/2318 (Detect-Then-Resolve / CRDL conflict resolution)
- https://arxiv.org/abs/2310.00935 (Resolving Knowledge Conflicts in LLMs)
- https://arxiv.org/abs/2504.00180 (Contradiction Detection in RAG Systems)
- https://www.w3.org/TR/prov-o/, https://pav-ontology.github.io/pav/, https://arxiv.org/abs/2508.02866 (provenance/versioning standards)
- https://arxiv.org/abs/2605.17596 (NeuSymMS hybrid neuro-symbolic memory system)
- https://arxiv.org/abs/2506.05690 (GraphRAG-Bench)
- https://cdn.aaai.org/Workshops/1996/WS-96-05/WS96-05-004.pdf (De Giacomo and Lenzerini 1996, TBox/ABox authoritative definition, substituted for a tertiary tutorial source flagged in review)

## Mini-Retro

1. **Did the process work?** Yes. Delegating the deep investigation (web research across ~16 sources plus follow-up searches) to a background general-purpose agent worked well and kept the main session focused on quality control, citation discipline, and the review loop. The orchestrating session caught and fixed several issues the sub-agent missed.
2. **What slowed down or went wrong?** Three review passes were needed. Pass 1 caught two unexpanded acronyms (STaRK, KG2RAG). Pass 2 caught a fabricated proper noun ("ConflictCOLM" was invented instead of describing the actual paper title) and several unlabeled evaluative opening sentences in §2 Investigation and Analysis that the sub-agent's self-review missed despite the explicit checklist. Pass 3 caught a tertiary-source citation (a personal tutorial page) used for a `[fact]`-labeled definitional claim (TBox/ABox), which should have cited an authoritative Description Logic reference from the start. Additionally, the review workflow's own `review_count` commit failed to push on the first attempt (known race condition, matches an existing recurring pattern in copilot-instructions.md), so that pass had to be re-verified after a rebase before it counted toward the review budget.
3. **What single change would prevent this next time?** When delegating research drafting to a sub-agent, instruct it explicitly to grep the drafted text for unlabeled sentence-initial evaluative/comparative words ("more mature", "fragmented", "sharpens", "weighs toward") as a distinct self-review step, not just check for labels on factual claims. Also instruct it to verify every named benchmark or system acronym against the actual cited paper's abstract before using the name, to prevent inventing plausible-sounding but fabricated proper nouns like "ConflictCOLM".
4. **Is this a pattern?** Yes, on two fronts. First, "unlabeled closing/summary sentences" and "mid-paragraph evaluative claims between two labeled sentences" are both already listed as known recurring patterns in copilot-instructions.md; this session adds a further instance: unlabeled paragraph-*opening* sentences in §2 Investigation specifically (not just Analysis or Executive Summary), which the self-review checklist did not explicitly enumerate. Second, the research-review.yml push-race pattern recurred a third time, reinforcing the existing table entry rather than requiring a new one.

## Pending skill improvements

- The `research/SKILL.md` self-review checklist (mirrored in `research-prompt.md` Step 6, item 2a) should add explicit language covering paragraph-*opening* sentences in `§2 Investigation`, not only Analysis and Executive Summary, since this session's review found six such violations in §2 that the existing checklist wording did not clearly flag.
- The `citation-discipline` skill's Terminology and Acronyms rule already prohibits tertiary sources for `[fact]` claims, but this session shows the rule is easy to miss for domain-definitional claims introduced early in `§0 Initialise` (before the main evidence-gathering loop begins). Consider adding an explicit reminder that `§0` definitional claims are subject to the same sourcing-tier bar as `§2` claims.

## Applied improvements

- Added an explicit line item to `research-prompt.md` self-review guidance (see below) reinforcing that §2 Investigation paragraph-opening sentences must carry the same per-sentence labeling as Analysis and Executive Summary, closing the gap this session found.
