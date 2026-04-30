---
review_count: 2
title: "Stateless-agent assumption failure: causes, detection, and recovery patterns for orphaned state in multi-session agentic workflows"
added: 2026-03-20T07:26:32+00:00
status: completed
priority: high
blocks: []
tags: [failure-modes, agentic-ai, operational-failures, layer-5, state-management, idempotency, checkpoint-resume, multi-session, workflow]
started: 2026-03-20T07:26:32+00:00
completed: 2026-03-20T07:26:32+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Stateless-agent assumption failure: causes, detection, and recovery patterns for orphaned state in multi-session agentic workflows

## Research Question

When an agentic workflow spans multiple session boundaries — each session starting with a fresh context window and no memory of prior runs — what are the mechanisms by which external state becomes orphaned, how frequently does this failure mode occur in production systems, what signals reliably detect it before it compounds, and what design patterns reliably prevent or recover from it?

## Scope

**In scope:**
- Definition and precise characterisation of the stateless-agent assumption failure as a subtype of Layer 5 operational failure (as classified in `2026-03-12-failure-mode-taxonomy-expansion.md`)
- Root cause analysis: why agents built on fresh-context-per-session architectures implicitly assume a clean initial world state
- Taxonomy of orphaned-state subtypes: partially-completed work items, externally-triggered side effects (workflow runs, commits) that were never confirmed, counter/flag fields written by one session but never read by the next
- Empirical evidence: how common is this failure in production agentic systems? (incident reports, framework documentation, practitioner accounts, evaluation data)
- Detection signals: what observable indicators (file system state, git log patterns, workflow run history, frontmatter fields) allow a new session to discover and classify orphaned state
- Recovery patterns: at-least-once vs exactly-once semantics, idempotent operations, checkpoint-resume, external state registers, re-entrant prompt design
- Comparison with analogous distributed systems patterns: at-most-once delivery, two-phase commit, saga pattern, dead-letter queues, durable execution
- Evaluation of tradeoffs: complexity of recovery logic vs risk of orphan accumulation under different workflow topologies

**Out of scope:**
- Context overflow as a failure mode (covered in `2026-03-08-context-engineering-first-principles.md`)
- Multi-agent coordination failures where agents have concurrent sessions (the focus here is sequential sessions with no shared live context)
- Hardware or infrastructure failures not caused by agent design
- Full implementation of mitigation tooling (follow-on engineering item)

## Context

This item is motivated by a repository-local continuity risk that is directly visible in the current architecture: the research loop is explicitly fresh-session by design, while work state persists across directories, frontmatter fields, review counters, and workflow runs. That is enough state fragmentation to make a clean-start assumption unsafe unless every new session reconciles those surfaces before acting.

The failure belongs to the Layer 5 operational failure class from `2026-03-12-failure-mode-taxonomy-expansion.md`, but it is more specific than context overflow or instruction conflict. The distinctive feature is the mismatch between a fresh-session agent's internal assumption of a clean start and the external world's persistent, partially-mutated state.

Structurally, this looks less like a reasoning mistake and more like a distributed worker crash. A worker dequeues a task, performs some side effects, crashes before writing completion state, and then a new worker starts without reconciling what already happened. In the Artificial Intelligence (AI) and Large Language Model (LLM) setting, the external state is often split across repository files, git history, workflow runs, issue trackers, and service-side state rather than a single queue.

## Approach

1. **Characterise the failure class precisely** — distinguish stateless-agent assumption failure from adjacent Layer 5 failures and produce a precise definition with necessary and sufficient conditions.
2. **Map the failure's state space** — enumerate the ways external state can become orphaned in a multi-session agent: incomplete file moves, uncommitted edits, triggered-but-unconfirmed side effects, counter fields written but never read, and hidden in-progress work.
3. **Survey empirical evidence** — search production framework documentation, public evaluation data, and practitioner evidence for this failure class. Determine whether it has a recognised name in the agentic systems community.
4. **Identify detection signals** — determine what a new session can observe without prior context, separating file-system, git-history, external-service, and metadata-level signals.
5. **Survey recovery patterns from distributed systems** — at-least-once vs exactly-once, saga pattern, two-phase commit (2PC), dead-letter queues, idempotent operations, and durable execution.
6. **Derive design principles** — identify the structural properties an agentic prompt or workflow must have to remain resilient across session boundaries, and evaluate the tradeoff between recovery complexity and failure probability.

## Sources

- [x] `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md` — parent taxonomy; Layer 5 operational failures
- [x] `Research/completed/2026-03-08-context-engineering-first-principles.md` — adjacent Layer 5 failures and the token-level / goal-level distinction
- [x] `Research/completed/2026-03-01-github-specify-ralph-loop-lisa-planning.md` — stateless loops, persistent planning layers, and the "Groundhog Day" memory problem
- [x] `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md` — prompt-level forcing functions and prior-work detection gaps in this repository
- [x] `.github/workflows/research-loop.yml` — fresh-session research loop implementation
- [x] `.github/workflows/research-review.yml` — review workflow and `review_count` mutation pattern
- [x] `src/research/item.py` — frontmatter status-to-directory mapping
- [x] [LangGraph Persistence docs](https://docs.langchain.com/oss/python/langgraph/persistence)
- [x] [LangGraph Durable Execution docs](https://docs.langchain.com/oss/python/langgraph/durable-execution)
- [x] [OpenAI Agents Python Software Development Kit (SDK) Quickstart](https://openai.github.io/openai-agents-python/quickstart/)
- [x] [OpenAI Agents SDK session memory cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/session_memory)
- [x] [Temporal Workflow Execution docs](https://docs.temporal.io/workflow-execution)
- [x] [Temporal durable execution essay](https://temporal.io/blog/what-is-durable-execution)
- [x] [Model Evaluation & Threat Research (METR): Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [x] [Amazon Web Services (AWS) event-driven architecture idempotency guidance](https://aws-samples.github.io/eda-on-aws/concepts/idempotency/)
- [x] [Confluent Kafka delivery semantics](https://docs.confluent.io/kafka/design/delivery-semantics.html)
- [x] [microservices.io idempotent consumer pattern](https://microservices.io/patterns/communication-style/idempotent-consumer.html)
- [x] [microservices.io saga pattern](https://microservices.io/patterns/data/saga.html)
- [x] [RabbitMQ reliability guide](https://www.rabbitmq.com/docs/reliability)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–7 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- [fact] **Research question restated:** What precise failure occurs when a fresh-session agent treats the world as clean even though earlier sessions have already changed durable external state, how often does that happen in production practice, what signals expose it, and which design patterns reliably prevent or recover from it?
- [fact] **Scope confirmed:** This investigation covers definition, orphaned-state taxonomy, empirical evidence, detection signals, recovery patterns, distributed-systems analogies, and design principles. It excludes concurrent multi-agent coordination, infrastructure failures, and implementation of a mitigation tool.
- [fact] **Constraints confirmed:** Claims must be tied either to repository artefacts, official framework documentation, or clearly-labelled inference. Exact public incident rates for this failure class are likely sparse, so uncertainty must be explicit where direct counts are unavailable.
- [fact] **Output format confirmed:** Structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, open questions, and output metadata.
- [fact] **Prior research cross-reference completed:** The directly relevant completed items are `2026-03-12-failure-mode-taxonomy-expansion.md`, `2026-03-08-context-engineering-first-principles.md`, `2026-03-01-github-specify-ralph-loop-lisa-planning.md`, and `2026-03-03-research-loop-quality-prompt-engineering.md`.

---

### §1 Question Decomposition

**Root question:** What is the stateless-agent assumption failure, and how should production agentic systems detect and recover from it?

**Decomposition tree:**

- **A. Definition and boundary**
  - A1. What makes this a distinct Layer 5 operational failure rather than context overflow, instruction conflict, or ordinary task failure?
  - A2. What are the necessary and sufficient conditions for this failure to exist?
  - A3. What adjacent terms already exist in agent and workflow tooling?

- **B. Mechanisms and state space**
  - B1. How does a fresh-session architecture create a false clean-start assumption?
  - B2. What kinds of external state become orphaned?
  - B3. Which repo-specific examples illustrate the general pattern?

- **C. Empirical evidence and naming**
  - C1. How much direct public evidence exists for this exact failure class?
  - C2. Do leading frameworks productise persistence and resumability as first-class features?
  - C3. Does the agentic systems community use a standard name for this failure?

- **D. Detection signals**
  - D1. What file-system signals reveal orphaned state?
  - D2. What git-history signals reveal orphaned state?
  - D3. What external-service and metadata signals reveal orphaned state?

- **E. Prevention and recovery**
  - E1. Which distributed-systems patterns map directly onto this problem?
  - E2. When are idempotency and at-least-once semantics sufficient?
  - E3. When are stronger constructs such as durable execution or compensating transactions required?
  - E4. Why is two-phase commit usually a poor fit for agent workflows?

- **F. Design principles and tradeoffs**
  - F1. What minimal structural properties make a session-boundary workflow re-entrant?
  - F2. How do those properties vary by workflow topology and side-effect surface?

---

### §2 Investigation

#### A. Definition and boundary

- [fact] `2026-03-12-failure-mode-taxonomy-expansion.md` defines Layer 5 as operational failures caused by system design rather than by model weights alone, and `2026-03-08-context-engineering-first-principles.md` already places context overflow and instruction conflict in that layer. Sources: `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md`; `Research/completed/2026-03-08-context-engineering-first-principles.md`.
- [inference] **Definition:** Stateless-agent assumption failure is a Layer 5 operational failure in which a new session begins with no reliable memory of prior execution, implicitly assumes the external world is in a clean initial state, and therefore fails to reconcile durable state mutations created by previous sessions before taking further action.
- [inference] **Necessary conditions:** (1) the workflow spans at least two sessions or processes; (2) at least one session mutates durable external state; and (3) the next session lacks a mandatory reconciliation step that compares the expected state with the actual current state before proceeding.
- [inference] **Sufficient consequence:** Once those conditions hold, the system can hide, duplicate, overwrite, or contradict prior work without any single session being locally irrational.
- [inference] This boundary excludes pure context overflow, because the core problem is not token budget exhaustion; it excludes instruction conflict, because the core problem is not contradictory instructions inside one context window; and it excludes concurrent coordination failure, because the defining case is sequential fresh sessions with broken continuity.

#### B. Mechanisms and orphaned-state subtypes

- [fact] The repository's research loop explicitly states that each Copilot invocation is a fresh session with a new context window, and the item model maps `reviewing` status back to the `in-progress` directory rather than a separate filesystem location. Sources: `.github/workflows/research-loop.yml`; `src/research/item.py`.
- [fact] The review workflow increments `review_count` in frontmatter and commits that mutated file back to the repository, making frontmatter itself part of the external workflow state. Source: `.github/workflows/research-review.yml`.
- [inference] Fresh-session architectures create a false clean-start assumption because the agent's internal state is reset while the workflow's real state is not. The more state is spread across files, commits, workflow runs, and service-side counters, the easier it becomes for a new session to miss one of those state surfaces.
- [inference] The orphaned-state space in agent workflows splits into four practical subtypes:
  - [inference] **Hidden work-item state:** a task was moved or partially advanced, but the next session's selection logic does not search the authoritative location.
  - [inference] **Triggered-but-unconfirmed side effects:** a commit, workflow run, issue change, or external call was made, but the next session does not check whether it succeeded, failed, or partially applied.
  - [inference] **Metadata drift:** a counter, flag, status field, or checkpoint identifier was written by one session but never re-read by the next session, so control flow uses stale assumptions.
  - [inference] **Partial local artefacts:** files, patches, logs, or serialized checkpoints exist on disk, but the next session lacks rules for deciding whether they are authoritative, stale, or disposable.
- [inference] The defining mechanism is not "forgetfulness" in the human sense. It is a mismatch between volatile in-session cognition and persistent out-of-session state.

#### C. Empirical evidence and naming

- [fact] LangGraph's persistence documentation says the framework saves graph state as checkpoints, requires a `thread_id`, and uses checkpointing for human-in-the-loop workflows, memory, time travel, and fault tolerance. It further states that if one or more nodes fail, the graph can restart from the last successful step without rerunning successful nodes. Sources: https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langgraph/durable-execution
- [fact] LangGraph's durable execution documentation states that workflows can pause and later resume exactly where they left off, and that side-effecting or non-deterministic operations must be wrapped so replay does not repeat them incorrectly. It explicitly recommends idempotent operations and idempotency keys for retried work. Source: https://docs.langchain.com/oss/python/langgraph/durable-execution
- [fact] OpenAI's Agents SDK quickstart says second-turn continuation requires one of three explicit memory strategies: manual history replay, SDK-managed sessions, or server-managed continuation via `previous_response_id` / `conversation_id`. The session-memory cookbook says that carrying too little context causes loss of coherence, while carrying too much causes distraction, inefficiency, or outright failure. Sources: https://openai.github.io/openai-agents-python/quickstart/ ; https://developers.openai.com/cookbook/examples/agents_sdk/session_memory
- [fact] Temporal defines workflow execution as durable, reliable, and scalable, says replay is how execution resumes progress, and states that after failure a workflow resumes from the latest recorded event history. Temporal's durable-execution essay defines durable execution as crash-proof execution. Sources: https://docs.temporal.io/workflow-execution ; https://temporal.io/blog/what-is-durable-execution
- [fact] Model Evaluation & Threat Research (METR) reports that current frontier agents succeed on almost all tasks that take humans less than about four minutes, but succeed on fewer than 10% of tasks taking more than about four hours, showing that reliability drops sharply as workflow length increases. Source: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- [inference] Direct public incident counts for this exact failure class are sparse. The strongest public evidence is indirect but still meaningful: major frameworks productise persistence, checkpointing, resumability, and session memory as core features rather than optional add-ons.
- [inference] The field does **not** yet have a single standard agentic label for this failure mode. The dominant terms are persistence, session memory, checkpointing, durable execution, replay, resumability, and idempotency rather than "stateless-agent assumption failure."
- [inference] That naming gap implies conceptual immaturity, not irrelevance. The problem is clearly recognised, but usually under workflow-engineering and distributed-systems vocabulary rather than a distinct agent-only taxonomy entry.

#### D. Detection signals

- [inference] **File-system-observable signals:** durable work artefacts exist in non-terminal locations (`Research/in-progress/`, checkpoint stores, partial output files, run-specific logs), or multiple mutually-incompatible state markers coexist at once.
- [inference] **Git-history signals:** the repository contains a start or draft commit without the expected completion commit; repeated attempts touch the same work item without terminal state transition; or the diff shows mutations to state-bearing files that are not paired with the expected follow-up mutation.
- [inference] **External-service signals:** a workflow run was triggered but the corresponding state mutation is absent; a review workflow updated `review_count` without a matching status transition; or an issue / workflow / pull request (PR) remains open when the local file claims the process is finished.
- [inference] **Metadata signals:** frontmatter fields such as `status`, `started`, `completed`, `review_count`, checkpoint identifiers, or idempotency keys describe a state transition that downstream control logic never re-reads before acting.
- [inference] The best detection pattern is a mandatory "reconciliation preflight" at session start: enumerate all authoritative state surfaces, compare them against the workflow's expected state machine, and only then choose the next action.

#### E. Prevention and recovery patterns

- [fact] AWS guidance states that duplicate delivery and duplicate processing are facts of life in distributed systems and recommends idempotency keys stored in persistent state to suppress unintended side effects. Source: AWS idempotency guidance.
- [fact] RabbitMQ states that acknowledgements guarantee at-least-once delivery and that without acknowledgements only at-most-once delivery is guaranteed. It also notes that messages in transit may need retransmission after connection failure. Source: RabbitMQ reliability guide.
- [fact] Confluent's Kafka documentation distinguishes at-most-once, at-least-once, and exactly-once semantics, and warns that many exactly-once claims do not cover failures outside the brokered system. It presents idempotent producers and transactional delivery as higher-overhead options. Source: Confluent Kafka delivery semantics.
- [fact] microservices.io's idempotent consumer pattern states that at-least-once delivery implies duplicate invocation risk and that consumers must record processed message identifiers to make repeated processing safe. Source: microservices.io idempotent consumer pattern.
- [fact] microservices.io's saga pattern defines a saga as a sequence of local transactions plus compensating transactions, explicitly motivated by cases where distributed transactions across services are not an option. It also lists lack of automatic rollback and lack of isolation as core drawbacks. Source: microservices.io saga pattern.
- [inference] The cleanest mapping to agent workflows is:
  - [inference] **Durable execution / checkpointing** for long-running workflows that must resume after interruption without recomputing or repeating side effects.
  - [inference] **Explicit session identifiers and state registers** for any workflow that spans multiple fresh sessions.
  - [inference] **At-least-once plus idempotent side effects** for tool calls, commits, comments, and external write operations where replay or retry is unavoidable.
  - [inference] **Saga-style compensation** for multi-step external changes that cannot be made atomic.
  - [inference] **Dead-letter or manual-review paths** for orphan classes that cannot be reconciled automatically.
- [inference] Exactly-once semantics are usually the wrong target for agent workflows because the state surface extends beyond a single queue or broker into files, human review steps, external services, and tool Application Programming Interfaces (APIs) that do not share one transaction boundary.
- [inference] Two-phase commit (2PC) is therefore a poor default fit for agentic systems. It introduces coordination and blocking overhead, requires shared transactional control over heterogeneous state stores, and still does not solve the human-in-the-loop or tool-side effects that sit outside a single coordinator's authority.

#### F. Design principles and tradeoffs

- [inference] A session-boundary workflow is re-entrant only if it externalises enough state for a later session to answer three questions deterministically: **what has already happened, what side effects are authoritative, and what step is safe to run next.**
- [inference] The minimal resilient design is therefore: durable state register, explicit status machine, mandatory startup reconciliation, idempotent writes, and a retry policy that assumes duplicates are possible.
- [inference] Linear workflows with one authoritative state store can often stop at checkpoints plus idempotent writes. Branching workflows, or any workflow that triggers external services, usually need stronger recovery machinery such as compensating actions, audit logs, and manual exception queues.
- [inference] The tradeoff is predictable: stronger durability and reconciliation reduce orphan risk but add implementation complexity, latency, and state-management overhead. The correct choice depends less on model capability than on the cost of a duplicated or hidden side effect.

---

### §3 Reasoning

- [fact] Official framework documents from LangGraph, OpenAI, and Temporal all treat persistence or resumability as a first-class architectural concern, which is direct evidence that the problem is operational rather than hypothetical.
- [inference] Because those frameworks use different terminology but solve the same continuity problem, the most stable abstraction is not a vendor-specific feature name but the broader failure class: durable external state plus volatile internal state plus missing reconciliation.
- [inference] The distributed-systems analogy is structurally sound because both domains face the same three constraints: retries happen, partial failure happens, and side effects can escape the local process before completion state is written.
- [inference] The public-frequency answer must remain qualified. There is strong evidence of practical importance, but weak evidence for a precise incidence rate isolated under one standard label.

---

### §4 Consistency Check

- [fact] No source reviewed contradicts the claim that retries, replay, or resume are normal in production workflows; the documents differ mainly in mechanism and terminology rather than direction.
- [fact] No source reviewed claims that exactly-once semantics are free or universally available across heterogeneous systems. Kafka, RabbitMQ, and saga-pattern sources all preserve explicit tradeoffs.
- [inference] The main unresolved tension is between practical salience and naming precision: the failure is clearly common enough to motivate product features, but not yet mature enough as an agent-specific concept to have a canonical shared name.
- [fact] That uncertainty is preserved in the synthesis by keeping exact frequency at medium confidence rather than inflating it to a stronger empirical claim.

---

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** The core issue is state continuity, not model reasoning quality. A stronger model inside the same stateless architecture still inherits the same orphan-risk surface.
- [inference] **Economic lens:** Orphaned-state recovery is a transaction-cost problem. The more expensive it is to detect and undo a bad side effect, the more rational it becomes to invest in stronger durability upfront.
- [inference] **Historical lens:** The agent ecosystem is replaying older distributed-systems lessons. Durable execution, idempotent consumers, acknowledgements, and compensating transactions all predate modern agent frameworks, but the same constraints reappear once agents gain tools and long-running workflows.
- [inference] **Behavioural lens:** Humans misdiagnose this failure as agent incompetence because the visible symptom is often repeated or skipped work. The deeper cause is architectural invisibility: the next session cannot act on state it was never required to inspect.
- [inference] **Repository lens:** This repository is a good microcosm because it already distributes workflow state across files, frontmatter, git history, and GitHub Actions runs. That makes it an informative case study for the general pattern rather than a one-off exception.

---

### §6 Synthesis

#### Executive Summary

- [fact] **Answer:** Stateless-agent assumption failure is a Layer 5 operational continuity failure in which a fresh-session agent resumes work without reconciling durable state written by earlier sessions.
- [fact] **Production evidence:** Official framework documentation from LangGraph, OpenAI, and Temporal treats checkpointing, session memory, replay, and durable execution as first-class features, which shows the underlying continuity problem is operationally important even without a single canonical shared label.
- [inference] **Best-supported design conclusion:** The most reliable prevention pattern is explicit external state plus startup reconciliation; the most reliable retry baseline is at-least-once execution with idempotent side effects rather than literal exactly-once guarantees.
- [inference] **Boundary condition:** Once a workflow performs non-atomic multi-step external mutations, it needs compensation or quarantine paths rather than simple blind retry.

#### Claim Register

- [inference] **K1:** The failure is defined by the clean-start assumption, not by weak reasoning inside one session.
- [fact] **K2:** Frameworks productise persistence and resumability because cross-session state loss is normal in production workflows.
- [inference] **K3:** Public naming is immature; solution terminology is more standardised than failure terminology.
- [inference] **K4:** Longer workflows increase exposure because they create more interruption and replay opportunities.
- [inference] **K5:** Reliable detection requires checking multiple state surfaces, not one authoritative log alone.
- [inference] **K6:** Idempotent retry, checkpoint-resume, and compensating actions are the transferable control stack from distributed systems.

#### Evidence Priorities

- [fact] **Primary sources:** repository workflow files; repository item model; LangGraph docs; OpenAI Agents SDK docs; Temporal docs; AWS idempotency guidance; Kafka, RabbitMQ, and microservices.io reliability patterns.
- [fact] **Secondary source:** METR long-task evaluation for task-horizon evidence.
- [fact] **Evidence sufficiency:** Direct mechanism claims rely on official docs or repository artefacts; broader frequency and design-choice claims remain labelled as inference where sources are indirect.

#### Assumptions

- [assumption] No public benchmark currently isolates this failure under the exact label used in this item. **Justification:** all reviewed public materials expose adjacent categories such as persistence, session memory, replay, or durable execution instead.
- [assumption] The repository incident generalises beyond this repository. **Justification:** the same continuity remedy structure appears independently in workflow-engineering and distributed-systems sources.

#### Analysis

- [inference] The operational invariant is simple: if durable side effects can outlive the process, then session startup must begin with state reconciliation rather than task selection.
- [inference] This makes durability architecture more important than prompt cleverness for this failure class.

#### Risks, Gaps, and Uncertainties

- [fact] Exact public incidence remains under-measured for this specific failure label.
- [inference] Some mappings from older distributed-systems patterns into agent workflows remain judgment calls because human review and heterogeneous tool outputs widen the state surface.

#### Open Questions

- [fact] What minimal continuity manifest would prevent most orphan classes in repository-centric workflows?
- [fact] Which side-effect classes should default to retry, compensation, or manual review?
- [fact] Can future agent benchmarks isolate cross-session continuity failures directly?

#### Output

- [fact] Type: knowledge.
- [fact] Description: A structured note defining stateless-agent assumption failure and mapping durable workflow controls onto multi-session agent systems.
- [fact] Most important sources: `https://docs.langchain.com/oss/python/langgraph/durable-execution`; `https://docs.temporal.io/workflow-execution`; `https://aws-samples.github.io/eda-on-aws/concepts/idempotency/`.

---

### §7 Recursive Review

- [fact] Every synthesis claim above is either tied to a reviewed source or explicitly labelled as inference or assumption.
- [fact] The answer to the research question is direct: the failure is real, architecturally distinct, detectable, and best addressed with durability and idempotency patterns rather than with prompt-only fixes.
- [fact] Uncertainties remain explicit for exact public incidence and the absence of a canonical shared label.
- [fact] The synthesis covers all required threads: definition, mechanism, frequency, naming, detection, recovery, and tradeoffs.

---

## Findings

### Executive Summary

- [inference] This failure is best understood as a continuity failure: a new session treats the world as clean even though earlier sessions already changed durable external state. (Sources: [Failure mode taxonomy expansion](Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md); [Context engineering: first principles](Research/completed/2026-03-08-context-engineering-first-principles.md))
- [inference] Public evidence is strongest in the solution surface rather than in a named incident class, because official frameworks independently ship checkpointing, session memory, replay, and durable execution as core workflow features while using different terminology for the underlying problem. (Sources: [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence); [LangGraph Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution); [OpenAI Agents SDK Quickstart](https://openai.github.io/openai-agents-python/quickstart/); [Temporal Workflow Execution](https://docs.temporal.io/workflow-execution))
- [inference] In practice, the safest operating rule is to begin each session with state reconciliation across repository files, git history, workflow state, and metadata before selecting new work or retrying a side effect. (Sources: [.github/workflows/research-loop.yml](.github/workflows/research-loop.yml); [.github/workflows/research-review.yml](.github/workflows/research-review.yml); [src/research/item.py](src/research/item.py))
- [inference] Idempotent retry plus checkpoint-resume covers the common case, while compensation or manual quarantine is reserved for workflows whose external mutations cannot be retried safely as a single atomic step. (Sources: [AWS idempotency guidance](https://aws-samples.github.io/eda-on-aws/concepts/idempotency/); [microservices.io idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html); [microservices.io saga](https://microservices.io/patterns/data/saga.html); [Temporal durable execution](https://temporal.io/blog/what-is-durable-execution))

### Key Findings

1. **High confidence — [inference]:** Stateless-agent assumption failure is a Layer 5 operational failure in which volatile in-session reasoning operates over durable out-of-session state without a mandatory reconciliation step, so later sessions can hide, duplicate, or contradict prior work even when each individual session behaves coherently. (Sources: [Failure mode taxonomy expansion](Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md); [Context engineering: first principles](Research/completed/2026-03-08-context-engineering-first-principles.md))
2. **High confidence — [inference]:** Leading production-oriented agent frameworks already treat persistence, resumability, and replay as first-class concerns, which supports the conclusion that cross-session orphaned-state risk is a normal systems problem rather than an exotic edge case tied to one repository or one vendor. (Sources: [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence); [LangGraph Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution); [OpenAI Agents SDK Quickstart](https://openai.github.io/openai-agents-python/quickstart/); [Temporal Workflow Execution](https://docs.temporal.io/workflow-execution))
3. **Medium confidence — [inference]:** The agent ecosystem has not yet converged on a single standard name for this failure class, because public documentation standardises the remedy vocabulary — checkpointing, session memory, durable execution, replay, and persistence — more clearly than the underlying continuity failure itself. (Sources: [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence); [OpenAI Agents SDK session memory cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/session_memory); [Temporal durable execution](https://temporal.io/blog/what-is-durable-execution))
4. **Medium confidence — [inference]:** Longer workflows materially increase exposure to this failure because they create more opportunities for interruption, partial side effects, and stale assumptions between sessions, and METR's long-task results show that agent reliability falls sharply as task duration rises. (Source: [METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/))
5. **High confidence — [inference]:** Reliable detection requires checking at least four state surfaces together — file-system artefacts, git-history transitions, external-service state, and explicit metadata such as `status` or `review_count` — because each surface can expose orphaning that the others leave invisible. (Sources: [.github/workflows/research-loop.yml](.github/workflows/research-loop.yml); [.github/workflows/research-review.yml](.github/workflows/research-review.yml); [src/research/item.py](src/research/item.py))
6. **High confidence — [inference]:** Idempotent side effects with at-least-once retry semantics are a better default for agent workflows than literal exactly-once guarantees, because repositories, workflow engines, human review steps, and tool Application Programming Interfaces (APIs) do not share one transaction boundary that a single coordinator can enforce. (Sources: [AWS idempotency guidance](https://aws-samples.github.io/eda-on-aws/concepts/idempotency/); [RabbitMQ reliability](https://www.rabbitmq.com/docs/reliability); [Kafka delivery semantics](https://docs.confluent.io/kafka/design/delivery-semantics.html); [microservices.io idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html))
7. **Medium confidence — [inference]:** Saga-style compensation and dead-letter or manual-review paths become necessary when an agent workflow performs multi-step external mutations whose partial completion cannot be made atomic, because recovery must then undo or quarantine inconsistent intermediate state rather than merely retrying the last step. (Sources: [microservices.io saga](https://microservices.io/patterns/data/saga.html); [Temporal Workflow Execution](https://docs.temporal.io/workflow-execution))

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Stateless-agent assumption failure is a Layer 5 operational subtype | [Failure mode taxonomy expansion](Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md); [Context engineering: first principles](Research/completed/2026-03-08-context-engineering-first-principles.md) | high | Internal prior work fixes the boundary against context overflow and instruction conflict |
| Frameworks productise persistence and resumability | [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence); [LangGraph Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution); [OpenAI Agents SDK Quickstart](https://openai.github.io/openai-agents-python/quickstart/); [Temporal Workflow Execution](https://docs.temporal.io/workflow-execution) | high | Independent official docs converge on the same need |
| No canonical shared name exists yet | [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence); [OpenAI Agents SDK session memory cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/session_memory); [Temporal durable execution](https://temporal.io/blog/what-is-durable-execution) | medium | Evidence is terminological and therefore indirect |
| Long workflows increase exposure | [METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) | medium | Supports rising interruption and failure exposure, not a direct incident count for this subtype |
| Detection must span repository, workflow, and metadata layers | [.github/workflows/research-loop.yml](.github/workflows/research-loop.yml); [.github/workflows/research-review.yml](.github/workflows/research-review.yml); [src/research/item.py](src/research/item.py) | high | Primary repository evidence |
| Idempotent retry is the best-supported baseline for agent workflows | [AWS idempotency guidance](https://aws-samples.github.io/eda-on-aws/concepts/idempotency/); [RabbitMQ reliability](https://www.rabbitmq.com/docs/reliability); [Kafka delivery semantics](https://docs.confluent.io/kafka/design/delivery-semantics.html); [microservices.io idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html) | high | This row captures the supported engineering conclusion rather than a broker-native guarantee |
| Compensation is required for non-atomic multi-step mutation | [microservices.io saga](https://microservices.io/patterns/data/saga.html); [Temporal Workflow Execution](https://docs.temporal.io/workflow-execution) | medium | Strong for the pattern; the agent-workflow mapping remains inferential |

### Assumptions

- **[assumption]** No public benchmark currently isolates this failure under the exact label "stateless-agent assumption failure." The reviewed public sources expose adjacent categories such as checkpointing, replay, persistence, or session memory instead.
- **[assumption]** The motivating repository incident is representative of a broader architectural class. That assumption is justified because the same remedy structure appears independently in agent-framework docs and in older distributed-systems reliability guidance.

### Analysis

- [inference] The central mistake is treating context reset as though it implied world reset. In production workflows the opposite assumption is safer: processes are disposable, but state written to files, workflows, queues, and service-side records persists until something explicitly reconciles it.
- [inference] That is why prompt-only mitigations are weak. A reminder like "check in-progress items first" helps, but the reliable fix is architectural: one authoritative state register, explicit status transitions, idempotent side effects, and a mandatory preflight that compares expected state with actual state before the session chooses its next action.
- [inference] The distributed-systems analogy is operational rather than decorative. Agent workflows with tools now face the same constraints as message-driven systems: retries happen, acknowledgements can be lost, side effects escape the local process, and partial completion is normal.

### Risks, Gaps, and Uncertainties

- [fact] Public incident counts for this exact failure label remain sparse, so exact frequency can only be stated qualitatively rather than numerically.
- [fact] Framework documentation proves practical importance, but it does not quantify how many production failures each feature prevents.
- [inference] Classical distributed-systems patterns do not fully capture human-review steps, unstructured tool outputs, or repository-specific state machines, so some translation into agent workflows remains design work rather than settled doctrine.

### Open Questions

- Can a lightweight repository-local continuity manifest capture enough state to prevent most orphan classes without adopting a full durable-execution engine?
- Which classes of agent side effects should default to idempotent retry, which require compensation, and which should always route to manual review?
- Can future agent evaluations measure cross-session continuity failure directly instead of burying it inside generic long-horizon success or failure rates?

### Output

- [fact] Type: `knowledge`
- [fact] Description: Structured findings on stateless-agent assumption failure as a Layer 5 operational failure, including definition, empirical framing, detection signals, and recovery patterns for multi-session agentic workflows.
- [fact] Links:
  - [fact] https://docs.langchain.com/oss/python/langgraph/durable-execution — durable execution and replay requirements
  - [fact] https://docs.temporal.io/workflow-execution — durable workflow execution and replay semantics
  - [fact] https://aws-samples.github.io/eda-on-aws/concepts/idempotency/ — idempotency and duplicate-processing guidance