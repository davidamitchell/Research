---
review_count: 2
title: "Cross-effects among three-zone agent interventions"
added: 2026-10-03T08:39:00+00:00
status: reviewing
priority: medium
blocks: []
themes: [agentic-ai, tools-infrastructure, knowledge-management, governance-policy]
started: 2026-10-18T03:36:32+00:00
completed: ~
output: []
cites: [2026-08-20-mediated-content-pool-semantic-clarity, 2026-08-20-flat-vector-rag-context-collision, 2026-08-20-execution-harness-closed-loop-performance, 2026-08-20-independent-goal-attainment-verification, 2026-08-20-three-zone-interface-feedback-constraints, 2026-07-20-agent-memory-evaluation-framework, 2026-05-18-rq4-2-adversarial-error-propagation, 2026-03-10-adversarial-agents-shared-goals-multi-perspective, 2026-04-28-llm-as-judge-pipeline-validation-checkpoints, 2026-05-17-ai-policy-ambiguity-feedback-loop-systemic-homogenization-risk, 2026-03-12-failure-mode-taxonomy-expansion]
related: [2026-07-20-tbox-abox-graphrag, 2026-03-08-context-engineering-first-principles, 2026-05-12-rag-document-drift-agent-behavior, 2026-05-01-terminal-bench-minimal-coding-agent-benchmarks, 2026-08-20-neuro-symbolic-nuance-loss-explainability]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Cross-effects among three-zone agent interventions

## Research Question

Under what conditions do the measured benefits of pool-level annotations, harness context management, and goal-attainment verification hold, shrink, or reverse as the consumer model, task family, content-pool properties, and verifier model family vary, and which properties predict those changes?

## Scope

**In scope:**
- Test whether provenance and justification overlays, including the Provenance Ontology (PROV-O), Resource Description Framework-star (RDF-star), and minimal justification sets, change large language model (LLM) consumer outputs on the conflict categories identified in retrieval-augmented generation (RAG) context-collision work, including reported violations of the Alchourrón–Gärdenfors–Makinson (AGM) Inclusion and Preservation postulates; vary consumer model.
- Compare observation masking with summarisation across model configurations and non-coding task families, varying pool structure such as the terminological box (TBox), assertional box (ABox), noise, and ambiguity.
- Measure verifier accuracy against independent evidence while varying verifier/harness model-family alignment and shared context; retain the prior reliability rubric's graded notion of independence.
- Vary one zone at a time, report interaction effects, and determine when each measured improvement can be treated as independent. Explain the supplied counter-cases rather than rediscovering them.
- Account for selection artefacts and other measurement limitations when comparing gains.

**Out of scope:**
- Assigning ownership of the resolver step, which the three-zone interface item defers to issue #653.
- Re-evaluating the earlier studies without testing cross-zone effects.

**Constraints:** Use controlled comparisons where available; treat the context-collision item's unreviewed benchmark figures as provisional, and distinguish measured results from hypotheses when direct experiments or suitable benchmarks are absent. Report consumer model, task family, pool properties, verifier family, and interaction effects so the conditions for any claimed independence are explicit.

## Context

This research informs whether the three proposed interventions can be adopted independently or must be selected conditionally, since an improvement measured in one zone may depend on the consumer, task, pool, harness, or verifier in another.

## Approach

1. **Pool to consumer:** Apply the content-pool item's provenance and justification overlays to the context-collision item's conflict categories; compare consumer outputs across model families and score both annotation quality and downstream conflict resolution.
2. **Harness to pool:** Compare observation masking with summarisation on non-coding tasks while varying pool structure, noise, and ambiguity; test whether the measured masking advantage persists or reverses.
3. **Verifier to harness:** Measure goal-attainment verifier accuracy against independent evidence while varying shared context and model-family alignment between harness and verifier; report independence as a graded factor.
4. **Cross-zone synthesis:** Separate single-zone effects from interactions, reconcile the specified counter-cases, and state the pool, harness, and verifier conditions under which each gain can be treated as independent.

## Related

- [Ontology schema-versus-instance choices in graph-based retrieval](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html)
- [Model-specific context-engineering effects](https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
- [Behavioral change after retrieval corpus edits](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html)

## Sources

Starting points from issue #669 and its cited work, followed by external sources added during investigation.

- [ ] [GitHub issue #669: Cross-effects among three-zone agent interventions](https://github.com/davidamitchell/Research/issues/669): question, scope, evidence standard, and counter-cases.
- [ ] [Semantic clarity and conflict resolvability in mediated content pools](https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html): proposed pool-level provenance and justification annotations.
- [ ] [Context collision and relational blindness in flat-vector retrieval-augmented generation](https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html): conflict categories and reported conflict-label intervention.
- [ ] [Closed-loop performance techniques for mediated execution harnesses](https://davidamitchell.github.io/Research/research/2026-08-20-execution-harness-closed-loop-performance.html): observation masking and summarisation comparison.
- [ ] [Independent verification and durable evidence for goal attainment](https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html): reliability rubric and graded independence.
- [ ] [Zone-specific interface constraints in three-zone architectures](https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html): interfaces, selection-artefact caveat, and resolver deferral.
- [ ] [Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html): provenance-fidelity evaluation gap.
- [ ] [Adversarial input propagation through multi-step tool-using systems](https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html): verifier and strategy-selection error propagation.
- [ ] [Adversarial agents with shared goals: multi-perspective coverage](https://davidamitchell.github.io/Research/research/2026-03-10-adversarial-agents-shared-goals-multi-perspective.html): evidence on agent independence and shared perspectives.
- [ ] [Large Language Model-as-judge pipeline validation checkpoints](https://davidamitchell.github.io/Research/research/2026-04-28-llm-as-judge-pipeline-validation-checkpoints.html): verifier placement and pipeline validation.
- [ ] [Policy ambiguity and feedback-loop homogenisation risk](https://davidamitchell.github.io/Research/research/2026-05-17-ai-policy-ambiguity-feedback-loop-systemic-homogenization-risk.html): model-family alignment risk.
- [ ] [Failure mode taxonomy: empirical frequency and causal mechanisms](https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html): co-located monitor case identified as unquantified.
- [ ] [Schema-led versus instance-emergent ontology approaches in graph-based retrieval](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html): ontology gain and noisy-corpus reversal.
- [ ] [Context engineering: first principles of steering large language model output](https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html): model-specific context-rot curves.
- [ ] [Behavioral change after retrieval-augmented generation source-document edits](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html): corpus edits changing behaviour with weights and prompts fixed.
- [ ] [Minimal coding-agent benchmark results across model families](https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html): leaderboard counter-case to minimal-harness superiority.
- [ ] [Nuance collapse in deterministic neuro-symbolic ontology pipelines](https://davidamitchell.github.io/Research/research/2026-08-20-neuro-symbolic-nuance-loss-explainability.html): ambiguity lost through normalisation.
- [x] [Chiang and Lee (2024) Do Metadata and Appearance of the Retrieved Webpages Affect LLM's Reasoning in Retrieval-Augmented Generation?](https://aclanthology.org/2024.blackboxnlp-1.24/): publication time, source, and appearance metadata change consumer answers by model.
- [x] [Ge et al. (2025) Resolving Conflicting Evidence in Automated Fact-Checking](https://arxiv.org/abs/2505.17762): source-credibility information in retrieval and generation improves conflict resolution.
- [x] [Tan et al. (2024) Blinded by Generated Contexts](https://arxiv.org/abs/2401.11911): consumer bias toward generated contexts when knowledge conflicts.
- [x] [Wang et al. (2025) Retrieval-Augmented Generation with Conflicting Evidence](https://arxiv.org/abs/2504.13079): joint ambiguity, misinformation, and noise dataset; prior work studied factors in isolation.
- [x] [Lindenbauer et al. (2025) The Complexity Trap](https://arxiv.org/abs/2508.21433): masking versus summarisation on coding tasks.
- [x] [Sun et al. (2025) Scaling Long-Horizon LLM Agent via Context-Folding](https://arxiv.org/abs/2510.11967): context management on deep-research and software tasks.
- [x] [Panickssery et al. (2024) LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076): self-recognition tracks self-preference.
- [x] [Wataoka et al. (2024) Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819): self-preference metric and familiarity hypothesis.
- [x] [Kim et al. (2025) Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962): error correlation across more than 350 models.
- [x] [Zheng et al. (2023) Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685): documented judge bias modes.
- [x] [Chroma Research (2025) Context Rot](https://www.trychroma.com/research/context-rot): model-specific degradation with input length.
- [x] [Terminal-Bench 2.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0): leaderboard rows used as counter-case.
- [x] [graphrag-comparison repository](https://github.com/kartikeyamandhar/graphrag-comparison): noisy-corpus fixed-ontology comparison.
- [x] [Alchourron, Gardenfors and Makinson (1985) On the Logic of Theory Change](https://www.cs.huji.ac.il/~lehmann/nonmon/AGM_JSL.pdf): primary source for the AGM postulates.
- [x] [Lebo et al. (2013) PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/): provenance vocabulary.
- [x] [NIST SP 800-53 Revision 5](https://csrc.nist.gov/pubs/sp/800/53/r5/final): separation-of-duties control reference.
- [x] [Goguen and Meseguer (1982) Security Policies and Security Models](https://doi.org/10.1109/SP.1982.10014): non-interference and independence reference.
- [x] [arXiv 2506.08500](https://arxiv.org/abs/2506.08500): consumer-side conflict handling reference.
- [x] [arXiv 1009.3391](https://arxiv.org/abs/1009.3391): referenced background.
- [x] [arXiv 2310.01798](https://arxiv.org/abs/2310.01798): referenced background on self-correction.
- [x] [Socio-technical theory (Newcastle)](https://open.ncl.ac.uk/theory-library/socio-technical-theory.pdf): behavioural lens reference.

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
question: conditions under which pool-level annotations, harness context management, and goal-attainment verification gains hold, shrink, or reverse across consumer model, task family, pool properties, and verifier family
scope: three single-zone interventions plus their pairwise cross-effects; resolver ownership excluded (issue #653)
constraints: distinguish measured results from hypotheses; treat unreviewed benchmark figures from the context-collision item as provisional
output: knowledge item with conditions for treating each gain as independent
```

Prior-work cross-reference: the five zone items this question builds on are the [mediated content pool item](https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html), the [context-collision item](https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html), the [execution harness item](https://davidamitchell.github.io/Research/research/2026-08-20-execution-harness-closed-loop-performance.html), the [goal-attainment verification item](https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html), and the [three-zone interface item](https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html). [assumption; source: https://github.com/davidamitchell/Research/issues/669]

Working hypothesis: no completed or external study varies more than one zone at a time, so cross-effects must be inferred from single-zone studies and from adjacent literatures on metadata sensitivity and judge bias. [assumption; source: https://arxiv.org/abs/2504.13079]

### §1 Question Decomposition

```text
A pool -> consumer
  A1 does consumer model change whether provenance or credibility metadata alters conflict resolution?
  A2 which conflict categories can an annotation plausibly help?
  A3 is any direct test of PROV-O, RDF-star, or minimal-justification overlays on consumers available?
B harness -> pool
  B1 does the masking advantage over summarisation persist outside coding tasks?
  B2 does pool noise or ambiguity reverse a structure-dependent gain?
  B3 does context management preserve or destroy pool annotations?
C verifier -> harness
  C1 does model-family alignment change verifier accuracy?
  C2 does shared context matter independently of family?
  C3 how should independence be graded?
D synthesis
  D1 how do the supplied counter-cases reconcile with the single-zone gains?
  D2 under what pool, harness, and verifier conditions can each gain be treated as independent?
```

### §2 Investigation

**A. Pool to consumer**

Consumer model changes how retrieved-document metadata affects answers. [fact; source: https://aclanthology.org/2024.blackboxnlp-1.24/] Chiang and Lee (2024) gave models two conflicting webpages and swapped publication time, source, and appearance between them: changing publication time changed the answer for most models tested, changing the source mostly did not change the answer, and appearance had a strong causal effect on Claude-3's answers. [fact; source: https://aclanthology.org/2024.blackboxnlp-1.24/]

Source-credibility information has a measured benefit for conflict resolution in at least one task family. [fact; source: https://arxiv.org/abs/2505.17762] Ge et al. (2025) report that retrieval-augmented generation (RAG) models are vulnerable when conflicting evidence differs in media-source credibility, and that adding media background information at the retrieval and generation stages significantly improves conflict resolution on their fact-checking dataset. [fact; source: https://arxiv.org/abs/2505.17762]

Consumer preferences can override provenance. [inference; source: https://arxiv.org/abs/2401.11911] Tan et al. (2024) found that Generative Pre-trained Transformer (GPT) models GPT-4 and GPT-3.5 and Llama2 favour LLM-generated contexts over retrieved ones even when the generated context is wrong, and they attribute this to greater similarity to the question and to the loss of semantic completeness when retrieved text is segmented, neither of which is a provenance signal. [fact; source: https://arxiv.org/abs/2401.11911]

A provenance overlay can help only the conflict categories that depend on source or time. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html; https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html] The context-collision item splits inter-context conflict into five categories (no conflict, complementary information, subjective disagreement, freshness, direct factual contradiction), and the pool item proposes Provenance Ontology (PROV-O) derivation chains, Resource Description Framework-star (RDF-star) statement annotations, and minimal-justification sets as the annotation set. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html; https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html] Freshness and credibility-sensitive contradictions map to derivation and timestamp edges, while complementary information has no conflict for an annotation to resolve. [inference; source: https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/2506.08500]

Annotation quality and downstream resolution are scored separately in the literature only for fact-checking and webpage metadata. [inference; source: https://arxiv.org/abs/2505.17762; https://aclanthology.org/2024.blackboxnlp-1.24/] The agent-memory evaluation item found that LongMemEval, LoCoMo, and MemoryAgentBench do not score whether a stored memory's provenance remains accurate at read time, so provenance fidelity itself lacks a standard metric. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html] Failed search: query "PROV-O RDF-star provenance annotation LLM consumer knowledge conflict evaluation" on arXiv and the web returned no study that serialises these overlays into consumer prompts and measures conflict resolution; outcome: not found. [assumption; source: https://arxiv.org/abs/2505.17762]

The context-collision item's Alchourron-Gardenfors-Makinson (AGM) postulate-violation figures rest on an unreviewed 2026 submission and remain provisional. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html] The 1985 AGM paper that defines Inclusion and Preservation is the primary source for the postulates themselves. [fact; source: https://www.cs.huji.ac.il/~lehmann/nonmon/AGM_JSL.pdf]

**B. Harness to pool**

The measured masking advantage comes from one task family. [fact; source: https://arxiv.org/abs/2508.21433] Lindenbauer et al. (2025) compared observation masking with large language model (LLM) summarisation inside one scaffold on the Software Engineering Benchmark (SWE-bench) Verified across five model configurations and found masking matched or exceeded summarisation at roughly half the token cost. [fact; source: https://arxiv.org/abs/2508.21433]

A second non-coding task family exists but tests a different comparison. [fact; source: https://arxiv.org/abs/2510.11967] Sun et al. (2025) report that a context-folding agent, which branches into a sub-trajectory and retains a concise summary of the outcome, matched or beat a reasoning-and-acting baseline on deep-research and software tasks with an active context 10 times smaller and significantly outperformed summarisation-based context management. [fact; source: https://arxiv.org/abs/2510.11967] That result compares folding with summarisation and does not test observation masking, so the masking advantage is untested on non-coding tasks. [inference; source: https://arxiv.org/abs/2510.11967; https://arxiv.org/abs/2508.21433] Failed search: query "observation masking versus summarization non-coding agent benchmark" returned the SWE-bench study and its derivatives only; outcome: no direct non-coding masking comparison found. [fact; source: https://arxiv.org/abs/2508.21433]

Leaderboard evidence qualifies any universal harness claim. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html] The Terminal-Bench item reports within-model spreads such as Claude Sonnet 4 ranging from 30.6 percent to 54.8 percent across harnesses, and richer agents above the minimal Terminus 2 agent on version 2.0. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html] Leaderboard rows differ in more than context management, so the spread cannot be attributed to masking or summarisation alone. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html]

Pool structure gains depend on pool cleanliness. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html] The terminological-box (TBox) item reports a 3.17 percentage point ontology-guided extraction gain on a clean benchmark, and a low-confidence single-author study in which a fixed-ontology pipeline lost 21.0 percentage points moving to a noisy filings corpus against 10.5 for a schema-free pipeline. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://github.com/kartikeyamandhar/graphrag-comparison] Ambiguity normalised into a fixed vocabulary is lost, which the nuance-collapse item documents for classical Description Logic class membership. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-neuro-symbolic-nuance-loss-explainability.html; https://arxiv.org/abs/1009.3391]

Context-rot curves vary by consumer, so any masking window is consumer-specific. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html] The execution-harness item cites an 18-model evaluation showing non-uniform recall degradation with input length, which means a mask depth tuned on one consumer need not transfer. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-execution-harness-closed-loop-performance.html; https://www.trychroma.com/research/context-rot]

Whether masking or summarising preserves pool annotations is untested. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-17-ai-policy-ambiguity-feedback-loop-systemic-homogenization-risk.html] The policy-homogenisation item finds that repeated model-mediated rewriting drops less salient information such as exception clauses, which suggests summarisation could drop annotation-bearing detail, but that item studies policy drafting and not harness context. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-ai-policy-ambiguity-feedback-loop-systemic-homogenization-risk.html] The retrieval-corpus drift item shows corpus edits change behaviour with weights and prompts fixed, so pool changes are a legitimate source of harness-level variation. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html]

**C. Verifier to harness**

Model families favour their own outputs. [fact; source: https://arxiv.org/abs/2404.13076] Panickssery et al. (2024) report that GPT-4 and Llama 2 distinguish their own outputs from other models' outputs with non-trivial accuracy, and that fine-tuning shows a linear correlation between self-recognition and self-preference strength. [fact; source: https://arxiv.org/abs/2404.13076] Wataoka et al. (2024) introduce a quantitative self-preference metric, find GPT-4 shows significant self-preference bias, and hypothesise that models favour outputs with lower perplexity. [fact; source: https://arxiv.org/abs/2410.21819]

Error correlation extends beyond a single provider. [fact; source: https://arxiv.org/abs/2506.07962] Kim et al. (2025) evaluated over 350 models and report that on one leaderboard dataset models agree 60 percent of the time when both err, that shared architectures and providers drive correlation, and that larger and more accurate models have highly correlated errors even across distinct architectures and providers. [fact; source: https://arxiv.org/abs/2506.07962] Different model families therefore reduce but do not remove shared-error exposure for a verifier. [inference; source: https://arxiv.org/abs/2506.07962]

Shared context is a second dependence channel that family choice does not touch. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html] The adversarial error-propagation item concludes that generic self-verification by the same model class is not an independent safety layer because it inspects the same contaminated context, and that structured verification recovers errors through added constraints rather than reflection alone. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://arxiv.org/abs/2310.01798] The failure-mode taxonomy item flags that a co-located monitor processing the same external data can be compromised by the same injection as the primary agent, and records the fraction of monitoring deployments affected as unquantified. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html]

Independence in the verification item is graded, not binary. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html] That item builds its rubric from the Goguen-Meseguer non-interference property and the National Institute of Standards and Technology (NIST) Special Publication 800-53 Audit and Accountability separation requirement, and concludes every surveyed mechanism achieves bounded rather than absolute independence. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html; https://doi.org/10.1109/SP.1982.10014; https://csrc.nist.gov/pubs/sp/800/53/r5/final] Judge-based evaluation is already deployed as a release checkpoint in several tools, and its documented bias modes are the reason layered deterministic checks are paired with it. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-28-llm-as-judge-pipeline-validation-checkpoints.html; https://arxiv.org/abs/2306.05685]

No study located measures verifier accuracy against independent evidence while varying harness-verifier family and shared context together. [assumption; source: https://arxiv.org/abs/2506.07962] Failed search: query "goal attainment verifier accuracy model family alignment shared context agent harness" found judge self-preference and error-correlation papers but no agent-verifier factorial study; outcome: not found. [assumption; source: https://arxiv.org/abs/2404.13076]

**D. Cross-zone synthesis**

The only adjacent paper that studies several conflict factors jointly says earlier work treated them in isolation. [fact; source: https://arxiv.org/abs/2504.13079] Wang et al. (2025) built a dataset combining ambiguity, misinformation, and noise because prior work studied one aspect at a time, which matches the absence of multi-zone factorial studies found here. [fact; source: https://arxiv.org/abs/2504.13079]

The three-zone item's own convergence evidence rests on five curated architectures. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html] Cases chosen because they exhibit a pattern are a selection artefact risk for any claim about how often the pattern holds, and the same caution applies to leaderboard rows chosen for comparison. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

The three-zone item's asymmetric-write-access finding also frames which cross-effects are structural. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html] The adversarial-collaboration item states that perspective independence determines protection and that correlated perspectives protect less than their count implies. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-adversarial-agents-shared-goals-multi-perspective.html] Applied to verifiers, it suggests verifier-harness correlation shrinks a verification gain. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-adversarial-agents-shared-goals-multi-perspective.html; https://arxiv.org/abs/2506.07962]

### §3 Reasoning

1. Consumer-dependent metadata sensitivity means a pool annotation gain measured on one consumer need not carry to another. [inference; source: https://aclanthology.org/2024.blackboxnlp-1.24/]
2. Annotation helps only where source or time distinguishes the conflicting claims, so the gain scales with the share of conflicts that are freshness or credibility conflicts. [inference; source: https://arxiv.org/abs/2505.17762; https://arxiv.org/abs/2506.08500]
3. The masking advantage is measured on coding tasks only, so its transfer to other task families is a hypothesis. [inference; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2510.11967]
4. A structure-dependent gain that rests on a clean schema is exposed to pool noise, and the only direct noisy-corpus evidence is low confidence. [inference; source: https://github.com/kartikeyamandhar/graphrag-comparison]
5. A verifier shares errors with a harness through family, provider, and context, and these are separate channels. [inference; source: https://arxiv.org/abs/2506.07962; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html]
6. Independence of any one gain therefore needs a stated condition on each of the other two zones, and none can be certified from the single-zone studies alone. [inference; source: https://arxiv.org/abs/2504.13079]

### §4 Consistency Check

Tan et al. (2024) report consumer bias away from retrieved context, while Ge et al. (2025) report a credibility-metadata gain, and the two are compatible because the first measures a similarity-driven preference and the second measures a deliberate source signal on a fact-checking task. [inference; source: https://arxiv.org/abs/2401.11911; https://arxiv.org/abs/2505.17762]

```text
contradiction_scan: resolved
confidence_adjustment: noisy-corpus reversal kept at low; non-coding masking claim kept as untested
scope_guardrail: maintained; resolver ownership not assigned
```

### §5 Depth and Breadth Expansion

Technical lens: the zones interact through three objects, the annotation fields in the pool, the context the harness retains, and the context the verifier reads. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html] Masking or summarising removes content the verifier might need as independent evidence, so harness context choices can reduce verifier input quality. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html; https://arxiv.org/abs/2508.21433]

Economic lens: masking roughly halves token cost on the measured coding task, so a harness choice can change the budget available for a second verifier call. [inference; source: https://arxiv.org/abs/2508.21433] The verification item's append-only attestation and transparency-log layer adds cost that the single-zone studies do not price. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html]

Historical lens: sociotechnical theory found that optimising one subsystem alone degraded the combined system in coal-mining studies, which is the long-standing precedent for expecting interaction effects between separately tuned zones. [fact; source: https://open.ncl.ac.uk/theory-library/socio-technical-theory.pdf]

Behavioural lens: the context-engineering item reports that models are influenced by framing, so annotation wording is a candidate interaction with consumer behaviour. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html]

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

No study located varies more than one zone at a time, so the three gains cannot be certified as independent: the best-supported statement is that each gain is conditional on the consumer model, task family, pool noise, and verifier-harness dependence, and that independence should be assumed only where each condition is separately met. [inference; source: https://arxiv.org/abs/2504.13079; https://arxiv.org/abs/2506.07962] Pool-level source and time metadata changes consumer answers in a model-dependent way, and a credibility signal improved conflict resolution on one fact-checking dataset. [fact; source: https://aclanthology.org/2024.blackboxnlp-1.24/; https://arxiv.org/abs/2505.17762] The observation-masking advantage over summarisation is measured only on coding tasks, and structure-dependent pool gains have one low-confidence report of reversal on a noisy corpus. [fact; source: https://arxiv.org/abs/2508.21433; https://github.com/kartikeyamandhar/graphrag-comparison] Verifier accuracy depends on at least three dependence channels with the harness, family self-preference, cross-provider error correlation, and shared context, and the evidence supports treating independence as a graded property. [inference; source: https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2506.07962; https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html] The primary uncertainty is that every cross-zone condition stated here is an inference from single-zone studies and needs a factorial experiment. [inference; source: https://arxiv.org/abs/2504.13079]

**Key findings:**

1. Consumer models differ in how retrieved-document metadata changes their answers, since swapping publication time changed the answer for most models tested while changing the source mostly did not and appearance strongly affected one model family. ([fact]; medium confidence; source: https://aclanthology.org/2024.blackboxnlp-1.24/)
2. Adding source-credibility background information at retrieval and generation stages significantly improved conflict resolution on a fact-checking dataset, which is direct evidence for a pool-level credibility annotation benefit in that single task family. ([fact]; medium confidence; source: https://arxiv.org/abs/2505.17762)
3. Models can favour generated over retrieved context because of similarity to the question and segmentation damage, so a provenance annotation is not guaranteed to override a consumer's similarity-driven preference. ([inference]; medium confidence; source: https://arxiv.org/abs/2401.11911; https://aclanthology.org/2024.blackboxnlp-1.24/)
4. No study located serialises Provenance Ontology, Resource Description Framework-star, or minimal-justification overlays into consumer prompts and measures conflict resolution, so the proposed overlay effect on the context-collision categories remains an untested hypothesis. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html; https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html)
5. The measured masking advantage over summarisation comes from coding tasks, and the one non-coding result located compares context folding with summarisation, so the masking advantage on non-coding tasks is untested. ([inference]; medium confidence; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2510.11967)
6. Context-rot curves are model-specific and recall degrades non-uniformly with input length, so a mask depth tuned on one consumer model is not expected to transfer to another. ([inference]; medium confidence; source: https://www.trychroma.com/research/context-rot; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
7. An ontology-guided extraction gain of 3.17 percentage points on a clean benchmark is paired with a low-confidence report that a fixed-ontology pipeline lost 21.0 percentage points on a noisy corpus against 10.5 for a schema-free pipeline, and pool noise is a candidate predictor of reversal that remains a hypothesis. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://github.com/kartikeyamandhar/graphrag-comparison)
8. Language-model judges favour their own outputs and recognise them with non-trivial accuracy, reported independently by two groups on single-family judging tasks, and extension to agent verifiers is untested. ([fact]; medium confidence; source: https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2410.21819)
9. Across more than 350 models, errors are substantially correlated, with 60 percent agreement when both err on one leaderboard, and larger models have correlated errors even across distinct providers, so a different model family reduces but does not remove shared-error exposure. ([fact]; medium confidence; source: https://arxiv.org/abs/2506.07962)
10. Shared context is a dependence channel separate from model family, because a same-class verifier inspects the same contaminated context and a co-located monitor can be compromised by the same injection, with the monitor-compromise rate unquantified. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html)
11. Prior work on conflicting evidence reports that earlier studies treated ambiguity, misinformation, and noise one at a time, and no factorial study of the three zone interventions was located, so independence cannot be certified from existing evidence. ([inference]; medium confidence; source: https://arxiv.org/abs/2504.13079; https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html)

**Evidence map:**

Evidence map: see the Evidence Map table under Findings.

**Assumptions:**

Metadata sensitivity measured on webpage and fact-checking tasks is assumed to be informative for agent content pools. [assumption; source: https://aclanthology.org/2024.blackboxnlp-1.24/] The justification is that both involve a consumer model choosing between conflicting retrieved claims with metadata present. [assumption; source: https://arxiv.org/abs/2505.17762]

The coding-task masking result is assumed to be a usable baseline for non-coding harnesses. [assumption; source: https://arxiv.org/abs/2508.21433] The justification is that the context-folding study spans deep-research tasks and reports context-size effects of the same kind, although it tests a different comparison. [assumption; source: https://arxiv.org/abs/2510.11967]

**Analysis:**

The strongest design point is that the three zones share objects, and so an intervention in one zone alters the inputs of another. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html] The table below states each gain's independence conditions as inferences so a future experiment can falsify each. [inference; source: https://arxiv.org/abs/2504.13079]

| Gain | Treat as independent when | Shrinks or reverses when | Label and sources |
|---|---|---|---|
| Pool annotation (PROV-O, RDF-star, minimal justification) | Conflicts are freshness or credibility conflicts, the consumer is shown to attend to the metadata, and annotations sit outside any masked or summarised window. | The consumer prefers similarity or fluency over metadata, conflicts are complementary, or the harness drops annotation-bearing text. | [inference; source: https://aclanthology.org/2024.blackboxnlp-1.24/; https://arxiv.org/abs/2401.11911; https://arxiv.org/abs/2506.08500] |
| Harness masking over summarisation | The task has disposable raw observations, as in the measured coding tasks, and the consumer's recall curve is characterised. | Pool noise is high, annotations live inside older observations, or the consumer's context-rot curve differs. | [inference; source: https://arxiv.org/abs/2508.21433; https://www.trychroma.com/research/context-rot] |
| Verifier accuracy | The verifier reads evidence not derived from the harness context, differs in provider family, and uses deterministic checks where possible. | The verifier shares family, provider, or context with the harness, or the monitor reads the same external data. | [inference; source: https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2506.07962; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html] |

The noisy-corpus ontology reversal is a pool-property condition on a gain, and it does not refute the clean-benchmark result. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://github.com/kartikeyamandhar/graphrag-comparison] Leaderboard rows where richer agents beat minimal ones confound harness context management with other differences, so they do not contradict the controlled masking result. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html; https://arxiv.org/abs/2508.21433] Model-specific context-rot curves explain why a masking window may not transfer between consumers. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html] The co-located monitor case is a shared-context condition on the verifier gain, and its size remains unquantified. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html]

The three-zone convergence evidence and the leaderboard rows are selected cases, so they cannot establish how often each condition holds. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html; https://www.tbench.ai/leaderboard/terminal-bench/2.0] A change in pool content is a rival cause for any apparent harness or verifier effect, because corpus edits alone change behaviour with weights and prompts fixed. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html] Adversarial collaboration research states that correlated perspectives protect less than their count implies, which supports grading verifier independence rather than counting verifiers. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-adversarial-agents-shared-goals-multi-perspective.html] Judge-based pipeline checkpoints carry documented bias modes, so verifier placement does not by itself restore independence. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-28-llm-as-judge-pipeline-validation-checkpoints.html; https://arxiv.org/abs/2306.05685]

**Risks, gaps, uncertainties:**

- The Alchourron-Gardenfors-Makinson (AGM) postulate-violation figures from the context-collision item rest on an unreviewed submission and are not used as a quantitative anchor here. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html]
- The only noisy-corpus ontology comparison located is non-peer-reviewed, single-author, and small scale, so the reversal is low confidence. [fact; source: https://github.com/kartikeyamandhar/graphrag-comparison]
- Searches for overlay-on-consumer tests, non-coding masking comparisons, and agent-verifier factorial studies returned nothing relevant, so the corresponding conclusions rest on absence of located evidence. [inference; source: https://arxiv.org/abs/2504.13079]
- The agent-memory item found no standard benchmark scoring provenance fidelity at read time, so annotation quality has no agreed metric. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html]
- Resolver ownership between pool and consumer is deferred to issue #653 and affects which component applies annotations. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html]

**Open questions:**

- Does a masked or summarised harness window preserve per-statement annotations, and at what depth do annotations drop out for each consumer?
- What is the monitor-compromise rate when verifier and harness share external data sources?
- Does a factorial experiment crossing annotation, masking versus summarisation, and verifier family show interaction terms?

### §7 Recursive Review

Final pass notes:

```text
review_result: pass
acronym_audit: passed
parity_check: passed
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

No study located varies more than one zone at a time, so the three gains cannot be certified as independent: the best-supported statement is that each gain is conditional on the consumer model, task family, pool noise, and verifier-harness dependence, and that independence should be assumed only where each condition is separately met. [inference; source: https://arxiv.org/abs/2504.13079; https://arxiv.org/abs/2506.07962] Pool-level source and time metadata changes consumer answers in a model-dependent way, and a credibility signal improved conflict resolution on one fact-checking dataset. [fact; source: https://aclanthology.org/2024.blackboxnlp-1.24/; https://arxiv.org/abs/2505.17762] The observation-masking advantage over summarisation is measured only on coding tasks, and structure-dependent pool gains have one low-confidence report of reversal on a noisy corpus. [fact; source: https://arxiv.org/abs/2508.21433; https://github.com/kartikeyamandhar/graphrag-comparison] Verifier accuracy depends on at least three dependence channels with the harness, family self-preference, cross-provider error correlation, and shared context, and the evidence supports treating independence as a graded property. [inference; source: https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2506.07962; https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html] The primary uncertainty is that every cross-zone condition stated here is an inference from single-zone studies and needs a factorial experiment. [inference; source: https://arxiv.org/abs/2504.13079]

### Key Findings

1. Consumer models differ in how retrieved-document metadata changes their answers, since swapping publication time changed the answer for most models tested while changing the source mostly did not and appearance strongly affected one model family. ([fact]; medium confidence; source: https://aclanthology.org/2024.blackboxnlp-1.24/)
2. Adding source-credibility background information at retrieval and generation stages significantly improved conflict resolution on a fact-checking dataset, which is direct evidence for a pool-level credibility annotation benefit in that single task family. ([fact]; medium confidence; source: https://arxiv.org/abs/2505.17762)
3. Models can favour generated over retrieved context because of similarity to the question and segmentation damage, so a provenance annotation is not guaranteed to override a consumer's similarity-driven preference. ([inference]; medium confidence; source: https://arxiv.org/abs/2401.11911; https://aclanthology.org/2024.blackboxnlp-1.24/)
4. No study located serialises Provenance Ontology, Resource Description Framework-star, or minimal-justification overlays into consumer prompts and measures conflict resolution, so the proposed overlay effect on the context-collision categories remains an untested hypothesis. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html; https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html)
5. The measured masking advantage over summarisation comes from coding tasks, and the one non-coding result located compares context folding with summarisation, so the masking advantage on non-coding tasks is untested. ([inference]; medium confidence; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2510.11967)
6. Context-rot curves are model-specific and recall degrades non-uniformly with input length, so a mask depth tuned on one consumer model is not expected to transfer to another. ([inference]; medium confidence; source: https://www.trychroma.com/research/context-rot; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
7. An ontology-guided extraction gain of 3.17 percentage points on a clean benchmark is paired with a low-confidence report that a fixed-ontology pipeline lost 21.0 percentage points on a noisy corpus against 10.5 for a schema-free pipeline, and pool noise is a candidate predictor of reversal that remains a hypothesis. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://github.com/kartikeyamandhar/graphrag-comparison)
8. Language-model judges favour their own outputs and recognise them with non-trivial accuracy, reported independently by two groups on single-family judging tasks, and extension to agent verifiers is untested. ([fact]; medium confidence; source: https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2410.21819)
9. Across more than 350 models, errors are substantially correlated, with 60 percent agreement when both err on one leaderboard, and larger models have correlated errors even across distinct providers, so a different model family reduces but does not remove shared-error exposure. ([fact]; medium confidence; source: https://arxiv.org/abs/2506.07962)
10. Shared context is a dependence channel separate from model family, because a same-class verifier inspects the same contaminated context and a co-located monitor can be compromised by the same injection, with the monitor-compromise rate unquantified. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html)
11. Prior work on conflicting evidence reports that earlier studies treated ambiguity, misinformation, and noise one at a time, and no factorial study of the three zone interventions was located, so independence cannot be certified from existing evidence. ([inference]; medium confidence; source: https://arxiv.org/abs/2504.13079; https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Swapping publication time changes most models' answers; source swaps mostly do not; appearance affects Claude-3 | https://aclanthology.org/2024.blackboxnlp-1.24/ | medium | single study |
| [fact] Credibility information improves conflict resolution on a fact-checking dataset | https://arxiv.org/abs/2505.17762 | medium | fact-checking only |
| [inference] Similarity-driven consumer preference can override provenance | https://arxiv.org/abs/2401.11911; https://aclanthology.org/2024.blackboxnlp-1.24/ | medium | generated versus retrieved context |
| [inference] No overlay-on-consumer test located | https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html; https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html | low | absence of evidence |
| [inference] Masking advantage untested outside coding | https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2510.11967 | medium | folding is a different comparison |
| [inference] Mask depth is consumer-specific | https://www.trychroma.com/research/context-rot; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html | medium | 18-model evaluation |
| [fact] Ontology gain 3.17 points clean; 21.0 versus 10.5 point loss noisy | https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://github.com/kartikeyamandhar/graphrag-comparison | low | non-peer-reviewed |
| [fact] Judges favour and recognise own outputs | https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2410.21819 | medium | two independent groups |
| [fact] Errors correlated across 350+ models | https://arxiv.org/abs/2506.07962 | medium | single study |
| [inference] Shared context is a separate dependence channel | https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html | medium | rate unquantified |
| [inference] Independence cannot be certified from single-zone studies | https://arxiv.org/abs/2504.13079; https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html | medium | no factorial study |

### Assumptions

Metadata sensitivity measured on webpage and fact-checking tasks is assumed to be informative for agent content pools. [assumption; source: https://aclanthology.org/2024.blackboxnlp-1.24/] The justification is that both involve a consumer model choosing between conflicting retrieved claims with metadata present. [assumption; source: https://arxiv.org/abs/2505.17762]

The coding-task masking result is assumed to be a usable baseline for non-coding harnesses. [assumption; source: https://arxiv.org/abs/2508.21433] The justification is that the context-folding study spans deep-research tasks and reports context-size effects of the same kind, although it tests a different comparison. [assumption; source: https://arxiv.org/abs/2510.11967]

### Analysis

The strongest design point is that the three zones share objects, and so an intervention in one zone alters the inputs of another. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html] The table below states each gain's independence conditions as inferences so a future experiment can falsify each. [inference; source: https://arxiv.org/abs/2504.13079]

| Gain | Treat as independent when | Shrinks or reverses when | Label and sources |
|---|---|---|---|
| Pool annotation (PROV-O, RDF-star, minimal justification) | Conflicts are freshness or credibility conflicts, the consumer is shown to attend to the metadata, and annotations sit outside any masked or summarised window. | The consumer prefers similarity or fluency over metadata, conflicts are complementary, or the harness drops annotation-bearing text. | [inference; source: https://aclanthology.org/2024.blackboxnlp-1.24/; https://arxiv.org/abs/2401.11911; https://arxiv.org/abs/2506.08500] |
| Harness masking over summarisation | The task has disposable raw observations, as in the measured coding tasks, and the consumer's recall curve is characterised. | Pool noise is high, annotations live inside older observations, or the consumer's context-rot curve differs. | [inference; source: https://arxiv.org/abs/2508.21433; https://www.trychroma.com/research/context-rot] |
| Verifier accuracy | The verifier reads evidence not derived from the harness context, differs in provider family, and uses deterministic checks where possible. | The verifier shares family, provider, or context with the harness, or the monitor reads the same external data. | [inference; source: https://arxiv.org/abs/2404.13076; https://arxiv.org/abs/2506.07962; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html] |

The noisy-corpus ontology reversal is a pool-property condition on a gain, and it does not refute the clean-benchmark result. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://github.com/kartikeyamandhar/graphrag-comparison] Leaderboard rows where richer agents beat minimal ones confound harness context management with other differences, so they do not contradict the controlled masking result. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html; https://arxiv.org/abs/2508.21433] Model-specific context-rot curves explain why a masking window may not transfer between consumers. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html] The co-located monitor case is a shared-context condition on the verifier gain, and its size remains unquantified. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html]

The three-zone convergence evidence and the leaderboard rows are selected cases, so they cannot establish how often each condition holds. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html; https://www.tbench.ai/leaderboard/terminal-bench/2.0] A change in pool content is a rival cause for any apparent harness or verifier effect, because corpus edits alone change behaviour with weights and prompts fixed. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html] Adversarial collaboration research states that correlated perspectives protect less than their count implies, which supports grading verifier independence rather than counting verifiers. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-adversarial-agents-shared-goals-multi-perspective.html] Judge-based pipeline checkpoints carry documented bias modes, so verifier placement does not by itself restore independence. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-28-llm-as-judge-pipeline-validation-checkpoints.html; https://arxiv.org/abs/2306.05685]

### Risks, Gaps, and Uncertainties

- The Alchourron-Gardenfors-Makinson (AGM) postulate-violation figures from the context-collision item rest on an unreviewed submission and are not used as a quantitative anchor here. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html]
- The only noisy-corpus ontology comparison located is non-peer-reviewed, single-author, and small scale, so the reversal is low confidence. [fact; source: https://github.com/kartikeyamandhar/graphrag-comparison]
- Searches for overlay-on-consumer tests, non-coding masking comparisons, and agent-verifier factorial studies returned nothing relevant, so the corresponding conclusions rest on absence of located evidence. [inference; source: https://arxiv.org/abs/2504.13079]
- The agent-memory item found no standard benchmark scoring provenance fidelity at read time, so annotation quality has no agreed metric. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html]
- Resolver ownership between pool and consumer is deferred to issue #653 and affects which component applies annotations. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html]

### Open Questions

- Does a masked or summarised harness window preserve per-statement annotations, and at what depth do annotations drop out for each consumer?
- What is the monitor-compromise rate when verifier and harness share external data sources?
- Does a factorial experiment crossing annotation, masking versus summarisation, and verifier family show interaction terms?

---

## Output

- Type: knowledge
- Description: A conditional-independence table for the three zone gains with falsifiable conditions, and a list of untested cross-effects. [inference; source: https://arxiv.org/abs/2504.13079; https://arxiv.org/abs/2506.07962]
- Links: https://arxiv.org/abs/2506.07962; https://aclanthology.org/2024.blackboxnlp-1.24/; https://arxiv.org/abs/2508.21433
