---
review_count: 2
title: "Reference architecture definition, framework landscape, and required detail level"
added: 2026-05-16T04:50:59+00:00
status: completed
priority: medium
blocks: []
tags: [reference-architecture, enterprise-architecture, capability-model, togaf, cloud-architecture]
started: 2026-05-16T09:55:38+00:00
completed: 2026-05-16T10:13:08+00:00
output: [knowledge]
cites:
  - 2026-03-21-technology-capability-models
related:
  - 2026-05-08-ai-capability-reference-architecture-second-cycle-update
  - 2026-05-06-ai-capability-reference-architecture-security-supply-chain-update
  - 2026-04-28-uelgf-tooling-reference-architecture
  - 2026-04-22-enterprise-ai-capability-model
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Reference architecture definition, framework landscape, and required detail level

## Research Question

What should a practical reference architecture include, which established architecture frameworks define or structure it, and how much detail should be specified across capabilities, components, flow diagrams, and technology choices so that stakeholders can use it consistently?

## Scope

**In scope:**
- Definitions of reference architecture from recognized standards bodies and enterprise architecture guidance
- Frameworks that explicitly describe reference architecture structure, including The Open Group Architecture Framework (TOGAF), International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC) / Institute of Electrical and Electronics Engineers (IEEE) 42010, and major cloud provider architecture frameworks
- Practical detail levels for capability views, component views, flow views, and technology-binding decisions
- Common interpretation of the statement "we need a reference architecture" in enterprise planning and governance contexts

**Out of scope:**
- Product-by-product implementation runbooks for a specific organization
- Deep evaluation of one vendor stack over another
- Domain-specific reference architectures for a single niche industry unless needed as examples

**Constraints:**
- Prioritize publicly accessible standards, framework documentation, and authoritative architecture guidance
- Distinguish normative definitions from consultancy opinion where possible
- Produce guidance that is usable across multiple organizations, not a single local environment

## Context

- [fact; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm] Standards and enterprise architecture guidance separate architecture from architecture description and use stakeholder concerns, views, and viewpoints to decide what must be documented.
- [fact; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework] Current cloud reference architecture guidance packages diagrams, workflows, components, and review considerations, but it also expects local tailoring rather than blind reuse.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html] Prior completed repository work found that framework combinations often separate capability classification from maturity or implementation assessment rather than solving both with a single artifact.
- [inference; source: https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework] The ambiguity in stakeholder requests usually comes from collapsing several different needs, common vocabulary, reusable solution pattern, and production baseline, into the single phrase "reference architecture."

## Approach

1. Compare formal definitions and structure rules from ISO/IEC/IEEE 42010 and TOGAF.
2. Examine how Azure, Amazon Web Services (AWS), and Google Cloud present reference architectures in practice.
3. Derive the minimum content set that makes a reference architecture reusable and reviewable.
4. Derive the boundary between a reference architecture, a solution pattern, and an implementation or deployment architecture.
5. Synthesize an interpretation guide for stakeholder requests that use the phrase "reference architecture."

## Sources

- [x] [The Open Group TOGAF](https://www.opengroup.org/togaf) - enterprise architecture framework overview and positioning
- [x] [The Open Group Developing Architecture Views](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm) - official Open Group explanation of views, viewpoints, concerns, and progressive detail
- [x] [The Open Group Consider different architecture reference models, viewpoints, and tools](https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm) - official Open Group step guidance on selecting reference models and concrete views
- [x] [ISO/IEC/IEEE 42010 Systems and software engineering - Architecture description](https://www.iso.org/standard/74393.html) - formal architecture description structure and viewpoint requirements
- [x] [Microsoft Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) - catalog of reference architectures, guides, and decision support
- [x] [Microsoft Azure Reference Architectures](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/) - Azure reference architecture entry point
- [x] [Microsoft Azure Basic web app reference architecture](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app) - concrete example with architecture, workflow, components, and considerations
- [x] [Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/architecture/framework/) - workload design principles and technical design areas
- [x] [AWS Architecture Center](https://aws.amazon.com/architecture/) - AWS architecture guidance entry point
- [x] [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) - architecture evaluation and design best practices
- [x] [AWS Key components of an AWS web hosting architecture](https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html) - concrete component and flow guidance
- [x] [AWS Security Reference Architecture introduction](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html) - official AWS reference architecture guidance and tailoring boundary
- [x] [AWS Modern Data Analytics Reference Architecture on AWS](https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html) - concrete multi-component reference architecture with numbered flows
- [x] [Google Cloud Architecture Center](https://cloud.google.com/architecture) - enterprise architecture guidance entry point
- [x] [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework) - pillars, perspectives, documentation, and design-for-change guidance
- [x] [Google Cloud Well-Architected Framework Operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence) - operational design principles and continuous improvement guidance
- [x] [Google Cloud Implement zero trust](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust) - example of control concerns expressed as layered recommendations
- [x] [Google Cloud Promote modular design](https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design) - modular component and clear-interface guidance
- [x] [Mitchell (2026) Technology Capability Models: Survey, Comparison, and Recommendation for Multi-Level IT Capability Mapping](https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html) - prior completed item on framework combinations and capability abstraction

---

## Research Skill Output

### §0 Initialise

- Question: what content, structure, and detail level make a reference architecture practically reusable and reviewable across organizations?
- Scope: definitions, framework structure, component and flow detail, and technology-binding boundaries; no vendor-by-vendor product selection or implementation runbooks.
- Constraints: public standards and official framework documents only where possible; separate normative structure rules from practical cloud examples.
- Output: knowledge, specifically a decision-oriented definition, framework comparison, detail ladder, and interpretation guide.
- Prior completed items reviewed before investigation: https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html ; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html ; https://davidamitchell.github.io/Research/research/2026-05-06-ai-capability-reference-architecture-security-supply-chain-update.html ; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html

### §1 Question Decomposition

- **Root question:** what should a practical reference architecture contain, and how much detail is enough to make it useful without collapsing it into implementation design?
- **A. Definition and formal structure**
  - A1. What do architecture-description standards require an architecture artifact to contain?
  - A2. How does TOGAF translate stakeholder concerns into views, viewpoints, and reusable reference material?
- **B. Practical reference-architecture content**
  - B1. What component, workflow, and consideration sections appear repeatedly in official vendor reference architectures?
  - B2. Which non-functional concerns must be explicit for the artifact to be reviewable?
- **C. Detail boundary**
  - C1. What belongs in a minimum viable reference architecture?
  - C2. What belongs in an implementation or deployment architecture instead?
  - C3. When should technology choices be fixed, bounded, or left open?
- **D. Interpretation**
  - D1. What do stakeholders usually mean when they ask for a reference architecture?
  - D2. What clarifying questions separate a conceptual pattern from a production baseline?

### §2 Investigation

#### 2.1 Definition and formal structure

- [fact; source: https://www.iso.org/standard/74393.html] ISO/IEC/IEEE 42010 specifies requirements for the structure and expression of an architecture description, distinguishes the architecture of an entity from the architecture description that expresses it, and requires architecture description frameworks, viewpoints, and model kinds that support the description.
- [fact; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm] The Open Group says architecture views are representations of the overall architecture that are meaningful to one or more stakeholders, and that a single comprehensive model is often too complex to communicate all relationships between business and technical components.
- [fact; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm] The Open Group defines a viewpoint as the perspective from which a view is taken, including how to construct and use the view, what information should appear in it, which modeling techniques are used, and the rationale for those choices.
- [fact; source: https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm] TOGAF's technology-architecture guidance says architects should select relevant reference models, viewpoints, and tools based on stakeholder concerns, and it gives example views such as networked computing or hardware, communications, processing, cost, and standards.
- [fact; source: https://www.opengroup.org/togaf] The current TOGAF overview positions the standard as an enterprise architecture framework that combines universal concepts with configurable detail and best-practice guidance rather than prescribing one fixed representation for every architecture artifact.
- [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm] A reference architecture is best understood as a reusable architecture description pattern built from stakeholder-oriented views and reusable reference material, not as a single picture or a product configuration sheet.

#### 2.2 What official cloud reference architectures contain in practice

- [fact; source: https://learn.microsoft.com/en-us/azure/architecture/; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/] Microsoft presents the Azure Architecture Center as a catalog of solution ideas, example workloads, reference architectures, technology decision guides, and architecture guides, which shows that reference architectures sit alongside, not instead of, decision and implementation guidance.
- [fact; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app] The Azure basic web app reference architecture includes an architecture diagram, a numbered workflow, a named component list, and a considerations section broken down by reliability, security, cost optimization, and operational excellence.
- [fact; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app] Microsoft explicitly says the basic web app architecture is designed for evaluation and learning, not for production deployments, and then lists which reliability and security capabilities are omitted and where the more production-ready baseline differs.
- [fact; source: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html] AWS says the Well-Architected Framework helps architects understand the pros and cons of decisions made while building systems, provides a consistent approach to measuring architectures against best practices, and links those decisions to improvement work.
- [fact; source: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html] AWS's web hosting guidance breaks the architecture into concrete sections for network management, content delivery, public Domain Name System (DNS), host security, load balancing, service discovery, and caching, which is a component-and-flow decomposition rather than a single abstract capability list.
- [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html] AWS says its Security Reference Architecture is a comprehensive set of guidance organized around a single-page architecture, but it also says customers must modify and tailor the recommendations to suit their own environment and security needs.
- [fact; source: https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html] AWS publishes reference architecture diagrams with numbered end-to-end flows, named services, centralized governance elements such as metadata repositories and audit trails, and downloadable editable diagram files.
- [fact; source: https://cloud.google.com/architecture/framework] Google says the Well-Architected Framework organizes recommendations into pillars and cross-pillar perspectives, instructs teams to document architecture clearly, preserve change history, design for change, decouple architecture, and use a stateless architecture where appropriate.
- [fact; source: https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust] Google treats zero trust as a holistic integration of multiple security layers and best practices rather than as a single product, and expresses the pattern through explicit access-control, network, segmentation, automation, logging, and monitoring recommendations.
- [fact; source: https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design] Google says modular design needs clearly defined interfaces, explicit dependencies, and component-level resource decisions so that parts of a system can be scaled and changed independently.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html; https://cloud.google.com/architecture/framework; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design] In practical cloud guidance, a reference architecture is expected to include at least a canonical diagram, named components, major flows, explicit quality or control considerations, and enough rationale to let teams adapt the pattern safely.

#### 2.3 Minimum viable detail level versus implementation detail

- [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app] The minimum viable reference architecture is a reusable logical architecture that states purpose, stakeholders or concerns, principal components or capability blocks, major interactions or flows, and the key constraints or review criteria that govern acceptable implementations.
- [inference; source: https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html] Component detail in a reference architecture should usually stop at logical building blocks or approved service classes plus their responsibilities and interfaces, because those are stable enough to reuse across implementations.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design] Flow detail should capture request flow, data flow, trust or network boundaries, and observability or control flow where those affect architecture quality, because interface behavior and dependency shape are central to scalability, security, and operability.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework] Exact product or service bindings should remain optional or bounded unless the goal is to publish a platform standard, because official frameworks consistently pair reusable guidance with explicit tailoring to local requirements.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://learn.microsoft.com/en-us/azure/architecture/framework/; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html] Implementation architecture begins where the artifact commits to deployment topology, environment-specific network design, service tiers, resilience targets, operational procedures, and production control settings rather than only naming the reusable pattern.

#### 2.4 What stakeholders usually mean by "we need a reference architecture"

- [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework] In enterprise practice the request usually points to one of three needs: a common vocabulary and decomposition of the problem space, a reusable solution pattern with standard components and flows, or a pre-approved baseline for later implementation design.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework] The fastest way to remove ambiguity is to ask whether the output must guide many implementations, approve one implementation family, or directly support production deployment and review.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html] Prior completed repository work also supports the distinction between stable capability abstraction and later maturity or implementation decisions, which is the same boundary at a broader capability-model scale.

### §3 Reasoning

- [fact; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm] The standards-level facts are that architecture descriptions use views and viewpoints tied to stakeholder concerns, and that multiple representations are expected because one comprehensive model is too complex for most purposes.
- [fact; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html; https://cloud.google.com/architecture/framework] The vendor-level facts are that official reference architectures include diagrams, components, flows, and review considerations, but they also preserve tailoring room and change-oriented guidance.
- [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app] The strongest synthesis is that a usable reference architecture must be specific enough to support consistent review and reuse, but abstract enough to survive more than one implementation.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework] The practical detail boundary is therefore not "high level versus low level" in the abstract, but "reusable logical pattern versus environment-specific commitment."
- [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm] The older public Open Group pages on views and viewpoints remain representative of the current TOGAF treatment of stakeholder-oriented views. Justification: the current TOGAF overview still positions the standard around configurable detail and enduring guidance, and the older pages expose the core concepts directly.

### §4 Consistency Check

- [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm] There is no contradiction between ISO/IEC/IEEE 42010 and TOGAF on structure: ISO/IEC/IEEE 42010 defines how architecture descriptions should be expressed, while TOGAF adds reusable enterprise architecture guidance on views, viewpoints, and reference models.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework] There is no contradiction between standards-level abstraction and vendor examples: the cloud examples simply instantiate the same idea at a more operational level and repeatedly preserve tailoring boundaries.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html; https://cloud.google.com/architecture/framework] The only material tension is between reuse and standardization speed, because some organizations want a reference architecture to pre-select technology. That tension is resolved by separating reusable logical architecture from bounded implementation profiles.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design] Technical lens: component boundaries and interfaces matter as much as named capabilities, because reference architectures are most useful when they clarify where coupling is allowed and where independence is expected.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust] Governance lens: a reference architecture becomes governance-grade only when it includes control viewpoints such as identity, access, logging, standards, and review criteria, not just functional components.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html] Economic lens: overspecifying products shortens reuse life, while underspecifying controls shifts design cost and review ambiguity downstream into every project.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework] Behavioral lens: teams often disagree about "reference architecture" because one group expects a teaching artifact and another expects a pre-approved production baseline, so the document should state its intended decision boundary explicitly.

### §6 Synthesis

**Executive summary:**

A practical reference architecture should define a reusable architecture description, the work product ISO/IEC/IEEE 42010 uses to express architecture, and organize that description through stakeholder-oriented views and viewpoints as TOGAF describes them, rather than collapsing directly into an implementation blueprint. [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm]
ISO/IEC/IEEE 42010 and TOGAF together supply the structural side of that answer, architecture description, views, viewpoints, and reference material, while Azure, AWS, and Google Cloud show how those ideas appear in working reference-architecture artifacts such as diagrams, workflows, named components, and review considerations. [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework]
The most reliable detail ladder is three-tiered: capability or conceptual reference architecture, logical or pattern reference architecture, and implementation or deployment architecture, with each level adding commitments that the level above intentionally leaves open. [inference; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html]
As a working heuristic, stakeholder requests for a reference architecture often map to one of three needs, common vocabulary, reusable solution pattern, or bounded implementation standard, so clarifying which need is in scope is the key scoping move. [inference; source: https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework]

**Key findings:**

1. **A practical reference architecture should be treated as a reusable architecture description, the work product used to express architecture, that is organized through stakeholder-oriented views and viewpoints instead of being reduced to a single diagram or a list of products.** ([inference]; high confidence; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm)
2. **ISO/IEC/IEEE 42010 provides the structural grammar for architecture descriptions, while TOGAF adds more operational guidance on selecting viewpoints, reference models, and concrete views, so together they cover both expression and reuse of the architecture artifact in practice.** ([inference]; medium confidence; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://www.opengroup.org/togaf)
3. **Official cloud reference architectures commonly include a canonical diagram, a flow or workflow description, named components, and explicit quality or control considerations in the same artifact family.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html)
4. **The minimum viable detail level for a reference architecture is logical rather than deployment-specific: it should name stable building blocks, their responsibilities, the major interaction paths, and the constraints used to evaluate later implementations.** ([inference]; high confidence; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app)
5. **Flow diagrams belong in a reference architecture when they show how requests, data, control actions, and trust boundaries move across components, because those flows determine whether the pattern is secure, operable, and scalable enough to reuse.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design)
6. **Exact technology choices should usually remain optional or be expressed as bounded options in a reference architecture, because the official frameworks repeatedly pair reusable guidance with an explicit instruction to tailor the pattern to local environment, risk, and operating needs.** ([inference]; high confidence; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework)
7. **Implementation architecture starts when the artifact commits to environment-specific topology, selected services or products, service tiers, operational procedures, resilience settings, and production control mechanisms instead of staying at the reusable-pattern level.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://learn.microsoft.com/en-us/azure/architecture/framework/; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
8. **A useful detail ladder has three levels, conceptual or capability reference architecture, logical or pattern reference architecture, and implementation or deployment architecture, because official guidance separates reusable structure from environment-specific commitments and production controls.** ([inference]; medium confidence; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
9. **A useful working heuristic is that the phrase "we need a reference architecture" can hide three different requests, common vocabulary, reusable pattern, or implementation baseline, so architects should clarify which deliverable is actually wanted before locking the artifact shape.** ([inference]; low confidence; source: https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] A practical reference architecture is a reusable architecture description, the work product used to express architecture, organized through stakeholder-oriented views and viewpoints rather than a single diagram or product list. | https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm | high | Standards structure |
| [inference] ISO/IEC/IEEE 42010 and TOGAF cover structural expression and operational reuse together. | https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://www.opengroup.org/togaf | medium | Comparative synthesis |
| [inference] Official cloud reference architectures commonly package diagrams, flows, components, and considerations together. | https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html | medium | Practical artifact shape |
| [inference] Minimum viable detail is logical, reusable, and evaluation-oriented rather than deployment-specific. | https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app | high | Reuse boundary |
| [inference] Flow diagrams belong when they show request, data, control, and trust movement across components. | https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design | medium | Flow as architecture logic |
| [inference] Technology choices should usually remain optional or bounded in a reference architecture. | https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework | high | Tailoring preserved |
| [inference] Implementation architecture begins with environment-specific commitments for topology, services, and production controls. | https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://learn.microsoft.com/en-us/azure/architecture/framework/; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html | medium | Deployment boundary |
| [inference] A usable detail ladder separates conceptual, logical, and implementation architecture levels. | https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html | medium | Detail ladder |
| [inference] The phrase "we need a reference architecture" can be used as a heuristic for multiple hidden deliverable requests. | https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework | low | Request-pattern heuristic |

**Assumptions:**

- [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm] The older public Open Group pages on views and viewpoints remain representative of the current TOGAF treatment of stakeholder-oriented views. Justification: the current TOGAF overview still frames the standard around configurable detail and reusable guidance, and the older pages expose the core concepts directly.

**Analysis:**

Combining standards-level structure with official working examples gives the strongest evidence base, because ISO/IEC/IEEE 42010 explains how an architecture description should be organized but not what a reusable enterprise reference artifact looks like on its own. [inference; source: https://www.iso.org/standard/74393.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html]
TOGAF fills that gap by linking stakeholder concerns to views, viewpoints, reference models, and concrete view types, which turns the architecture description idea into a reusable enterprise-architecture practice. [inference; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm]
Azure provides the clearest official evidence for the detail boundary because one page separates architecture, workflow, components, and considerations, then explicitly distinguishes a learning-oriented baseline from a production-grade baseline. [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app]
AWS and Google qualify against over-specification by repeatedly framing reference architectures as guidance to adapt, review, and tailor rather than as immutable blueprints. [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html; https://cloud.google.com/architecture/framework]
A rival interpretation is that a reference architecture should already lock exact technologies so delivery teams can move faster. That reading is valid only when the real need is a platform standard or approved implementation profile; treating every reference architecture that way destroys the reuse boundary that the standards and vendor guidance preserve. [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://www.opengroup.org/togaf]

**Risks, gaps, uncertainties:**

- [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm] The most detailed directly accessible TOGAF evidence in this session came from older public Open Group pages plus the current TOGAF overview rather than from the latest full standard text.
- [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework] The cloud vendor examples are strong for practical structure and detail boundaries, but they are still vendor-authored examples and therefore stronger on reusable document shape than on a universal enterprise taxonomy.
- [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/togaf] The conclusion about what stakeholders usually mean by "reference architecture" is a synthesis of framework structure and common artifact patterns rather than a direct survey result.

**Open questions:**

- Should this repository formalize a house template that separates conceptual reference architecture, logical pattern architecture, and implementation architecture into explicit sections or file types?
- Which governance domains, identity, data, network, observability, and policy, should always be mandatory viewpoints in enterprise reference architectures, regardless of workload?
- Would a lightweight intake checklist reduce ambiguity by forcing requesters to choose between vocabulary map, reusable pattern, and implementation baseline before architecture work starts?

### §7 Recursive Review

- Review status: pass candidate
- Acronym audit status: complete
- Claim audit status: complete
- Source audit status: complete
- Consistency status: synchronized

---

## Findings

### Executive Summary

A practical reference architecture should define a reusable architecture description, the work product ISO/IEC/IEEE 42010 uses to express architecture, and organize that description through stakeholder-oriented views and viewpoints as TOGAF describes them, rather than collapsing directly into an implementation blueprint. [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm]
ISO/IEC/IEEE 42010 and TOGAF together supply the structural side of that answer, architecture description, views, viewpoints, and reference material, while Azure, AWS, and Google Cloud show how those ideas appear in working reference-architecture artifacts such as diagrams, workflows, named components, and review considerations. [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework]
The most reliable detail ladder is three-tiered: capability or conceptual reference architecture, logical or pattern reference architecture, and implementation or deployment architecture, with each level adding commitments that the level above intentionally leaves open. [inference; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html]
As a working heuristic, stakeholder requests for a reference architecture often map to one of three needs, common vocabulary, reusable solution pattern, or bounded implementation standard, so clarifying which need is in scope is the key scoping move. [inference; source: https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework]

### Key Findings

1. **A practical reference architecture should be treated as a reusable architecture description, the work product used to express architecture, that is organized through stakeholder-oriented views and viewpoints instead of being reduced to a single diagram or a list of products.** ([inference]; high confidence; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm)
2. **ISO/IEC/IEEE 42010 provides the structural grammar for architecture descriptions, while TOGAF adds more operational guidance on selecting viewpoints, reference models, and concrete views, so together they cover both expression and reuse of the architecture artifact in practice.** ([inference]; medium confidence; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://www.opengroup.org/togaf)
3. **Official cloud reference architectures commonly include a canonical diagram, a flow or workflow description, named components, and explicit quality or control considerations in the same artifact family.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html)
4. **The minimum viable detail level for a reference architecture is logical rather than deployment-specific: it should name stable building blocks, their responsibilities, the major interaction paths, and the constraints used to evaluate later implementations.** ([inference]; high confidence; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app)
5. **Flow diagrams belong in a reference architecture when they show how requests, data, control actions, and trust boundaries move across components, because those flows determine whether the pattern is secure, operable, and scalable enough to reuse.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design)
6. **Exact technology choices should usually remain optional or be expressed as bounded options in a reference architecture, because the official frameworks repeatedly pair reusable guidance with an explicit instruction to tailor the pattern to local environment, risk, and operating needs.** ([inference]; high confidence; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework)
7. **Implementation architecture starts when the artifact commits to environment-specific topology, selected services or products, service tiers, operational procedures, resilience settings, and production control mechanisms instead of staying at the reusable-pattern level.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://learn.microsoft.com/en-us/azure/architecture/framework/; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
8. **A useful detail ladder has three levels, conceptual or capability reference architecture, logical or pattern reference architecture, and implementation or deployment architecture, because official guidance separates reusable structure from environment-specific commitments and production controls.** ([inference]; medium confidence; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
9. **A useful working heuristic is that the phrase "we need a reference architecture" can hide three different requests, common vocabulary, reusable pattern, or implementation baseline, so architects should clarify which deliverable is actually wanted before locking the artifact shape.** ([inference]; low confidence; source: https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] A practical reference architecture is a reusable architecture description, the work product used to express architecture, organized through stakeholder-oriented views and viewpoints rather than a single diagram or product list. | https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm | high | Standards structure |
| [inference] ISO/IEC/IEEE 42010 and TOGAF cover structural expression and operational reuse together. | https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm; https://www.opengroup.org/togaf | medium | Comparative synthesis |
| [inference] Official cloud reference architectures commonly package diagrams, flows, components, and considerations together. | https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html | medium | Practical artifact shape |
| [inference] Minimum viable detail is logical, reusable, and evaluation-oriented rather than deployment-specific. | https://www.iso.org/standard/74393.html; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app | high | Reuse boundary |
| [inference] Flow diagrams belong when they show request, data, control, and trust movement across components. | https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-components-of-an-aws-web-hosting-architecture.html; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design | medium | Flow as architecture logic |
| [inference] Technology choices should usually remain optional or bounded in a reference architecture. | https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://cloud.google.com/architecture/framework | high | Tailoring preserved |
| [inference] Implementation architecture begins with environment-specific commitments for topology, services, and production controls. | https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://learn.microsoft.com/en-us/azure/architecture/framework/; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html | medium | Deployment boundary |
| [inference] A usable detail ladder separates conceptual, logical, and implementation architecture levels. | https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html | medium | Detail ladder |
| [inference] The phrase "we need a reference architecture" can be used as a heuristic for multiple hidden deliverable requests. | https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework | low | Request-pattern heuristic |

### Assumptions

- **Assumption:** The older public Open Group pages on views and viewpoints remain representative of the current TOGAF treatment of stakeholder-oriented views. **Justification:** The current TOGAF overview still frames the standard around configurable detail and reusable guidance, and the older pages expose the core concepts directly. [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm]

### Analysis

ISO/IEC/IEEE 42010 answers the structural question but intentionally does not prescribe one architecture artifact shape, which is why a standards-only answer would still leave teams uncertain about deliverable form. [inference; source: https://www.iso.org/standard/74393.html]
TOGAF answers more of the practical enterprise-architecture question by tying stakeholder concerns to views, viewpoints, reference models, and view selection, which is the missing bridge between formal architecture description and usable architecture work products. [inference; source: https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm; https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p2/ta/ta_views.htm]
Azure provides the clearest evidence for the detail ladder because one official example separates architecture, workflow, components, and considerations, then explicitly explains why the basic version is not production-ready and what the next level adds. [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app]
AWS and Google qualify the opposite failure mode, overcommitting too early, by repeatedly framing reference architectures as guidance to review and tailor, supported by principles such as design for change, modularity, and environment-specific adaptation. [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html; https://cloud.google.com/architecture/framework; https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design]
A plausible rival remedy is to force every reference architecture to name one preferred technology stack so projects move faster. That can be useful for a platform-standard profile, but it is a different artifact type because it trades reuse breadth for governance speed and vendor commitment. [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://www.opengroup.org/togaf]

### Risks, Gaps, and Uncertainties

- The most detailed directly accessible TOGAF evidence in this session came from older public Open Group pages plus the current TOGAF overview rather than the latest full standard text. [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm]
- The cloud-vendor examples are strong for practical document shape and detail boundaries, but they are still vendor-authored examples and therefore stronger on artifact form than on a universal enterprise taxonomy. [inference; source: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html; https://cloud.google.com/architecture/framework]
- The conclusion about what stakeholders usually mean by "reference architecture" is a synthesis of framework structure and observed artifact patterns rather than a direct survey result. [inference; source: https://www.iso.org/standard/74393.html; https://www.opengroup.org/togaf; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/; https://aws.amazon.com/architecture/; https://cloud.google.com/architecture/framework]

### Open Questions

- Should this repository formalize a house template that separates conceptual reference architecture, logical pattern architecture, and implementation architecture into explicit sections or file types?
- Which governance domains, identity, data, network, observability, and policy, should always be mandatory viewpoints in enterprise reference architectures, regardless of workload?
- Would a lightweight intake checklist reduce ambiguity by forcing requesters to choose between vocabulary map, reusable pattern, and implementation baseline before architecture work starts?

---

## Output

- Type: knowledge
- Description: Decision guide for scoping reference architectures versus implementation architectures across standards-based and cloud-framework contexts. [inference; source: https://www.iso.org/standard/74393.html; https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app; https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html]
- Links:
  - https://www.iso.org/standard/74393.html
  - https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm
  - https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app
