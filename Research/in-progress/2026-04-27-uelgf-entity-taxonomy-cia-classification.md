---
title: "Universal Entity Lifecycle Governance Framework (UELGF): canonical entity taxonomy and Confidentiality, Integrity, and Availability (CIA) classification system for determining governance intensity"
added: 2026-04-27T01:28:25+00:00
status: reviewing
priority: high
blocks: [2026-04-27-uelgf-synthesis-complete-framework]
tags: [uelgf, entity-taxonomy, cia-classification, governance-profile, agentic-ai, autonomous-agents, citizen-development, saas, data-products, regulated-banking, risk-tiering]
started: 2026-04-27T05:37:31+00:00
completed: ~
output: [knowledge]
---

# Universal Entity Lifecycle Governance Framework (UELGF): canonical entity taxonomy and Confidentiality, Integrity, and Availability (CIA) classification system for determining governance intensity

## Research Question

What canonical entity taxonomy and Confidentiality, Integrity, and Availability (CIA) classification system should the UELGF use to determine governance intensity, ensuring that every entity type, from a fully autonomous Artificial Intelligence (AI) agent to a procurement decision, receives a governance profile that is proportionate to its actual risk and that the classification process cannot be gamed by builder self-assessment at high CIA tiers?

## Scope

**In scope:**
- Canonical entity taxonomy covering all entity types: Artificial Intelligence (AI) agents (subdivided by autonomy level), software services, Software as a Service (SaaS) products, data products, frontend applications, integration components, decision workflows, and policy and content artefacts
- For each entity type: distinguishing properties, observable characteristics at rail entry, mandatory classification inputs the builder must provide, mandatory invariants assigned at scaffold generation, and lifecycle stage variations
- CIA rating system: Confidentiality axis (data classification, subject count), Integrity axis (action reversibility, blast radius at machine speed), Availability axis (dependency criticality, failure consequence)
- CIA rating tiers (minimum: Low, Medium, High, Critical) with explicit thresholds per axis and tier
- CIA rating assignment process: who assigns, on what evidence, appeal and override process, and automatic rating floors by entity type
- Governance profile matrix: mapping of entity type x CIA tier to applicable policy layers, mandatory hard gates, manual checkpoint requirements, observability requirements, and maximum re-evaluation intervals
- Criteria for automatic rating escalation when observed behaviour exceeds declared classification

**Out of scope:**
- Rail specifications for each entity type and CIA tier combination (covered by `2026-04-27-uelgf-governed-golden-rails`)
- Policy architecture design (covered by `2026-04-27-uelgf-policy-architecture-8-layer-context`)
- Foundational framework principles (covered by `2026-04-27-uelgf-foundational-definitions-principles`)
- Decommission and runtime feedback loop specifications

**Constraints:**
- The taxonomy must be exhaustive for the purposes of the framework
- CIA classification thresholds must be grounded in observable, measurable criteria, not qualitative self-assessment at Medium tier and above
- The AI agent autonomy sub-taxonomy must place a given agent in exactly one sub-category without ambiguity

## Context

[fact; source: https://handbook.apra.gov.au/standard/cps-234; https://handbook.apra.gov.au/ppg/cpg-234] Australian Prudential Regulation Authority (APRA) Prudential Standard (CPS) 234 and Prudential Practice Guide (CPG) 234 require information assets to be protected with controls commensurate with their criticality and sensitivity, so the UELGF needs a classification layer that turns asset properties into proportionate governance intensity.

[fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF) Core says the Map function must document intended purpose, human oversight, knowledge limits, organizational risk tolerance, and the likelihood and magnitude of impacts before a go or no-go decision is made, so the UELGF cannot rely on a single undifferentiated risk label.

[inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Prior completed repository work already established that enterprise governance depends on distinct machine identities, proportional risk tiering, lifecycle-aware enforcement topology, and a central policy plane, so this item supplies the missing classification substrate those controls must consume.

## Approach

1. **Entity type taxonomy construction:** Survey operational taxonomies and adjacent completed repository work to identify stable distinctions between passive artefacts, interactive surfaces, execution components, data assets, decision objects, and AI agents.
2. **AI agent autonomy sub-taxonomy:** Produce mutually exclusive autonomy classes with observable entry criteria and explicit falsification rules.
3. **CIA framework selection and adaptation:** Combine APRA criticality and sensitivity guidance, NIST Special Publication (SP) 800-30 impact and likelihood framing, NIST AI RMF context mapping, and Payment Card Industry Data Security Standard (PCI DSS) scoping floors into a three-axis model.
4. **Rating floor and override mechanisms:** Translate non-discretionary classification patterns from regulated information security, payment-card scoping, and software assurance into anti-gaming floor rules.
5. **Governance profile matrix construction:** Build tier baselines and entity-type modifiers that map into the eight-layer context model and the repository's adjacent governance items.
6. **Invariants at scaffold generation:** Identify which declared attributes become immutable until formal re-evaluation.

## Sources

- [x] [APRA CPS 234 Information Security](https://handbook.apra.gov.au/standard/cps-234) - primary definitions for confidentiality, integrity, availability, criticality, sensitivity, and board accountability
- [x] [APRA CPG 234 Information Security](https://handbook.apra.gov.au/ppg/cpg-234) - primary guidance on classification methodology, lifecycle controls, and annual or material-change review
- [x] [APRA information security landing page](https://www.apra.gov.au/information-security) - official APRA source pointing to the current CPS 234 and CPG 234 artefacts
- [x] [APRA CPG 234 PDF](https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf) - primary text used for direct extraction of classification-methodology clauses
- [x] [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) - primary risk-assessment guidance for likelihood and impact framing
- [x] [NIST likelihood glossary entry](https://csrc.nist.gov/glossary/term/likelihood) - direct NIST definition linked back to SP 800-30
- [x] [NIST AI RMF 1.0 publication page](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) - primary description of the AI RMF's purpose and scope
- [x] [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - primary source for intended purpose, human oversight, impact likelihood and magnitude, and go or no-go logic
- [x] [NIST AI RMF Playbook Map page](https://airc.nist.gov/airmf-resources/playbook/map/) - official companion page for Map-function implementation guidance
- [x] [PCI DSS standard page](https://www.pcisecuritystandards.org/standards/pci-dss/) - official scoping statement for cardholder data, sensitive authentication data, and systems that could impact the cardholder data environment
- [x] [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) - official document-library entry point for PCI DSS v4.0.1 artefacts
- [x] [Amazon Web Services (AWS) ARN and namespace reference](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) - primary evidence that operational asset taxonomies distinguish resources by service namespace and resource type
- [x] [The Open Group ArchiMate 4 Specification overview](https://publications.opengroup.org/c260) - official reference that enterprise architecture uses explicit domain distinctions rather than one undifferentiated asset class
- [x] [Federal Aviation Administration (FAA) Order 8110.49A](https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf) - official software-approval guidance showing software levels are assigned by system safety assessment rather than developer preference
- [x] [Federal Aviation Administration (FAA) AC 20-115C](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115C.pdf) - official advisory circular that ties compliance activities to the assigned software level
- [x] [AI agent control plane architecture for enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) - prior completed item on autonomy levels and control-plane implications
- [x] [AI agent identity and access management for enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - prior completed item on machine identity, delegation, and least privilege by actor type
- [x] [AI and low-code risk tier classification and controls](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html) - prior completed item on highest-triggered-tier logic and proportional control depth
- [x] [Business-led low-code agent governance](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html) - prior completed item on bounded complexity, central governance, and maker incentives
- [x] [Policy Administration Point (PAP) dynamic policy profiling and proportionality](https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html) - prior completed item on CIA-driven proportional enforcement topology
- [x] [ServiceNow Common Service Data Model (CSDM): Practical Data Modelling Across ITSM, APM, SPM, IRM, and FSO](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html) - prior completed item on business application, service instance, and technical-service distinctions
- [x] [AI concept classification taxonomy](https://davidamitchell.github.io/Research/research/2026-03-10-ai-concept-classification-taxonomy.html) - prior completed item on mutually exclusive taxonomy construction
- [x] [Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) - prior completed item on machine-speed blast radius and least-privilege amplification

## Related

- [AI and low-code risk tier classification and controls](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html)
- [Policy Administration Point (PAP) dynamic policy profiling and proportionality](https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html)
- [AI agent identity and access management for enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://handbook.apra.gov.au/standard/cps-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] **Research question restated:** what single canonical taxonomy and CIA assignment process should the Universal Entity Lifecycle Governance Framework (UELGF) use so that each governed entity receives one unambiguous type, one evidence-based CIA classification, and one governance profile that cannot be reduced by optimistic builder self-assessment?
- [fact; source: https://handbook.apra.gov.au/ppg/cpg-234; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://www.pcisecuritystandards.org/standards/pci-dss/] **Scope confirmed:** the investigation covers taxonomy, AI agent autonomy classes, CIA thresholds, automatic floors, assignment and appeal process, scaffold-time invariants, and governance-profile mapping, but does not design the downstream rail implementations.
- [fact; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://www.federalregister.gov/documents/2025/09/24/2025-18468/computer-software-assurance-for-production-and-quality-system-software-guidance-for-industry-and-food] Access note: official nuclear and pharmaceutical high-assurance sources were partially inaccessible in this runtime, and the Federal Register anti-bot page blocked deeper retrieval of the Food and Drug Administration (FDA) guidance notice, so decisive floor evidence in this item relies on APRA, PCI DSS, NIST, and Federal Aviation Administration (FAA) material rather than on a full cross-domain triad.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] **Prior work cross-reference:** adjacent completed items already established the control-plane architecture, machine-identity model, proportional risk-tier logic, and PAP-side topology derivation that this classification layer must drive.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] **Output format confirmed:** knowledge, expressed as a canonical taxonomy, a CIA threshold model, floor and override rules, scaffold-time invariants, and a compositional governance matrix mapped to the eight-layer context model.

### §1 Question Decomposition

1. **Canonical taxonomy**
   1. What stable entity families are needed so every governed object maps to exactly one class?
   2. What tie-breaker should apply when an entity looks like more than one type?
2. **AI agent autonomy**
   1. What mutually exclusive autonomy classes are operationally distinguishable at rail entry?
   2. What observable falsification criterion moves an agent to the next class?
3. **CIA model**
   1. What should the Confidentiality axis measure?
   2. What should the Integrity axis measure?
   3. What should the Availability axis measure?
   4. Should overall tier be averaged or set by the highest triggered axis?
4. **Floors and anti-gaming**
   1. Which entity types need automatic minimum tiers?
   2. Who supplies evidence and who is allowed to assign or override a tier?
   3. What appeal path is safe without restoring self-assessment bias?
5. **Scaffold invariants and escalation**
   1. Which declared attributes should become immutable until re-evaluation?
   2. Which observed behaviours should automatically escalate classification?
6. **Governance profile**
   1. Which policy layers, gates, manual checkpoints, observability controls, and review cadences belong to each tier?
   2. Which extra controls are entity-specific modifiers rather than generic tier baselines?

### §2 Investigation

#### Source replacement and continuity notes

- [fact; source: https://www.apra.gov.au/information-security; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] The seeded APRA PDF path returned 404 in this runtime, so the source list was updated to the current APRA information-security landing page and the working current PDF URL.
- [fact; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] The seeded ServiceNow class-hierarchy page did not yield accessible text in this runtime, so the taxonomy baseline relies on the accessible AWS and Open Group sources plus the prior completed ServiceNow Common Service Data Model (CSDM) item for the operational service-application split.

#### A. What existing taxonomies imply about canonical entity classes

- [fact; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html] Amazon Web Services (AWS) identifies operational assets by service namespace and resource type, which is direct evidence that enterprise-governed estates stay tractable when resource classes are defined by what the entity is and does, not by which team owns it.
- [fact; source: https://publications.opengroup.org/c260] The Open Group positions ArchiMate as a modeling language for describing relationships among business domains through explicit domain distinctions rather than through one undifferentiated asset bucket.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] The completed ServiceNow CSDM item found that durable enterprise models distinguish business applications, service instances, technical services, reference data, and portfolio overlays because operational traceability and governance break when strategic objects and runtime objects are collapsed into one class.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-ai-concept-classification-taxonomy.html] The completed AI concept taxonomy item concluded that a stable taxonomy requires a mutually exclusive, collectively exhaustive rule plus a deterministic tie-breaker for borderline cases.
- [inference; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-03-10-ai-concept-classification-taxonomy.html] The UELGF taxonomy should therefore separate entities by dominant executed function at rail entry: passive content or policy artefact, passive data product, interactive frontend surface, execution component, shared software service, SaaS product or tenant-bound platform surface, decision workflow, and AI agent.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The correct tie-breaker is "highest-action surface wins": if a nominal data product also executes actions, it is classified as an execution component or AI agent rather than as a passive data object, because governance intensity must follow consequence, not packaging.

#### B. What the evidence supports for AI agent autonomy classes

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Map 2.2 requires documentation of an AI system's knowledge limits and how outputs will be utilized and overseen by humans, which makes human initiation, oversight pattern, and execution independence first-class classification inputs.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Map 3.5 requires processes for human oversight to be defined, assessed, and documented, which supports distinguishing agent classes by whether a run is initiated, supervised, or halted by a human.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html] The completed business-led low-code governance item found that durable citizen-development programs bound business-user automations to low-complexity attended use cases and central governance, rather than allowing unconstrained autonomous execution.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The completed control-plane item treated heterogeneous enforcement adapters, event-driven policy propagation, and persistent runtime governance as requirements only once agents operate beyond a single attended interaction.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The completed machine-identity item concluded that autonomous work should run under a bounded non-human identity rather than under borrowed human sessions, which is direct evidence that autonomy class and identity model are coupled.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The operationally defensible four-class agent ladder is: Agent-1 declarative or scoped assistant, Agent-2 user-invoked tool-using action agent, Agent-3 event-triggered bounded autonomous agent, and Agent-4 fully autonomous agent that can maintain or reprioritize work across time.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The falsification rules are crisp: a side-effecting tool call moves an entity above Agent-1; a scheduled or event-triggered run without per-run human initiation moves it above Agent-2; the ability to create, chain, or reprioritize tasks across sessions moves it above Agent-3.

#### C. What existing frameworks contribute to a CIA model

- [fact; source: https://handbook.apra.gov.au/standard/cps-234] CPS 234 defines confidentiality as access restricted only to those authorised, integrity as completeness, accuracy, and freedom from unauthorised change or usage, availability as accessibility and usability when required, criticality as the potential impact of a loss of availability, and sensitivity as the potential impact of a loss of confidentiality or integrity.
- [fact; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] CPG 234 says all information assets must be classified by criticality and sensitivity, that the methodology should rate criticality and sensitivity separately, and that assets not intrinsically critical or sensitive can still require a higher classification if they could be used to compromise critical or sensitive assets.
- [fact; source: https://csrc.nist.gov/glossary/term/likelihood; https://csrc.nist.gov/pubs/sp/800/30/r1/final] NIST SP 800-30 defines likelihood as a weighted factor based on the probability that a threat can exploit a vulnerability and uses impact as the magnitude of harm expected from compromise, so a defensible classification model needs explicit, reviewable threshold criteria rather than narrative labels alone.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Map 1.1, 2.2, 3.3, 3.5, and 5.1 require intended purpose, knowledge limits, targeted application scope, human oversight, and the likelihood and magnitude of impacts to be documented before deployment.
- [fact; source: https://www.pcisecuritystandards.org/standards/pci-dss/] PCI DSS applies not only to entities that store, process, or transmit cardholder data and sensitive authentication data, but also to entities that could impact the security of the cardholder data environment, which is a direct example of a non-discretionary classification floor driven by consequence and adjacency.
- [inference; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] The best-fit UELGF model is therefore a three-axis CIA scheme that keeps the APRA split between availability and confidentiality or integrity, uses NIST-style impact framing to define thresholds, imports AI RMF inputs for action systems, and uses PCI-style in-scope logic to apply minimum floors where certain surfaces are categorically high consequence.
- [inference; source: https://handbook.apra.gov.au/standard/cps-234; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] Overall tier should be the maximum triggered axis after entity floors are applied, not an average of the three axes, because a single Critical Integrity surface such as payment execution must not be diluted by Low Confidentiality or Medium Availability scores.

#### D. What floor mechanisms prevent classification gaming

- [fact; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115C.pdf] FAA Order 8110.49A and AC 20-115C repeatedly treat software level as something assigned by the system safety assessment and then used to determine assurance activities, which is evidence that high-assurance governance does not let builders choose their own minimum consequence class.
- [fact; source: https://handbook.apra.gov.au/standard/cps-234] CPS 234 places ultimate information-security responsibility on the Board and requires controls commensurate with asset criticality and sensitivity, which means the accountable governance function, not the builder alone, must own the final classification outcome.
- [fact; source: https://www.pcisecuritystandards.org/standards/pci-dss/] PCI DSS establishes that handling sensitive payment data or being able to affect the payment-card environment puts a system in scope by rule rather than by self-description, which is the strongest accessible analogue for automatic floors.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] The completed access-control amplification item showed that machine-speed execution changes blast radius even under unchanged permissions, so autonomy and write authority must create minimum Integrity floors before any likelihood modeling is debated.
- [inference; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://handbook.apra.gov.au/standard/cps-234; https://www.pcisecuritystandards.org/standards/pci-dss/; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] The safe assignment pattern is: the builder submits evidence, the platform or PAP computes provisional floors automatically, architecture and security validate Medium, High, and Critical triggers, and any downward override above Low requires independent approval plus evidence that the triggering attribute is absent rather than merely mitigated.

#### E. What should become scaffold-time invariants

- [fact; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] CPG 234 recommends a process that updates classification at least annually or when there is a material change to information assets or the business environment, which implies that some declared attributes must be stable enough to detect and govern material change.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Map requires intended purpose, knowledge limits, targeted application scope, and human oversight processes to be documented as part of context establishment and categorization.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Adjacent completed items already depend on machine-identity type, privileged-access status, and declared invariants to derive enforcement topology, so those values cannot be treated as ordinary mutable metadata.
- [inference; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] The scaffold-time invariants should be: canonical entity type, AI agent autonomy class if applicable, declared data classes, declared write surfaces, privileged-access status, external exposure, regulatory domain, dependency criticality, and human-checkpoint pattern.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] A change to any invariant should trigger full re-evaluation rather than a minor update, because each of those attributes alters either intended purpose, human oversight, or impact magnitude.

#### F. What should trigger automatic escalation after deployment

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Measure and Manage require production monitoring, tracking of existing and emergent risks over time, and deactivation or disengagement when deployed systems perform inconsistently with intended use.
- [fact; source: https://handbook.apra.gov.au/ppg/cpg-234] CPG 234 links lifecycle controls, configuration management, monitoring, and change management to the criticality and sensitivity of information assets, which supports automatic reclassification when runtime facts diverge from the declared model.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://handbook.apra.gov.au/ppg/cpg-234; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Automatic escalation should be triggered when observed behaviour exceeds declared classification, including: new side-effecting tools, scheduled or event-triggered operation added after intake, widened data-domain access, increased subject-count range, new privileged credentials, failure of a human checkpoint, new downstream dependency on a critical operation, or repeated runtime policy denials indicating undeclared intended use.

### §3 Reasoning

- [inference; source: https://handbook.apra.gov.au/standard/cps-234; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The model should separate entity type from CIA tier because taxonomy answers "what kind of governed object is this?" while CIA answers "how much governance does this instance require?" and collapsing the two would make the taxonomy unstable whenever risk changes over time.
- [inference; source: https://handbook.apra.gov.au/standard/cps-234; https://www.pcisecuritystandards.org/standards/pci-dss/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] Highest-triggered-tier logic is safer than averaging because single-surface catastrophic consequence is common in regulated systems, for example a low-volume payment rail or privileged policy-update path.
- [inference; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://handbook.apra.gov.au/standard/cps-234; https://www.pcisecuritystandards.org/standards/pci-dss/] Minimum floors should be determined by consequence-bearing surface rather than by builder narrative, because every accessible high-assurance analogue in the evidence base uses externally assigned or rule-based minimum consequence classes.
- [assumption; source: https://handbook.apra.gov.au/ppg/cpg-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Subject-count bands are usable as an observable Confidentiality proxy where exact counts are not yet known. **Justification:** both APRA and NIST require classification before full operational history exists, so the intake model needs bounded proxy thresholds for initial assignment.

### §4 Consistency Check

- [fact; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] The proposed CIA axes remain consistent with APRA because they preserve APRA's distinction between availability impact and confidentiality or integrity impact instead of collapsing them into one score.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] The proposed automatic floors do not contradict NIST's context-sensitive framing because floors establish a minimum starting class, while context, likelihood, and magnitude can still escalate the entity above that floor.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] The proposed governance matrix is aligned with adjacent repository work because it feeds machine-identity constraints, PAP topology derivation, and the eight-layer context hierarchy instead of creating a competing control model.

### §5 Depth and Breadth Expansion

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] **Behavioural lens:** builder self-assessment is structurally biased downward because governance friction is experienced locally by the builder while blast radius is borne by the enterprise, so independent assignment is a control against incentive distortion rather than a bureaucratic flourish.
- [inference; source: https://handbook.apra.gov.au/ppg/cpg-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] **Regulatory lens:** annual review or material-change review is too slow for autonomous or event-driven entities unless runtime observability can trigger automatic reclassification, which is why static intake alone is insufficient.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] **Economic lens:** a precise Low tier for passive artefacts and read-only utilities is not cosmetic, because over-classifying low-risk items creates workaround pressure and shadow development that eventually weakens governance for the genuinely high-risk items.
- [inference; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://handbook.apra.gov.au/standard/cps-234; https://www.pcisecuritystandards.org/standards/pci-dss/] **Historical lens:** the most durable control regimes start from consequence classes, then scale assurance activities from those classes, which supports using floors plus evidence-based escalation rather than free-form expert scoring.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

[inference; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] The UELGF should classify every governed object into one canonical entity type and one CIA tier using highest-triggered-axis scoring plus mandatory floors, because APRA separates availability impact from confidentiality or integrity impact, NIST requires documented context and impact analysis, and PCI shows that some control surfaces are high consequence by rule rather than by self-description.

[inference; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The canonical taxonomy should distinguish passive policy or content artefacts, passive data products, interactive frontend applications, integration components, software services, SaaS products, decision workflows, and four mutually exclusive AI agent autonomy classes, with classification assigned to the highest-action surface exposed at rail entry.

[inference; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://handbook.apra.gov.au/standard/cps-234; https://www.pcisecuritystandards.org/standards/pci-dss/; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Builder self-assessment should stop at evidence submission, because the accessible high-assurance analogues all place minimum consequence class assignment outside developer discretion, and machine-speed blast radius means autonomy, privileged access, and regulated-data adjacency must impose automatic floors before builder optimism can reduce them.

[inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Governance intensity should then be applied compositionally: tier baselines determine which policy layers, gates, manual checkpoints, observability controls, and review cadences apply, while entity-type modifiers add specific controls for agents, decision workflows, data products, and privileged execution surfaces.

**Key findings:**

1. [inference; confidence: high; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] A stable UELGF taxonomy should classify entities by dominant executed function rather than by owning team or implementation medium, because operational taxonomies remain durable only when runtime consequence, service role, and domain boundary are separated explicitly.
2. [inference; confidence: high; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] AI agents need four mutually exclusive autonomy classes with observable falsifiers, because human oversight, trigger mode, and task persistence cleanly separate attended assistants from tool-using, event-triggered, and fully autonomous actors at intake.
3. [inference; confidence: high; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The CIA model should keep Confidentiality, Integrity, and Availability separate and set overall tier to the highest triggered axis, because regulated guidance treats those harms as distinct and a single catastrophic action surface must not be averaged away.
4. [inference; confidence: high; source: https://handbook.apra.gov.au/standard/cps-234; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Confidentiality thresholds should be driven by data class and subject scale, Integrity thresholds by reversibility and machine-speed blast radius, and Availability thresholds by dependency criticality and outage tolerance, because those are the observable factors the reviewed standards repeatedly require teams to document.
5. [inference; confidence: high; source: https://www.pcisecuritystandards.org/standards/pci-dss/; https://handbook.apra.gov.au/standard/cps-234; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Mandatory floors must be attached to entity type and consequence-bearing surfaces rather than to builder opinion, because payment-card scope, prudential information-security accountability, software-assurance levels, and agentic blast-radius evidence all show that some classes are too consequential for discretionary downgrading.
6. [inference; confidence: high; source: https://handbook.apra.gov.au/standard/cps-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html] High and Critical assignments should be independently validated and downward appeals should require contrary evidence instead of compensating-control narratives, because the enterprise bears the downside of under-classification while the builder experiences only the local cost of stronger governance.
7. [inference; confidence: high; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Scaffold generation should stamp immutable invariants for entity type, autonomy class, data class, write capability, privilege level, external exposure, dependency criticality, and human-checkpoint pattern, because any change to those attributes materially changes risk and enforcement topology.
8. [inference; confidence: high; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] The governance profile should be implemented as tier baselines plus entity modifiers rather than as a flat bespoke matrix, because that structure is exhaustive, composable, and directly consumable by the adjacent policy-layer and PAP-topology items.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Dominant-function taxonomy is more durable than owner-based classification. | https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html ; https://publications.opengroup.org/c260 ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html | high | External operational taxonomies plus prior completed ServiceNow work support the split between passive, interactive, and execution entities. |
| [inference] Four autonomy classes with falsifiers are operationally distinguishable. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | high | Human oversight, trigger mode, and persistent work are the decisive separators. |
| [inference] Overall CIA tier should equal the highest triggered axis. | https://handbook.apra.gov.au/standard/cps-234 ; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf ; https://csrc.nist.gov/pubs/sp/800/30/r1/final ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | high | APRA's split and NIST's impact framing both support non-averaged consequence handling. |
| [inference] Axis thresholds should be tied to data class, reversibility or blast radius, and dependency criticality. | https://handbook.apra.gov.au/standard/cps-234 ; https://csrc.nist.gov/pubs/sp/800/30/r1/final ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | high | These are the observable intake fields the standards repeatedly require. |
| [inference] Mandatory floors should be rule-based for certain types and surfaces. | https://www.pcisecuritystandards.org/standards/pci-dss/ ; https://handbook.apra.gov.au/standard/cps-234 ; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html | high | PCI scoping, APRA board accountability, FAA assigned software levels, and agentic blast radius all point to non-discretionary minima. |
| [inference] High and Critical assignments should be independently validated and only downgraded with contrary evidence. | https://handbook.apra.gov.au/standard/cps-234 ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html | high | Incentive asymmetry makes builder-only classification unsafe. |
| [inference] Scaffold-time invariants must include type, autonomy, data, write surface, privilege, exposure, dependency, and checkpoint pattern. | https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html | high | Those attributes drive lifecycle controls and topology derivation. |
| [inference] Tier baselines plus entity modifiers are the right governance-profile construction method. | https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html | high | This keeps the matrix compositional and aligned with adjacent work. |

**Assumptions:**

- [assumption; source: https://handbook.apra.gov.au/ppg/cpg-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Subject-count bands can be used as an intake proxy for Confidentiality where exact live counts are unavailable. **Justification:** pre-deployment classification still requires measurable thresholds before runtime history exists.
- [assumption; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] The accessible AWS and ArchiMate sources plus the completed ServiceNow CSDM item are sufficient to anchor the entity-family split despite the seeded ServiceNow hierarchy page being inaccessible in this runtime. **Justification:** all three sources support the same active-versus-passive and strategic-versus-runtime distinctions.

**Analysis:**

[inference; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-03-10-ai-concept-classification-taxonomy.html] **Proposed canonical entity taxonomy and default floors:**

| Entity type | Distinguishing property | Observable entry evidence | Mandatory builder inputs | Scaffold invariants | Default floor |
|---|---|---|---|---|---|
| Policy or content artefact | Declares, constrains, or communicates but does not execute | File type, publication target, no runtime identity | audience, regulated use, downstream enforcement use | regulated use, publication channel | Low |
| Data product | Primary value is maintained data for consumption by others | dataset schema, access path, producer, consumers | data classes, subject-count band, refresh cadence | data classes, subject-count band, external sharing | Low, or High if regulated data |
| Frontend application | Interactive user surface without independent orchestration | user interface, session model, channel exposure | auth model, data classes, write surfaces | auth mode, write surfaces, external exposure | Low |
| Integration component | Moves, transforms, or synchronizes data or commands across systems | connector list, endpoints, triggers | source and target systems, directionality, write surfaces | endpoint scope, trigger mode, write surfaces | Medium |
| Software service | Hosts business or technical capability behind an interface | service endpoint, deployment identity, dependent systems | dependency class, write surfaces, recovery tolerance | dependency criticality, privilege level | Medium |
| SaaS product | Externally provided application surface with tenant-level governance | vendor platform, tenant boundaries, admin surface | vendor role, system-of-record status, data classes | vendor role, system-of-record status | Medium |
| Decision workflow | Produces binding approval or rejection state | workflow engine, approval outcome, downstream actuation | decision consequence, reversal path, human checkpoint | decision consequence, checkpoint pattern | High |
| AI agent | Uses model-led reasoning to answer, decide, or act | model component, tool surface, trigger mode | autonomy class, tool set, checkpoint pattern | autonomy class, tool set, checkpoint pattern | Class-dependent |

[inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] **AI agent autonomy sub-taxonomy:**

| Class | Definition | Entry test | Falsification trigger | Floor |
|---|---|---|---|---|
| Agent-1 Declarative or scoped assistant | Generates content or analysis inside a user-invoked interaction and has no side-effecting tool execution | no external write, no independent trigger | any side-effecting tool call | Low |
| Agent-2 User-invoked action agent | Runs only inside an explicit user request but can call tools or APIs to read or write during that session | user initiation required per run | scheduled or event-triggered execution | Medium |
| Agent-3 Event-triggered bounded autonomous agent | Executes on schedule or event without per-run initiation, but goal is predefined and bounded | autonomous trigger, fixed scope | persistent task creation or reprioritization | High |
| Agent-4 Fully autonomous agent | Can create, chain, or reprioritize work across time and operate under its own bounded machine identity | persistent work graph or independent re-entry | not applicable, this is top class | High, or Critical with privileged or consequential write access |

[inference; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] **CIA threshold model:**

| Axis | Low | Medium | High | Critical |
|---|---|---|---|---|
| Confidentiality | public or internal operational data, no regulated personal or secret material | internal confidential business data or limited personal data | customer personal, financial, authentication, or security-sensitive data, or broad subject-scale exposure | payment credentials, encryption keys, privileged secrets, or data whose exposure materially threatens customers or enterprise control |
| Integrity | read-only or fully reversible internal changes | bounded writes with routine correction path | consequential writes to production, regulated records, customer communications, or approval states | legally, financially, or operationally irreversible machine-speed action, including privileged policy or payment execution |
| Availability | outage tolerable for more than five business days with simple workaround | outage tolerable for one to five business days with costly workaround | outage materially disrupts critical operations or customers within one business day | outage threatens critical operation, regulatory obligation, or customer access within hours |

[inference; source: https://www.pcisecuritystandards.org/standards/pci-dss/; https://handbook.apra.gov.au/standard/cps-234; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] **Automatic floors and assignment process:**

| Trigger | Minimum result | Why it floors |
|---|---|---|
| Cardholder or sensitive authentication data, or system can impact that environment | Confidentiality High and overall High minimum | PCI treats those surfaces as in scope by rule |
| Privileged credentials, policy mutation, payment execution, or production deployment authority | Integrity Critical | Reversal is too slow or incomplete once action is exercised |
| Decision workflow affecting customer, credit, procurement, or regulatory commitment | Integrity High minimum | The primary risk is wrong or premature binding state change |
| Agent-3 autonomy | overall High minimum | Non-attended execution removes per-run human initiation |
| Agent-4 plus privileged or consequential write access | overall Critical minimum | Machine-speed multi-step action creates enterprise-scale blast radius |
| System of record for critical operation | Availability High minimum | Operational dependency dominates governance intensity |

| Step | Actor | Rule |
|---|---|---|
| Evidence submission | builder | declares type, surfaces, data, dependencies, autonomy, and checkpoints |
| Provisional scoring | platform or PAP | computes axis scores and floors automatically |
| Medium validation | architecture plus security owner | confirms declared evidence and floors |
| High validation | architecture, security, and risk owner | required before rail approval |
| Critical validation | architecture, security, risk, and accountable executive | required before build or deployment progresses |
| Downward appeal | independent review body | allowed only if triggering attribute is factually absent |

[inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] **Governance profile matrix, built as tier baselines plus entity modifiers:**

| Tier baseline | Applicable policy layers | Mandatory hard gates | Manual checkpoints | Observability | Maximum re-evaluation interval |
|---|---|---|---|---|---|
| Low | Layers 5, 7, 8 | scaffold lint and policy conformance only | none by default | inventory plus basic audit log | 12 months |
| Medium | Layers 5, 6, 7, 8 | intake validation, identity check, delivery gate | owner approval | inventory, decision log, change log, dependency map | 6 months |
| High | Layers 1, 5, 6, 7, 8 | intake gate, identity gate, delivery gate, pre-production readiness gate | architecture, security, and risk checkpoint | full decision logs, access logs, policy-denial logs, anomaly alerts | 90 days |
| Critical | Layers 1, 2, 3, 5, 6, 7, 8 | hard intake gate, hard identity gate, hard delivery gate, production enablement gate | accountable executive plus independent risk sign-off | real-time telemetry, immutable audit trail, rollback and kill-switch validation, continuous anomaly monitoring | 30 days |

| Entity modifier | Extra controls added to baseline |
|---|---|
| Policy or content artefact | add review for regulated publication and version integrity when downstream enforcement depends on content |
| Data product | add schema drift, access-pattern, and downstream-consumer monitoring |
| Frontend application | add user-session telemetry and channel-specific abuse monitoring |
| Integration component | add connector allow-list, source-target lineage, and rate anomaly monitoring |
| Software service | add dependency health, privileged-operation logging, and release provenance |
| SaaS product | add vendor-admin review, tenant-boundary review, and compensating-control check |
| Decision workflow | add mandatory human override route, outcome attribution, and decision-sampling review |
| AI agent | add autonomy-specific tool-call logs, prompt or policy version binding, and checkpoint-failure escalation |

**Risks, gaps, uncertainties:**

- [fact; source: https://www.federalregister.gov/documents/2025/09/24/2025-18468/computer-software-assurance-for-production-and-quality-system-software-guidance-for-industry-and-food] The official Federal Register path for current FDA Computer Software Assurance guidance was anti-bot gated in this runtime, so pharmaceutical-manufacturing evidence was not used to support the final floor model.
- [fact; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] APRA gives methodology direction rather than numeric thresholds, so the exact subject-count and outage-tolerance bands in the proposed model are a synthesis layer rather than regulator-prescribed numbers.
- [fact; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115C.pdf] FAA material in this runtime was more usable for the governance pattern of assigned consequence classes than for a detailed extraction of all software-level definitions, so aviation is used here as an assignment analogue rather than as a one-to-one numeric template.

**Open questions:**

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Should the PAP expose floors as human-readable policy rules or only as computed outputs from a topology-derivation function?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Should Agent-4 entities be split again by whether they can modify their own tool graph or only their task graph?
- [inference; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] What empirical subject-count and outage-tolerance thresholds best fit the target banking context without creating unnecessary High classifications for low-consequence internal data sets?

### §7 Recursive Review

- [fact; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] Each substantive claim in the synthesis is either tied to accessible primary sources or labelled as inference or assumption, and the final model preserves the reviewed standards' separation between context establishment, consequence assessment, and proportional control application.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Repository cross-reference was performed against adjacent completed items touching identity, policy topology, and proportional control depth, and the synthesis is aligned with those items rather than duplicating or contradicting them.
- [inference; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://www.federalregister.gov/documents/2025/09/24/2025-18468/computer-software-assurance-for-production-and-quality-system-software-guidance-for-industry-and-food] The main unresolved gap is not the structure of the proposed UELGF model but the incomplete retrieval of nuclear and pharmaceutical source material in this runtime, which is why the final answer treats aviation, prudential information security, and PCI scoping as the decisive floor analogues.

---

## Findings

### Executive Summary

[inference; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] The UELGF should classify every governed object into one canonical entity type and one CIA tier using highest-triggered-axis scoring plus mandatory floors, because APRA separates availability impact from confidentiality or integrity impact, NIST requires documented context and impact analysis, and PCI shows that some control surfaces are high consequence by rule rather than by self-description.

[inference; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The canonical taxonomy should distinguish passive policy or content artefacts, passive data products, interactive frontend applications, integration components, software services, SaaS products, decision workflows, and four mutually exclusive AI agent autonomy classes, with classification assigned to the highest-action surface exposed at rail entry.

[inference; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://handbook.apra.gov.au/standard/cps-234; https://www.pcisecuritystandards.org/standards/pci-dss/; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Builder self-assessment should stop at evidence submission, because the accessible high-assurance analogues all place minimum consequence class assignment outside developer discretion, and machine-speed blast radius means autonomy, privileged access, and regulated-data adjacency must impose automatic floors before builder optimism can reduce them.

[inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Governance intensity should then be applied compositionally: tier baselines determine which policy layers, gates, manual checkpoints, observability controls, and review cadences apply, while entity-type modifiers add specific controls for agents, decision workflows, data products, and privileged execution surfaces.

### Key Findings

1. [inference; confidence: high; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] A stable UELGF taxonomy should classify entities by dominant executed function rather than by owning team or implementation medium, because operational taxonomies remain durable only when runtime consequence, service role, and domain boundary are separated explicitly.
2. [inference; confidence: high; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] AI agents need four mutually exclusive autonomy classes with observable falsifiers, because human oversight, trigger mode, and task persistence cleanly separate attended assistants from tool-using, event-triggered, and fully autonomous actors at intake.
3. [inference; confidence: high; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The CIA model should keep Confidentiality, Integrity, and Availability separate and set overall tier to the highest triggered axis, because regulated guidance treats those harms as distinct and a single catastrophic action surface must not be averaged away.
4. [inference; confidence: high; source: https://handbook.apra.gov.au/standard/cps-234; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Confidentiality thresholds should be driven by data class and subject scale, Integrity thresholds by reversibility and machine-speed blast radius, and Availability thresholds by dependency criticality and outage tolerance, because those are the observable factors the reviewed standards repeatedly require teams to document.
5. [inference; confidence: high; source: https://www.pcisecuritystandards.org/standards/pci-dss/; https://handbook.apra.gov.au/standard/cps-234; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Mandatory floors must be attached to entity type and consequence-bearing surfaces rather than to builder opinion, because payment-card scope, prudential information-security accountability, software-assurance levels, and agentic blast-radius evidence all show that some classes are too consequential for discretionary downgrading.
6. [inference; confidence: high; source: https://handbook.apra.gov.au/standard/cps-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html] High and Critical assignments should be independently validated and downward appeals should require contrary evidence instead of compensating-control narratives, because the enterprise bears the downside of under-classification while the builder experiences only the local cost of stronger governance.
7. [inference; confidence: high; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Scaffold generation should stamp immutable invariants for entity type, autonomy class, data class, write capability, privilege level, external exposure, dependency criticality, and human-checkpoint pattern, because any change to those attributes materially changes risk and enforcement topology.
8. [inference; confidence: high; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] The governance profile should be implemented as tier baselines plus entity modifiers rather than as a flat bespoke matrix, because that structure is exhaustive, composable, and directly consumable by the adjacent policy-layer and PAP-topology items.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Dominant-function taxonomy is more durable than owner-based classification. | https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html ; https://publications.opengroup.org/c260 ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html | high | External operational taxonomies plus prior completed ServiceNow work support the split between passive, interactive, and execution entities. |
| [inference] Four autonomy classes with falsifiers are operationally distinguishable. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | high | Human oversight, trigger mode, and persistent work are the decisive separators. |
| [inference] Overall CIA tier should equal the highest triggered axis. | https://handbook.apra.gov.au/standard/cps-234 ; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf ; https://csrc.nist.gov/pubs/sp/800/30/r1/final ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | high | APRA's split and NIST's impact framing both support non-averaged consequence handling. |
| [inference] Axis thresholds should be tied to data class, reversibility or blast radius, and dependency criticality. | https://handbook.apra.gov.au/standard/cps-234 ; https://csrc.nist.gov/pubs/sp/800/30/r1/final ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | high | These are the observable intake fields the standards repeatedly require. |
| [inference] Mandatory floors should be rule-based for certain types and surfaces. | https://www.pcisecuritystandards.org/standards/pci-dss/ ; https://handbook.apra.gov.au/standard/cps-234 ; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html | high | PCI scoping, APRA board accountability, FAA assigned software levels, and agentic blast radius all point to non-discretionary minima. |
| [inference] High and Critical assignments should be independently validated and only downgraded with contrary evidence. | https://handbook.apra.gov.au/standard/cps-234 ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html | high | Incentive asymmetry makes builder-only classification unsafe. |
| [inference] Scaffold-time invariants must include type, autonomy, data, write surface, privilege, exposure, dependency, and checkpoint pattern. | https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html | high | Those attributes drive lifecycle controls and topology derivation. |
| [inference] Tier baselines plus entity modifiers are the right governance-profile construction method. | https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html | high | This keeps the matrix compositional and aligned with adjacent work. |

### Assumptions

- [assumption; source: https://handbook.apra.gov.au/ppg/cpg-234; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Subject-count bands can be used as an intake proxy for Confidentiality where exact live counts are unavailable. **Justification:** pre-deployment classification still requires measurable thresholds before runtime history exists.
- [assumption; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] The accessible AWS and ArchiMate sources plus the completed ServiceNow CSDM item are sufficient to anchor the entity-family split despite the seeded ServiceNow hierarchy page being inaccessible in this runtime. **Justification:** all three sources support the same active-versus-passive and strategic-versus-runtime distinctions.

### Analysis

[inference; source: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html; https://publications.opengroup.org/c260; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-03-10-ai-concept-classification-taxonomy.html] **Proposed canonical entity taxonomy and default floors:**

| Entity type | Distinguishing property | Observable entry evidence | Mandatory builder inputs | Scaffold invariants | Default floor |
|---|---|---|---|---|---|
| Policy or content artefact | Declares, constrains, or communicates but does not execute | file type, publication target, no runtime identity | audience, regulated use, downstream enforcement use | regulated use, publication channel | Low |
| Data product | Primary value is maintained data for consumption by others | dataset schema, access path, producer, consumers | data classes, subject-count band, refresh cadence | data classes, subject-count band, external sharing | Low, or High if regulated data |
| Frontend application | Interactive user surface without independent orchestration | user interface, session model, channel exposure | auth model, data classes, write surfaces | auth mode, write surfaces, external exposure | Low |
| Integration component | Moves, transforms, or synchronizes data or commands across systems | connector list, endpoints, triggers | source and target systems, directionality, write surfaces | endpoint scope, trigger mode, write surfaces | Medium |
| Software service | Hosts business or technical capability behind an interface | service endpoint, deployment identity, dependent systems | dependency class, write surfaces, recovery tolerance | dependency criticality, privilege level | Medium |
| SaaS product | Externally provided application surface with tenant-level governance | vendor platform, tenant boundaries, admin surface | vendor role, system-of-record status, data classes | vendor role, system-of-record status | Medium |
| Decision workflow | Produces binding approval or rejection state | workflow engine, approval outcome, downstream actuation | decision consequence, reversal path, human checkpoint | decision consequence, checkpoint pattern | High |
| AI agent | Uses model-led reasoning to answer, decide, or act | model component, tool surface, trigger mode | autonomy class, tool set, checkpoint pattern | autonomy class, tool set, checkpoint pattern | Class-dependent |

[inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] **AI agent autonomy sub-taxonomy:**

| Class | Definition | Entry test | Falsification trigger | Floor |
|---|---|---|---|---|
| Agent-1 Declarative or scoped assistant | Generates content or analysis inside a user-invoked interaction and has no side-effecting tool execution | no external write, no independent trigger | any side-effecting tool call | Low |
| Agent-2 User-invoked action agent | Runs only inside an explicit user request but can call tools or APIs to read or write during that session | user initiation required per run | scheduled or event-triggered execution | Medium |
| Agent-3 Event-triggered bounded autonomous agent | Executes on schedule or event without per-run initiation, but goal is predefined and bounded | autonomous trigger, fixed scope | persistent task creation or reprioritization | High |
| Agent-4 Fully autonomous agent | Can create, chain, or reprioritize work across time and operate under its own bounded machine identity | persistent work graph or independent re-entry | not applicable, this is top class | High, or Critical with privileged or consequential write access |

[inference; source: https://handbook.apra.gov.au/standard/cps-234; https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://csrc.nist.gov/pubs/sp/800/30/r1/final; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.pcisecuritystandards.org/standards/pci-dss/] **CIA threshold model:**

| Axis | Low | Medium | High | Critical |
|---|---|---|---|---|
| Confidentiality | public or internal operational data, no regulated personal or secret material | internal confidential business data or limited personal data | customer personal, financial, authentication, or security-sensitive data, or broad subject-scale exposure | payment credentials, encryption keys, privileged secrets, or data whose exposure materially threatens customers or enterprise control |
| Integrity | read-only or fully reversible internal changes | bounded writes with routine correction path | consequential writes to production, regulated records, customer communications, or approval states | legally, financially, or operationally irreversible machine-speed action, including privileged policy or payment execution |
| Availability | outage tolerable for more than five business days with simple workaround | outage tolerable for one to five business days with costly workaround | outage materially disrupts critical operations or customers within one business day | outage threatens critical operation, regulatory obligation, or customer access within hours |

[inference; source: https://www.pcisecuritystandards.org/standards/pci-dss/; https://handbook.apra.gov.au/standard/cps-234; https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] **Automatic floors and assignment process:**

| Trigger | Minimum result | Why it floors |
|---|---|---|
| Cardholder or sensitive authentication data, or system can impact that environment | Confidentiality High and overall High minimum | PCI treats those surfaces as in scope by rule |
| Privileged credentials, policy mutation, payment execution, or production deployment authority | Integrity Critical | Reversal is too slow or incomplete once action is exercised |
| Decision workflow affecting customer, credit, procurement, or regulatory commitment | Integrity High minimum | The primary risk is wrong or premature binding state change |
| Agent-3 autonomy | overall High minimum | Non-attended execution removes per-run human initiation |
| Agent-4 plus privileged or consequential write access | overall Critical minimum | Machine-speed multi-step action creates enterprise-scale blast radius |
| System of record for critical operation | Availability High minimum | Operational dependency dominates governance intensity |

| Step | Actor | Rule |
|---|---|---|
| Evidence submission | builder | declares type, surfaces, data, dependencies, autonomy, and checkpoints |
| Provisional scoring | platform or PAP | computes axis scores and floors automatically |
| Medium validation | architecture plus security owner | confirms declared evidence and floors |
| High validation | architecture, security, and risk owner | required before rail approval |
| Critical validation | architecture, security, risk, and accountable executive | required before build or deployment progresses |
| Downward appeal | independent review body | allowed only if triggering attribute is factually absent |

[inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] **Governance profile matrix, built as tier baselines plus entity modifiers:**

| Tier baseline | Applicable policy layers | Mandatory hard gates | Manual checkpoints | Observability | Maximum re-evaluation interval |
|---|---|---|---|---|---|
| Low | Layers 5, 7, 8 | scaffold lint and policy conformance only | none by default | inventory plus basic audit log | 12 months |
| Medium | Layers 5, 6, 7, 8 | intake validation, identity check, delivery gate | owner approval | inventory, decision log, change log, dependency map | 6 months |
| High | Layers 1, 5, 6, 7, 8 | intake gate, identity gate, delivery gate, pre-production readiness gate | architecture, security, and risk checkpoint | full decision logs, access logs, policy-denial logs, anomaly alerts | 90 days |
| Critical | Layers 1, 2, 3, 5, 6, 7, 8 | hard intake gate, hard identity gate, hard delivery gate, production enablement gate | accountable executive plus independent risk sign-off | real-time telemetry, immutable audit trail, rollback and kill-switch validation, continuous anomaly monitoring | 30 days |

| Entity modifier | Extra controls added to baseline |
|---|---|
| Policy or content artefact | add review for regulated publication and version integrity when downstream enforcement depends on content |
| Data product | add schema drift, access-pattern, and downstream-consumer monitoring |
| Frontend application | add user-session telemetry and channel-specific abuse monitoring |
| Integration component | add connector allow-list, source-target lineage, and rate anomaly monitoring |
| Software service | add dependency health, privileged-operation logging, and release provenance |
| SaaS product | add vendor-admin review, tenant-boundary review, and compensating-control check |
| Decision workflow | add mandatory human override route, outcome attribution, and decision-sampling review |
| AI agent | add autonomy-specific tool-call logs, prompt or policy version binding, and checkpoint-failure escalation |

### Risks, Gaps, and Uncertainties

- [fact; source: https://www.federalregister.gov/documents/2025/09/24/2025-18468/computer-software-assurance-for-production-and-quality-system-software-guidance-for-industry-and-food] The official Federal Register path for current FDA Computer Software Assurance guidance was anti-bot gated in this runtime, so pharmaceutical-manufacturing evidence was not used to support the final floor model.
- [fact; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf] APRA gives methodology direction rather than numeric thresholds, so the exact subject-count and outage-tolerance bands in the proposed model are a synthesis layer rather than regulator-prescribed numbers.
- [fact; source: https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.49A.pdf; https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115C.pdf] FAA material in this runtime was more usable for the governance pattern of assigned consequence classes than for a detailed extraction of all software-level definitions, so aviation is used here as an assignment analogue rather than as a one-to-one numeric template.

### Open Questions

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Should the PAP expose floors as human-readable policy rules or only as computed outputs from a topology-derivation function?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Should Agent-4 entities be split again by whether they can modify their own tool graph or only their task graph?
- [inference; source: https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019.pdf; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] What empirical subject-count and outage-tolerance thresholds best fit the target banking context without creating unnecessary High classifications for low-consequence internal data sets?

---

## Output

- Type: knowledge
- Description: Canonical UELGF entity taxonomy, AI agent autonomy ladder, CIA threshold model, automatic-floor assignment rules, scaffold-time invariants, and compositional governance-profile matrix.
- Links:
  - https://handbook.apra.gov.au/standard/cps-234
  - https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  - https://www.pcisecuritystandards.org/standards/pci-dss/
