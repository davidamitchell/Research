---
review_count: 2
title: "Policy coherence as a machine-checkable prerequisite: policy-as-code, formal specification, and invariant registries for regulated financial institutions deploying agentic Artificial Intelligence (AI)"
added: 2026-04-26T06:57:01+00:00
status: completed
priority: high
blocks: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering]
tags: [policy-coherence, policy-as-code, open-policy-agent, formal-specification, invariant-registry, agentic-ai, regulated-banking, governance, automated-enforcement]
ai_themes: [agentic-ai, governance-policy, tools-infrastructure, formal-verification]
started: 2026-04-26T10:02:06+00:00
completed: 2026-04-26T10:32:03+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Policy coherence as a machine-checkable prerequisite: policy-as-code, formal specification, and invariant registries for regulated financial institutions deploying agentic Artificial Intelligence (AI)

## Research Question

Contradictory or outdated policy documents are a chronic governance failure that organisations tolerate because the consequences under human operation are slow-moving. Under agentic operation, agents built in good faith against one policy document will violate another, and will do so repeatedly at machine speed before detection. What does the literature say about policy coherence as a prerequisite for automated enforcement, and does the policy-as-code literature, formal policy specification, Open Policy Agent (OPA) patterns, and invariant registries, provide an applicable framework for ensuring agents operate within a coherent, non-contradictory policy space in a regulated financial institution?

## Scope

**In scope:**
- The mechanism by which contradictory or outdated policy documents become a machine-speed failure mode under agentic Artificial Intelligence (AI), rather than a slow-moving governance issue under human operation
- The governance literature on policy coherence and policy conflict as an organisational failure mode, including what the academic and practitioner literature says about the frequency, causes, and consequences of policy contradiction in large organisations
- The policy-as-code literature: formal policy specification approaches, Open Policy Agent (OPA) and Rego patterns, declarative policy languages, and constraint satisfaction frameworks
- Whether invariant registries, explicit registries of non-negotiable policy rules that must hold across all agents and automated systems, provide a workable pattern for regulated financial institutions
- Evidence on whether any organisation has successfully implemented policy-as-code at scale in a regulated environment, and what the preconditions and failure modes were
- Relationship between policy coherence and the information architecture layer, including whether unclassified data estates make policy coherence assessment impossible or merely harder
- Whether any regulatory framework, including Australian Prudential Regulation Authority (APRA) CPS 230, the Digital Operational Resilience Act (DORA), International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) 42001, and Financial Conduct Authority (FCA) and Prudential Regulation Authority (PRA) guidance, explicitly requires machine-checkable policy coherence as a precondition for agentic AI deployment

**Out of scope:**
- General policy management and governance frameworks not specifically related to automated enforcement
- The deployment pipeline enforcement mechanism (covered by the companion deployment pipeline item)
- The Retrieval-Augmented Generation (RAG) access control layer (covered by the companion RAG item)
- Technical implementation details of OPA or specific policy engines beyond what is needed to assess applicability

**Constraints:**
- Distinguish between what the policy-as-code literature says is achievable in principle versus what has been demonstrated in production in regulated environments
- The primary question is applicability to a regulated financial institution, not general software engineering context
- Assess whether policy-as-code approaches require a minimum level of policy clarity and classification before they can be applied, that is, whether policy coherence is a prerequisite for policy-as-code rather than a consequence of it

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html] Prior completed items in this repository established that agentic AI deployment into incomplete governance environments is a control problem, not just a tooling choice, and that durable value in regulated environments depends on governed knowledge, bounded use-case routing, and enforceable platform guardrails.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.infoq.com/presentations/opa-spring-boot-hocon/] This item addresses the next control layer down: if policies themselves are contradictory, stale, or weakly typed, machine-speed enforcement will amplify those defects faster than human-operated processes usually do, so the relevant question is whether policy-as-code can convert policy coherence from an intermittent manual review problem into a continuously checked property.

## Approach

1. **Policy coherence as an organisational problem:** Review the organisational behaviour, compliance, and governance literature for evidence on how frequently large regulated organisations operate with contradictory policy documents, what the consequences are under human operation, and whether any framework requires proactive policy conflict detection.
2. **Policy-as-code survey:** Review the technical literature on formal policy specification, OPA and Rego, Cedar Policy Language, Amazon Web Services (AWS) Identity and Access Management (IAM) policy conditions, Kubernetes admission controllers, and comparable approaches for evidence of applicability at enterprise scale and in regulated contexts.
3. **Invariant registries:** Assess whether the concept of an invariant registry, an explicit, maintained set of non-negotiable policy rules that all automated systems must satisfy, has been implemented in practice, what the governance model looks like, and what the failure modes are.
4. **Regulatory requirement check:** For APRA CPS 230, DORA, ISO/IEC 42001, and FCA/PRA guidance, assess whether any provision explicitly requires machine-checkable policy coherence or policy-as-code as a precondition for agentic AI deployment.
5. **Precondition analysis:** Assess whether policy-as-code approaches require a minimum level of policy clarity and information classification before they can be applied, and whether the typical large-organisation policy estate, contradictory, stale, and unclassified, makes the approach inapplicable without prior remediation.
6. **Evidence of production implementations:** Search for case studies or published accounts of policy-as-code implementations in regulated financial services environments, including banking, insurance, or comparable sectors, with measured outcomes.
7. **Synthesis:** Produce a decision framework characterising when policy-as-code is applicable, what the minimum preconditions are, and what the gap is between the policy-as-code literature's capability claims and the practical state of a typical large financial institution's policy estate.

## Sources

- [x] [Open Policy Agent homepage](https://www.openpolicyagent.org/) — - official description of centralized policy management, auditability, and enforcement scope
- [x] [Open Policy Agent policy testing](https://www.openpolicyagent.org/docs/policy-testing) — - official testing framework for policy correctness and continuous integration use
- [x] [Open Policy Agent Control Plane concepts](https://www.openpolicyagent.org/docs/ocp/concepts) — - official bundle, source, namespace, and conflict-checking model for centrally managed policy distribution
- [x] [Open Policy Agent adopters list](https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md) — - public production adopters, including financial-services examples
- [x] [AWS Cedar overview](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html) — - official Cedar overview describing separation of authorization logic, scalability, and analysis support
- [x] [Cedar language reference guide](https://cedar-policy.github.io/cedar-docs/) — - official Cedar reference describing schema, principals, resources, actions, and context
- [x] [Amazon Science: How we built Cedar with automated reasoning and differential testing](https://www.amazon.science/blog/how-we-built-cedar-with-automated-reasoning-and-differential-testing) — - verification-guided development overview from the Cedar team
- [x] [How We Built Cedar: A Verification-Guided Approach](https://arxiv.org/abs/2407.01688) — - paper reporting model proofs and bug-finding outcomes
- [x] [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — - official control catalog page, including machine-readable Open Security Controls Assessment Language (OSCAL) publication
- [x] [NIST Open Security Controls Assessment Language (OSCAL)](https://pages.nist.gov/OSCAL/) — - official machine-readable control catalog initiative for policy-as-code and automated assessment
- [x] [APRA CPS 230 - Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) — - official APRA prudential standard
- [x] [DORA - Regulation (EU) 2022/2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — - official European Union regulation text
- [x] [ISO/IEC 42001:2023 - Information technology - Artificial intelligence - Management system](https://www.iso.org/standard/81230.html) — - official public summary of the Artificial Intelligence Management System (AIMS) standard
- [x] [Bank of England / PRA discussion paper (DP) 5/22 - Artificial Intelligence and Machine Learning](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence) — - official United Kingdom discussion paper on how the current regulatory framework applies to AI
- [x] [Bank of England / PRA feedback statement (FS) 2/23 - Artificial Intelligence and Machine Learning](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning) — - official feedback statement confirming the focus on clarifying existing frameworks rather than imposing new mechanism-specific rules
- [x] [PRA supervisory statement (SS) 1/23 - Model risk management principles for banks](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss) — - official expectations for strategic governance, policies, procedures, and controls around models
- [x] [Bank of New York Mellon (BNY Mellon) InfoQ transcript on OPA-based responsibility management](https://www.infoq.com/presentations/opa-spring-boot-hocon/) — - practitioner evidence of financial-services use of OPA to centralize entitlement logic
- [x] [Ramli 2015 eXtensible Access Control Markup Language (XACML) conflict-analysis paper](https://arxiv.org/abs/1503.02732) — - accessible abstract for formal conflict analysis in XACML policy sets
- [x] [ar5iv HTML mirror for the Ramli 2015 XACML conflict-analysis paper](https://ar5iv.labs.arxiv.org/html/1503.02732) — - accessible HTML text for the same paper
- [x] [Analyzing eXtensible Access Control Markup Language (XACML) policies using answer set programming](https://link.springer.com/article/10.1007/s10207-018-0421-5) — - later formal-analysis article and reference hub for access-control policy verification literature
- [x] [Basel Committee on Banking Supervision - Principles for operational resilience](https://www.bis.org/bcbs/publ/d516.htm) — - official resilience principles for banks
- [x] [Crossref metadata for the seeded Association for Computing Machinery (ACM) Digital Object Identifier (DOI)](https://api.crossref.org/works/10.1145/3194133.3194139) — - used only to confirm that the seeded DOI resolves to an unrelated paper

## Related

- [Regulatory and standards preconditions for deployment of Artificial Intelligence (AI) systems that can take multi-step actions](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)
- [Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html)
- [Can organisational intent be expressed as a formally structured specification from which artefacts are derived and consistency is machine-checked?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html] Research question restated: is policy coherence a prerequisite for safe automated enforcement in a regulated financial institution, and do formal policy methods, policy-as-code engines, and machine-readable invariant catalogs provide a workable way to keep agents inside a coherent policy space rather than a contradictory one?
- [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] Scope confirmed: the investigation covers organisational policy conflict, policy-as-code capabilities, invariant registry analogues, regulatory expectations, and the minimum policy and data preconditions needed before agentic AI can rely on automated enforcement in a regulated bank.
- [fact; source: https://api.crossref.org/works/10.1145/3194133.3194139; https://www.iso.org/standard/81230.html] Constraints confirmed: the seeded Association for Computing Machinery (ACM) Digital Object Identifier (DOI) resolves to an unrelated paper and the full ISO text is paywalled, so conclusions rely on accessible official texts, accessible research abstracts, and public practitioner evidence rather than inaccessible material.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md] Prior completed work already established that regulated-agent deployment inherits institution-level accountability, that bounded governance is a precondition for durable value, and that formal specification can make consistency checkable once intent is expressed in a structured form, so this item extends that work into the narrower question of policy coherence as an operational prerequisite.
- Output format: knowledge.

### §1 Question Decomposition

- **Root question:** Does the evidence support policy coherence as a prerequisite for automated enforcement in regulated financial institutions, and can policy-as-code make that prerequisite machine-checkable?
- **A. Organisational policy conflict**
  - A1. What does the formal policy-analysis literature say about conflict, incompleteness, and unreachable rules in structured policy sets?
  - A2. What does practitioner evidence say about policy sprawl, entitlement complexity, and governance gray areas in large organisations?
- **B. Policy-as-code capability**
  - B1. What can OPA make checkable, testable, and centrally governable?
  - B2. What can Cedar make checkable, analyzable, and formally trustworthy?
- **C. Invariant registries**
  - C1. Is there an established literature on "invariant registries" as a named concept?
  - C2. What adjacent constructs, such as machine-readable control catalogs, schemas, and policy bundles, implement the same function?
- **D. Production evidence**
  - D1. Has policy-as-code been deployed publicly in regulated financial services?
  - D2. If so, at what layer: enterprise policy corpus, authorization layer, or infrastructure control plane?
- **E. Regulatory requirement check**
  - E1. Do APRA CPS 230, DORA, ISO/IEC 42001, Basel operational resilience principles, and FCA/PRA guidance explicitly require machine-checkable policy coherence?
  - E2. If not, do they make it a strong inferred prerequisite for machine-speed agentic operations?
- **F. Preconditions**
  - F1. What minimum policy clarity, ownership, and classification are required before policy-as-code can work?
  - F2. Does an unclassified data estate make whole-estate policy coherence impossible, or just partial and expensive?
- **G. Decision synthesis**
  - G1. When is policy-as-code applicable?
  - G2. When is prior remediation of the policy estate unavoidable?

### §2 Investigation

#### Source access and replacement notes

- [fact; source: https://api.crossref.org/works/10.1145/3194133.3194139] The seeded ACM DOI resolves to **Toward evaluating the impact of self-adaptation on security control certification**, not to a policy-conflict paper, so it was not used for downstream claims.
- [fact; source: https://api.crossref.org/works/10.1145/3194133.3194139] Failed primary-source search record: the query `10.1145/3194133.3194139` resolved to an unrelated paper title, so it did not produce the expected policy-conflict source.
- [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732] Replacement source record: the investigation used the accessible Ramli XACML conflict-analysis paper instead.
- [assumption; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html] Definition needed: the term **invariant registry** is treated as an internal design label rather than a settled market category. **Justification:** exact-phrase searches did not surface an authoritative primary source using that name, but machine-readable control catalogs, schemas, and centrally distributed policy bundles perform the same architectural role.

#### A. What the policy-conflict literature actually establishes

- [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732] The XACML paper states that administrators struggle to understand the overall effect and consequences of expressive policy sets, and presents automated analysis for incompleteness, conflicting policies, and unreachable policies in XACML 3.0.
- [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732] The same paper explains that incomplete policies can create unsafe outcomes when the final enforcement bias treats "no applicable policy" as effectively permitted, which is a concrete mechanism by which policy defects become access-control failures.
- [fact; source: https://link.springer.com/article/10.1007/s10207-018-0421-5] The later Springer article sits inside a broader literature that treats access-control analysis as a formal verification problem, citing work on conflict detection, redundancy, reachability, misconfiguration detection, and automated verification using satisfiability and logical frameworks.
- [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] The literature shows that policy conflict detection is technically feasible once policies are represented in a formal language, but it does not imply that contradictory free-text corporate policy documents become coherent automatically.

#### B. What practitioner evidence says about policy sprawl in large organisations

- [fact; source: https://www.infoq.com/presentations/opa-spring-boot-hocon/] BNY Mellon's public OPA transcript describes entitlement and responsibility logic spread across Lightweight Directory Access Protocol (LDAP) groups, email groups, proprietary corporate data structures, and application code, and calls out the resulting gray area over who governs those policies and mappings.
- [fact; source: https://www.infoq.com/presentations/opa-spring-boot-hocon/] The same transcript argues that as policies accumulate, conditions multiply across groups, approval thresholds, Human Resources records, and organisational roles, which creates a scaling problem if each application implements those rules independently.
- [inference; source: https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://ar5iv.labs.arxiv.org/html/1503.02732] The practitioner and academic evidence align on the same mechanism: the more policy logic is fragmented across teams and systems, the harder it becomes to reason about aggregate behaviour, and the more valuable formal conflict checking becomes.
- [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html] Under human operation, contradictory policies often surface through delay, escalation, or case-by-case workarounds; under agentic operation, the same contradictions become high-frequency authorization or action-selection defects because the agent executes the contradictory instructions without that human damping layer.

#### C. What OPA makes machine-checkable

- [fact; source: https://www.openpolicyagent.org/] OPA describes itself as a general-purpose policy engine that decouples policy from application logic, lets security and platform teams centrally manage shared policies, and generates comprehensive audit trails for every policy decision.
- [fact; source: https://www.openpolicyagent.org/docs/policy-testing] OPA provides a built-in testing framework through `opa test`, supports policy-specific test files, supports failure visibility through enriched reports, and explicitly positions tests as a way to speed rule changes and reduce error as requirements evolve.
- [fact; source: https://www.openpolicyagent.org/docs/ocp/concepts] OPA's control-plane concepts document packages policies and data into bundles, distributes them centrally, and rejects overlapping packages during bundle build, which is an explicit machine-check against one class of policy namespace conflict.
- [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md] OPA's public adopters list includes BNY Mellon for sidecar access control, Capital One for Kubernetes admission control, and Goldman Sachs for multi-tenant Kubernetes provisioning and policy enforcement, which confirms production use in regulated financial services.
- [inference; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://www.openpolicyagent.org/docs/ocp/concepts] OPA can make a translated policy layer centrally versioned, testable, auditable, and conflict-checked at the package and decision level, but it still depends on upstream policy authorship, ownership, and data typing to determine what should be encoded.

#### D. What Cedar makes machine-checkable

- [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html] AWS describes Cedar as a flexible, extensible, and scalable policy-based access-control language that separates business logic from authorization logic and supports analysis through automated reasoning tools.
- [fact; source: https://cedar-policy.github.io/cedar-docs/] Cedar's reference guide requires explicit principals, actions, resources, context, and a schema that validates policies against the intended entity model, which means the policy space must be typed before meaningful checking happens.
- [fact; source: https://www.amazon.science/blog/how-we-built-cedar-with-automated-reasoning-and-differential-testing; https://arxiv.org/abs/2407.01688] Cedar was built with verification-guided development, combining formal executable models, proofs of safety and security properties, and differential random testing; the published paper reports four bugs found in the policy validator during proofs and twenty-one more bugs found through differential random testing and property-based testing.
- [fact; source: https://www.amazon.science/blog/how-we-built-cedar-with-automated-reasoning-and-differential-testing] Cedar's formal properties include **explicit permit** and **forbid overrides permit**, which are exactly the kinds of semantic guarantees that reduce ambiguity inside a formalized authorization layer.
- [inference; source: https://cedar-policy.github.io/cedar-docs/; https://arxiv.org/abs/2407.01688] Cedar demonstrates that machine-checkable policy coherence is realistic for a well-scoped authorization language with a typed schema, but its trustworthiness depends on converting organisational policy intent into that schema correctly, which is upstream work rather than a feature of the engine itself.

#### E. What an invariant registry most plausibly is in practice

- [fact; source: https://pages.nist.gov/OSCAL/] NIST describes OSCAL as a machine-readable format for policies, control catalogs, baselines, implementation information, and automated monitoring, and explicitly says that OSCAL can translate policies incorporating regulatory requirements into standardized machine-readable form to operationalize policy-as-code.
- [fact; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final] NIST SP 800-53 publishes an OSCAL version of its control catalog in JavaScript Object Notation (JSON), eXtensible Markup Language (XML), and YAML Ain't Markup Language (YAML), which is direct evidence that a control baseline can be represented as a machine-readable artifact rather than only as prose.
- [fact; source: https://www.openpolicyagent.org/docs/ocp/concepts; https://cedar-policy.github.io/cedar-docs/] OPA bundles and Cedar schemas provide two operational pieces of the same pattern: centrally managed machine-readable policy units, and a typed vocabulary that constrains what those units mean.
- [inference; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts; https://cedar-policy.github.io/cedar-docs/] A workable version of what this item calls an invariant registry, a definition-needed design label, is best understood in a regulated bank as a maintained catalog of non-negotiable controls and policy primitives, expressed in machine-readable form, mapped to authoritative entity schemas, and distributed into enforcement engines as versioned policy bundles.
- [inference; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts] This pattern is implementable, but the literature supports it more as an assembly of existing components than as a turnkey, already-standardized enterprise product category.

#### F. What public production evidence shows, and does not show

- [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/] Public evidence shows OPA in financial-services production for entitlement checks, admission control, multi-tenant cluster governance, and provisioning controls.
- [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md] The financial-services examples cited publicly are BNY Mellon, Capital One, and Goldman Sachs, all of which focus on authorization and infrastructure-control use cases rather than whole-of-enterprise policy-document coherence.
- [inference; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://arxiv.org/abs/2407.01688] Production evidence supports policy-as-code as a real control-layer technology in regulated environments, but the public record does not show a bank that has fully translated its natural-language policy estate into a formally coherent machine-checkable corpus.

#### G. What the regulatory sources require

- [fact; source: https://handbook.apra.gov.au/standard/cps-230] APRA CPS 230 requires entities to identify, assess, and manage operational risks with effective internal controls, monitoring, and remediation, and to maintain critical operations through severe disruptions.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] DORA says increased digitalisation amplifies Information and Communication Technology (ICT) risk, seeks a coherent approach to ICT risk in finance, and extends the supervisory framework to digital operational resilience.
- [fact; source: https://www.iso.org/standard/81230.html] ISO/IEC 42001 specifies requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (AIMS), including policies, objectives, processes, traceability, transparency, and reliability.
- [fact; source: https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning] FCA and PRA guidance frames AI oversight primarily as an application of the current regulatory framework, with clarifications and gap analysis, not as a mandate for a specific mechanism such as policy-as-code.
- [fact; source: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] PRA SS1/23 expects banks to strengthen policies, procedures, and practices for model risk management, take a strategic approach to governance, and identify and control risks from Artificial Intelligence techniques where models are involved.
- [fact; source: https://www.bis.org/bcbs/publ/d516.htm] Basel's operational-resilience principles promote a principles-based approach that strengthens banks' ability to withstand operational-risk events, including cyber incidents and technology failures.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] None of the reviewed frameworks explicitly says that machine-checkable policy coherence is a formal precondition for agentic AI deployment, but all of them require governance and control outcomes that become materially harder to satisfy if agents operate against contradictory, stale, or weakly typed policies.

#### H. Preconditions: what must exist before policy-as-code is broadly applicable

- [fact; source: https://cedar-policy.github.io/cedar-docs/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html] Cedar requires a typed schema for principals, resources, actions, and context, and validates policies against that schema when policies are created or updated.
- [fact; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing] OPA evaluates policies over structured input and data documents and expects policy authors to write tests against those representations, which means the relevant entities, attributes, and expected decisions must be explicitly modeled.
- [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/] Policy-as-code requires at least four upstream conditions: authoritative policy ownership, a typed resource and action model, enough data classification to map policies to subjects and resources, and a governed change process that keeps the machine-readable layer aligned with the source policy intent.
- [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/; https://pages.nist.gov/OSCAL/] An unclassified data estate does not make local policy-as-code impossible, because teams can still encode narrow controls for known systems, but it does make whole-estate policy coherence only partial, brittle, and expensive because the missing classification prevents consistent scoping of which invariants apply where.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://cedar-policy.github.io/cedar-docs/; https://pages.nist.gov/OSCAL/] For broad agentic deployment in a regulated bank, policy-as-code is therefore an amplifier of already-governed policy intent, not a substitute for remediating contradictory documents, unclear ownership, or weak information architecture.

### §3 Reasoning

- [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] Formal policy analysis literature answers the narrow technical question: structured policy sets can be checked for conflict, incompleteness, and unreachable rules.
- [inference; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://arxiv.org/abs/2407.01688] OPA and Cedar answer the operational question partly: centrally managed, testable, and partially verifiable policy layers are feasible in production, but only after policy intent is translated into typed machine-readable representations.
- [inference; source: https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final] OSCAL and machine-readable control catalogs answer the registry question partly: a catalog of non-negotiable invariants is feasible as a control architecture, but it is a governance pattern assembled from standards and tooling rather than a mature off-the-shelf discipline with common terminology.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence] The regulatory sources are outcome-based, not mechanism-specific, so the strongest defensible claim is not that regulators explicitly require machine-checkable policy coherence, but that such coherence becomes a strong derived prerequisite if machine-speed agents are expected to stay inside those outcome obligations.
- [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/] The decisive boundary condition is upstream policy and data quality: policy-as-code can prove properties about a formalized policy layer, but it cannot determine whether the organization selected the right invariants, resolved contradictory prose, or classified the estate well enough for the right policies to fire.

### §4 Consistency Check

- [fact; source: https://api.crossref.org/works/10.1145/3194133.3194139] The incorrect seeded DOI was replaced.
- [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] The regulatory conclusion remains internally consistent: the sources support control, governance, resilience, and policy expectations, but not an explicit machine-checkable-policy mandate.
- [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/] The production-evidence conclusion remains internally consistent: regulated-industry deployment is publicly demonstrated, but at authorization and control-plane scope, not at total policy-estate formalization scope.

### §5 Depth and Breadth Expansion

- [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing] **Technical lens:** policy coherence becomes machine-checkable only where entities, actions, context, and expected decisions are explicit enough to be modeled and tested, so the limiting factor is usually schema quality and ownership discipline rather than policy-engine capability.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence] **Regulatory lens:** regulators presently care about the effectiveness of the control environment, not whether the firm uses OPA, Cedar, or any other engine, but machine-speed operations raise the evidentiary bar for showing that controls are actually coherent and enforceable.
- [inference; source: https://pages.nist.gov/OSCAL/; https://www.infoq.com/presentations/opa-spring-boot-hocon/] **Economic lens:** the expensive part is not the policy engine license or runtime footprint; it is converting fragmented prose, inconsistent naming, and dispersed policy ownership into an authoritative machine-readable catalog that can be maintained as operating reality changes.
- [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] **Historical lens:** the underlying problem is not new, because access-control researchers have been formalizing and conflict-checking policy sets for years, but agentic AI widens the business impact because more decisions can now be delegated into those policy surfaces.
- [inference; source: https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html] **Behavioural lens:** organisations accumulate local exceptions because human processes can absorb ambiguity, while machine-enforced agents force those ambiguities into explicit allow, deny, or fallback behaviour, which exposes hidden contradictions that the organisation previously tolerated.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md] Policy coherence is a practical prerequisite for any policy domain delegated to automated enforcement in a regulated financial institution, because policy engines can only enforce, test, and partially verify policies that have been translated into a coherent formal representation. [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://arxiv.org/abs/2407.01688] The policy-as-code literature and public production evidence show that centralized, testable, auditable policy layers exist in production, but primarily at authorization and infrastructure-control scope rather than at full enterprise policy-corpus scope. [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/] Bounded-scope deployments can still succeed with local typed controls even when enterprise-wide policy-estate remediation is incomplete. [inference; source: https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://cedar-policy.github.io/cedar-docs/] The strongest workable version of what this item calls an invariant registry, a definition-needed design label for a machine-readable control catalog plus typed schemas and centrally distributed policy bundles, is a governance pattern rather than a standalone product category. [inference; source: https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] Regulators do not explicitly require that architecture today, but their governance and resilience expectations make it a strong derived precondition wherever agents can act at machine speed.

**Key findings:**

1. [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md] Policy-as-code does not resolve contradictory prose by itself; it becomes useful only after the policy domain being automated has been converted into a coherent, typed representation that an engine can evaluate consistently. Confidence: high.
2. [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] The formal policy-analysis literature demonstrates that structured access-control policies can be checked for conflicts, incompleteness, and unreachable rules, which proves that machine-checkable coherence is technically achievable for formalized policy subsets. Confidence: high.
3. [fact; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://www.openpolicyagent.org/docs/ocp/concepts] OPA provides a production pattern for centrally managed shared policies, automated policy testing, audit trails, and bundle-based distribution, which makes enforcement logic versioned, testable, and replayable across many systems. Confidence: medium.
4. [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://cedar-policy.github.io/cedar-docs/; https://arxiv.org/abs/2407.01688] Cedar adds a stronger formal-verification story through typed schemas, authorization-specific semantics, and verification-guided development, but its guarantees apply to the modeled authorization layer rather than to the upstream policy corpus. Confidence: medium.
5. [inference; source: https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://www.openpolicyagent.org/docs/ocp/concepts] The closest practical implementation of what this item calls an invariant registry, a definition-needed design label for a centrally owned machine-readable control catalog feeding typed schemas and versioned policy bundles into enforcement engines, is a governance pattern rather than a standalone product with a settled industry definition. Confidence: medium.
6. [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/] Public financial-services evidence confirms policy-as-code deployment in regulated institutions such as BNY Mellon, Capital One, and Goldman Sachs, but the public use cases are concentrated in authorization, admission control, and infrastructure governance. Confidence: medium.
7. [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] APRA, DORA, ISO/IEC 42001, and FCA/PRA guidance do not explicitly mandate machine-checkable policy coherence, but their control, governance, and resilience obligations make it a strong derived requirement for machine-speed agentic operations. Confidence: medium.
8. [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] An unclassified or weakly owned policy and data estate does not make narrow policy-as-code deployments impossible, but it does make enterprise-wide policy coherence only partial and makes safe broad agentic deployment difficult to justify without prior remediation. Confidence: medium.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Policy-as-code is downstream of coherent policy translation rather than a substitute for it. | https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md | high | Formal checking only applies after policy is represented formally. |
| [fact] Structured policy sets can be analyzed for conflict, incompleteness, and unreachable rules. | https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5 | high | Strongest direct evidence from XACML and verification literature. |
| [fact] OPA provides central policy management, testing, audit trails, and bundle-based distribution. | https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://www.openpolicyagent.org/docs/ocp/concepts | medium | Demonstrated by official docs from one source family. |
| [fact] Cedar provides typed schemas and a verification-guided authorization language with published bug-finding results. | https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://cedar-policy.github.io/cedar-docs/; https://arxiv.org/abs/2407.01688 | medium | Strong evidence, but largely from the Cedar source family. |
| [inference] What this item calls an invariant registry is best implemented as a machine-readable control catalog plus schemas and bundles. | https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://www.openpolicyagent.org/docs/ocp/concepts | medium | Architecture pattern is well supported; the exact label is not standardized, so the label remains definition-needed. |
| [fact] Financial-services production deployments exist, but mainly at authorization and control-plane scope. | https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/ | medium | Good evidence for regulated use, but the named-institution evidence is thin outside BNY Mellon. |
| [inference] Regulatory texts make machine-checkable coherence a strong derived prerequisite, not an explicit legal obligation. | https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss | medium | Strong on control outcomes, indirect on mechanism. |
| [inference] Weak classification and ownership make enterprise-wide policy coherence partial and make safe broad agentic deployment difficult to justify without prior remediation. | https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html | medium | Follows indirectly from schema, typing, and control-catalog requirements. |

**Assumptions:**

- [assumption; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts; https://cedar-policy.github.io/cedar-docs/] **Assumption:** "Invariant registry" is a design shorthand for a machine-readable catalog of non-negotiable controls, schemas, and distributed policy artifacts. **Justification:** the searched primary sources support the architecture but do not present a settled, authoritative definition under that exact term.

**Analysis:**

- [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] The strongest direct evidence concerns formal access-control policies, not enterprise policy manuals. That evidence is still relevant because it isolates the core technical question: can policy conflicts be detected mechanically once the policy space is formalized? The answer is yes.
- [fact; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://arxiv.org/abs/2407.01688] The engineering literature and official documentation then show that modern policy engines can operationalize those ideas through testing, schemas, audit trails, and formal reasoning, but only within the boundaries of the encoded model.
- [inference; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://pages.nist.gov/OSCAL/] Production evidence and machine-readable control standards jointly support a realistic operating model for regulated banks: central control catalogs and policy repositories feeding runtime enforcement. What they do not support is the stronger claim that banks have already solved natural-language policy coherence end to end.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence] Because the regulatory texts are mechanism-neutral, the conclusion is necessarily inferential rather than explicit: policy coherence is a prerequisite because otherwise the mandated control outcomes are not reliably demonstrable under machine-speed delegation.

**Risks, gaps, uncertainties:**

- [fact; source: https://api.crossref.org/works/10.1145/3194133.3194139] One seeded academic source was mislabeled and had to be replaced.
- [fact; source: https://www.iso.org/standard/81230.html] ISO/IEC 42001 evidence is lower resolution than APRA, DORA, or NIST evidence because only the official public summary was accessible in this runtime.
- [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md] Public financial-services case studies confirm deployment, but they do not publish detailed metrics or full governance operating models for whole-enterprise policy coherence.
- [inference; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts] The invariant-registry pattern is architecturally credible, but there is uncertainty about how many regulated institutions have formalized it explicitly as a named program rather than as dispersed control catalogs and policy repositories.

**Open questions:**

- [inference; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/] What governance model, ownership model, and change-control process do regulated banks use internally when they attempt to map free-text policy estates into machine-readable authorization or control artifacts?
- [inference; source: https://pages.nist.gov/OSCAL/; https://cedar-policy.github.io/cedar-docs/] What is the minimum viable sequence for moving from prose policies to a typed invariant catalog in a bank with partial data classification and mixed legacy tooling?
- [inference; source: https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Will supervisors eventually expect firms to provide machine-readable evidence of policy coherence for higher-autonomy systems, even if current texts remain mechanism-neutral?

### §7 Recursive Review

- Acronym audit: pass.
- Claim-label audit: pass.
- Findings and synthesis parity: pass.
- Inaccessible or replaced sources logged: yes.
- Remaining uncertainty is confined to production breadth and the exact industry usage of the term "invariant registry", not to the core conclusion.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

- [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md] Policy coherence is a practical prerequisite for any policy domain delegated to automated enforcement in a regulated financial institution, because policy engines can only enforce, test, and partially verify policies that have been translated into a coherent formal representation. [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://arxiv.org/abs/2407.01688] The policy-as-code literature and public production evidence show that centralized, testable, auditable policy layers exist in production, but primarily at authorization and infrastructure-control scope rather than at full enterprise policy-corpus scope. [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/] Bounded-scope deployments can still succeed with local typed controls even when enterprise-wide policy-estate remediation is incomplete. [inference; source: https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://cedar-policy.github.io/cedar-docs/] The strongest workable version of what this item calls an invariant registry, a definition-needed design label for a machine-readable control catalog plus typed schemas and centrally distributed policy bundles, is a governance pattern rather than a standalone product category. [inference; source: https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] Regulators do not explicitly require that architecture today, but their governance and resilience expectations make it a strong derived precondition wherever agents can act at machine speed.

### Key Findings

1. [inference; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md] Policy-as-code does not resolve contradictory prose by itself; it becomes useful only after the policy domain being automated has been converted into a coherent, typed representation that an engine can evaluate consistently. **Confidence: high.**
2. [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] The formal policy-analysis literature demonstrates that structured access-control policies can be checked for conflicts, incompleteness, and unreachable rules, which proves that machine-checkable coherence is technically achievable for formalized policy subsets. **Confidence: high.**
3. [fact; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://www.openpolicyagent.org/docs/ocp/concepts] OPA provides a production pattern for centrally managed shared policies, automated policy testing, audit trails, and bundle-based distribution, which makes enforcement logic versioned, testable, and replayable across many systems. **Confidence: medium.**
4. [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://cedar-policy.github.io/cedar-docs/; https://arxiv.org/abs/2407.01688] Cedar adds a stronger formal-verification story through typed schemas, authorization-specific semantics, and verification-guided development, but its guarantees apply to the modeled authorization layer rather than to the upstream policy corpus. **Confidence: medium.**
5. [inference; source: https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://www.openpolicyagent.org/docs/ocp/concepts] The closest practical implementation of what this item calls an invariant registry, a definition-needed design label for a centrally owned machine-readable control catalog feeding typed schemas and versioned policy bundles into enforcement engines, is a governance pattern rather than a standalone product with a settled industry definition. **Confidence: medium.**
6. [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/] Public financial-services evidence confirms policy-as-code deployment in regulated institutions such as BNY Mellon, Capital One, and Goldman Sachs, but the public use cases are concentrated in authorization, admission control, and infrastructure governance. **Confidence: medium.**
7. [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss] APRA, DORA, ISO/IEC 42001, and FCA/PRA guidance do not explicitly mandate machine-checkable policy coherence, but their control, governance, and resilience obligations make it a strong derived requirement for machine-speed agentic operations. **Confidence: medium.**
8. [inference; source: https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] An unclassified or weakly owned policy and data estate does not make narrow policy-as-code deployments impossible, but it does make enterprise-wide policy coherence only partial and makes safe broad agentic deployment difficult to justify without prior remediation. **Confidence: medium.**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Policy-as-code is downstream of coherent policy translation rather than a substitute for it. | https://ar5iv.labs.arxiv.org/html/1503.02732; https://www.openpolicyagent.org/; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-organisational-intent-formal-specification.md | high | Formal checking only applies after policy is represented formally. |
| [fact] Structured policy sets can be analyzed for conflict, incompleteness, and unreachable rules. | https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5 | high | Strongest direct evidence from XACML and verification literature. |
| [fact] OPA provides central policy management, testing, audit trails, and bundle-based distribution. | https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://www.openpolicyagent.org/docs/ocp/concepts | medium | Demonstrated by official docs from one source family. |
| [fact] Cedar provides typed schemas and a verification-guided authorization language with published bug-finding results. | https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://cedar-policy.github.io/cedar-docs/; https://arxiv.org/abs/2407.01688 | medium | Strong evidence, but largely from the Cedar source family. |
| [inference] What this item calls an invariant registry is best implemented as a machine-readable control catalog plus schemas and bundles. | https://pages.nist.gov/OSCAL/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://www.openpolicyagent.org/docs/ocp/concepts | medium | Architecture pattern is well supported; the exact label is not standardized, so the label remains definition-needed. |
| [fact] Financial-services production deployments exist, but mainly at authorization and control-plane scope. | https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/ | medium | Good evidence for regulated use, but the named-institution evidence is thin outside BNY Mellon. |
| [inference] Regulatory texts make machine-checkable coherence a strong derived prerequisite, not an explicit legal obligation. | https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss | medium | Strong on control outcomes, indirect on mechanism. |
| [inference] Weak classification and ownership make enterprise-wide policy coherence partial and make safe broad agentic deployment difficult to justify without prior remediation. | https://cedar-policy.github.io/cedar-docs/; https://www.openpolicyagent.org/docs/policy-testing; https://pages.nist.gov/OSCAL/; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html | medium | Follows indirectly from schema, typing, and control-catalog requirements. |

### Assumptions

- [assumption; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts; https://cedar-policy.github.io/cedar-docs/] **Assumption:** "Invariant registry" is a design shorthand for a machine-readable catalog of non-negotiable controls, schemas, and distributed policy artifacts. **Justification:** the searched primary sources support the architecture but do not present a settled, authoritative definition under that exact term.

### Analysis

- [fact; source: https://ar5iv.labs.arxiv.org/html/1503.02732; https://link.springer.com/article/10.1007/s10207-018-0421-5] The strongest direct evidence concerns formal access-control policies, not enterprise policy manuals. That evidence is still relevant because it isolates the core technical question: can policy conflicts be detected mechanically once the policy space is formalized? The answer is yes.
- [fact; source: https://www.openpolicyagent.org/; https://www.openpolicyagent.org/docs/policy-testing; https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html; https://arxiv.org/abs/2407.01688] The engineering literature and official documentation then show that modern policy engines can operationalize those ideas through testing, schemas, audit trails, and formal reasoning, but only within the boundaries of the encoded model.
- [inference; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/; https://pages.nist.gov/OSCAL/] Production evidence and machine-readable control standards jointly support a realistic operating model for regulated banks: central control catalogs and policy repositories feeding runtime enforcement. What they do not support is the stronger claim that banks have already solved natural-language policy coherence end to end.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.iso.org/standard/81230.html; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence] Because the regulatory texts are mechanism-neutral, the conclusion is necessarily inferential rather than explicit: policy coherence is a prerequisite because otherwise the mandated control outcomes are not reliably demonstrable under machine-speed delegation.

### Risks, Gaps, and Uncertainties

- [fact; source: https://api.crossref.org/works/10.1145/3194133.3194139] One seeded academic source was mislabeled and had to be replaced.
- [fact; source: https://www.iso.org/standard/81230.html] ISO/IEC 42001 evidence is lower resolution than APRA, DORA, or NIST evidence because only the official public summary was accessible in this runtime.
- [fact; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md] Public financial-services case studies confirm deployment, but they do not publish detailed metrics or full governance operating models for whole-enterprise policy coherence.
- [inference; source: https://pages.nist.gov/OSCAL/; https://www.openpolicyagent.org/docs/ocp/concepts] The invariant-registry pattern is architecturally credible, but there is uncertainty about how many regulated institutions have formalized it explicitly as a named program rather than as dispersed control catalogs and policy repositories.

### Open Questions

- [inference; source: https://github.com/open-policy-agent/opa/blob/master/ADOPTERS.md; https://www.infoq.com/presentations/opa-spring-boot-hocon/] What governance model, ownership model, and change-control process do regulated banks use internally when they attempt to map free-text policy estates into machine-readable authorization or control artifacts?
- [inference; source: https://pages.nist.gov/OSCAL/; https://cedar-policy.github.io/cedar-docs/] What is the minimum viable sequence for moving from prose policies to a typed invariant catalog in a bank with partial data classification and mixed legacy tooling?
- [inference; source: https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Will supervisors eventually expect firms to provide machine-readable evidence of policy coherence for higher-autonomy systems, even if current texts remain mechanism-neutral?

---

## Output

- Type: knowledge
- Description: Research conclusion that policy coherence is a practical prerequisite for agentic enforcement, that policy-as-code can make coherence checkable only after policy intent is formalized, and that a machine-readable control catalog plus schemas and policy bundles is the most workable invariant-registry pattern for a regulated bank.
- Links:
  - https://ar5iv.labs.arxiv.org/html/1503.02732
  - https://www.openpolicyagent.org/
  - https://pages.nist.gov/OSCAL/
