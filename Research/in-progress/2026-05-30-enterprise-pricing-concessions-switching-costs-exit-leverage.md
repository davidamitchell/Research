---
review_count: 2
title: "Enterprise software pricing concessions, switching costs, and exit leverage"
added: 2026-05-30T21:51:23+00:00
status: reviewing
priority: medium
blocks: []
themes: [enterprise-adoption, cost-performance, governance-policy, software-engineering]
started: 2026-06-02T11:29:22+00:00
completed: ~
output: [knowledge]
cites: [transaction-costs, financial-forecasting-it-run-costs, vendor-platform-governance-constraints-compensating-controls]
related: [transaction-costs, financial-forecasting-it-run-costs, vendor-platform-governance-constraints-compensating-controls]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Enterprise software pricing concessions, switching costs, and exit leverage

## Research Question

How do enterprise software vendors use upfront pricing concessions to increase switching costs over contract lifecycles, and what abstraction or architectural investment strategies demonstrably reduce total cost of ownership (TCO) by preserving exit leverage?

## Scope

**In scope:**
- Empirical evidence that discount-at-signing followed by lock-in dynamics occurs in enterprise software contracts.
- TCO models and studies that capture lifecycle costs (migration, integration, retraining, data egress, and renegotiation), not only initial licensing.
- Evidence-backed architecture or abstraction strategies that lower switching costs and preserve bargaining power at renewal.

**Out of scope:**
- Consumer software pricing and non-enterprise subscription markets.
- Legal drafting guidance for specific jurisdictions.
- Purely theoretical architecture guidance without measurable cost or switching outcomes.

**Constraints:** Prioritise peer-reviewed economics and information systems literature, regulator/competition authority reports, and vendor-neutral enterprise case studies from the last 10-15 years.

## Context

Enterprise buyers regularly sign software contracts that include upfront discounts or favourable initial pricing. Over the contract lifecycle, switching costs accumulate through data lock-in, deep customisation, integration dependencies, and retraining burdens, shifting bargaining power to the vendor at renewal. The issue asks for evidence that this upfront-discount-to-lock-in sequence is real, for a lifecycle TCO framing rather than signing-price comparisons, and for practical architecture decisions that preserve exit leverage as a control on long-term enterprise software spend. "Exit leverage" is used here to mean the credible ability to migrate to an alternative vendor or platform at a cost low enough to discipline incumbent pricing at renewal.

## Approach

1. Establish the empirical pattern by synthesising research and market studies on switching costs, contract dynamics, and post-discount price/cost escalation in enterprise software.
2. Compare TCO frameworks used in enterprise software sourcing to identify which cost categories most consistently explain ex-post lock-in and renegotiation disadvantage.
3. Evaluate architectural interventions (for example open standards, interface abstraction, portable data models, and modular integration boundaries) and map which ones show measurable reductions in migration cost or switching friction.

## Sources

- [Farrell and Klemperer (2007) Coordination and Lock-In: Competition with Switching Costs and Network Effects](https://cepr.org/publications/dp5798). Economics foundation for switching-cost lock-in mechanisms. Source correction: the seeded URL https://www.nber.org/papers/w12911 resolves to a different paper (Banerjee, Iyer, and Somanathan on public goods); replaced with the CEPR discussion paper for the same Farrell/Klemperer work.
- [Klemperer (1987) Markets with Consumer Switching Costs](https://www.jstor.org/stable/1885068). Classic model of switching-cost competition dynamics.
- [UK Competition and Markets Authority (CMA) Cloud Services Market Investigation Final Decision (2025)](https://www.gov.uk/cma-cases/cloud-services-market-investigation). Contemporary regulator evidence on enterprise switching barriers in cloud infrastructure.
- [European Union Data Act (Regulation (EU) 2023/2854)](https://digital-strategy.ec.europa.eu/en/policies/data-act). Policy intervention focused on cloud and data-processing service switching and portability.
- [EU Data Act Article 25 (contractual terms for switching)](https://data-act-law.eu/article/25/). Primary legal text on switching rights and fee restrictions.
- [Cloud Native Computing Foundation (CNCF) Cloud Native Definition v1.1](https://github.com/cncf/toc/blob/main/DEFINITION.md). Architecture principles frequently cited as reducing platform lock-in risk.
- [ERP Research: Total Cost of Ownership Calculator and Guide](https://www.erpresearch.com/en-us/erp-tco-calculator). Practitioner-facing TCO framework for Enterprise Resource Planning lifecycle cost estimation.
- [Arion ERP: Beyond the Sticker Price, unpacking the true TCO for ERP systems](https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html). Industry analysis of ERP cost distribution across licence, implementation, migration, and support.

## Research Skill Output

### §0 Initialise

Question: How do enterprise software vendors use upfront pricing concessions to increase switching costs over contract lifecycles, and what abstraction or architectural investment strategies demonstrably reduce total cost of ownership (TCO) by preserving exit leverage?

Scope: Enterprise software categories including cloud infrastructure, Enterprise Resource Planning (ERP), and horizontal software-as-a-service (SaaS) platforms. Lifecycle cost framing; not limited to signing prices.

Constraints: Peer-reviewed economics, regulator reports, and vendor-neutral case studies from the last 10-15 years. Exclude consumer markets and jurisdiction-specific legal drafting.

Output format: `knowledge` item with structured Findings section covering the empirical pattern, TCO framework analysis, and architectural mitigation strategies.

Working hypotheses (to be tested against evidence):
- [assumption; source: https://cepr.org/publications/dp5798] Vendors with high-switching-cost products rationally compete aggressively for new customers at low margins, expecting to recoup profit from the locked-in installed base.
- [assumption; source: https://www.erpresearch.com/en-us/erp-tco-calculator] Organisations that model only initial licence costs when evaluating enterprise software will systematically underestimate lifecycle TCO because migration, integration, and retraining costs materialise later.
- [assumption; source: https://github.com/cncf/toc/blob/main/DEFINITION.md] Architectural investments in open standards and portable abstractions reduce technical switching costs even when contractual exit costs remain.

Source correction noted: The seeded National Bureau of Economic Research (NBER) URL (https://www.nber.org/papers/w12911) resolves to a different paper by Banerjee, Iyer, and Somanathan (2007) on public goods provision. The Farrell and Klemperer switching-costs survey is available at the Centre for Economic Policy Research (CEPR) as discussion paper DP5798: https://cepr.org/publications/dp5798. The Sources section has been updated accordingly.

### §1 Question Decomposition

The research question decomposes into three sub-questions, each decomposed further into atomic questions:

**Sub-question A: Does the empirical pattern of upfront-discount-to-lock-in exist in enterprise software markets?**

- A1. What does switching-cost economics predict about vendor pricing strategy across the customer lifecycle?
- A2. Do competition authority investigations confirm that switching rates in enterprise cloud markets are low and that commercial barriers are significant?
- A3. Are maintenance-fee escalation and egress-fee structures documented as post-discount revenue recovery mechanisms?

**Sub-question B: Which TCO cost categories most consistently explain ex-post lock-in and renegotiation disadvantage?**

- B1. What share of ERP or enterprise software TCO is represented by initial licensing versus migration, integration, and support costs?
- B2. Which cost categories most reliably identify renegotiation disadvantage at renewal?
- B3. How does asset specificity (in the Williamson sense) amplify TCO over the contract lifecycle?

**Sub-question C: Which architectural interventions demonstrably reduce switching costs or preserve exit leverage?**

- C1. What do open-standards and container-based portability architectures provide in terms of measurable switching-friction reduction?
- C2. What does regulatory evidence say about the effect of mandated portability rules on switching behaviour?
- C3. How does credible threat of exit affect vendor pricing and contract terms?

### §2 Investigation

**A1. Switching-cost economics and vendor lifecycle pricing strategy**

[fact; source: https://www.jstor.org/stable/1885068] Klemperer (1987) "Markets with Consumer Switching Costs" in the Quarterly Journal of Economics, 102(2), 375-394, establishes the central theoretical result: in markets where consumers face switching costs, firms compete intensely for new customers (accepting low margins or even losses at acquisition) but exercise market power over their existing, locked-in customer base by setting higher prices than they could in a frictionless market.

[fact; source: https://cepr.org/publications/dp5798] Farrell and Klemperer (2007) "Coordination and Lock-In: Competition with Switching Costs and Network Effects" (CEPR Discussion Paper 5798, subsequently published in the Handbook of Industrial Organization, Vol 3, eds. Armstrong and Porter) consolidates the theoretical and empirical literature. Key result: in two-period models with switching costs, firms set below-cost or heavily discounted prices in period one to attract customers, then exploit the locked-in installed base through higher prices in period two. The mechanism is rational for vendors because expected lifetime profit is positive even when period-one pricing is unprofitable.

[inference; source: https://cepr.org/publications/dp5798] This dynamic maps to observed enterprise software contracting practice: initial-year discounts or "land and expand" pricing strategies followed by maintenance-fee escalation and proprietary upgrade dependencies over multi-year agreements. The theoretical prediction is that vendors with high switching-cost products will use initial discounts specifically as an investment in future installed-base pricing power.

[inference; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068] The Williamson (1985) concept of asset specificity (covered by the related completed item at https://davidamitchell.github.io/Research/research/2026-03-02-transaction-costs.html) reinforces the switching-cost model: once an enterprise has made relationship-specific investments (customising an ERP, training staff on vendor-proprietary workflows, integrating the platform into other systems), the vendor gains hold-up leverage because the buyer cannot credibly threaten to switch without incurring those sunk costs. The combination of switching-cost economics and hold-up theory means the lock-in mechanism is over-determined.

**A2. Competition authority evidence on switching rates and commercial barriers**

[fact; source: https://www.gov.uk/cma-cases/cloud-services-market-investigation; https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] The Competition and Markets Authority (CMA) published its final decision on the cloud services market investigation on 31 July 2025. The CMA found that competition in the United Kingdom (UK) cloud infrastructure services market is not working well, citing significant commercial and technical barriers to switching between cloud providers.

[fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf; https://datacentrereview.com/2025/08/aws-microsoft-to-face-competition-probe-as-cma-concludes-uk-cloud-market-investigation/] Fewer than 1% of enterprise cloud customers switch providers annually in the UK market, a finding the CMA attributed primarily to high switching costs including egress fees and technical lock-in from lack of interoperability.

[fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] Microsoft and Amazon Web Services (AWS) each hold approximately 30-40% of UK cloud infrastructure spend; Google Cloud holds approximately 5-10%. The CMA concluded that market concentration is expected to endure, reinforcing provider market power.

[fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] The CMA found that even a 5% overcharge in a less competitive market could cost UK organisations approximately £500 million in additional annual costs on a £10.5 billion cloud spend base.

[inference; source: https://www.gov.uk/cma-cases/cloud-services-market-investigation] The CMA recommended that its digital markets powers be used to consider Strategic Market Status (SMS) designations for AWS and Microsoft, which could enable binding conduct remedies on egress fees and switching-related practices from 2026 onward.

**A3. Post-discount revenue recovery mechanisms: maintenance fees and egress fees**

[inference; source: https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Enterprise software vendors including Oracle and SAP have historically structured annual maintenance and support fees at approximately 20-22% of the initial licence price, with annual escalation clauses of 3-5%. Because these fees are calculated on the original licence value rather than current market rates, they represent a predictable aftermarket revenue stream that does not require the vendor to remain price-competitive with alternatives.

[fact; source: https://assets.publishing.service.gov.uk/media/688b8143d8da16bcb8469523/Appendix_M_-_Egress_fees___analysis_of_customers__cost_scenarios.pdf] The CMA found that egress fees (charges for transferring data out of a cloud provider) constitute a key commercial barrier to switching. Customers find it difficult to anticipate full switching costs because egress fees are complex, non-transparent, and significant, and are often excluded from initial migration cost analyses.

Access note: The CMA Appendix M on egress-fee cost scenarios was accessible via the CMA case page at https://www.gov.uk/cma-cases/cloud-services-market-investigation.

**B1. Share of ERP TCO: licensing versus lifecycle costs**

[inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Industry TCO analysis consistently finds that software licensing accounts for only 20-30% of the true TCO of an ERP or large enterprise software platform over a five-to-ten year lifecycle. The remaining 70-80% comprises implementation services, customisation, data migration, integration maintenance, user retraining, and ongoing support costs.

[inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Organisations that rely on vendor-quoted licensing costs when comparing platforms underestimate true TCO by 40-60%, because post-signing costs are invisible at the time of the sourcing decision. This information asymmetry structurally favours vendors offering lower headline prices with higher expected lifecycle lock-in.

[inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://davidamitchell.github.io/Research/research/2026-03-13-financial-forecasting-it-run-costs.html] TCO forecast uncertainty compounds further over multi-year horizons: the completed research item on IT run-cost forecasting found that forecast error can compound to ±75% under correlated cost inputs over a five-year period, which reinforces why enterprises that anchor their evaluation to vendor-quoted initial prices underestimate not only the expected lifecycle cost but also the range of possible outcomes.

[inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator] When migration to an alternative vendor is considered, switching costs including data extraction, business process redesign, integration re-platforming, and productivity loss during transition can reach 25-50% of the original platform investment, making the threat of switching non-credible unless the cost difference with the incumbent is substantial.

**B2. Cost categories driving renegotiation disadvantage**

[inference; source: https://cepr.org/publications/dp5798; https://www.erpresearch.com/en-us/erp-tco-calculator] The cost categories that most consistently create renegotiation disadvantage at contract renewal are: (1) proprietary data formats and model dependencies that require bespoke extraction tooling for migration; (2) deep customisation built on vendor-proprietary development environments; (3) integration coupling that links the platform to other production systems through vendor-specific interfaces rather than open standards; and (4) staff expertise that has been trained on vendor-specific workflows, increasing the retraining cost of any migration.

[assumption; source: https://cepr.org/publications/dp5798] Enterprises without an independently developed and maintained migration playbook are at a structural disadvantage at renewal negotiations because the vendor can credibly assume the buyer lacks the operational readiness to execute a switch within a normal notice period.

**B3. Asset specificity amplification over the contract lifecycle**

[inference; source: https://davidamitchell.github.io/Research/research/2026-03-02-transaction-costs.html; https://cepr.org/publications/dp5798] Williamson's concept of asset specificity (covered in the related completed item on Transaction Cost Economics) directly explains why switching costs compound over the contract lifecycle: each additional customisation, integration, or workflow optimisation built on vendor-specific infrastructure increases the specificity of the enterprise's investment to this particular vendor relationship, raising the cost and risk of switching and thus strengthening the vendor's hold-up position at renewal.

**C1. Open standards, containerisation, and portability architectures**

[fact; source: https://github.com/cncf/toc/blob/main/DEFINITION.md] The Cloud Native Computing Foundation (CNCF) Cloud Native Definition v1.1 (approved 2024-02-26) defines cloud-native practices as enabling organisations to develop, build, and deploy workloads in computing environments (public, private, and hybrid cloud) through loosely coupled systems that interoperate in a secure, resilient, manageable, sustainable, and observable manner. The CNCF lists containers, service meshes, microservices, immutable infrastructure, and declarative Application Programming Interfaces (APIs) as representative technologies.

[inference; source: https://github.com/cncf/toc/blob/main/DEFINITION.md] Container-based deployment using standardised orchestration (specifically Kubernetes) decouples application workloads from cloud-provider-specific execution environments, reducing the technical component of switching costs by enabling workloads to run identically across providers.

[inference; source: https://github.com/cncf/toc/blob/main/DEFINITION.md] Open-standards-based integration using declarative APIs rather than proprietary connectors reduces the interface coupling category of lock-in because the interface contract is defined by the standard rather than by the vendor.

[inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-vendor-platform-governance-constraints-compensating-controls.html; https://github.com/cncf/toc/blob/main/DEFINITION.md] The completed research item on vendor platform governance constraints found that keeping policy, approval logic, and control objectives outside the vendor plane is the architectural design principle that most reliably reduces lock-in and roadmap volatility. This is directly complementary to the CNCF cloud-native approach: both position ownership of control surfaces at the enterprise layer, with vendor infrastructure as an execution environment rather than a policy authority.

**C2. Regulatory evidence on mandated portability and switching behaviour**

[fact; source: https://digital-strategy.ec.europa.eu/en/policies/data-act] The European Union (EU) Data Act (Regulation (EU) 2023/2854) entered into force on 11 January 2024 and entered into application on 12 September 2025. It includes mandatory switching-facilitation obligations for cloud and data-processing service providers operating in the EU.

[fact; source: https://data-act-law.eu/article/25/] Article 25 of the EU Data Act requires that contracts include clauses allowing customers to switch providers within a maximum 30-calendar-day transitional period (or up to seven months where technically unfeasible), a maximum two-month notice period, 30-day minimum data-retrieval rights after transition, and full data erasure provisions. Providers must support the customer's exit strategy and maintain business continuity and security throughout the switching process.

[fact; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://data-act-law.eu/article/25/] Under the EU Data Act, egress and switching fees must be reduced to cost-based levels during the 2025-2027 transition period and eliminated entirely by January 2027 for provider-to-provider switching.

[inference; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://www.gov.uk/cma-cases/cloud-services-market-investigation] The regulatory response by both the EU (Data Act) and the UK CMA confirms that switching barriers in cloud services markets are sufficiently severe to require legislative and regulatory intervention, consistent with the theoretical prediction that vendors in high-switching-cost markets exploit installed-base pricing power.

**C3. Effect of credible exit threat on vendor pricing and terms**

[inference; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068] Switching-cost economics predicts that enterprises with a credible outside option (an alternative vendor they could plausibly migrate to at acceptable cost) receive better pricing and contract terms because the incumbent vendor cannot exploit hold-up leverage. The threat of exit is only credible if the enterprise has invested in the preconditions for switching: portable data formats, documented integration interfaces, maintained migration playbooks, and staff capability to operate on an alternative platform.

[inference; source: https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Industry practitioners report that enterprises with experienced software procurement teams and independent benchmarking data obtain materially better pricing and contract flexibility at renewal. The improvement is attributed to credible switching threats rather than to negotiation skill alone.

### §3 Reasoning

The causal chain from upfront discount to lock-in to renegotiation disadvantage runs as follows:

1. [inference; source: https://cepr.org/publications/dp5798] Vendors with high inherent switching costs rationally set discounted initial pricing to maximise installed-base size, because future installed-base profit exceeds the cost of the initial discount.

2. [inference; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068] Once onboarded, enterprises accumulate asset-specific investments (customisations, integrations, trained workflows) that increase switching costs monotonically over time and strengthen the vendor's hold-up position.

3. [inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Because lifecycle costs (70-80% of TCO) materialise after contract signing and are not visible in the initial procurement analysis, the buyer's information disadvantage compounds the switching-cost disadvantage.

4. [fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] Annual switching rates below 1% in the UK cloud market confirm that the theoretical prediction of low switching is empirically realised.

5. [inference; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://www.gov.uk/cma-cases/cloud-services-market-investigation] Regulatory response (EU Data Act, CMA SMS designation process) confirms that market forces alone are insufficient to correct the pricing distortion created by high switching costs.

Rival explanation: competitive dynamic pricing without lock-in exploitation. An alternative interpretation is that vendors offer initial discounts to demonstrate product value (a signalling story) rather than to build lock-in. This interpretation is inconsistent with the CMA evidence of sub-1% annual switching rates and the documented escalation of maintenance fees and egress charges after onboarding. [inference; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf; https://cepr.org/publications/dp5798]

Complementary explanation: network effects. The primary theoretical source, Farrell and Klemperer (2007), explicitly treats network effects as a distinct lock-in mechanism that can independently explain low switching rates and installed-base pricing power. In markets where the value of a platform increases with the number of users (such as collaboration tools, marketplaces, and cloud ecosystems with large ecosystems of compatible third-party services), network effects can sustain incumbent positions even after switching costs are reduced. For cloud infrastructure markets, the CMA investigation treated both switching costs and network effects as material factors in market structure. The two mechanisms are complementary rather than substitutes: switching costs explain why individual enterprises do not switch even when alternatives are available; network effects explain why the market as a whole converges on a small number of providers. [inference; source: https://cepr.org/publications/dp5798; https://www.gov.uk/cma-cases/cloud-services-market-investigation]

### §4 Consistency Check

```text
contradiction_scan: none found
  licensing share (20-30% of TCO) consistent across ERP TCO sources
  CMA switching-rate evidence (<1% annually) consistent with theoretical prediction
  EU Data Act egress-fee timeline: cost-based 2025-2027, zero 2027+ (no contradiction)
rival_explanation_handled: yes (signalling alternative addressed in §3)
scope_guardrail: consumer markets excluded; theoretical-only architecture excluded
confidence_adjustment: medium maintained; ERP TCO figures are industry practitioner estimates,
  not peer-reviewed empirical studies; regulatory findings are primary sources
asset_specificity_reference: linked to completed TCE item, not duplicated
```

### §5 Depth and Breadth Expansion

**Regulatory lens:** The concurrent emergence of the EU Data Act (2023/2854) and the UK CMA SMS designation process for cloud providers represents a structural shift: switching barriers that were previously treated as private contract matters are now subject to public regulation. For enterprises operating in EU or UK jurisdictions, compliance obligations on cloud providers (transparent switching terms, 30-day portability windows, fee elimination by 2027) represent an externally enforced reduction in technical and commercial switching costs. [inference; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://www.gov.uk/cma-cases/cloud-services-market-investigation]

**Economic lens:** The Williamson hold-up problem (asset specificity raising switching costs after relationship-specific investment) and the Klemperer/Farrell installed-base pricing model jointly predict that switching-cost markets produce below-competitive prices for new customers and above-competitive prices for incumbents. This creates a market structure where aggressive initial pricing is a rational investment in future market power rather than a sign of competitive vigour. [inference; source: https://cepr.org/publications/dp5798; https://davidamitchell.github.io/Research/research/2026-03-02-transaction-costs.html]

**Architectural lens:** The CNCF cloud-native approach separates the problem into technical switching costs (reduced by containerisation, open APIs, and portable data models) and commercial switching costs (addressed by contract terms, exit clauses, and regulatory rules). Technical architectural investment reduces the cost floor for switching even when commercial costs remain; the floor matters because it determines whether the threat of exit is credible at renewal. [inference; source: https://github.com/cncf/toc/blob/main/DEFINITION.md]

**Historical lens:** Enterprise Resource Planning lock-in (SAP, Oracle) is one of the most extensively documented instances of the switching-cost dynamic in practice. The pattern: aggressive initial licensing discounts in the 1990s-2000s built installed bases, then annual maintenance fees (standardised at 18-22% of licence value) created a stable, escalating, and difficult-to-exit revenue stream. The empirical outcome is that switching rates for large ERP implementations are estimated to be materially below 5% per renewal cycle. [inference; source: https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html; https://cepr.org/publications/dp5798]

**Behavioural lens:** Enterprises frequently underinvest in architectural portability during the initial implementation because the costs of lock-in are distant and uncertain, while the benefits of rapid deployment are immediate and visible. This is consistent with hyperbolic discounting (over-weighting near-term costs versus future costs). The result is that even enterprises aware of the lock-in risk structurally under-invest in the preconditions for credible exit. [assumption; source: https://cepr.org/publications/dp5798]

### §6 Synthesis

**Executive Summary (§6 draft, seeded into Findings)**

Enterprise software vendors systematically use upfront pricing concessions to build installed bases, then exploit accumulated switching costs at renewal through maintenance-fee escalation, egress charges, and proprietary integration dependencies. [inference; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068] The Competition and Markets Authority (CMA) 2025 final decision confirmed fewer than 1% annual switching rates in UK cloud infrastructure and identified egress fees and technical lock-in as the primary commercial barriers. [fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] Software licensing represents only 20-30% of enterprise software total cost of ownership (TCO) over a five-to-ten year lifecycle; migration, integration, and support costs account for the remaining 70-80%, explaining why sourcing decisions based on headline pricing structurally underestimate lock-in exposure. [inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Regulatory interventions (EU Data Act, CMA Strategic Market Status process) confirm that market forces alone are insufficient to correct the pricing distortions created by high switching costs, and mandate vendor-side changes including egress fee elimination by 2027. [inference; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] Architectural investments in open standards, container portability, and portable data models reduce the technical floor of switching costs, making exit threats credible and improving bargaining position at renewal even before regulatory obligations take effect. [inference; source: https://github.com/cncf/toc/blob/main/DEFINITION.md; https://cepr.org/publications/dp5798]

**Key Findings (§6 draft)**

1. The theoretical model of two-period pricing in switching-cost markets predicts that vendors set below-cost initial prices to build installed bases and recoup profit through higher installed-base prices, a prediction corroborated by observed maintenance-fee structures and the sub-1% annual switching rates documented by the CMA. ([inference]; high confidence; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068)

2. The CMA 2025 final decision found that fewer than 1% of enterprise cloud customers switch cloud infrastructure providers annually in the UK, attributing this low switching rate to egress fees, lack of interoperability, and technical lock-in as primary commercial barriers. ([fact]; high confidence; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf)

3. Microsoft and AWS each hold approximately 30-40% of UK cloud infrastructure spend by revenue, with the CMA estimating that even a 5% overcharge due to reduced competitive pressure would cost UK organisations approximately £500 million in additional annual expenditure. ([fact]; high confidence; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf)

4. Software licensing typically accounts for only 20-30% of the lifecycle TCO of enterprise software such as an ERP platform; implementation, migration, integration maintenance, and support costs account for the remaining 70-80%, and organisations relying on headline pricing underestimate true TCO by 40-60%. ([inference]; medium confidence; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html)

5. When enterprise customers consider migrating to an alternative vendor, direct switching costs including data extraction, process redesign, integration re-platforming, and productivity loss during transition are estimated at 25-50% of the original platform investment, making exit threats non-credible unless the cost differential with the incumbent is substantial. ([inference]; medium confidence; source: https://www.erpresearch.com/en-us/erp-tco-calculator)

6. The EU Data Act (Regulation (EU) 2023/2854) entered into application in September 2025 and mandates that cloud and data-processing service providers reduce switching fees to cost-based levels by the end of 2026 and eliminate them entirely by January 2027, representing a legislated structural reduction in commercial exit costs for EU-based enterprise customers. ([fact]; high confidence; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://data-act-law.eu/article/25/)

7. The EU Data Act Article 25 requires that provider contracts include mandatory 30-calendar-day portability windows, maximum two-month notice periods, 30-day minimum data-retrieval rights, and exit-strategy support obligations, establishing a contractual floor for switching rights that applies to all new and existing contracts from 12 September 2025. ([fact]; high confidence; source: https://data-act-law.eu/article/25/)

8. The CNCF cloud-native approach, using container orchestration and declarative APIs, reduces the technical component of switching costs by decoupling application workloads from cloud-provider-specific infrastructure, but does not by itself address commercial lock-in created by data model dependencies or proprietary managed-service integrations. ([inference]; medium confidence; source: https://github.com/cncf/toc/blob/main/DEFINITION.md)

9. Enterprises with documented migration playbooks, portable data exports, open-standards-based integrations, and staff capability on alternative platforms can make credible exit threats that discipline incumbent pricing at renewal, because the vendor cannot rely on the assumption that switching is operationally infeasible within the notice period. ([inference]; medium confidence; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068)

10. The asset-specificity concept from Williamson's transaction cost economics explains why switching costs compound over the contract lifecycle: each additional customisation or integration built on vendor-proprietary infrastructure raises the relationship-specific investment, increasing the vendor's hold-up leverage at renewal. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-02-transaction-costs.html; https://cepr.org/publications/dp5798)

**Assumptions**

- [assumption; source: https://cepr.org/publications/dp5798] The two-period pricing model from switching-cost economics applies to multi-year enterprise software contracts where the "first period" is the initial signing and the "second period" is the renewal sequence.
- [assumption; source: https://www.erpresearch.com/en-us/erp-tco-calculator] The 20-30% licensing / 70-80% lifecycle cost split is a robust order-of-magnitude estimate; exact figures vary by platform complexity, implementation depth, and organisation size.
- [assumption; source: https://github.com/cncf/toc/blob/main/DEFINITION.md] Architectural investments that reduce technical switching costs also reduce total exit costs by making the commercial negotiation credible, but the relationship is not one-to-one because commercial and technical costs are partially independent.

**Risks and Gaps**

- The ERP TCO figures (20-30% licensing, 70-80% lifecycle) are drawn from industry practitioner sources rather than peer-reviewed academic studies. No systematic quantitative study of switching costs across enterprise software categories was identified in this investigation. A primary empirical study with a defined sample would strengthen these estimates.
- The CMA findings apply to cloud infrastructure (Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) categories) in the UK. It is not established that the sub-1% switching rate applies equally to SaaS platforms, ERP systems, or enterprise collaboration tools; these are separately structured markets.
- The EU Data Act switching rights (Article 25) entered into application in September 2025, which is recent enough that empirical evidence on their effect on switching behaviour is not yet available. The predicted reduction in commercial exit costs is theoretically grounded but not yet empirically confirmed.
- Architectural investment in portability increases short-term implementation cost and complexity. No empirical study was identified that directly measures the return on investment (ROI) of portability investment versus expected lock-in cost savings; this remains a decision that enterprises must make under uncertainty.

**Open Questions**

- Does the upfront-discount-to-lock-in dynamic differ systematically between on-premises ERP, cloud SaaS platforms, and cloud infrastructure? What are the switching cost compositions in each category?
- What is the empirical relationship between early architectural investment in portability and negotiated pricing improvements at renewal? Is there a measurable premium for enterprises that maintain credible exit options?
- How do the EU Data Act switching obligations affect the pricing strategies of cloud providers subject to it? Will vendors offset eliminated egress fees through other mechanisms?

**Output**

- Type: knowledge
- Description: This item synthesises the switching-cost economics literature, regulator findings, and architectural strategy evidence to characterise the upfront-discount-to-lock-in dynamic in enterprise software markets and identify the most evidence-backed strategies for preserving exit leverage across the contract lifecycle. [inference; source: https://cepr.org/publications/dp5798; https://www.gov.uk/cma-cases/cloud-services-market-investigation]
- Key sources: https://cepr.org/publications/dp5798, https://www.gov.uk/cma-cases/cloud-services-market-investigation, https://digital-strategy.ec.europa.eu/en/policies/data-act

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  TCO: expanded in Research Question
  ERP: expanded at first use in §2 Investigation
  CMA: expanded at first use in §0 Initialise
  EU: expanded at first use in §2 Investigation (C2)
  SaaS: expanded at first use in §0 Initialise
  CNCF: expanded at first use in §2 Investigation (C1)
  API: expanded at first use in §2 Investigation (C1)
  SMS: expanded at first use in §2 Investigation (A2)
  AWS: expanded at first use in §2 Investigation (A2)
  UK: expanded at first use in §2 Investigation (A2)
  ROI: expanded as "return on investment (ROI)" at first use in §6 Risks
  IaaS: expanded as "Infrastructure as a Service (IaaS)" at first use in §6 Risks/Gaps
  PaaS: expanded as "Platform as a Service (PaaS)" at first use in §6 Risks/Gaps
  CEPR: expanded at first use in §0 source correction
  NBER: expanded at first use in §0 source correction
  IoT: not used in body text
claim_audit: every factual or inferential claim carries [fact], [inference], or [assumption] label
source_audit: every claim binds to an accessible URL; seeded NBER URL corrected in Sources
style_audit: em-dashes removed from Sources section; no bold full-sentence claims in Findings
scope_guardrail: consumer markets and purely-theoretical architecture excluded throughout
rival_explanation: signalling alternative addressed in §3; network effects complementary explanation addressed in §3 (Farrell/Klemperer paper covers both switching costs and network effects; item explains why switching costs are the primary focus for architectural and contractual remediation)
cross_item_integration: financial-forecasting-it-run-costs cross-referenced in §2 B1; vendor-platform-governance-constraints-compensating-controls cross-referenced in §2 C1
parity_check: §6 Synthesis and Findings are aligned
```

## Findings

### Executive Summary

Enterprise software vendors systematically use upfront pricing concessions to build installed bases, then exploit accumulated switching costs at renewal through maintenance-fee escalation, egress charges, and proprietary integration dependencies. [inference; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068] The Competition and Markets Authority (CMA) 2025 final decision confirmed fewer than 1% annual switching rates in UK cloud infrastructure and identified egress fees and technical lock-in as the primary commercial barriers. [fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] Software licensing represents only 20-30% of enterprise software TCO over a five-to-ten year lifecycle; migration, integration, and support costs account for the remaining 70-80%, explaining why sourcing decisions based on headline pricing structurally underestimate lock-in exposure. [inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Regulatory interventions (EU Data Act, CMA Strategic Market Status process) confirm that market forces alone are insufficient to correct the pricing distortions created by high switching costs, and mandate vendor-side changes including egress fee elimination by 2027. [inference; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] Architectural investments in open standards, container portability, and portable data models reduce the technical floor of switching costs, making exit threats credible and improving bargaining position at renewal even before regulatory obligations take effect. [inference; source: https://github.com/cncf/toc/blob/main/DEFINITION.md; https://cepr.org/publications/dp5798]

### Key Findings

1. The theoretical model of two-period pricing in switching-cost markets predicts that vendors set below-cost initial prices to build installed bases and recoup profit through higher installed-base prices at renewal, a prediction corroborated by the sub-1% annual switching rates documented by the CMA and by documented maintenance-fee structures. ([inference]; high confidence; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068)

2. The CMA 2025 final decision found that fewer than 1% of enterprise cloud customers switch cloud infrastructure providers annually in the United Kingdom, attributing this low rate to egress fees, lack of interoperability, and technical lock-in as the primary commercial barriers that depress competitive pressure on incumbents. ([fact]; high confidence; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf)

3. Microsoft and Amazon Web Services (AWS) each hold approximately 30-40% of UK cloud infrastructure spend, and the CMA estimated that even a 5% overcharge due to reduced competition would cost UK organisations approximately £500 million in additional annual expenditure on a total cloud spend base of £10.5 billion. ([fact]; high confidence; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf)

4. Software licensing typically represents only 20-30% of the lifecycle TCO of enterprise software such as an Enterprise Resource Planning (ERP) platform; implementation, migration, integration maintenance, and support costs account for 70-80%, and organisations relying on vendor-quoted licensing prices underestimate true TCO by 40-60%. ([inference]; medium confidence; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html)

5. Direct enterprise switching costs including data extraction, process redesign, integration re-platforming, and productivity loss during transition are estimated at 25-50% of the original platform investment, making exit threats non-credible at renewal unless the cost differential with the incumbent is large enough to justify that expenditure. ([inference]; medium confidence; source: https://www.erpresearch.com/en-us/erp-tco-calculator)

6. The EU Data Act (Regulation (EU) 2023/2854), applicable from September 2025, mandates that cloud and data-processing service providers reduce switching fees to cost-based levels by end 2026 and eliminate them entirely by January 2027, providing a legislated floor for commercial exit rights for EU-based enterprise customers. ([fact]; high confidence; source: https://digital-strategy.ec.europa.eu/en/policies/data-act; https://data-act-law.eu/article/25/)

7. EU Data Act Article 25 requires provider contracts to include 30-calendar-day portability windows, maximum two-month notice periods, 30-day data-retrieval minimums, and exit-strategy support obligations, establishing contractual switching rights that apply to all new and existing contracts from September 2025. ([fact]; high confidence; source: https://data-act-law.eu/article/25/)

8. The Cloud Native Computing Foundation (CNCF) cloud-native approach using container orchestration and declarative Application Programming Interfaces (APIs) reduces the technical component of switching costs by decoupling workloads from provider-specific infrastructure, but does not address commercial lock-in created by data model dependencies or proprietary managed-service integrations. ([inference]; medium confidence; source: https://github.com/cncf/toc/blob/main/DEFINITION.md)

9. Enterprises that invest in documented migration playbooks, portable data exports, open-standards-based integrations, and staff capability on alternative platforms can make credible exit threats that discipline incumbent pricing at renewal, because the vendor cannot reliably assume that switching is operationally infeasible within the contract notice period. ([inference]; medium confidence; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068)

10. Williamson's asset-specificity concept from transaction cost economics explains why switching costs compound over the contract lifecycle: each additional customisation or integration built on vendor-proprietary infrastructure raises relationship-specific investment and increases the vendor's hold-up leverage at every subsequent renewal. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-02-transaction-costs.html; https://cepr.org/publications/dp5798)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Vendors in switching-cost markets set below-cost initial prices and extract profit from locked-in installed base at renewal | https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068 | high | Theoretical prediction from Klemperer (1987) and Farrell and Klemperer (2007); consistent with CMA empirical findings |
| [fact] Fewer than 1% of enterprise cloud customers switch providers annually in the UK | https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf | high | CMA primary finding, 2025 final decision |
| [fact] Microsoft and AWS hold approximately 30-40% each of UK cloud spend; 5% overcharge ~ £500M annual extra cost | https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf | high | CMA market structure finding |
| [inference] Software licensing = 20-30% of ERP TCO; lifecycle costs = 70-80% | https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html | medium | Industry practitioner sources; peer-reviewed empirical study not identified |
| [inference] Direct switching costs for ERP = 25-50% of original platform investment | https://www.erpresearch.com/en-us/erp-tco-calculator | medium | Order-of-magnitude estimate; no systematic cross-platform study identified |
| [fact] EU Data Act mandates fee elimination for cloud switching by January 2027 | https://digital-strategy.ec.europa.eu/en/policies/data-act; https://data-act-law.eu/article/25/ | high | Primary regulation text; verified against Article 25 and Article 29 of the Data Act |
| [fact] EU Data Act Article 25: 30-day portability windows, 2-month notice maximum, exit-strategy support | https://data-act-law.eu/article/25/ | high | Primary legal text |
| [inference] CNCF cloud-native containerisation reduces technical switching costs but not commercial lock-in | https://github.com/cncf/toc/blob/main/DEFINITION.md | medium | Logical inference from architecture definition; no controlled experiment identified |
| [inference] Credible exit threats reduce incumbent pricing power at renewal | https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068 | medium | Theoretical prediction; consistent with industry practitioner observations |
| [inference] Asset specificity compounds switching costs over the contract lifecycle | https://davidamitchell.github.io/Research/research/2026-03-02-transaction-costs.html; https://cepr.org/publications/dp5798 | medium | Synthesis of Williamson TCE and Farrell/Klemperer lock-in model |

### Assumptions

- Two-period pricing model maps to multi-year enterprise contracts: the Klemperer/Farrell model uses a two-period structure, but enterprise contracts run over multiple renewal cycles. The assumption is that the first-period discount logic extends to multi-period settings because each renewal cycle re-applies the installed-base pricing logic. Justification: this is consistent with the empirical observation of escalating maintenance fees over time. [assumption; source: https://cepr.org/publications/dp5798]

- The 20-30% / 70-80% TCO split is an order-of-magnitude estimate. Exact figures depend on platform complexity, depth of customisation, and organisational size. Justification: multiple independent industry practitioner sources converge on this order of magnitude. [assumption; source: https://www.erpresearch.com/en-us/erp-tco-calculator]

- Architectural portability investment reduces total exit costs: reducing technical switching costs (via open standards, containers) creates a credible exit option even when commercial costs remain. Justification: switching-cost theory predicts that credibility depends on total switching cost being below a threshold; reducing the technical component brings total cost closer to that threshold. [assumption; source: https://github.com/cncf/toc/blob/main/DEFINITION.md; https://cepr.org/publications/dp5798]

### Analysis

The upfront-discount-to-lock-in dynamic is a rational equilibrium in any market where switching costs are high, predictable, and accumulate post-onboarding. [inference; source: https://cepr.org/publications/dp5798] Farrell and Klemperer's model predicts that, from a social welfare perspective, such markets can be competitive in total (vendors compete for new customers), but the welfare is distributed unfavourably: the discounts go to new customers who have not yet been locked in, while the incumbents recoup the investment from existing customers who cannot credibly exit. [inference; source: https://cepr.org/publications/dp5798; https://www.jstor.org/stable/1885068]

CMA evidence from the 2025 final decision confirms the theoretical prediction quantitatively in a specific, well-documented market (UK cloud infrastructure). [fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf] A sub-1% annual switching rate is consistent with the theoretical prediction of near-zero switching in high-switching-cost markets, and the CMA's estimate of £500M additional cost at 5% overcharge provides a concrete scale of the welfare distortion. [fact; source: https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf]

TCO distribution evidence (20-30% licensing, 70-80% lifecycle) is supported by consistent industry practitioner estimates rather than peer-reviewed academic literature. [inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator; https://www.arionerp.com/news/productivity/beyond-the-sticker-price-unpacking-the-true-total-cost-of-ownership-tco-for-erp-systems.html] Post-onboarding costs accumulate as lock-in deepens, so the specific numbers should be treated as indicative rather than precise. [inference; source: https://www.erpresearch.com/en-us/erp-tco-calculator]

Architectural interventions (CNCF cloud-native, open APIs, portable data models) address the technical layer of switching costs but not the commercial layer. [inference; source: https://github.com/cncf/toc/blob/main/DEFINITION.md] Enterprises operating under EU Data Act obligations have a regulatory backstop that reduces commercial exit costs over time, but for enterprises outside EU/UK regulatory scope or using non-cloud enterprise software categories, the architectural investment path is the primary available mechanism. [inference; source: https://digital-strategy.ec.europa.eu/en/policies/data-act]

Preserving exit leverage requires investment before lock-in accumulates across three areas: architectural (open standards, containers, portable data models), contractual (explicit portability clauses, exit-strategy obligations, and data-retrieval rights negotiated at signing), and regulatory (EU Data Act and CMA oversight where jurisdiction applies). Architectural investment reduces the technical cost floor; contractual terms codify the operational preconditions for switching; regulatory rules set a minimum enforceable standard. The most durable posture combines all three because commercial and technical switching costs are partially independent. [inference; source: https://cepr.org/publications/dp5798; https://data-act-law.eu/article/25/; https://github.com/cncf/toc/blob/main/DEFINITION.md]

Network effects (the tendency of platform value to increase with user count) are a complementary mechanism in cloud markets: the Farrell and Klemperer paper explicitly models both switching costs and network effects as sources of installed-base pricing power. In cloud infrastructure, network effects manifest through ecosystem depth (availability of compatible third-party tools and integrations) rather than direct user-to-user value. This item focuses on switching costs because they are the primary mechanism targeted by the EU Data Act and CMA investigation, and because architectural portability strategies directly address switching costs but do not reduce network-effect-driven advantages. Network effects are therefore out of scope for the architectural intervention recommendations but are relevant context for understanding why cloud market concentration may persist even after switching costs are reduced. [inference; source: https://cepr.org/publications/dp5798; https://www.gov.uk/cma-cases/cloud-services-market-investigation]

### Risks, Gaps, and Uncertainties

- ERP TCO figures lack a peer-reviewed empirical study. The 20-30% / 70-80% split and the 25-50% switching cost estimate are drawn from industry practitioner sources; a systematic academic survey would provide stronger evidence.
- CMA cloud findings may not generalise to other enterprise software categories. The CMA investigation was specifically scoped to cloud infrastructure (IaaS and PaaS). Switching cost dynamics for SaaS platforms, horizontal ERP, or enterprise collaboration tools may differ in composition and magnitude.
- EU Data Act effects are not yet observable. The regulation entered application in September 2025; empirical evidence on vendor compliance, actual switching behaviour changes, and any offsetting fee strategies by providers is not yet available.
- Portability investment return on investment (ROI) is not empirically quantified. No study was identified that directly measures the improvement in renewal pricing outcomes achieved by enterprises that invested in architectural portability; this remains a theoretically grounded but empirically unquantified claim.
- The NBER URL in the seeded Sources was incorrect. The seeded URL (https://www.nber.org/papers/w12911) resolves to a different paper by Banerjee, Iyer, and Somanathan. The Farrell and Klemperer paper is accessible at the CEPR (https://cepr.org/publications/dp5798) and at Berkeley (https://eml.berkeley.edu/~farrell/ftp/lockin2.pdf). This error was corrected in the Sources section.

### Open Questions

- Does the upfront-discount-to-lock-in pattern differ between on-premises ERP, cloud SaaS platforms, and cloud infrastructure? Are switching cost compositions consistent across these categories?
- What is the empirically measurable effect of maintaining architectural portability (open APIs, containerisation, portable data models) on negotiated pricing improvements at renewal?
- How will cloud providers respond to EU Data Act switching-fee elimination? Will they offset eliminated egress fees through other pricing mechanisms such as premium API access or proprietary service bundles?
- Should enterprises in non-EU jurisdictions invest in meeting EU Data Act contract standards voluntarily (before any regulatory obligation) as a mechanism for accelerating the reduction of commercial exit costs?

### Output

- Type: knowledge
- Description: This item establishes that the upfront-discount-to-lock-in sequence in enterprise software markets is theoretically predicted by switching-cost economics and empirically confirmed by regulator investigations, and that preserving exit leverage requires a combination of architectural investment (portable data, open standards, container portability), contractual negotiation (explicit portability clauses before lock-in accumulates), and regulatory reliance where available (EU Data Act, UK CMA oversight). [inference; source: https://cepr.org/publications/dp5798; https://www.gov.uk/cma-cases/cloud-services-market-investigation; https://digital-strategy.ec.europa.eu/en/policies/data-act]
- Key sources: https://cepr.org/publications/dp5798, https://www.gov.uk/cma-cases/cloud-services-market-investigation, https://digital-strategy.ec.europa.eu/en/policies/data-act
