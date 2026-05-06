---
title: "What measurement systems and frameworks exist for quantifying Information Technology system legibility, the ability to reason about, understand, and comprehensively characterise a runtime ecosystem of interconnected applications, services, and systems, who is actively defining and applying them, and how?"
added: 2026-05-06T07:32:54+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [observability, enterprise-architecture, dependency-mapping, it-architecture, measurement, governance]
started: 2026-05-06T09:16:34+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-21-dependency-mapping-dotnet-terraform-dynatrace, 2026-03-21-technology-capability-models]
related: [2026-04-27-enterprise-stack-value-distribution-governance-frameworks, 2026-03-15-tracking-work-across-systems]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What measurement systems and frameworks exist for quantifying Information Technology system legibility, the ability to reason about, understand, and comprehensively characterise a runtime ecosystem of interconnected applications, services, and systems, who is actively defining and applying them, and how?

## Research Question

What measurement systems and frameworks exist for quantifying Information Technology (IT) system legibility, defined here as the ability to reason about, understand, and comprehensively characterise the entirety of interconnected applications, services, and systems that constitute an organisation's runtime ecosystem, who in academic research, standards bodies, and industry practice is actively defining and applying these frameworks, and what does practical implementation look like?

## Scope

**In scope:**
- Definitions and theoretical models of IT system legibility, system comprehensibility, and whole-estate understandability
- Formal measurement frameworks and metrics for quantifying how well-understood a runtime IT ecosystem is, for example architectural fitness functions, architectural health metrics, Configuration Management Database (CMDB) coverage rates, and service dependency completeness
- Adjacent concepts, including architectural observability, cognitive complexity of IT estates, system transparency, run-book coverage, and infrastructure discoverability
- Academic research, practitioner frameworks, standards, for example The Open Group Architecture Framework (TOGAF), Banking Industry Architecture Network (BIAN), and TM Forum, plus vendor tooling in this space
- Who is actively working in this area, including research groups, standards bodies, enterprise architecture practices, and observability vendors
- Practical implementation examples, including tooling, assessment approaches, maturity models, and case studies

**Out of scope:**
- Individual-service observability and monitoring, for example application performance metrics for a single service, unless used as a component of a whole-ecosystem legibility framework
- Network topology mapping as a standalone discipline, in scope only when used as input to a legibility framework
- Purely theoretical computer science complexity measures, for example Kolmogorov complexity or cyclomatic complexity, unless they are applied directly to IT estate characterisation

**Constraints:**
- Primary sources preferred; secondary synthesis acceptable where primary is unavailable
- Recency matters; sources older than five years are flagged where the field has moved
- The question is practitioner-oriented, so applied frameworks and implementations are weighted more heavily than abstract theory

## Context

Large organisations distribute estate knowledge across software catalogs, architecture repositories, configuration records, and runtime topology views rather than through one settled cross-industry "legibility" score. [fact; source: https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492]

Prior completed repository work already found that dependency mapping and capability modelling are layered, partial, and governance-sensitive activities rather than single-tool problems. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html]

This item therefore tests whether "system legibility" already exists as a formal measurement discipline, or whether practice is better described as a composite of adjacent measurement systems for coverage, correctness, discoverability, dependency visibility, and shared human understanding. [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt]

## Approach

1. **Definition:** Identify how standards bodies, practitioner literature, and adjacent research define estate understandability, relationship visibility, and shared system comprehension.
2. **Frameworks and metrics:** Separate explicit scorecards from looser guidance, and catalogue the measurable proxies actually used in practice.
3. **Who is working in this space:** Identify the standards forums, vendors, and research programs currently shaping the area.
4. **Tooling and practical implementation:** Compare how catalogs, enterprise architecture repositories, CMDBs, runtime topology tools, and software-intelligence tools operationalise legibility.
5. **Practical application examples:** Extract published implementation patterns and outcome claims, then judge how strong that evidence is.

## Sources

- [x] [Ford et al. (2017) Building Evolutionary Architectures](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) - seed source; public page exposed metadata only
- [x] [Thoughtworks Building Evolutionary Architectures](https://www.thoughtworks.com/insights/books/building-evolutionary-architectures) - accessible public companion page for the architectural-fitness-function lineage
- [x] [Thoughtworks Architectural Fitness Function](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) - public definition of architectural fitness functions as objective integrity assessments
- [x] [The Open Group TOGAF Standard](https://www.opengroup.org/togaf) - enterprise architecture method and framework
- [x] [The Open Group ArchiMate Overview](https://www.opengroup.org/archimate-forum/archimate-overview) - modelling language for describing, analysing, and visualising relationships across business and technology domains
- [x] [BIAN Service Landscape](https://bian.org/service-landscape/) - sector-specific capability and service-domain reference model
- [x] [TM Forum Open Digital Architecture](https://www.tmforum.org/open-digital-architecture/) - checked; official page returned 403 in this environment and is not used as core evidence
- [x] [ServiceNow CMDB Health Dashboard, Completeness, Compliance & Correctness](https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492) - explicit operational scorecard for configuration-data quality
- [x] [ServiceNow Strengthening Common Service Data Model (CSDM) Data Foundations](https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446) - governance and implementation guidance for Common Service Data Model (CSDM) foundations
- [x] [ServiceNow Aligning Architecture Blueprint with TOGAF Standard](https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009) - blueprinting approach for current-state and planned-state platform legibility
- [x] [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/) - ownership and discoverability model for large software estates
- [x] [Spotify Engineering (2024) Supercharged Developer Portals](https://engineering.atspotify.com/2024/04/supercharged-developer-portals) - practitioner account of Backstage as a legibility and productivity layer
- [x] [SAP LeanIX Application Portfolio Management](https://www.leanix.net/en/products/application-portfolio-management) - inventory, dependency, ownership, and rationalisation metrics for estate visibility
- [x] [LeanIX Application Portfolio Management Guide](https://www.leanix.net/en/wiki/ea/application-portfolio-management) - practitioner guidance on inventory transparency and application visibility
- [x] [Dynatrace Smartscape](https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape) - real-time topology and relationship model
- [x] [Dynatrace Service Dependency Graph](https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph) - live upstream and downstream dependency mapping
- [x] [Dynatrace Smartscape Platform Overview](https://www.dynatrace.com/platform/application-topology-discovery/smartscape/) - always-accurate topology and blast-radius positioning
- [x] [CAST Imaging](https://www.castsoftware.com/imaging) - architecture recovery, impact analysis, design-drift tracking, and structural visibility
- [x] [Thoughtworks Codebase Cognitive Debt](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt) - human-understanding dimension of legibility
- [x] [DevOps Research and Assessment (DORA)](https://dora.dev/) - research program on capabilities that drive software delivery and operations performance
- [x] [Mitchell (2026) Dependency Mapping Across .NET Codebases, Terraform, Dynatrace, Confluence, Log Aggregation, and the Configuration and Service Data Model](https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html) - prior completed repository item on layered dependency evidence
- [x] [Mitchell (2026) Technology Capability Models: Survey, Comparison, and Recommendation for Multi-Level IT Capability Mapping](https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html) - prior completed repository item on capability-model structure and maturity overlays
- [x] [Mitchell (2026) Enterprise Data Stack Value-Distribution Frameworks](https://davidamitchell.github.io/Research/research/2026-04-27-enterprise-stack-value-distribution-governance-frameworks.html) - prior completed repository item on governance as a cross-layer function

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: which measurement systems and frameworks currently quantify IT system legibility, who defines them, and what practical implementation looks like.
- Scope: cross-industry standards, sector reference models, practitioner scorecards, and tool-native measurement systems for whole-estate understanding.
- Constraints: public sources only; primary sources preferred; vendor claims accepted where clearly marked and weighed against standards or prior repository work.
- Prior-work check: completed-item scan identified direct dependencies on the repository's dependency-mapping and capability-model items, plus adjacent governance framing. Sources: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html; https://davidamitchell.github.io/Research/research/2026-04-27-enterprise-stack-value-distribution-governance-frameworks.html
- Output: structured knowledge item with explicit claims, mirrored synthesis and findings, URL-backed evidence map, and frontmatter cites/related fields set from the synthesis.

### §1 Question Decomposition

- **A. Definition and lineage**
  - A1. Do standards or research sources use a direct equivalent of "system legibility" for enterprise IT estates?
  - A2. Which adjacent concepts capture the same practical concern, for example completeness, discoverability, topology visibility, and shared understanding?
- **B. Formal measurement systems**
  - B1. Which sources provide explicit scorecards or measurable integrity assessments?
  - B2. Which sources define structure and coverage but not a single score?
- **C. Active definers and implementers**
  - C1. Which standards bodies are defining modelling and coverage frameworks?
  - C2. Which vendors or practitioner communities are operationalising legibility through products?
- **D. Practical implementation**
  - D1. How do catalogs, architecture repositories, CMDBs, runtime graphs, and software-intelligence platforms each measure a different slice of legibility?
  - D2. What composite implementation pattern appears across the sources?
- **E. Evidence quality**
  - E1. Which claims come from standards or documentation?
  - E2. Which outcome claims come mainly from vendors or practitioner reports?

### §2 Investigation

#### Source audit and source-access notes

- Access note: the TM Forum Open Digital Architecture seeded source returned 403 in this environment, so TM Forum is treated as relevant context but not as a core evidence base for the conclusions below.
- Access note: the O'Reilly page for *Building Evolutionary Architectures* exposed title and overview metadata only; the accessible Thoughtworks public pages were used for the operational definition of architectural fitness functions.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.html; https://davidamitchell.github.io/Research/research/2026-03-21-technology-capability-models.html] Prior completed repository work already established that whole-estate understanding is assembled from multiple partial layers, especially dependency evidence, capability maps, and governance overlays.

#### A. Definitions and adjacent concepts

- [fact; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview] TOGAF defines enterprise architecture as a method for aligning business and technology domains, and ArchiMate defines a modelling language to describe, analyse, and visualise relationships among those domains in an unambiguous way.
- [fact; source: https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://www.thoughtworks.com/insights/books/building-evolutionary-architectures] Thoughtworks defines an architectural fitness function as an objective integrity assessment of architectural characteristics, which turns selected architecture qualities into measurable, repeatable checks.
- [fact; source: https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt] Thoughtworks defines codebase cognitive debt as the growing gap between a system's implementation and a team's shared understanding of how and why it works.
- [fact; source: https://backstage.io/docs/features/software-catalog/; https://engineering.atspotify.com/2024/04/supercharged-developer-portals] Backstage frames the problem as software ownership and discoverability across large ecosystems, explicitly targeting orphan software and fragmented knowledge.
- [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://backstage.io/docs/features/software-catalog/] The field does not converge on the exact phrase "IT system legibility"; instead it uses adjacent concepts that cover model completeness, relationship visibility, discoverability, and preservation of shared understanding under change.

#### B. Explicit measurement systems and measurable proxies

- [fact; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] ServiceNow's CMDB Health Dashboard provides the clearest explicit scorecard found in this review, using completeness, compliance, and correctness as top-level dimensions.
- [fact; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] ServiceNow defines correctness through duplicate, orphan, and stale Configuration Items (CIs), which makes freshness and relationship quality measurable rather than descriptive only.
- [fact; source: https://backstage.io/docs/features/software-catalog/] Backstage measures estate legibility indirectly through software-catalog coverage, owner assignment, and metadata maintenance, with the catalog intended to make all software and ownership discoverable.
- [fact; source: https://www.leanix.net/en/products/application-portfolio-management; https://www.leanix.net/en/wiki/ea/application-portfolio-management] SAP LeanIX measures portfolio visibility through trustworthy inventory, dependency mapping, ownership, business-capability alignment, and standardised application assessment criteria such as Gartner TIME.
- [fact; source: https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/] Dynatrace measures runtime legibility through automatically updated topology, upstream and downstream service-call relationships, blast radius, and ownership context.
- [fact; source: https://www.castsoftware.com/imaging] CAST Imaging measures structural legibility through architecture recovery across five abstraction layers, impact analysis, design-drift tracking, and ISO 5055 views of reliability, security, and efficiency.
- [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging] The common measurable proxies are coverage, correctness, freshness, ownership attribution, dependency completeness, impact-analysis capability, and drift detection, not one universally accepted single score.

#### C. Who is defining and applying these frameworks

- [fact; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview] The Open Group is actively defining the architecture-method and modelling-language layer through TOGAF and ArchiMate, including the communities that maintain those standards.
- [fact; source: https://bian.org/service-landscape/] BIAN is actively evolving a sector-specific service-landscape model, with releases in 2023, 2025, and 2026 that add business capabilities, service domains, wireframes, and links to ISO20022.
- [fact; source: https://backstage.io/docs/features/software-catalog/; https://engineering.atspotify.com/2024/04/supercharged-developer-portals] Spotify and the Backstage community are actively applying catalog-based legibility through ownership, discoverability, and internal developer portal patterns at scale.
- [fact; source: https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] SAP LeanIX, Dynatrace, CAST, and ServiceNow are actively productising distinct slices of legibility through enterprise architecture repositories, runtime topology, software intelligence, and CMDB scorecards.
- [fact; source: https://dora.dev/; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt] DevOps Research and Assessment (DORA) and Thoughtworks are shaping the human and operational side of legibility by tying delivery performance, cognitive load, and architectural guardrails to the ability to understand systems as they evolve.

#### D. Practical implementation patterns

- [fact; source: https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009] ServiceNow's architecture-blueprint guidance treats current-state and planned-state diagrams, integration landscape, instance topology, infrastructure details, and governance roles as the practical baseline for platform legibility.
- [fact; source: https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446] ServiceNow's Common Service Data Model (CSDM) data-foundation guidance requires clear ownership, stewardship, documented lifecycle processes, central repositories, and governance reviews to keep legibility artifacts accurate enough for automation and reporting.
- [fact; source: https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://backstage.io/docs/features/software-catalog/] Spotify describes Backstage as having begun as a software catalog for components, ownership, and discoverability, later becoming a single pane of glass for engineering knowledge, and reports better productivity for frequent Backstage users.
- [fact; source: https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph] Dynatrace positions Smartscape as an always-accurate dependency graph for understanding cause, blast radius, ownership, and runtime-vs-intended architecture drift.
- [fact; source: https://www.leanix.net/en/products/application-portfolio-management] SAP LeanIX positions trustworthy inventory, dependency visibility, quality seals, and business-context mapping as the basis for faster architecture decisions, and reports 80 percent transparency improvement in 12 weeks in its product evidence.
- [fact; source: https://www.castsoftware.com/imaging] CAST positions architecture recovery, what-if analysis, and change-impact visibility as practical tools for modernization, onboarding, and structural-risk management.
- [inference; source: https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging] Mature legibility practice is composite: intended architecture is documented in blueprints or models, ownership is maintained in catalogs and CMDBs, live relationships are validated through runtime topology, and change impact is checked through software-intelligence or dependency-analysis tools.

#### E. Contradictions, limits, and evidence quality

- [fact; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://bian.org/service-landscape/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] Standards and practitioner sources agree that legibility depends on explicit relationships and coverage, but they operate at different layers, with standards focusing on modelling structure and products focusing on operational scorecards or discovery.
- [fact; source: https://www.leanix.net/en/products/application-portfolio-management; https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.castsoftware.com/imaging; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/] Most outcome evidence for implementation success is vendor- or practitioner-reported rather than benchmarked through neutral cross-vendor studies.
- [inference; source: https://www.opengroup.org/togaf; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape] No single source in this review establishes a universal cross-industry numeric "IT system legibility" benchmark, so the best-supported answer is a composite measurement framework rather than a settled standalone discipline.

### §3 Reasoning

- [fact; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function] Explicit measurable mechanisms do exist, but they target specific slices of the problem, for example CMDB quality and architectural-characteristic integrity.
- [fact; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://bian.org/service-landscape/] Standards frameworks provide the modelling vocabulary and coverage structure needed to describe an estate, but they do not publish a dominant universal legibility score.
- [inference; source: https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] The evidence therefore supports a layered model in which catalog, repository, CMDB, runtime, and structural-analysis measurements jointly quantify legibility.
- [assumption; source: https://www.leanix.net/en/products/application-portfolio-management; https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/] Vendor- and practitioner-reported outcome improvements are treated as directionally informative but not as neutral proof of comparative superiority, because accessible public evidence is not benchmark-normalised across tools.

### §4 Consistency Check

- [fact; source: https://www.opengroup.org/archimate-forum/archimate-overview; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] The sources are internally consistent about the core problem: legibility requires explicit entities, explicit relationships, and enough freshness to support decisions.
- [fact; source: https://www.opengroup.org/togaf; https://www.leanix.net/en/products/application-portfolio-management; https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009] There is a scope tension between standards-heavy architecture modelling and product-heavy operational dashboards, but the tension is about level of abstraction rather than about contradictory claims.
- [inference; source: https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging] The apparent contradiction resolves if standards are treated as intended-state structure and tools are treated as operational evidence sources for whether that structure is complete, current, and still understandable.

### §5 Depth and Breadth Expansion

- [fact; source: https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://backstage.io/docs/features/software-catalog/] Technical lens: runtime topology, structural analysis, and software catalogs each illuminate different blind spots, so no single technical mechanism captures the full estate.
- [fact; source: https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446; https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009; https://www.opengroup.org/togaf] Governance lens: ownership, stewardship, review forums, and standardised artifacts are part of measurement, because stale or ownerless records destroy legibility even when tools exist.
- [fact; source: https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/] Economic lens: vendors position legibility as a decision-speed, risk-reduction, and cost-optimisation capability rather than as documentation for its own sake.
- [fact; source: https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://engineering.atspotify.com/2024/04/supercharged-developer-portals] Behavioural lens: legibility includes the human capacity to keep a shared mental model of the estate, not only the presence of stored metadata or graphs.
- [inference; source: https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] The strongest composite framework combines machine-readable coverage metrics with human-comprehension guardrails, for example ownership, cognitive-load control, and architectural fitness checks.

### §6 Synthesis

**Executive summary:**

There is no single cross-industry framework that directly measures "IT system legibility" as one settled property; the field measures it through a composite of adjacent systems for architecture-model completeness, catalog discoverability, configuration-data quality, dependency visibility, drift detection, and shared team understanding. [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt]

The Open Group, BIAN, ServiceNow, Spotify's Backstage ecosystem, SAP LeanIX, Dynatrace, CAST, Thoughtworks, and DORA are the main active definers or operators visible in the accessible evidence, but they define different slices of the problem rather than one shared benchmark. [fact; source: https://www.opengroup.org/togaf; https://bian.org/service-landscape/; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://dora.dev/]

The most explicit operational scorecard found in this review is ServiceNow's CMDB Health model of completeness, compliance, and correctness, while the clearest complementary runtime and structural models come from Dynatrace Smartscape, Backstage software catalog coverage, LeanIX inventory and dependency visibility, CAST architecture recovery, and Thoughtworks architectural fitness functions. [fact; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://www.castsoftware.com/imaging; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function]

Practical implementation therefore looks like a layered control system: intended-state architecture blueprints and models, ownership-bearing catalogs and CMDBs, live runtime topology, structural impact analysis, and governance routines that reconcile drift and stale data. [inference; source: https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.castsoftware.com/imaging]

**Key findings:**

1. **No accessible primary source in this review defines a universal, cross-vendor numeric benchmark for "IT system legibility"; the best-supported conclusion is that practitioners quantify legibility through a bundle of adjacent measures rather than one standard score.** ([inference]; high confidence; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging)
2. **TOGAF, ArchiMate, and BIAN provide the strongest standards-based structure for legibility because they define how to model business, application, technology, and service relationships, but they stop short of publishing a dominant universal scoring rubric for whole-estate understanding.** ([fact]; high confidence; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://bian.org/service-landscape/)
3. **ServiceNow currently provides the clearest explicit operational legibility scorecard in the accessible evidence, because its CMDB Health model quantifies completeness, compliance, and correctness and further decomposes correctness into duplicate, orphan, and stale configuration records.** ([fact]; high confidence; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492)
4. **Backstage and Spotify's internal developer portal practice treat discoverability, ownership, and catalog coverage as measurable legibility proxies, showing that a component is not truly legible to an organisation if nobody can find it, identify its owner, or keep its metadata current.** ([inference]; high confidence; source: https://backstage.io/docs/features/software-catalog/; https://engineering.atspotify.com/2024/04/supercharged-developer-portals)
5. **SAP LeanIX operationalises estate legibility at portfolio level by combining trustworthy inventory, dependency visibility, ownership, business-context mapping, and standardised application-assessment criteria, which makes it a planning and rationalisation framework rather than a runtime truth source.** ([fact]; medium confidence; source: https://www.leanix.net/en/products/application-portfolio-management; https://www.leanix.net/en/wiki/ea/application-portfolio-management)
6. **Dynatrace Smartscape operationalises legibility at runtime by continuously mapping service and infrastructure relationships, upstream and downstream dependency chains, ownership, and blast radius, which makes it the strongest live-topology evidence source in this review.** ([fact]; high confidence; source: https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/)
7. **CAST Imaging operationalises legibility at structural-code level by recovering architecture across multiple abstraction layers, exposing change impact, and tracking design adherence and drift, which addresses blind spots that catalogs and runtime tools do not cover well.** ([fact]; medium confidence; source: https://www.castsoftware.com/imaging)
8. **Thoughtworks' architectural fitness functions and codebase cognitive debt framing show that legibility is partly a human-governance property, because an estate can be instrumented and documented yet still become hard to reason about if teams lose shared understanding or stop enforcing architectural constraints.** ([inference]; high confidence; source: https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt)
9. **The strongest practical implementation pattern is a layered composite in which architecture standards define intended structure, catalogs and CMDBs assign coverage and ownership, runtime topology validates live relationships, and software-intelligence tools test for structural drift and change impact.** ([inference]; high confidence; source: https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging)
10. **Published implementation evidence suggests that better legibility improves onboarding, decision speed, incident routing, audit readiness, and change-impact analysis, but confidence in comparative tool superiority remains limited because most accessible outcome claims are vendor- or practitioner-reported rather than cross-vendor benchmark studies.** ([inference]; medium confidence; source: https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] No universal cross-vendor numeric benchmark exists; practice uses a composite of measures. | https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging | high | Synthesis across standards and tools |
| [fact] TOGAF, ArchiMate, and BIAN define structure and coverage, not one dominant score. | https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://bian.org/service-landscape/ | high | Standards layer |
| [fact] ServiceNow CMDB Health uses completeness, compliance, and correctness, including duplicate, orphan, and stale checks. | https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492 | high | Explicit scorecard |
| [inference] Backstage uses discoverability, ownership, and catalog coverage as legibility proxies. | https://backstage.io/docs/features/software-catalog/; https://engineering.atspotify.com/2024/04/supercharged-developer-portals | high | Catalog layer |
| [fact] LeanIX uses trustworthy inventory, dependencies, ownership, and assessment criteria for portfolio visibility. | https://www.leanix.net/en/products/application-portfolio-management; https://www.leanix.net/en/wiki/ea/application-portfolio-management | medium | Vendor product evidence |
| [fact] Dynatrace uses live topology, dependency chains, blast radius, and ownership context for runtime legibility. | https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/ | high | Runtime layer |
| [fact] CAST uses recovered architecture layers, impact analysis, and drift tracking for structural legibility. | https://www.castsoftware.com/imaging | medium | Vendor product evidence |
| [inference] Human understanding and architectural guardrails are part of legibility, not an optional extra. | https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt | high | Human-governance layer |
| [inference] The strongest implementation pattern is a layered composite rather than a single tool. | https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging | high | Cross-layer synthesis |
| [inference] Outcome claims are positive but mostly vendor- or practitioner-reported, so comparative claims should stay cautious. | https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009 | medium | Evidence-quality limit |

**Assumptions:**

- [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492] "IT system legibility" is used in this item as a synthesis label for adjacent source terms such as architecture visibility, catalog discoverability, CMDB health, dependency completeness, and shared system understanding, because the exact phrase is not the dominant industry label. Justification: accessible sources describe the same operational problem using different but overlapping terms.
- [assumption; source: https://www.leanix.net/en/products/application-portfolio-management; https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/] Public vendor and practitioner outcome numbers are treated as directional signals about implementation value rather than as neutral comparative benchmarks. Justification: the accessible evidence base does not provide a common independent scoring protocol across tools.

**Analysis:**

The evidence was weighted most heavily toward sources that clearly separate structure from measurement, because that distinction answers the core question more directly than generic marketing claims do. [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492]

This weighting makes ServiceNow's CMDB Health model unusually important, because it is the only source in the review that exposes a concrete, named scorecard for estate-data quality rather than only describing architecture artifacts or discovery features. [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/]

The competing interpretation was that runtime topology tools such as Dynatrace already solve legibility alone, but that view did not hold once the evidence was compared with standards, catalogs, and structural-analysis sources, all of which address blind spots that runtime traces cannot fully close. [inference; source: https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://backstage.io/docs/features/software-catalog/; https://www.castsoftware.com/imaging; https://www.opengroup.org/togaf]

The most defensible synthesis is therefore plural rather than singular: legibility is an emergent property produced by several measurable control surfaces, and the relevant design decision is how to compose those surfaces into a governance loop. [inference; source: https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009; https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function]

**Risks, gaps, uncertainties:**

- Independent cross-vendor benchmarking of legibility frameworks is thin in the accessible public evidence, so comparative product judgments should remain conservative. [fact; source: https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://www.castsoftware.com/imaging]
- The most explicit operational metrics come from vendor or platform ecosystems, which creates a risk that the reviewed measures reflect product boundaries more than a universally agreed ontology of whole-estate understanding. [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management]
- BIAN strengthens the standards picture for financial services, but its sector specificity limits direct generalisation to non-banking estates. [fact; source: https://bian.org/service-landscape/]
- The DORA and Thoughtworks sources strengthen the human-understanding argument, but they do not themselves provide estate-wide relationship-coverage scorecards. [fact; source: https://dora.dev/; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt]

**Open questions:**

- Which minimal cross-tool metric set would let an organisation compare catalog coverage, CMDB quality, runtime dependency completeness, and structural-drift signals on one dashboard? [inference; source: https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging]
- How should organisations weight human comprehension metrics, for example team cognitive load or onboarding time, against machine-readable coverage metrics in a composite legibility index? [inference; source: https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://engineering.atspotify.com/2024/04/supercharged-developer-portals]
- Is there enough published evidence to define maturity levels for estate legibility that are portable across ServiceNow, Backstage, LeanIX, Dynatrace, and CAST rather than remaining vendor-specific? [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging]

### §7 Recursive Review

- Claim audit: complete
- Cross-reference status: completed; reflected in frontmatter `cites` and `related`
- Overall confidence: medium
- Supersession status: no superseded prior item identified

---

## Findings

### Executive Summary

There is no single cross-industry framework that directly measures "IT system legibility" as one settled property; the field measures it through a composite of adjacent systems for architecture-model completeness, catalog discoverability, configuration-data quality, dependency visibility, drift detection, and shared team understanding. [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt]

The Open Group, BIAN, ServiceNow, Spotify's Backstage ecosystem, SAP LeanIX, Dynatrace, CAST, Thoughtworks, and DORA are the main active definers or operators visible in the accessible evidence, but they define different slices of the problem rather than one shared benchmark. [fact; source: https://www.opengroup.org/togaf; https://bian.org/service-landscape/; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://dora.dev/]

The most explicit operational scorecard found in this review is ServiceNow's CMDB Health model of completeness, compliance, and correctness, while the clearest complementary runtime and structural models come from Dynatrace Smartscape, Backstage software catalog coverage, LeanIX inventory and dependency visibility, CAST architecture recovery, and Thoughtworks architectural fitness functions. [fact; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://www.castsoftware.com/imaging; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function]

Practical implementation therefore looks like a layered control system: intended-state architecture blueprints and models, ownership-bearing catalogs and CMDBs, live runtime topology, structural impact analysis, and governance routines that reconcile drift and stale data. [inference; source: https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.castsoftware.com/imaging]

### Key Findings

1. **No accessible primary source in this review defines a universal, cross-vendor numeric benchmark for "IT system legibility"; the best-supported conclusion is that practitioners quantify legibility through a bundle of adjacent measures rather than one standard score.** ([inference]; high confidence; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging)
2. **TOGAF, ArchiMate, and BIAN provide the strongest standards-based structure for legibility because they define how to model business, application, technology, and service relationships, but they stop short of publishing a dominant universal scoring rubric for whole-estate understanding.** ([fact]; high confidence; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://bian.org/service-landscape/)
3. **ServiceNow currently provides the clearest explicit operational legibility scorecard in the accessible evidence, because its CMDB Health model quantifies completeness, compliance, and correctness and further decomposes correctness into duplicate, orphan, and stale configuration records.** ([fact]; high confidence; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492)
4. **Backstage and Spotify's internal developer portal practice treat discoverability, ownership, and catalog coverage as measurable legibility proxies, showing that a component is not truly legible to an organisation if nobody can find it, identify its owner, or keep its metadata current.** ([inference]; high confidence; source: https://backstage.io/docs/features/software-catalog/; https://engineering.atspotify.com/2024/04/supercharged-developer-portals)
5. **SAP LeanIX operationalises estate legibility at portfolio level by combining trustworthy inventory, dependency visibility, ownership, business-context mapping, and standardised application-assessment criteria, which makes it a planning and rationalisation framework rather than a runtime truth source.** ([fact]; medium confidence; source: https://www.leanix.net/en/products/application-portfolio-management; https://www.leanix.net/en/wiki/ea/application-portfolio-management)
6. **Dynatrace Smartscape operationalises legibility at runtime by continuously mapping service and infrastructure relationships, upstream and downstream dependency chains, ownership, and blast radius, which makes it the strongest live-topology evidence source in this review.** ([fact]; high confidence; source: https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/)
7. **CAST Imaging operationalises legibility at structural-code level by recovering architecture across multiple abstraction layers, exposing change impact, and tracking design adherence and drift, which addresses blind spots that catalogs and runtime tools do not cover well.** ([fact]; medium confidence; source: https://www.castsoftware.com/imaging)
8. **Thoughtworks' architectural fitness functions and codebase cognitive debt framing show that legibility is partly a human-governance property, because an estate can be instrumented and documented yet still become hard to reason about if teams lose shared understanding or stop enforcing architectural constraints.** ([inference]; high confidence; source: https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt)
9. **The strongest practical implementation pattern is a layered composite in which architecture standards define intended structure, catalogs and CMDBs assign coverage and ownership, runtime topology validates live relationships, and software-intelligence tools test for structural drift and change impact.** ([inference]; high confidence; source: https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging)
10. **Published implementation evidence suggests that better legibility improves onboarding, decision speed, incident routing, audit readiness, and change-impact analysis, but confidence in comparative tool superiority remains limited because most accessible outcome claims are vendor- or practitioner-reported rather than cross-vendor benchmark studies.** ([inference]; medium confidence; source: https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] No universal cross-vendor numeric benchmark exists; practice uses a composite of measures. | https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging | high | Cross-source synthesis |
| [fact] TOGAF, ArchiMate, and BIAN define structure and coverage, not one dominant score. | https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://bian.org/service-landscape/ | high | Standards layer |
| [fact] ServiceNow CMDB Health uses completeness, compliance, and correctness, including duplicate, orphan, and stale checks. | https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492 | high | Explicit scorecard |
| [inference] Backstage uses discoverability, ownership, and catalog coverage as legibility proxies. | https://backstage.io/docs/features/software-catalog/; https://engineering.atspotify.com/2024/04/supercharged-developer-portals | high | Catalog layer |
| [fact] LeanIX uses trustworthy inventory, dependencies, ownership, and assessment criteria for portfolio visibility. | https://www.leanix.net/en/products/application-portfolio-management; https://www.leanix.net/en/wiki/ea/application-portfolio-management | medium | Vendor product evidence |
| [fact] Dynatrace uses live topology, dependency chains, blast radius, and ownership context for runtime legibility. | https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/ | high | Runtime layer |
| [fact] CAST uses recovered architecture layers, impact analysis, and drift tracking for structural legibility. | https://www.castsoftware.com/imaging | medium | Vendor product evidence |
| [inference] Human understanding and architectural guardrails are part of legibility, not an optional extra. | https://www.thoughtworks.com/radar/techniques/architectural-fitness-function; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt | high | Human-governance layer |
| [inference] The strongest implementation pattern is a layered composite rather than a single tool. | https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging | high | Cross-layer synthesis |
| [inference] Outcome claims are positive but mostly vendor- or practitioner-reported, so comparative claims should stay cautious. | https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009 | medium | Evidence-quality limit |

### Assumptions

- **Assumption:** This item uses "IT system legibility" as a synthesis label for overlapping source concepts such as architecture visibility, catalog discoverability, CMDB health, dependency completeness, and shared system understanding. **Justification:** the exact phrase is not the dominant source label even though the operational problem is clearly shared. [assumption; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492]
- **Assumption:** Public vendor and practitioner outcome numbers are directionally informative but not neutral comparative benchmarks. **Justification:** the accessible evidence does not provide one independent cross-vendor evaluation protocol. [assumption; source: https://www.leanix.net/en/products/application-portfolio-management; https://engineering.atspotify.com/2024/04/supercharged-developer-portals; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/]

### Analysis

The evidence was weighted most heavily toward sources that clearly separate structure from measurement, because that distinction answers the research question more directly than generic platform positioning does. [inference; source: https://www.opengroup.org/togaf; https://www.opengroup.org/archimate-forum/archimate-overview; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492]

That weighting makes ServiceNow's CMDB Health model unusually important, because it is the only source in the review that exposes a concrete, named scorecard for estate-data quality rather than only describing architecture artifacts or discovery features. [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape]

The main competing interpretation was that runtime topology tools already solve legibility by themselves, but that interpretation weakened once catalog, CMDB, architecture, and structural-analysis sources were compared, because each addresses blind spots that live telemetry alone cannot close. [inference; source: https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://www.castsoftware.com/imaging; https://www.opengroup.org/togaf]

The strongest conclusion is therefore plural rather than singular: legibility is an emergent property produced by several measurable control surfaces, and the practical design problem is how to compose those surfaces into a governance loop that detects drift faster than the estate changes. [inference; source: https://www.servicenow.com/community/developer-blog/aligning-servicenow-architecture-blueprint-with-togaf-standard/ba-p/3464009; https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446; https://www.thoughtworks.com/radar/techniques/architectural-fitness-function]

### Risks, Gaps, and Uncertainties

- Independent cross-vendor benchmarking of legibility frameworks is thin in the accessible public evidence, so comparative product judgments should remain conservative. [fact; source: https://www.leanix.net/en/products/application-portfolio-management; https://www.dynatrace.com/platform/application-topology-discovery/smartscape/; https://www.castsoftware.com/imaging]
- The most explicit operational metrics come from vendor or platform ecosystems, which creates a risk that the reviewed measures reflect product boundaries more than a universally agreed ontology of whole-estate understanding. [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management]
- BIAN strengthens the standards picture for financial services, but its sector specificity limits direct generalisation to non-banking estates. [fact; source: https://bian.org/service-landscape/]
- The DORA and Thoughtworks sources strengthen the human-understanding argument, but they do not themselves provide estate-wide relationship-coverage scorecards. [fact; source: https://dora.dev/; https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt]

### Open Questions

- Which minimal cross-tool metric set would let an organisation compare catalog coverage, CMDB quality, runtime dependency completeness, and structural-drift signals on one dashboard? [inference; source: https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging]
- How should organisations weight human-comprehension metrics, for example team cognitive load or onboarding time, against machine-readable coverage metrics in a composite legibility index? [inference; source: https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt; https://engineering.atspotify.com/2024/04/supercharged-developer-portals]
- Is there enough published evidence to define maturity levels for estate legibility that are portable across ServiceNow, Backstage, LeanIX, Dynatrace, and CAST rather than remaining vendor-specific? [inference; source: https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://backstage.io/docs/features/software-catalog/; https://www.leanix.net/en/products/application-portfolio-management; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging]

---

## Output

- Type: knowledge
- Description: Composite measurement framework for whole-estate legibility across architecture, catalog, CMDB, runtime-topology, and structural-analysis layers. [inference; source: https://www.opengroup.org/togaf; https://backstage.io/docs/features/software-catalog/; https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492; https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape; https://www.castsoftware.com/imaging]
- Links:
  - https://www.servicenow.com/community/cmdb-forum/cmdb-health-dashboard-completeness-compliance-amp-correctness/m-p/3488492
  - https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape
  - https://www.opengroup.org/archimate-forum/archimate-overview
