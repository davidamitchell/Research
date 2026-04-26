---
review_count: 2
title: "Permission-safe Retrieval-Augmented Generation (RAG) in enterprise information architectures: technical constraints, architectural options, and failure modes at scale"
added: 2026-04-26T06:57:01+00:00
status: completed
priority: high
blocks: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering]
tags: [rag, access-control, information-architecture, embedding-inference, enterprise-ai, regulated-banking, agentic-ai]
started: 2026-04-26T09:52:26+00:00
completed: 2026-04-26T10:00:12+00:00
output: [knowledge]
---

# Permission-safe Retrieval-Augmented Generation (RAG) in enterprise information architectures: technical constraints, architectural options, and failure modes at scale

## Research Question

What are the technical constraints on permission-safe Retrieval-Augmented Generation (RAG) in an enterprise information architecture with incoherent access controls, collaboration groups created ad hoc, document-store Access Control Lists (ACLs) unaudited, file-level sharing at individual discretion, and what are the architectural options (per-user token delegation, per-security-boundary index partitioning, ACL metadata filtering) with their respective failure modes at enterprise scale, including the embedding inference problem and the permission-change propagation problem?

## Scope

**In scope:**
- Why an incoherent enterprise permission model is a technical blocker for RAG, not merely a governance risk
- The embedding inference problem: whether dense vector embedding models leak information about documents the querying user cannot access through retrieval space geometry regardless of query-time ACL filtering, and what evidence exists from the research literature
- The three main architectural options for permission-safe RAG: per-user token delegation, per-security-boundary index partitioning, and ACL metadata filtering
- Failure modes of each architectural option at enterprise scale, including storage and compute implications of per-user ingestion
- The permission-change propagation problem: how promptly and correctly each architecture responds when user permissions change
- Whether correct query-time ACL filtering is necessary but not sufficient for permission safety, and under what conditions
- Applicable enterprise information architectures: Microsoft 365 and SharePoint Online, Azure AI Search, AWS Bedrock Knowledge Bases
- Relevant academic and technical literature on RAG security and enterprise knowledge retrieval

**Out of scope:**
- General RAG architecture without the permission-safety dimension
- Model safety, hallucination, or output quality issues unrelated to access control
- Cross-tenant data isolation (focus is on per-user isolation within a single tenant)
- The dependency ordering problem (covered by the companion synthesis item)

**Constraints:**
- Distinguish between what can be claimed as a published empirical result versus what is an inference from retrieval-space geometry first principles
- Assess architectural options against a Microsoft 365 / SharePoint Online / Azure AI Search context as the primary use case, with AWS Bedrock as a secondary case
- Sources must be assessable for applicability to a regulated financial institution operating at enterprise scale

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html] Prior completed research established that governed knowledge curation is a prerequisite for enterprise Artificial Intelligence (AI) capability in regulated institutions, and that regulatory and standards frameworks require data classification and controlled access before deploying agentic AI.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html] The unresolved question is the technical mechanism by which a weak permission estate stops safe Retrieval-Augmented Generation (RAG) deployment, because a system that cannot represent permissions coherently also cannot prove that retrieval, embeddings, and generated answers stay inside the intended access boundary.

## Approach

1. **Establish the technical blocker claim:** Review the literature and vendor documentation on whether RAG access control implementations can correctly enforce permissions they cannot characterise, that is, whether an incoherent ACL model is a technical precondition failure, not a governance preference.
2. **Investigate the embedding inference problem:** Search the research literature for evidence on whether dense vector embedding models leak information about documents the querying user cannot access through retrieval space geometry; assess whether query-time ACL filtering is sufficient or merely necessary.
3. **Architectural options survey:** For each of the three main options (per-user token delegation, per-security-boundary index partitioning, ACL metadata filtering), describe the mechanism, the security model, the implementation complexity, and the known failure modes.
4. **Scale failure modes:** Assess storage and compute implications of per-user ingestion and per-security-boundary partitioning at enterprise scale (thousands of users, millions of documents, frequent permission changes).
5. **Permission-change propagation:** For each architectural option, assess how the architecture handles permission changes, such as a user added to a group, a document reclassified, or an ACL modified, and what the window of vulnerability is.
6. **Platform-specific assessment:** Assess how Microsoft Azure AI Search (Semantic Ranking, index-level security filtering), AWS Bedrock Knowledge Bases (metadata filtering), and SharePoint Online (permission inheritance) handle each of these problems.
7. **Synthesis:** Produce a decision framework characterising when each architectural option is appropriate and what minimum information architecture preconditions must be satisfied before any RAG deployment is permission-safe.

## Sources

- [x] [Microsoft Azure AI Search - security filtering for multi-tenant search](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search) - Microsoft documentation on security trimming; primary source for the Access Control List (ACL) metadata filtering approach
- [x] [Microsoft Azure AI Search - security and access controls overview](https://learn.microsoft.com/en-us/azure/search/search-security-overview) - overview of index-level and document-level security models in Azure AI Search
- [x] [AWS Bedrock Knowledge Bases - security and access control](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html) - AWS documentation for Bedrock Knowledge Bases permission model
- [x] [SharePoint Online - permission inheritance and sharing model](https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels) - Microsoft documentation on the SharePoint Online permission model that underpins Microsoft 365 (M365) RAG data sources
- [x] https://arxiv.org/abs/2309.11495 - seeded identifier reviewed during investigation; resolved to an unrelated Chain-of-Verification paper and excluded from the evidence set
- [x] https://arxiv.org/abs/2401.05566 - seeded identifier reviewed during investigation; resolved to an unrelated deceptive-alignment paper and excluded from the evidence set
- [x] [Azure AI Search - document-level access overview](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview)
- [x] [Azure AI Search - query-time ACL and role-based access control enforcement](https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement)
- [x] [Azure AI Search - SharePoint ACL ingestion and synchronization](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists)
- [x] [Azure AI Search - remote SharePoint knowledge source](https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote)
- [x] [Microsoft 365 Copilot Retrieval Application Programming Interface (API) overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview)
- [x] [Amazon Bedrock Knowledge Bases - query configuration and metadata filtering](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
- [x] [Amazon Bedrock Retrieve API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html)
- [x] [Amazon Bedrock RetrievalFilter API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html)
- [x] [Amazon Bedrock metadata filtering blog](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-metadata-filtering-to-improve-retrieval-accuracy/)
- [x] [Amazon Bedrock access control with metadata filtering blog](https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/)
- [x] [Text Embeddings Reveal (Almost) As Much As Text](https://arxiv.org/abs/2310.06816)
- [x] [Transferable Embedding Inversion Attack: Uncovering Privacy Risks in Text Embeddings without Model Queries](https://arxiv.org/abs/2406.10280)
- [x] [Mitigating Privacy Risks in Large Language Model (LLM) Embeddings from Embedding Inversion](https://arxiv.org/abs/2411.05034)
- [x] [Is My Data in Your Retrieval Database? Membership Inference Attacks Against Retrieval Augmented Generation](https://arxiv.org/abs/2405.20446)
- [x] [SoK: Privacy Risks and Mitigations in Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2601.03979)

## Related

- [Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)
- [Regulatory and standards preconditions for deployment of agentic AI systems](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)
- [Context compression RAG enterprise knowledge](https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html] **Research question restated:** What technical constraints make permission-safe Retrieval-Augmented Generation (RAG) impossible or fragile when an enterprise permission estate is incoherent, and how do per-user token delegation, per-security-boundary partitioning, and ACL metadata filtering compare on security, scale, and permission-change propagation?
- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] **Scope confirmed:** The investigation is limited to document-level authorization inside a single tenant, with Microsoft 365 and SharePoint Online plus Azure AI Search as the primary case and Amazon Web Services (AWS) Bedrock Knowledge Bases as a secondary comparator; general model safety and cross-tenant isolation stay out of scope.
- [fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2405.20446] **Constraints confirmed:** Published evidence is stronger for embedding inversion and membership inference than for direct proof that ordinary enterprise query-time ACL filtering leaks through vector geometry alone, so the item distinguishes demonstrated attacks from first-principles inference.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html] **Prior work cross-reference:** Prior completed items already established that regulated deployment depends on authoritative knowledge governance, controlled access, and disciplined context assembly; this item extends that work by specifying the access-control architecture required for permission-safe RAG.
- Output format: knowledge, specifically a decision framework for permission-safe RAG in regulated enterprise information architectures.

### §1 Question Decomposition

- **Root question:** Under what conditions can an enterprise RAG system be called permission-safe rather than merely security-trimmed?
- **A. Technical blocker**
  - A1. What do the platform documents require in order to enforce document-level access at query time?
  - A2. Why does an incoherent or partially represented permission model become a technical precondition failure rather than a governance preference?
- **B. Embedding and retrieval leakage**
  - B1. What published evidence shows that dense text embeddings leak source information or support inversion attacks?
  - B2. What published evidence shows that RAG systems leak retrieval-database membership?
  - B3. What remains an inference rather than a demonstrated enterprise attack?
- **C. Architectural options**
  - C1. How does per-user token delegation or live source retrieval work?
  - C2. How does per-security-boundary partitioning work?
  - C3. How does ACL metadata filtering work?
- **D. Failure modes at scale**
  - D1. What breaks when there are unsupported groups, ad hoc file shares, long ACL lists, or stale permission copies?
  - D2. What are the storage and compute implications of per-user or per-boundary duplication?
- **E. Permission-change propagation**
  - E1. How are permission changes reflected in Azure AI Search copied-permission models?
  - E2. How are permission changes reflected in AWS Bedrock metadata-filter models?
  - E3. Which option minimizes the stale-permission window?
- **F. Platform-specific synthesis**
  - F1. What is the strongest Microsoft-path architecture for SharePoint-heavy estates?
  - F2. What is the realistic AWS Bedrock pattern today?
  - F3. What minimum information-architecture preconditions must exist before any copied-index RAG can be called permission-safe?

### §2 Investigation

#### Source access, seed-source triage, and evidence-quality notes

- Access note: [fact; source: https://arxiv.org/abs/2309.11495] seeded arXiv 2309.11495 resolved to Chain-of-Verification, unrelated to embedding privacy, excluded from evidence.
- Access note: [fact; source: https://arxiv.org/abs/2401.05566] seeded arXiv 2401.05566 resolved to a deceptive-alignment paper, unrelated to RAG access control, excluded from evidence.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview] Azure AI Search SharePoint ACL ingestion and native document-level access control are public-preview features without a service-level agreement and are not recommended for production workloads in their present preview form.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] Microsoft documents a separate live-retrieval path through the Copilot Retrieval API and remote SharePoint knowledge sources that keeps data in place and preserves source access controls.

#### A. Why an incoherent permission model is a technical blocker

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search] Azure AI Search security filtering with strings is not authentication or authorization through the security principal; the principal is only a string used in a filter expression that includes or excludes documents.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement] Azure AI Search native document-level access control requires permission metadata to be ingested into filterable fields and requires a user token in `x-ms-query-source-authorization` so the service can construct internal security filters from user identifiers, group memberships, or role-based access control scopes.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] Amazon Bedrock Knowledge Bases retrieval filtering is implemented as metadata predicates such as `equals`, `in`, `listContains`, `andAll`, and `orAll` over document attributes that are added during ingestion.
- [fact; source: https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] SharePoint permissions inherit from site to library to file until inheritance is broken, and sharing a single document with someone who lacks inherited access automatically breaks inheritance on that document.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search; https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] An incoherent enterprise permission model is a technical blocker because every reviewed enforcement path assumes that permissions can be represented either as correct metadata attached to indexed documents or as a live identity passed to the source system; if permissions are ad hoc, unsupported, or unknown, the system cannot compute a reliable allow-set.

#### B. Embedding leakage and retrieval-database leakage

- [fact; source: https://arxiv.org/abs/2310.06816] "Text Embeddings Reveal (Almost) As Much As Text" reports that a multi-step inversion method can recover 92% of 32-token inputs exactly from dense text embeddings and can recover sensitive personal information such as full names from clinical notes.
- [fact; source: https://arxiv.org/abs/2406.10280] "Transferable Embedding Inversion Attack" reports that attackers can infer sensitive information from text embeddings without direct access to the victim embedding model by using a surrogate model in a transfer setting.
- [fact; source: https://arxiv.org/abs/2411.05034] "Mitigating Privacy Risks in Large Language Model (LLM) Embeddings from Embedding Inversion" describes embedding vector databases as vulnerable to inversion attacks and proposes a defense precisely because raw embeddings leak meaningful source information.
- [fact; source: https://arxiv.org/abs/2405.20446] "Is My Data in Your Retrieval Database?" shows that Membership Inference Attacks (MIAs) against RAG systems can determine whether a passage appears in the retrieval database in both black-box and gray-box settings by crafting appropriate prompts.
- [fact; source: https://arxiv.org/abs/2601.03979] "SoK: Privacy Risks and Mitigations in Retrieval-Augmented Generation Systems" surveys 72 sources and treats membership inference and information leakage as recurring privacy risks across the indexing, retrieval, and generation stages of the RAG pipeline.
- [inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2405.20446; https://arxiv.org/abs/2601.03979] Query-time ACL filtering is therefore necessary but not sufficient for permission safety, because correct result trimming does not make embeddings or retrieval databases privacy-neutral assets if an attacker can access vector representations, retrieval outputs, or side channels that reveal membership.
- [inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280] The literature demonstrates inversion and leakage from embeddings themselves, but it does not yet prove that ordinary enterprise users can recover forbidden documents from well-isolated managed-vector services solely through retrieval-space geometry with no access to embeddings or outputs beyond the authorized interface.

#### C. Architectural option 1, per-user token delegation or live source retrieval

- [fact; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview] The Microsoft 365 Copilot Retrieval API grounds generative solutions without replicating, indexing, chunking, or securing data in a separate index, keeps data in place, and upholds the access and governance controls of Microsoft 365.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] A remote SharePoint knowledge source queries SharePoint directly on behalf of the user, requires that the caller identity be recognized in both Azure and Microsoft 365, and does not require a copied search index or connection string.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] The live SharePoint retrieval path preserves source permissions and governance controls, but it is limited by request quotas, file-type support, query-length limits, and the requirement for a Microsoft 365 Copilot license or pay-as-you-go support.
- [inference; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] Per-user token delegation is the safest architecture for a complex Microsoft 365 permission estate because authorization remains at the source of truth and permission-change propagation is effectively immediate at query time rather than dependent on copied metadata refresh.

#### D. Architectural option 2, per-security-boundary partitioning

- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] Per-security-boundary partitioning means building separate indexes or knowledge bases for coarse security domains such as business unit, geography, or classification band, so that no query crosses a boundary and only within-boundary retrieval needs filtering.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement; https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html] This architecture reduces the risk of cross-boundary leakage inside a single retrieval corpus, but it multiplies ingestion pipelines, embedding jobs, synchronization work, and operational configuration as the number of boundaries grows.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement] Partitioning is only operationally credible when the number of boundaries is low and stable, because otherwise duplicated corpora and parallel resync operations produce a different scale problem rather than solving the access-control problem.

#### E. Architectural option 3, ACL metadata filtering and copied permission models

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search] Azure AI Search string-based security trimming requires a security identifier field in the index, recommends the `search.in` function for performance, and relies on the application to pass user or group identifiers as filter strings.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api] Azure AI Search native push-API ACL fields are preview features, support at most 1000 values in `userIds` or `groupIds` fields, and authorize a document if any configured ACL field type matches.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement] Azure query-time ACL enforcement requires both application access to the index and a user token in `x-ms-query-source-authorization`; if ACL evaluation fails, the service returns a 5xx error rather than a partially filtered result set.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html] Amazon Bedrock metadata filtering works by attaching metadata files or attributes during ingestion and then applying explicit filter operators at retrieval time before the system returns source chunks.
- [fact; source: https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/] AWS's own secure-access example validates a doctor's patient authorization outside the knowledge base, then passes patient identifiers as metadata filters into the knowledge base query, which shows that application-side authorization logic remains part of the security model.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html; https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/] ACL metadata filtering is only as correct as the metadata capture, filter injection, and synchronization process, because the retrieval layer enforces the permission representation it is given rather than discovering the full source authorization state on its own.

#### F. Scale and permission-change propagation failure modes

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview] Azure's SharePoint ACL ingestion preview captures ACLs during initial ingestion, requires explicit reindex or ACL resync when permissions change, and warns that the index serves stale ACL data for previously ingested files if no update mechanism is triggered.
- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] Azure's SharePoint ACL preview does not support full SharePoint group fidelity, "Anyone" links, "People in your organization" links, guest users, or Information Management policies, and it recommends remote SharePoint knowledge sources when full SharePoint permissions and sensitivity labels are required.
- [fact; source: https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] SharePoint item-level sharing can break inheritance automatically, which increases the number of unique permission scopes that a copied-index system must represent and refresh.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-metadata-filtering-to-improve-retrieval-accuracy/] Bedrock Knowledge Bases require data-source synchronization to ingest changed content and metadata, and metadata filtering depends on the metadata files or attributes associated with the ingested documents.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] Permission-change propagation in copied-index architectures is a consistency problem, not just a retrieval problem, because every access change must be copied into the retrieval corpus before the system can safely answer queries under the new policy.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] Per-user ingestion is the weakest scaling pattern, because it turns one corpus into many entitlement-specific materializations and makes storage, embeddings, and refresh work grow with the number of users or unique entitlement sets rather than with the corpus alone.

#### G. Platform-specific assessment

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] Microsoft now documents two distinct patterns: copied permission metadata inside Azure AI Search, and live remote retrieval from SharePoint through the Copilot Retrieval API.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] For a SharePoint-heavy enterprise with broken inheritance, unsupported group forms, and ad hoc sharing, the live remote retrieval path is more credible than copied ACL indexing because it avoids partial reimplementation of the SharePoint permission model.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html] AWS Bedrock Knowledge Bases expose an Identity and Access Management (IAM) service-role model for accessing sources and vector stores plus retrieval-time metadata filters, but the reviewed official documentation does not describe native per-user delegated authorization against the source system at query time.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/] In AWS Bedrock today, permission-safe deployment depends on external identity validation, disciplined metadata tagging, and timely reingestion of changed permissions, so it is a stronger fit for stable and well-characterized security boundaries than for chaotic per-file enterprise permissions.

### §3 Reasoning

- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html] The technical blocker claim follows directly from platform mechanics: no reviewed platform can enforce document-level permissions that are absent, stale, unsupported, or never converted into either query-time identity or permission metadata.
- [inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2405.20446] The embedding-inference problem is real enough to matter for architecture because both embeddings and retrieval outputs have demonstrated privacy leakage channels, even though the exact enterprise attack path differs between raw-vector exposure and black-box RAG interaction.
- [inference; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] Permission-change propagation is the decisive differentiator between live delegated retrieval and copied-index retrieval, because live retrieval evaluates source permissions at query time while copied-index retrieval depends on separate refresh workflows that can lag or fail.
- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] Per-security-boundary partitioning and ACL metadata filtering are both valid only when the boundary model is already coherent; neither architecture repairs an incoherent permission estate, and both merely materialize it in a new place.

### §4 Consistency Check

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] Microsoft documentation is internally consistent that copied-index enforcement depends on ingested permission metadata and explicit query-time identity, and that stale or unsupported permission representations remain a real limitation of copied ACL models.
- [fact; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] Microsoft documentation is also internally consistent that the Retrieval API and remote SharePoint knowledge sources keep data in place and preserve source governance rather than copying permissions into a separate index.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html] AWS documentation is consistent that Bedrock Knowledge Bases provide service-role permissions plus metadata filters, not a documented live source-authorization model at retrieval time.
- [fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2405.20446; https://arxiv.org/abs/2601.03979] The literature is consistent that privacy leakage exists at both the embedding layer and the retrieval-database layer, while the strongest unsupported leap would be claiming that every enterprise RAG deployment necessarily leaks unauthorized content through vector geometry alone.

### §5 Depth and Breadth Expansion

- [inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview] **Technical lens:** Copied-index authorization is a distributed-systems consistency problem as much as a security problem, because correctness depends on whether permission state in the retrieval corpus converges quickly enough on the source of truth.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html] **Regulatory lens:** Regulated institutions need explainable access decisions and auditable control ownership, which favors either live source-governed retrieval or coarse stable security boundaries over opaque application-managed per-file filter logic.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-metadata-filtering-to-improve-retrieval-accuracy/; https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search] **Economic lens:** Metadata filtering is cheaper than per-user duplication because it avoids materializing many entitlement-specific corpora, but it transfers the cost into metadata hygiene, synchronization, and incident risk when permissions are wrong.
- [inference; source: https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] **Behavioral lens:** Ad hoc sharing behavior in SharePoint erodes permission coherence faster than central teams can manually document it, so the unsafe state emerges socially before it is noticed architecturally.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

[inference; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] An incoherent permission estate is a technical blocker for permission-safe RAG, because every reviewed architecture needs permissions to be either represented correctly as retrieval metadata or evaluated live at query time, and an ad hoc enterprise file-sharing model defeats both requirements.

[inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2405.20446] Query-time ACL filtering is necessary but not sufficient for permission safety, because published work shows that both dense embeddings and RAG retrieval databases can leak source information or document membership through inversion and black-box interaction.

[inference; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] For Microsoft 365 and SharePoint estates with broken inheritance and unsupported principal types, live delegated retrieval is safer than copied ACL indexing, because it preserves source governance and avoids stale-permission windows that copied-index architectures must manage explicitly.

[inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/; https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api] Per-security-boundary partitioning and ACL metadata filtering remain useful only after the permission model has been rationalized into stable, auditable boundaries; before that point they reproduce the underlying incoherence rather than containing it.

**Key findings:**

1. [high][inference; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search; https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html] An enterprise with incoherent document permissions cannot operate permission-safe RAG, because the reviewed platforms only enforce the permission representation they are given, and none can infer a correct allow-set from ad hoc, unsupported, or unknown sharing state.
2. [high][fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2411.05034] Dense text embeddings are not intrinsically permission-safe artifacts, because published inversion work shows exact or high-fidelity recovery of source text and sensitive attributes from embeddings, including attacks that do not require direct access to the victim embedding model.
3. [high][fact; source: https://arxiv.org/abs/2405.20446; https://arxiv.org/abs/2601.03979] RAG systems can leak whether a document exists in the retrieval database through Membership Inference Attacks, so the vector store and retrieval corpus must be treated as sensitive assets rather than as harmless indexes.
4. [medium][inference; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] Per-user token delegation or live source retrieval is the safest architecture for complex Microsoft 365 estates because it keeps authorization in the source-of-truth system and largely eliminates copied-permission propagation lag.
5. [medium][inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] Copied ACL indexing over SharePoint is fragile when inheritance is frequently broken or when unsupported principal types are common, because the copied model only partially reproduces SharePoint's real permission semantics and can serve stale ACLs until explicit refresh occurs.
6. [medium][inference; source: https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement] Per-security-boundary partitioning is appropriate only when security domains are coarse and stable, because it reduces within-index leakage risk but duplicates ingestion, embedding, synchronization, and operational control planes as boundary count increases.
7. [medium][fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html; https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/] AWS Bedrock Knowledge Bases currently implement secure retrieval through application-managed metadata filters rather than documented live source authorization at query time, so access correctness depends on external identity validation and timely metadata synchronization.
8. [high][fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html] Permission-change propagation is a first-order failure mode in copied-index architectures, because Azure copied ACLs require explicit reindex or resync after source permission changes and Bedrock copied metadata requires source updates plus knowledge-base synchronization before changed permissions can take effect.
9. [medium][inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] In a regulated enterprise, the minimum preconditions for copied-index permission-safe RAG are stable group-based boundaries, complete metadata capture, explicit token validation, rapid permission-resync workflows, and independent evidence that unsupported sharing modes are either absent or excluded.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Incoherent permissions are a technical blocker because enforcement requires correct metadata or live identity. | [Azure security filtering](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search); [Azure document-level access overview](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview); [Bedrock RetrievalFilter API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html) | high | Strong agreement across primary platform docs. |
| [fact] Dense text embeddings leak source information and support inversion attacks. | [arXiv:2310.06816](https://arxiv.org/abs/2310.06816); [arXiv:2406.10280](https://arxiv.org/abs/2406.10280); [arXiv:2411.05034](https://arxiv.org/abs/2411.05034) | high | Peer-reviewed or recent research converges on leakage risk. |
| [fact] RAG databases support membership inference attacks. | [arXiv:2405.20446](https://arxiv.org/abs/2405.20446); [arXiv:2601.03979](https://arxiv.org/abs/2601.03979) | high | One direct attack paper plus a systematic survey. |
| [inference] Live delegated retrieval is safest for complex Microsoft 365 permissions. | [Copilot Retrieval API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview); [Remote SharePoint knowledge source](https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote) | medium | Primary docs explicitly say data stays in place and access controls are preserved, but both sources are from Microsoft. |
| [inference] Copied ACL indexing over SharePoint is fragile under broken inheritance and unsupported principal types. | [SharePoint permission levels](https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels); [Azure SharePoint ACL ingestion](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists) | medium | Product docs show the mechanics and limitations; fragility is the architectural inference. |
| [inference] Per-security-boundary partitioning scales only when boundaries are coarse and stable. | [Azure push API ACL schema](https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api); [Azure query-time ACL enforcement](https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement) | medium | Architectural inference from duplication and synchronization requirements. |
| [fact] Bedrock secure retrieval is metadata-filter based and application-managed. | [Bedrock query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html); [Bedrock Retrieve API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html); [AWS access-control blog](https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/) | medium | AWS docs are clear on filters; the blog shows external authorization logic. |
| [fact] Copied-index permission propagation requires explicit refresh operations. | [Azure SharePoint ACL ingestion](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists); [Azure query-time ACL enforcement](https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement); [Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) | high | Azure states this directly; Bedrock documents data-source sync as the change path. |
| [inference] Regulated copied-index RAG needs stable boundaries, full metadata, explicit token validation, and rapid resync. | [Azure SharePoint ACL ingestion](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists); [Copilot Retrieval API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview); [Bedrock query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) | medium | Derived from the failure modes of the reviewed architectures. |

**Assumptions:**

- [assumption; source: https://learn.microsoft.com/en-us/azure/search/search-security-overview; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html] Managed search and knowledge-base services do not expose raw vectors directly to ordinary end users in the default product path. **Justification:** The reviewed platform documents emphasize managed service endpoints and service-role access rather than raw vector export APIs for end users, so the most realistic leakage path in ordinary deployments is via retrieval behavior or privileged backend access.
- [assumption] Enterprise scale in this item means thousands of users, millions of documents, and regular permission changes. **Justification:** The item's own scope explicitly frames the scale question that way, so scale recommendations are evaluated against that operating assumption.

**Analysis:**

[inference; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview] The core trade-off is between fidelity to the source permission model and the operational convenience of a copied retrieval corpus. Live delegated retrieval maximizes fidelity because authorization stays in the source system, but it reduces platform portability and inherits source-specific limits. Copied-index architectures maximize control over search behavior and latency, but they convert authorization into a data-synchronization problem that the institution must now operate correctly.

[inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446] The embedding literature and the RAG membership-inference literature shift the burden of proof. It is no longer enough to say that unauthorized chunks are filtered out at query time, because the retrieval corpus itself is a sensitive representation whose leakage properties matter to the architecture decision.

[inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] The correct sequencing is therefore: rationalize permissions, collapse entitlements into stable group-based boundaries where possible, decide whether live retrieval is needed for full-fidelity estates, and only then build copied-index RAG where the permission model can actually be represented and refreshed reliably.

**Risks, gaps, uncertainties:**

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api] Azure's strongest copied-permission features are still public preview, so production-readiness evidence is weaker than the design logic.
- [fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280] The literature proves embedding inversion and transfer leakage, but it does not yet publish a direct end-user enterprise attack showing unauthorized document recovery from a well-isolated managed vector service with no vector access.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] The reviewed AWS documentation does not describe a native live source-authorization model for Bedrock Knowledge Bases, so the comparison of Bedrock against delegated-retrieval architectures is limited to what the public docs state.
- [inference; source: https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] SharePoint estates with heavy use of unsupported link types or unresolved SharePoint groups could be even harder to represent safely in copied-index RAG than the public preview limitations already suggest.

**Open questions:**

1. What empirical latency and recall trade-offs emerge when a Microsoft 365 estate moves from copied ACL indexing to live Copilot Retrieval API grounding for the same workload?
2. Can a regulated enterprise define a practical maximum stale-permission window for copied-index RAG, and what controls are needed to prove compliance with that window?
3. What attack results appear when modern enterprise vector services are tested for unauthorized document recovery without direct vector export, rather than for generic inversion under lab access?
4. At what boundary cardinality does per-security-boundary partitioning become more costly than live delegated retrieval in a large regulated enterprise?

### §7 Recursive Review

- Metadata: Prior-work check completed against three related completed items with URL-backed links.
- Metadata: The seeded arXiv identifiers were checked explicitly and excluded from evidence because they were off-topic.
- Metadata: Sections 0-6 distinguish published facts from architectural inferences and label assumptions separately.
- Metadata: The main unresolved uncertainty is not whether embeddings and RAG stores can leak, but how directly those attack paths map into ordinary managed-enterprise deployments without privileged access.
- Metadata: Verdict: PASS.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

[inference; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] An incoherent permission estate is a technical blocker for permission-safe Retrieval-Augmented Generation (RAG), because every reviewed architecture needs permissions to be either represented correctly as retrieval metadata or evaluated live at query time, and ad hoc enterprise sharing defeats both requirements.

[inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2405.20446] Query-time ACL filtering is necessary but not sufficient for permission safety, because published work shows that dense embeddings and RAG retrieval databases can leak source information or document membership through inversion and black-box interaction.

[inference; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] For Microsoft 365 and SharePoint estates with broken inheritance and unsupported principal types, live delegated retrieval is safer than copied ACL indexing because it preserves source governance and avoids stale-permission windows that copied-index architectures must manage explicitly.

[inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/; https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api] Per-security-boundary partitioning and ACL metadata filtering remain useful only after the permission model has been rationalized into stable, auditable boundaries; before that point they reproduce the underlying incoherence rather than containing it.

### Key Findings

1. [high][inference; source: https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search; https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html] An enterprise with incoherent document permissions cannot operate permission-safe RAG, because the reviewed platforms only enforce the permission representation they are given, and none can infer a correct allow-set from ad hoc, unsupported, or unknown sharing state.
2. [high][fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280; https://arxiv.org/abs/2411.05034] Dense text embeddings are not intrinsically permission-safe artifacts, because published inversion work shows exact or high-fidelity recovery of source text and sensitive attributes from embeddings, including attacks that do not require direct access to the victim embedding model.
3. [high][fact; source: https://arxiv.org/abs/2405.20446; https://arxiv.org/abs/2601.03979] RAG systems can leak whether a document exists in the retrieval database through Membership Inference Attacks, so the vector store and retrieval corpus must be treated as sensitive assets rather than as harmless indexes.
4. [medium][inference; source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote] Per-user token delegation or live source retrieval is the safest architecture for complex Microsoft 365 estates because it keeps authorization in the source-of-truth system and largely eliminates copied-permission propagation lag.
5. [medium][inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels] Copied ACL indexing over SharePoint is fragile when inheritance is frequently broken or when unsupported principal types are common, because the copied model only partially reproduces SharePoint's real permission semantics and can serve stale ACLs until explicit refresh occurs.
6. [medium][inference; source: https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement] Per-security-boundary partitioning is appropriate only when security domains are coarse and stable, because it reduces within-index leakage risk but duplicates ingestion, embedding, synchronization, and operational control planes as boundary count increases.
7. [medium][fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html; https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/] AWS Bedrock Knowledge Bases currently implement secure retrieval through application-managed metadata filters rather than documented live source authorization at query time, so access correctness depends on external identity validation and timely metadata synchronization.
8. [high][fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement; https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html] Permission-change propagation is a first-order failure mode in copied-index architectures, because Azure copied ACLs require explicit reindex or resync after source permission changes and Bedrock copied metadata requires source updates plus knowledge-base synchronization before changed permissions can take effect.
9. [medium][inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] In a regulated enterprise, the minimum preconditions for copied-index permission-safe RAG are stable group-based boundaries, complete metadata capture, explicit token validation, rapid permission-resync workflows, and independent evidence that unsupported sharing modes are either absent or excluded.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Incoherent permissions are a technical blocker because enforcement requires correct metadata or live identity. | [Azure security filtering](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search); [Azure document-level access overview](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview); [Bedrock RetrievalFilter API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html) | high | Strong agreement across primary platform docs. |
| [fact] Dense text embeddings leak source information and support inversion attacks. | [arXiv:2310.06816](https://arxiv.org/abs/2310.06816); [arXiv:2406.10280](https://arxiv.org/abs/2406.10280); [arXiv:2411.05034](https://arxiv.org/abs/2411.05034) | high | Peer-reviewed or recent research converges on leakage risk. |
| [fact] RAG databases support membership inference attacks. | [arXiv:2405.20446](https://arxiv.org/abs/2405.20446); [arXiv:2601.03979](https://arxiv.org/abs/2601.03979) | high | One direct attack paper plus a systematic survey. |
| [inference] Live delegated retrieval is safest for complex Microsoft 365 permissions. | [Copilot Retrieval API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview); [Remote SharePoint knowledge source](https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-how-to-sharepoint-remote) | medium | Primary docs explicitly say data stays in place and access controls are preserved, but both sources are from Microsoft. |
| [inference] Copied ACL indexing over SharePoint is fragile under broken inheritance and unsupported principal types. | [SharePoint permission levels](https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels); [Azure SharePoint ACL ingestion](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists) | medium | Product docs show the mechanics and limitations; fragility is the architectural inference. |
| [inference] Per-security-boundary partitioning scales only when boundaries are coarse and stable. | [Azure push API ACL schema](https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api); [Azure query-time ACL enforcement](https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement) | medium | Architectural inference from duplication and synchronization requirements. |
| [fact] Bedrock secure retrieval is metadata-filter based and application-managed. | [Bedrock query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html); [Bedrock Retrieve API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html); [AWS access-control blog](https://aws.amazon.com/blogs/machine-learning/access-control-for-vector-stores-using-metadata-filtering-with-knowledge-bases-for-amazon-bedrock/) | medium | AWS docs are clear on filters; the blog shows external authorization logic. |
| [fact] Copied-index permission propagation requires explicit refresh operations. | [Azure SharePoint ACL ingestion](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists); [Azure query-time ACL enforcement](https://learn.microsoft.com/en-us/azure/search/search-query-access-control-rbac-enforcement); [Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) | high | Azure states this directly; Bedrock documents data-source sync as the change path. |
| [inference] Regulated copied-index RAG needs stable boundaries, full metadata, explicit token validation, and rapid resync. | [Azure SharePoint ACL ingestion](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists); [Copilot Retrieval API overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview); [Bedrock query configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) | medium | Derived from the failure modes of the reviewed architectures. |

### Assumptions

- [assumption; source: https://learn.microsoft.com/en-us/azure/search/search-security-overview; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html] **Assumption:** Managed search and knowledge-base services do not expose raw vectors directly to ordinary end users in the default product path. **Justification:** The reviewed platform documents emphasize managed service endpoints and service-role access rather than raw vector export APIs for end users, so the most realistic leakage path in ordinary deployments is via retrieval behavior or privileged backend access.
- [assumption] **Assumption:** Enterprise scale in this item means thousands of users, millions of documents, and regular permission changes. **Justification:** The item's own scope explicitly frames the scale question that way, so scale recommendations are evaluated against that operating assumption.

### Analysis

[inference; source: https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview; https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview] The core trade-off is between fidelity to the source permission model and the operational convenience of a copied retrieval corpus. Live delegated retrieval maximizes fidelity because authorization stays in the source system, but it reduces platform portability and inherits source-specific limits. Copied-index architectures maximize control over search behavior and latency, but they convert authorization into a data-synchronization problem that the institution must now operate correctly.

[inference; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2405.20446] The embedding literature and the RAG membership-inference literature shift the burden of proof. It is no longer enough to say that unauthorized chunks are filtered out at query time, because the retrieval corpus itself is a sensitive representation whose leakage properties matter to the architecture decision.

[inference; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] The correct sequencing is therefore: rationalize permissions, collapse entitlements into stable group-based boundaries where possible, decide whether live retrieval is needed for full-fidelity estates, and only then build copied-index RAG where the permission model can actually be represented and refreshed reliably.

### Risks, Gaps, and Uncertainties

- [fact; source: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists; https://learn.microsoft.com/en-us/azure/search/search-index-access-control-lists-and-rbac-push-api] Azure's strongest copied-permission features are still public preview, so production-readiness evidence is weaker than the design logic.
- [fact; source: https://arxiv.org/abs/2310.06816; https://arxiv.org/abs/2406.10280] The literature proves embedding inversion and transfer leakage, but it does not yet publish a direct end-user enterprise attack showing unauthorized document recovery from a well-isolated managed vector service with no vector access.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html; https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html] The reviewed AWS documentation does not describe a native live source-authorization model for Bedrock Knowledge Bases, so the comparison of Bedrock against delegated-retrieval architectures is limited to what the public docs state.
- [inference; source: https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels; https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists] SharePoint estates with heavy use of unsupported link types or unresolved SharePoint groups could be even harder to represent safely in copied-index RAG than the public preview limitations already suggest.

### Open Questions

1. What empirical latency and recall trade-offs emerge when a Microsoft 365 estate moves from copied ACL indexing to live Copilot Retrieval API grounding for the same workload?
2. Can a regulated enterprise define a practical maximum stale-permission window for copied-index RAG, and what controls are needed to prove compliance with that window?
3. What attack results appear when modern enterprise vector services are tested for unauthorized document recovery without direct vector export, rather than for generic inversion under lab access?
4. At what boundary cardinality does per-security-boundary partitioning become more costly than live delegated retrieval in a large regulated enterprise?

---

## Output

*(Filled in on completion: what was produced as a result of this research?)* 

- Type: knowledge
- Description: Decision framework for when a regulated enterprise can and cannot treat Retrieval-Augmented Generation as permission-safe, with platform-specific failure modes for Azure AI Search, SharePoint Online, and AWS Bedrock Knowledge Bases.
- Links:
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview
  - https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists
  - https://arxiv.org/abs/2405.20446
