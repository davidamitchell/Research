---
title: "Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy"
added: 2026-07-20T09:07:23+00:00
status: reviewing
priority: high
blocks: []
themes: [agentic-ai, memory-context, benchmarks-eval, rag-retrieval]
started: 2026-07-20T22:19:39+00:00
completed: ~
output: []
cites: [2026-03-02-agent-memory-management-context-injection, 2026-03-17-ai-memory-systems-rag-neuroscience, 2026-05-02-knowledge-graph-schema-cross-session-research-mcp]
related: [2026-07-20-agent-memory-forgetting-information-curation, 2026-07-20-agent-memory-consolidation-episodic-semantic, 2026-07-20-hybrid-agent-memory-symbolic-connectionist-synchronisation, 2026-07-20-privacy-preserving-agent-long-term-memory]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy

## Research Question

What benchmark suite and metric design best measures the quality, relevance, retrieval accuracy, freshness, and governance correctness of agentic memory systems across heterogeneous tasks?

## Scope

**In scope:**
- Existing long-term memory benchmarks and datasets for conversational or agentic systems, including where they measure recall well and where they fail to capture utility or governance
- Metric design for retrieval correctness, relevance, temporal freshness, provenance fidelity, contradiction handling, latency, and downstream task impact
- How evaluation should differ across memory types: episodic, semantic, procedural, and hybrid graph-based stores built on Retrieval-Augmented Generation (RAG) architectures
- Whether a unified suite should combine synthetic benchmarks, replay-based evaluation, and in-the-loop task outcome measures
- Failure cases such as privacy leakage, scope contamination, stale-memory retrieval, and over-retention of irrelevant context

**Out of scope:**
- Implementation of a new benchmark harness in this repository
- Memory-architecture design choices except where needed to define what the metric must observe
- General Large Language Model (LLM) evaluations unrelated to persistent or cross-session memory

**Constraints:** Prioritise public 2024-2026 benchmarks and evaluation papers. Distinguish clearly between metrics that test recall accuracy and metrics that test governance, utility, or safety, because prior repository work found those are often conflated.

## Context

The earlier agent-memory survey found that LongMemEval and LoCoMo provide useful recall benchmarks but do not establish a shared industry standard, and they do not test governance, provenance, or scoping correctness. That leaves the rest of the memory stack hard to compare. This item asks what a truly decision-useful evaluation framework would need to measure before the other items in this cluster can be compared rigorously.

## Approach

1. Catalogue existing memory benchmarks and identify exactly which failure modes each can and cannot detect.
2. Separate memory-quality dimensions: recall, relevance, freshness, provenance, latency, utility, privacy leakage, and scope correctness.
3. Compare benchmark styles: fixed datasets, long-horizon replay, task-based agent evaluation, and human-judged usefulness.
4. Investigate how graph-based and hybrid memory systems are currently evaluated, including whether multi-hop retrieval needs distinct metrics.
5. Synthesize a benchmark framework that could serve as the measuring stick for the curation, consolidation, and hybrid-memory questions in this cluster.

## Sources

- [x] [Wu et al. (2024) LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813): long-term interactive memory benchmark for chat assistants; defines five core abilities (information extraction, multi-session reasoning, knowledge updates, temporal reasoning, abstention)
- [x] [Maharana et al. (2024) Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)](https://github.com/snap-research/LoCoMo): long conversational memory dataset and evaluation code for question answering and event-summarization tasks
- [x] [GraphRAG-Bench/GraphRAG-Benchmark (2025) When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark): benchmark framework for graph-based Retrieval-Augmented Generation systems; corrected from the seeded `microsoft/graphrag-bench` URL, which returns HTTP 404 (paper: [arXiv:2506.05690](https://arxiv.org/abs/2506.05690))
- [x] [AlShikh et al. (2025) Towards Outcome-Oriented, Task-Agnostic Evaluation of AI Agents](https://arxiv.org/abs/2511.08242): evaluation framing beyond narrow component metrics, argues for outcome-based rather than infrastructure-based metrics
- [x] [GitHub Blog (2026) Building an agentic memory system for GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/): production view of validity, freshness, and citation-based verification as evaluation targets
- [x] [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html): prior corpus baseline on benchmark gaps and memory-quality concerns
- [x] [Hu et al. (2025) Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (MemoryAgentBench)](https://arxiv.org/abs/2507.05257): added during investigation; defines four competencies (accurate retrieval, test-time learning, long-range understanding, conflict resolution) for incremental, multi-turn agent memory evaluation


## Related

- [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [Mitchell (2026) Artificial Intelligence memory systems: Retrieval-Augmented Generation, vendor implementations, and neuroscience foundations](https://davidamitchell.github.io/Research/research/2026-03-17-ai-memory-systems-rag-neuroscience.html)
- [Mitchell (2026) What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence agent using the Model Context Protocol memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. sections 0 through 5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: What benchmark suite and metric design best measures the quality, relevance, retrieval accuracy, freshness, and governance correctness of agentic memory systems across heterogeneous tasks?
Scope: In scope is metric design across recall, relevance, freshness, provenance, contradiction handling, latency, and downstream utility, plus a review of existing benchmarks that cover episodic, semantic, procedural, and graph-based memory stores. Out of scope is building a new benchmark harness in this repository and general Large Language Model (LLM) evaluation unrelated to persistent memory.
Constraints: Prioritise public 2024-2026 benchmarks and evaluation papers; keep recall-accuracy metrics analytically separate from governance, utility, and safety metrics, because prior repository work on this cluster found those dimensions are frequently conflated in vendor evaluation claims.
Working hypothesis [assumption]: no single public benchmark measures all of recall, freshness, provenance, and governance correctness together, so a decision-useful framework must combine multiple existing benchmark styles rather than adopt one as sufficient. Justification: the prior repository item on agent memory management explicitly flagged this gap as unresolved. (source: [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html))

### §1 Question Decomposition

1. What existing benchmarks measure agentic long-term memory, and which specific failure modes can each detect or not detect?
   1.1 What does LongMemEval measure and what does it explicitly not measure?
   1.2 What does LoCoMo measure and what does it explicitly not measure?
   1.3 What does MemoryAgentBench measure and what does it explicitly not measure?
   1.4 What does GraphRAG-Bench measure for graph-structured memory and retrieval, and how does it differ from single-hop recall benchmarks?
2. How should memory-quality dimensions be separated analytically?
   2.1 What is the difference between a recall metric and a relevance metric?
   2.2 What is the difference between a freshness metric and a contradiction-handling metric?
   2.3 What would a provenance-fidelity metric need to observe that recall metrics do not capture?
   2.4 What would a governance or privacy-leakage metric need to observe that quality metrics do not capture?
3. What benchmark styles exist and what are their comparative strengths and weaknesses?
   3.1 What can a fixed-dataset benchmark measure that a live task-based evaluation cannot, and vice versa?
   3.2 What does a production A/B test (in the sense of a controlled comparison between two live variants) measure that a static benchmark cannot?
4. How are graph-based and hybrid memory systems currently evaluated, and do they need distinct metrics from flat vector-store memory?
   4.1 Does multi-hop retrieval require a distinct accuracy metric from single-hop question answering (QA)?
5. What would a synthesised, decision-useful evaluation framework look like, and what would it need to borrow from each existing benchmark style?

### §2 Investigation

**1.1 LongMemEval.** LongMemEval is a benchmark for chat assistants that tests five distinct abilities: information extraction (finding a specific fact anywhere in a long, multi-session history), multi-session reasoning (aggregating facts distributed across non-consecutive sessions), knowledge updates (correctly using the newest version of a fact when an earlier one has been superseded), temporal reasoning (correctly ordering or filtering by time), and abstention (declining to answer when the premise is unsupported by the history). [fact; source: https://arxiv.org/abs/2410.10813] The benchmark reports task-specific accuracy per ability rather than a single aggregate score, which lets an evaluator separate a system's raw recall competence from its temporal and conflict-resolution competence. [inference; source: https://arxiv.org/abs/2410.10813] LongMemEval does not evaluate provenance fidelity, privacy scoping, or downstream task utility outside the question-answering setting; it is a chat-transcript recall and reasoning benchmark, not a governance or task-outcome benchmark. [inference; source: https://arxiv.org/abs/2410.10813]

**1.2 LoCoMo.** LoCoMo is a very long-term conversational memory dataset built from ten synthetically generated long conversations, each annotated for question-answering and event-summarization tasks, with dialogue that can additionally support multimodal-dialogue-generation tasks. [fact; source: https://github.com/snap-research/LoCoMo] Because the conversations and question-answer pairs are LLM-generated rather than drawn from real user interaction logs, LoCoMo's recall accuracy numbers describe performance on synthetic long-horizon dialogue rather than on production memory traffic, which limits how directly its scores transfer to an agentic coding or research assistant deployment. [inference; source: https://github.com/snap-research/LoCoMo] LoCoMo does not test knowledge updates, temporal filtering, or governance correctness as separate axes the way LongMemEval does; its annotation schema is built around recall and summarization quality. [inference; source: https://github.com/snap-research/LoCoMo]

**1.3 MemoryAgentBench.** MemoryAgentBench evaluates agent memory across four competencies: accurate retrieval (precisely locating a target fact in a long interaction history, including multi-hop retrieval), test-time learning (immediately applying a new rule or fact introduced mid-session without parameter updates), long-range understanding (forming an abstracted, global understanding of an extended interaction rather than only piecemeal recall), and conflict resolution (reconciling contradictory or updated facts, such as replacing an outdated address with a corrected one). [fact; source: https://arxiv.org/abs/2507.05257] The benchmark uses an incremental, multi-turn evaluation protocol, meaning memory is built up and queried progressively rather than presented as a single static context window, which more closely matches how an agentic system accumulates memory across a session. [inference; source: https://arxiv.org/abs/2507.05257] Reported empirical results show that no evaluated architecture reliably mastered all four competencies simultaneously, with conflict resolution and test-time learning the weakest, which corroborates the prior repository finding that recall benchmarks understate the difficulty of update-handling. [inference; source: https://arxiv.org/abs/2507.05257]

**1.4 GraphRAG-Bench.** GraphRAG-Bench evaluates graph-based Retrieval-Augmented Generation (RAG) systems across four difficulty levels: fact retrieval, complex reasoning, contextual summarization, and creative generation, each scored with accuracy and a Recall-Oriented Understudy for Gisting Evaluation (ROUGE-L) overlap metric where applicable. [fact; source: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark] The benchmark's own stated motivation is that GraphRAG frequently underperforms vanilla RAG on many real-world tasks, and the benchmark was built specifically to identify when graph structure provides a measurable benefit rather than to assume it always does. [fact; source: https://arxiv.org/abs/2506.05690] This framing implies that a memory-evaluation suite covering graph-based or hybrid stores needs a task-difficulty gradient (single-hop fact lookup through multi-hop reasoning to open-ended synthesis) rather than a single recall number, because graph structure's benefit is difficulty-dependent rather than uniform. [inference; source: https://arxiv.org/abs/2506.05690]

**2.1 Recall versus relevance.** A recall metric asks whether the correct fact was retrieved at all (a binary hit or a ranked position such as top-k), whereas a relevance metric asks whether the retrieved set is proportionate to the query, penalizing over-retrieval of tangential context even when the target fact is present. [inference; source: https://arxiv.org/abs/2410.10813] LongMemEval's evidence-recall-and-precision protocol operationalizes this distinction directly by scoring both whether the needed session was retrieved and how much irrelevant context accompanied it. [fact; source: https://arxiv.org/abs/2410.10813]

**2.2 Freshness versus contradiction handling.** A freshness metric checks whether a system uses the most recently valid version of a fact, typically by comparing an answer against a `valid_at` or update timestamp. [inference; source: https://arxiv.org/abs/2410.10813] A contradiction-handling metric checks a distinct capability: whether the system detects that two stored facts conflict and applies an explicit resolution policy, rather than merely defaulting to recency. [inference; source: https://arxiv.org/abs/2507.05257] LongMemEval's knowledge-update tasks conflate these two by testing only whether the newest fact is used, and MemoryAgentBench's conflict-resolution axis is the source that separately tests explicit conflict detection and reconciliation, which is why a decision-useful framework needs both benchmark styles rather than either alone. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257]

**2.3 Provenance fidelity.** None of LongMemEval, LoCoMo, or MemoryAgentBench score whether a system's stored memory correctly attributes a fact to a verifiable source location; each treats the correctness of the answer as the unit of evaluation, not the correctness of the citation trail behind it. [inference; source: https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://arxiv.org/abs/2507.05257] A production counter-example exists: GitHub Copilot's agentic memory system stores every fact with citations to specific code locations and verifies those citations at read time before the memory is used, which converts provenance into a directly observable, checkable property (does the citation point to real content that still supports the claim) rather than an implicit trust assumption. [fact; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/] A provenance-fidelity metric can therefore be defined operationally as the proportion of retrieved memories whose citations resolve to content that still supports the stored claim, which is a directly measurable analogue to the accuracy metrics already used in recall benchmarks. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

**2.4 Governance and privacy-leakage metrics.** GitHub's production system scopes memories so they can only be created from and used within the same repository, and the team explicitly stress-tested resilience by seeding adversarial memories, facts that contradicted the codebase with citations pointing to nonexistent or irrelevant locations, and measured whether the agent detected and corrected them. [fact; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/] This demonstrates a governance-metric pattern distinct from quality metrics: an adversarial-injection test rate (the proportion of seeded bad memories detected and corrected) and a scope-boundary test (whether memory ever crosses a defined access boundary), neither of which is captured by recall, relevance, or freshness scores. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/] None of the three academic benchmarks reviewed (LongMemEval, LoCoMo, MemoryAgentBench) include a privacy-scoping or adversarial-injection test as a scored axis. [inference; source: https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://arxiv.org/abs/2507.05257]

**3.1 Fixed-dataset versus task-based live evaluation.** A fixed-dataset benchmark such as LongMemEval or LoCoMo can isolate a specific capability (for example, temporal reasoning) under controlled, reproducible conditions and enables direct cross-system comparison on identical inputs, but it cannot measure whether the retrieved memory changes a downstream task outcome in a live deployment. [inference; source: https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo] The Outcome-Oriented, Task-Agnostic evaluation paper argues that infrastructure-focused metrics such as latency or throughput do not capture whether an agent's decisions produce the intended business or task outcome, and proposes outcome-based metrics such as a goal completion rate instead. [fact; source: https://arxiv.org/abs/2511.08242] This argument transfers directly to memory evaluation: a memory system can score well on a fixed recall benchmark while still failing to move a real task-outcome metric if the retrieved memory is technically correct but not the memory that was decision-relevant for the task at hand. [inference; source: https://arxiv.org/abs/2511.08242]

**3.2 Production A/B testing (a controlled comparison between two live system variants).** GitHub measured its memory system's real-world impact with an A/B test comparing agents with and without memory, reporting a 3 percentage point increase in code-review precision and a 4 percentage point increase in recall when memory was enabled, plus a separate developer-facing metric of a 7 percent increase in one pull-request outcome measure for the coding agent. [fact; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/] This is a task-outcome measure in the sense the Outcome-Oriented evaluation paper calls for, and it is only obtainable through live deployment, not through any of the three static benchmarks reviewed, because a static benchmark has no mechanism for observing a downstream workflow-level effect. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/; https://arxiv.org/abs/2511.08242]

**4.1 Multi-hop retrieval and graph-structured memory.** GraphRAG-Bench's difficulty levels move from single-fact retrieval to complex reasoning that requires connecting multiple entities across a graph structure, and the benchmark's own motivating question, given that GraphRAG frequently underperforms vanilla RAG, is precisely whether graph structure earns its complexity cost on multi-hop tasks. [fact; source: https://arxiv.org/abs/2506.05690] This implies that a memory-evaluation suite covering hybrid or graph-based stores needs a metric that isolates multi-hop accuracy specifically, separate from single-hop recall, because a system can score well on single-hop fact lookup while failing at reasoning that requires traversing more than one relation. [inference; source: https://arxiv.org/abs/2506.05690] None of the flat-context benchmarks (LongMemEval, LoCoMo, MemoryAgentBench) test multi-hop graph traversal directly; MemoryAgentBench's accurate-retrieval axis does include multi-hop retrieval as a sub-case, but not graph-structured multi-hop traversal specifically. [inference; source: https://arxiv.org/abs/2507.05257]

Access note: `arxiv.org/pdf/2511.08242` fetch returned raw Portable Document Format (PDF) bytes, not renderable text; claims corroborated via secondary web-search summary of the abstract, not full-text read.

### §3 Reasoning

The evidence converges on a five-axis separation that no single existing benchmark covers in full: recall/relevance (LongMemEval, LoCoMo, GraphRAG-Bench fact-retrieval level), freshness and conflict resolution (LongMemEval knowledge-updates plus MemoryAgentBench conflict-resolution), provenance fidelity (demonstrated only in GitHub's production citation-verification system, not in any academic benchmark reviewed), governance and privacy scoping (demonstrated only in GitHub's adversarial-injection stress test), and downstream task outcome (demonstrated only through live A/B measurement, argued for conceptually by the Outcome-Oriented evaluation paper). [inference; source: https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://arxiv.org/abs/2507.05257; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/; https://arxiv.org/abs/2511.08242] Graph-structured and hybrid memory stores add a sixth consideration, a difficulty gradient from single-hop to multi-hop retrieval, that flat-context benchmarks do not exercise. [inference; source: https://arxiv.org/abs/2506.05690] A synthesised framework therefore cannot be a single dataset; it must be a composite of benchmark styles, each contributing the axis it is actually built to measure, because no reviewed benchmark or production report combines all axes into one scored suite. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

### §4 Consistency Check

```text
contradiction_scan: resolved
confidence_adjustment: multi-hop-vs-flat-context claim kept at medium because only one graph benchmark (GraphRAG-Bench) was directly reviewed
scope_guardrail: maintained; implementation of a new harness excluded per Scope
source_pdf_limitation: noted as an assumption in §2, not carried into Findings as a sourced fact
```

### §5 Depth and Breadth Expansion

**Technical lens:** The GitHub production case shows that provenance and governance metrics require instrumentation that a static dataset cannot provide, specifically a live citation-resolution check and an adversarial-seeding harness, which means a decision-useful framework must specify not just what to measure but what runtime hooks (citation storage, access-scope tagging) are prerequisites for measuring it at all. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

**Economic lens:** The Outcome-Oriented evaluation paper's central argument, that infrastructure metrics do not capture business value, implies that a memory-evaluation framework justified only by academic recall scores risks under-selling or over-selling a system relative to its actual operational cost and benefit; GitHub's reported precision and recall percentage-point deltas are a more decision-relevant number for a deployment decision than any static-benchmark accuracy score, because they are measured against the same downstream metric a deployment decision would use. [inference; source: https://arxiv.org/abs/2511.08242; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

**Behavioural lens:** MemoryAgentBench's finding that conflict resolution and test-time learning are the weakest competencies across evaluated architectures suggests that agentic memory systems are more likely to fail silently at handling contradictory information than at basic recall, which means an evaluation framework that only reports an aggregate accuracy score would systematically mask the failure mode most likely to cause a user-visible error, such as an agent acting on a stale fact. [inference; source: https://arxiv.org/abs/2507.05257]

**Historical/methodological lens:** LoCoMo's first public release (per its repository's own release notes) contained fifty conversations and was later reduced to a curated ten-conversation subset for cost-effective evaluation of closed-source LLMs, which illustrates a recurring trade-off in this benchmark class between dataset scale and evaluation cost, a trade-off that a synthesised framework should treat as an explicit design parameter rather than an incidental detail. [fact; source: https://github.com/snap-research/LoCoMo]

### §6 Synthesis

**Executive summary:**

No single existing public benchmark measures agentic memory quality across all of recall, freshness, provenance, governance, and downstream task outcome; each reviewed benchmark or production system covers a distinct subset, and a decision-useful evaluation framework must be a composite of at least four complementary evaluation styles rather than one dataset. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

**Key findings:**

See Findings section below (mirrored).

**Evidence map:**

See Findings section below (mirrored).

**Assumptions:**

See Findings section below (mirrored).

**Analysis:**

See Findings section below (mirrored).

**Risks, gaps, uncertainties:**

See Findings section below (mirrored).

**Open questions:**

See Findings section below (mirrored).

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed (LLM, RAG, QA, PDF, ROUGE-L expanded at first use)
claim_label_audit: passed (all §2-§5 claims carry fact/inference/assumption labels)
parity_check: passed (Findings mirrors §6 Synthesis content)
self_referential_citation_audit: passed (no citations to this file's own sections)
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

No single existing public benchmark measures agentic memory quality across all of recall, freshness, provenance, governance, and downstream task outcome; each reviewed benchmark or production system covers a distinct subset. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/] LongMemEval and MemoryAgentBench together provide the strongest coverage of recall, temporal reasoning, and conflict resolution for flat conversational memory, but neither tests provenance fidelity or privacy scoping. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257] Provenance fidelity and governance correctness are demonstrated only in a production system, GitHub Copilot's citation-based memory verification, not in any academic benchmark reviewed, which means an evaluation framework borrowing only from academic datasets would leave those two dimensions unmeasured. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/] Graph-structured and hybrid memory stores need an additional multi-hop-versus-single-hop difficulty gradient that flat-context benchmarks do not exercise. [inference; source: https://arxiv.org/abs/2506.05690] A decision-useful evaluation framework for this repository's memory-cluster items should therefore combine a fixed recall-and-reasoning dataset, an incremental conflict-resolution benchmark, a provenance-verification check modeled on the GitHub citation pattern, an adversarial governance-scoping stress test, and a live task-outcome measurement, rather than rely on any single existing suite. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/; https://arxiv.org/abs/2511.08242]

### Key Findings

1. LongMemEval separately scores five distinct memory abilities, information extraction, multi-session reasoning, knowledge updates, temporal reasoning, and abstention, and this per-ability scoring is what lets an evaluator distinguish raw recall competence from conflict and temporal competence rather than reading a single blended accuracy number. ([fact]; high confidence; source: https://arxiv.org/abs/2410.10813)
2. LoCoMo's ten-conversation evaluation set is synthetically generated by prompting two LLM agents with assigned personas rather than sampled from real user interaction logs, which limits how directly its recall accuracy numbers transfer to production agentic memory traffic. ([inference]; medium confidence; source: https://github.com/snap-research/LoCoMo)
3. MemoryAgentBench defines four competencies for incremental agent memory, accurate retrieval, test-time learning, long-range understanding, and conflict resolution, and reports that no evaluated architecture reliably mastered all four simultaneously, with conflict resolution and test-time learning the weakest. ([fact]; high confidence; source: https://arxiv.org/abs/2507.05257)
4. GraphRAG-Bench was built specifically because GraphRAG frequently underperforms vanilla Retrieval-Augmented Generation (RAG) on real-world tasks, and its four-level difficulty gradient from fact retrieval to creative generation exists to isolate exactly when graph structure earns its added complexity cost. ([fact]; high confidence; source: https://arxiv.org/abs/2506.05690)
5. None of LongMemEval, LoCoMo, or MemoryAgentBench score whether a stored memory's provenance, its attribution to a verifiable source, remains accurate at read time; each treats answer correctness as the unit of evaluation rather than citation-trail correctness. ([inference]; medium confidence; source: https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://arxiv.org/abs/2507.05257)
6. GitHub Copilot's production memory system stores every memory with citations to specific code locations and verifies those citations before use, converting provenance fidelity into a directly measurable proportion of memories whose citations still support the stored claim. ([fact]; high confidence; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
7. GitHub's team stress-tested governance correctness by deliberately seeding adversarial memories with citations pointing to nonexistent or irrelevant code locations and measuring whether agents detected and corrected them, a governance metric class absent from all three academic benchmarks reviewed. ([inference]; medium confidence; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
8. A live A/B test (a controlled comparison between two deployed system variants) on GitHub Copilot code review found memory usage produced a 3 percentage point increase in precision and a 4 percentage point increase in recall, a downstream task-outcome measurement obtainable only through production deployment and not through any of the static benchmarks reviewed. ([fact]; high confidence; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
9. The Outcome-Oriented, Task-Agnostic evaluation paper argues that infrastructure-focused metrics such as latency and throughput fail to capture whether an agent's decisions produce the intended task or business outcome, and proposes outcome-based metrics such as a goal completion rate instead. ([fact]; medium confidence; source: https://arxiv.org/abs/2511.08242)
10. A freshness metric (using the most recently valid fact) and a conflict-resolution metric (detecting and reconciling contradictory facts) test analytically distinct capabilities, and LongMemEval's knowledge-update tasks test only the former while MemoryAgentBench's conflict-resolution axis is the reviewed source that separately tests the latter. ([inference]; medium confidence; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257)
11. A decision-useful evaluation framework for graph-based or hybrid agentic memory needs a multi-hop-specific accuracy metric distinct from single-hop recall, because GraphRAG-Bench's difficulty gradient shows that a system can succeed at single-fact lookup while failing at reasoning that requires traversing more than one relation. ([inference]; medium confidence; source: https://arxiv.org/abs/2506.05690)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] LongMemEval scores five distinct memory abilities separately | https://arxiv.org/abs/2410.10813 | high | Primary arXiv paper abstract and corroborating search summary |
| [inference] LoCoMo's synthetic generation limits production transfer of its recall numbers | https://github.com/snap-research/LoCoMo | medium | Repository README states LLM-agent-generated conversations |
| [fact] MemoryAgentBench defines four competencies and finds no architecture masters all four | https://arxiv.org/abs/2507.05257 | high | arXiv abstract corroborated by secondary summary |
| [fact] GraphRAG-Bench built because GraphRAG underperforms vanilla RAG on real tasks | https://arxiv.org/abs/2506.05690 | high | Stated directly in the benchmark repository and paper abstract |
| [inference] No reviewed academic benchmark scores provenance fidelity | https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://arxiv.org/abs/2507.05257 | medium | Absence-of-metric inference across three sources' documented scoring schemes |
| [fact] GitHub Copilot verifies citations before using a stored memory | https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/ | high | Directly described in the production engineering blog post |
| [inference] Adversarial-injection stress testing is a governance metric class absent from academic benchmarks | https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/ | medium | Comparative absence inferred, not directly stated by any single source |
| [fact] Live A/B test showed 3-point precision and 4-point recall increase from memory | https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/ | high | Directly reported production metric |
| [fact] Outcome-Oriented paper argues for outcome metrics over infrastructure metrics | https://arxiv.org/abs/2511.08242 | medium | PDF body not directly renderable; corroborated via secondary abstract summary, not full-text read |
| [inference] Freshness and conflict-resolution are analytically distinct capabilities requiring separate metrics | https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257 | medium | Derived by comparing the two benchmarks' scoring schemes |
| [inference] Graph-based memory needs a multi-hop-specific metric distinct from single-hop recall | https://arxiv.org/abs/2506.05690 | medium | Derived from the benchmark's stated difficulty-gradient design rationale |

### Assumptions

No single public benchmark reviewed combines recall, freshness, provenance, governance, and task-outcome measurement into one scored suite. [assumption; source: https://arxiv.org/abs/2410.10813] This is based on reviewing the four benchmarks and one production report cited in this item rather than an exhaustive survey of every published memory benchmark, so an unreviewed benchmark could in principle combine more axes than assumed here.

The web-search summary of the Outcome-Oriented evaluation paper's eleven-metric structure and goal-completion-rate framing is treated as an accurate paraphrase of the paper's abstract. [assumption; source: https://arxiv.org/abs/2511.08242] This is because the paper's PDF body could not be rendered as text through the available fetch tool in this session, so the claim rests on a secondary summary rather than a direct read of the full paper.

### Analysis

The four reviewed sources split cleanly along the axis they were each built to measure, and none overlaps with another's core contribution. LongMemEval and MemoryAgentBench both address flat conversational memory but emphasize different sub-problems: LongMemEval isolates recall, temporal reasoning, and abstention against a static long-history dataset, while MemoryAgentBench isolates conflict resolution and test-time learning against an incremental, multi-turn protocol. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257] Neither academic benchmark reaches provenance or governance correctness, which only appears as a measured property in GitHub's production system; this gap is not a benchmark-design oversight so much as a difference in what is observable, provenance verification requires a live citation-resolution mechanism that a static dataset cannot simulate without also simulating the underlying code or knowledge base the citations point to. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

A plausible rival position is that task-outcome measurement (live A/B testing) alone is sufficient and that component-level benchmarks such as LongMemEval are unnecessary academic exercises. This is not well supported: the Outcome-Oriented paper's own argument is that outcome metrics should supplement, not replace, more granular measurement, because an aggregate outcome metric cannot localize which specific capability, recall, freshness, or conflict handling, caused a failure. [inference; source: https://arxiv.org/abs/2511.08242] The GitHub case supports this: the team combined component-level stress testing (adversarial-injection resilience) with an aggregate outcome measure (the A/B precision and recall deltas), rather than relying on the aggregate measure alone. [inference; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]

Graph-based memory evaluation is the least mature area reviewed. Only one benchmark, GraphRAG-Bench, was directly examined, and its own stated motivation, that graph structure often fails to outperform simpler retrieval, argues against assuming graph-specific metrics matter for every memory system; a hybrid or graph-augmented memory design should be evaluated with a graph-specific multi-hop metric only when the design actually claims a multi-hop reasoning benefit, not by default. [inference; source: https://arxiv.org/abs/2506.05690]

### Risks, Gaps, and Uncertainties

- Only one graph-based memory benchmark (GraphRAG-Bench) was directly reviewed, so the claim that flat-context benchmarks are insufficient for graph-structured memory rests on a single source rather than cross-benchmark corroboration. [assumption; source: https://arxiv.org/abs/2506.05690]
- The Outcome-Oriented evaluation paper's eleven-metric framework was reviewed through a secondary summary rather than the full PDF text, so its specific metric definitions could not be independently verified in this session. [assumption; source: https://arxiv.org/abs/2511.08242]
- GitHub's reported A/B test percentages (3 percentage point precision increase, 4 percentage point recall increase, 7 percent pull-request outcome increase) come from a single vendor's internal deployment and have not been independently replicated or peer-reviewed, so they should be read as a production existence proof of measurability rather than as a generalizable effect size. [assumption; source: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]
- No source reviewed in this item evaluates procedural memory (stored skills or reusable action sequences) as a distinct evaluation target; all four sources address episodic, semantic, or graph-relational memory, leaving procedural-memory evaluation design an open gap for this cluster.

### Open Questions

- What would a procedural-memory-specific benchmark need to measure, given that none of the four reviewed sources addresses procedural memory directly? This could seed a new backlog item scoped to procedural or skill-memory evaluation.
- Can a provenance-verification mechanism modeled on GitHub's citation-checking pattern be adapted to a non-code domain (for example, a research or knowledge-management agent) where "citation" means a document passage or a prior research item rather than a code location?
- What would an adversarial governance-scoping test suite look like for a multi-tenant research or knowledge system, distinct from GitHub's single-repository scoping model?

---

## Output

- Type: knowledge
- Description: A synthesised evaluation framework showing that agentic memory quality requires at least five distinct measurement styles, recall/relevance benchmarking, incremental conflict-resolution testing, provenance-verification checking, adversarial governance stress testing, and live task-outcome measurement, because no single reviewed benchmark or production system combines all of them. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2507.05257; https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/]
- Links: [LongMemEval](https://arxiv.org/abs/2410.10813), [MemoryAgentBench](https://arxiv.org/abs/2507.05257), [Building an agentic memory system for GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)
