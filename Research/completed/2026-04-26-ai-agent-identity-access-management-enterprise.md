---
review_count: 2
title: "What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?"
added: 2026-04-26T10:11:11+00:00
status: completed
priority: high
blocks: [2026-04-26-ai-lowcode-governance-enforcement-architecture, 2026-04-26-ai-lowcode-observability-telemetry-governance, 2026-04-26-ai-agent-control-plane-architecture-enterprise]
tags: [identity, access-management, machine-identity, ai-agents, low-code, credential-management, enterprise-iam, delegation, attribution]
started: 2026-04-26T10:55:16+00:00
completed: 2026-04-26T18:14:01+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?

## Research Question

What identity and access management (IAM) model is required for non-human actors, AI agents and low-code artefacts, operating within enterprise systems, specifically: how should machine identities be assigned and managed; what delegation models (user-initiated vs autonomous execution) are appropriate; how should permission inheritance, credential management, and end-to-end attribution of actions across users, agents, and downstream systems be handled?

## Scope

**In scope:**
- Machine identity standards applicable to AI agents and low-code automation artefacts (workload identity, service accounts, managed identities)
- Delegation models: user-initiated delegation (agent acts on behalf of user), system-level delegation (agent acts autonomously within a defined permission scope), and the conditions under which each is appropriate
- Permission inheritance: how an agent or low-code artefact should inherit, constrain, or exceed the permissions of the initiating user or system context
- Credential management: lifecycle management of credentials held by non-human actors (rotation, revocation, scope limitation, secret management)
- End-to-end attribution: how actions taken by agents or artefacts can be attributed to the initiating user, the artefact, and any intermediate systems for audit and accountability purposes
- Applicability to major enterprise identity platforms (Microsoft Entra, Amazon Web Services (AWS) Identity and Access Management (IAM), Google Cloud Identity)
- Relevant standards (OAuth 2.0 token delegation, OpenID Connect, Secure Production Identity Framework For Everyone (SPIFFE), SPIFFE Runtime Environment (SPIRE), National Institute of Standards and Technology (NIST) Special Publication (SP) 800-63)

**Out of scope:**
- General enterprise IAM architecture for human users
- The enforcement mechanisms that consume identity (covered by Q3)
- Observability of identity-attributed actions (covered by Q4)
- Vendor-specific limitations on machine identity (covered by Q11)

**Constraints:**
- Must address the distinction between identity (who an actor is) and authorization (what it may do)
- Must be grounded in existing standards rather than proposing novel identity architectures
- Sources must be assessable for applicability to a regulated enterprise with existing identity infrastructure

## Context

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Prior completed repository work already showed that regulated low-code agent deployment fails when access is overshared, permission boundaries are incoherent, or central governance cannot attribute action to an accountable actor, so this item focuses on the identity substrate those other controls depend on.

Cross-references:
- Q3: `2026-04-26-ai-lowcode-governance-enforcement-architecture`
- Q4: `2026-04-26-ai-lowcode-observability-telemetry-governance`
- Q1: `2026-04-26-ai-lowcode-decision-rights-accountability-liability`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`

## Approach

1. **Survey machine identity standards:** Review National Institute of Standards and Technology (NIST) Special Publication (SP) 800-63, OAuth 2.0 Token Exchange, Request for Comments (RFC) 8693, SPIFFE/SPIRE workload identity, and Microsoft Entra workload identities for their applicability to AI agent and low-code artefact identity.
2. **Delegation model analysis:** Characterise user-initiated delegation (agent acts within user's permission scope via token exchange) vs autonomous execution (agent operates under its own identity and permission scope), assess when each model is appropriate, what risks each introduces, and how each should be authorised.
3. **Permission inheritance and least privilege:** Assess how permission scoping should work for agents (should an agent be able to do everything the delegating user can, or only a defined subset?) and what mechanisms enforce least-privilege for non-human actors.
4. **Credential lifecycle:** Review credential management best practices for non-human actors, rotation frequency, revocation mechanisms, secret store integration, and the risks of long-lived credentials held by autonomous agents.
5. **Attribution chain:** Assess how a full attribution chain can be maintained from the initiating user through the agent to downstream systems, what identity claims need to propagate, and at what points the chain is typically broken in practice.
6. **Enterprise platform assessment:** Assess how Microsoft Entra, AWS IAM, and Google Cloud Identity handle machine identity for AI workloads.
7. **Synthesis:** Produce a machine identity and delegation model suitable for enterprise AI governance, with explicit decision criteria for when each pattern applies.

## Sources

- [x] [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-63-3 Digital Identity Guidelines landing page](https://pages.nist.gov/800-63-3/) - seeded source; confirms the suite and that SP 800-63-3 is now superseded by SP 800-63-4.
- [x] [NIST SP 800-63C Federation and Assertions](https://pages.nist.gov/800-63-3/sp800-63c.html) - primary NIST source for federation and assertion semantics; used to test applicability to non-human identity.
- [x] [Request for Comments (RFC) 8693, OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693) - primary standard for delegation vs impersonation semantics and actor-aware token exchange.
- [x] [SPIFFE and SPIRE overview](https://spiffe.io/) - primary workload-identity source for strongly attested cryptographic identities in distributed systems.
- [x] [Microsoft Entra workload identities overview](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview) - primary Microsoft source for non-human identity types and lifecycle concerns.
- [x] [Managed identities for Azure resources overview](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) - primary Microsoft source for secretless Azure workload identity.
- [x] [Microsoft Entra workload identity federation considerations](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations) - primary source for issuer and subject matching, propagation delay, and federation constraints.
- [x] [Service principal sign-in logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins) - primary Microsoft source for non-user sign-in attribution.
- [x] [Microsoft Entra workload identity risk](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk) - primary Microsoft source for leaked-credential and anomalous-sign-in detection and remediation.
- [x] [AWS IAM Roles Anywhere introduction](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) - seeded source; primary AWS source for external workload identity and temporary credentials outside AWS.
- [x] [Temporary security credentials in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) - primary AWS source for short-lived credentials, delegation, and federation.
- [x] [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) - primary AWS source for SourceIdentity and chained attribution.
- [x] [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) - primary AWS source for assumed-role session attribution and how temporary credentials were obtained.
- [x] [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) - primary architecture source for per-session least privilege, subject composition, and identity-driven access decisions.
- [x] [Google Cloud service account overview](https://cloud.google.com/iam/docs/service-account-overview) - primary Google source for service accounts as non-human identities and short-lived vs key-based credentials.
- [x] [Google Cloud Workload Identity Federation overview](https://cloud.google.com/iam/docs/workload-identity-federation) - primary Google source for external workload federation, attribute mapping, and short-lived access.
- [x] [Google Cloud service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) - primary Google source for short-lived impersonation and dual-identity audit behavior.
- [x] [Best practices for using service accounts securely](https://cloud.google.com/iam/docs/best-practices-service-accounts) - primary Google source for least privilege, single-purpose identities, serviceAccountDelegationInfo, and key avoidance.

## Related

- [Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html)
- [Permission-safe Retrieval-Augmented Generation (RAG) in enterprise information architectures](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)
- [What control-plane architecture is required to manage AI agents and low-code systems](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview] **Research question restated:** What identity and access model should enterprises use for AI agents and low-code artefacts so that non-human actors have first-class machine identities, user-initiated work uses accountable delegation, autonomous work uses bounded non-human permissions, credentials stay short-lived where possible, and downstream actions remain attributable end to end?
- [fact; source: https://pages.nist.gov/800-63-3/sp800-63c.html; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation] **Scope confirmed:** The investigation covers standards and platform patterns for machine identity, delegation, permission scoping, credential lifecycle, and attribution across Microsoft, Amazon Web Services (AWS), and Google Cloud.
- [fact; source: https://pages.nist.gov/800-63-3/; https://pages.nist.gov/800-63-3/sp800-63c.html] **Constraint note:** the seeded National Institute of Standards and Technology (NIST) Special Publication (SP) 800-63-3 landing page now states that the suite was superseded by SP 800-63-4 in August 2025, so SP 800-63C was used mainly to test how far subscriber federation concepts transfer to non-human actors.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] **Prior work cross-reference:** prior completed items already established that overshared permissions, weak access-control representation, and missing central control planes are current or foreseeable control failures under agentic operation, so this item narrows the problem to the identity model that must exist before those controls can work.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final] **Output format confirmed:** knowledge, specifically a machine identity and delegation model with platform-specific decision criteria.

### §1 Question Decomposition

- **Root question:** What machine identity, delegation, credential, and attribution model lets enterprises treat AI agents and low-code artefacts as accountable non-human actors rather than as borrowed human sessions or shared technical accounts?
- **A. Standards applicability**
  - A1. Which standards directly address non-human workload identity?
  - A2. Which standards are useful only as adjacent federation or access-control patterns?
- **B. Delegation semantics**
  - B1. What is the difference between delegation and impersonation?
  - B2. When should a user-initiated agent preserve both the user and the actor identity?
  - B3. When should an autonomous agent run only under its own identity?
- **C. Permission inheritance**
  - C1. Should an agent ever inherit the delegating user's full permission set?
  - C2. Which platform mechanisms let enterprises constrain the effective permission set below both the user and the agent maximum?
- **D. Credential lifecycle**
  - D1. Which vendor patterns eliminate long-lived secrets?
  - D2. What lifecycle controls still matter when secrets cannot be eliminated?
- **E. Attribution**
  - E1. Which logs or token claims preserve the initiator, the acting machine identity, and the downstream session?
  - E2. Where does attribution break when keys, shared accounts, or attached identities are used?
- **F. Platform synthesis**
  - F1. What is the Microsoft pattern?
  - F2. What is the AWS pattern?
  - F3. What is the Google Cloud pattern?
  - F4. What common enterprise model emerges across all three?

### §2 Investigation

#### Source access and applicability notes

- [fact; source: https://pages.nist.gov/800-63-3/] Access note: the seeded NIST SP 800-63-3 page is accessible, but it now points to SP 800-63-4 as the current suite; the research therefore used SP 800-63C for federation detail and did not treat SP 800-63-3 as the current workload-identity baseline.
- [inference; source: https://pages.nist.gov/800-63-3/sp800-63c.html; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://cloud.google.com/iam/docs/service-account-overview] NIST SP 800-63C is useful for federation and assertion structure, but it is framed around subscribers, identity providers, and relying parties, so it is not a direct machine-identity lifecycle standard in the way the cloud workload-identity documents are.
- [assumption; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://cloud.google.com/iam/docs/service-account-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html] Low-code artefacts that call downstream systems are treated as software workloads for identity-design purposes. **Justification:** the vendor identity models distinguish humans from non-human applications, service principals, service accounts, and external workloads, and low-code artefacts that execute Application Programming Interface (API) calls or write records fit that operational class.

#### A. Which standards and platform patterns directly fit non-human identity

- [fact; source: https://pages.nist.gov/800-63-3/sp800-63c.html] NIST SP 800-63C defines federation as assertions from an identity provider to a relying party about a subscriber and focuses on federated identity systems for subscribers rather than on non-human workload identity lifecycle.
- [fact; source: https://csrc.nist.gov/pubs/sp/800/207/final] NIST SP 800-207 says authorized subjects can include the combination of user, application or service, and device, and says access to enterprise resources should be granted on a per-session basis with the least privileges needed to complete the task.
- [fact; source: https://spiffe.io/] Secure Production Identity Framework For Everyone (SPIFFE) and SPIFFE Runtime Environment (SPIRE) describe a uniform identity control plane that provides strongly attested cryptographic identities to workloads across heterogeneous infrastructure and explicitly position workload identity as a distributed-systems problem rather than a human-login problem.
- [fact; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview] Microsoft Entra defines workload identities as applications, service principals, and managed identities, distinguishes them from human identities, and says managed identities eliminate the need for developers to manage credentials.
- [fact; source: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html] AWS uses IAM roles, AWS Security Token Service (STS) temporary credentials, and IAM Roles Anywhere to let workloads obtain temporary permissions without long-term credentials.
- [fact; source: https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-overview] Google Cloud uses service accounts and Workload Identity Federation so workloads can authenticate either directly as federated principals or by impersonating service accounts without using service account keys.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation] The standards and vendor evidence converge on a first principle: AI agents and low-code artefacts should be represented as separate machine identities, not as durable extensions of human accounts.

#### B. Delegation and impersonation semantics

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] Request for Comments (RFC) 8693 says impersonation makes principal A indistinguishable from principal B within the rights context of the token, while delegation preserves A as a distinct actor representing B.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 also defines `subject_token` for the party on behalf of whom a request is made, `actor_token` for the acting party, and the `act` claim for representing delegation chains in JSON Web Tokens (JWTs).
- [fact; source: https://cloud.google.com/iam/docs/service-account-impersonation] Google Cloud service account impersonation always involves two identities, the authenticated principal and the service account being impersonated, and typically uses short-lived credentials rather than long-lived keys.
- [fact; source: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html] AWS STS lets callers obtain temporary credentials for delegation scenarios and preserve a SourceIdentity value that remains fixed across the role session and persists through role chaining.
- [fact; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations] Microsoft Entra workload identity federation validates exact `issuer` and `subject` matches from the external token before issuing an access token, which means delegated or federated agent access is anchored to a specific external workload identity rather than a generic shared broker.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] User-initiated agent activity should default to delegation semantics that preserve both the user and the acting machine identity, because that model best preserves accountability, policy evaluation, and incident reconstruction.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final] Autonomous execution should not rely on retained user delegation tokens except for narrowly bounded continuation windows, because a scheduled or event-driven agent is no longer acting under an actively supervised user session and should be re-authorized under its own machine identity.

#### C. Permission inheritance and least privilege

- [fact; source: https://csrc.nist.gov/pubs/sp/800/207/final] NIST SP 800-207 requires minimum privileges per session and treats authorization as a dynamic decision over subject and device state rather than as a one-time broad grant.
- [fact; source: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html] AWS IAM Roles Anywhere profiles can apply session policies that limit the permissions in the returned session, and temporary credentials derived through STS cannot outlive their configured short lifetime.
- [fact; source: https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/best-practices-service-accounts] Google Cloud Workload Identity Federation supports direct resource access for federated principals, principal sets based on groups or attributes, and attribute conditions that restrict which identities can authenticate and help avoid confused deputy problems.
- [fact; source: https://cloud.google.com/iam/docs/best-practices-service-accounts] Google advises creating single-purpose service accounts, avoiding default shared service accounts, and limiting service-account privileges because shared or overly privileged service accounts make activity harder to trace and increase escalation risk.
- [fact; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations] Microsoft Entra federated identity credentials depend on exact issuer and subject values and support only up to 20 federated identity credentials per application or user-assigned managed identity, which pushes administrators toward explicit workload registration instead of unconstrained inheritance.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/best-practices-service-accounts] The effective permission set for a user-initiated agent should be the intersection of user entitlement, agent entitlement, and resource policy, not the full union of what either party could do independently.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Allowing an agent to inherit the delegating user's full permission estate by default recreates the exact machine-speed amplification problem already established in the related access-control item.

#### D. Credential lifecycle and secret handling

- [fact; source: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview] Microsoft says managed identities replace secrets such as access keys or passwords, and that credentials for managed identities are not accessible to developers.
- [fact; source: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html] AWS says temporary security credentials are short-term, generated dynamically, and preferable because applications do not need embedded long-term AWS credentials.
- [fact; source: https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-impersonation] Google says Workload Identity Federation eliminates the maintenance and security burden of service account keys, and that short-lived impersonation credentials create less risk than long-lived service account keys.
- [fact; source: https://cloud.google.com/iam/docs/best-practices-service-accounts] Google explicitly recommends avoiding service account keys whenever possible, managing service accounts with the lifecycle of their associated workload, disabling unused accounts before deleting them, and using single-purpose service accounts.
- [fact; source: https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] Microsoft Entra workload identity risk detects leaked credentials, suspicious sign-ins, and anomalous service-principal activity, and recommends adding a new credential, removing compromised credentials, and rotating Azure Key Vault secrets the service principal can access.
- [inference; source: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/best-practices-service-accounts] The correct enterprise default is therefore secretless or ephemeral credentialing, and any fallback to stored secrets should be treated as an exception path that requires inventory, vaulting, rotation, revocation, and owner review.

#### E. End-to-end attribution and audit chain

- [fact; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview] Microsoft Entra sign-in logs capture non-user sign-ins by applications and service principals, record authentication details such as credential type and target resource, and Microsoft also exposes sign-in activity for managed identities.
- [fact; source: https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] Microsoft Entra workload identity risk uses sign-in behavior and offline compromise indicators such as leaked credentials, suspicious API traffic, and anomalous service-principal activity, which makes machine identity an actively monitored security object rather than a passive technical account.
- [fact; source: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html] AWS CloudTrail records assumed-role sessions as `AssumedRole`, shows the role session context and session issuer, and can preserve immutable SourceIdentity values across role chaining so administrators can determine who or what performed actions with shared roles.
- [fact; source: https://cloud.google.com/iam/docs/service-account-impersonation; https://cloud.google.com/iam/docs/best-practices-service-accounts; https://cloud.google.com/iam/docs/workload-identity-federation] Google Cloud says most audit logs for service account impersonation include both the authenticated principal and the impersonated service account, and Google documents `serviceAccountDelegationInfo` and `principalSubject` as the fields that help interpret impersonation and federated identity chains.
- [fact; source: https://cloud.google.com/iam/docs/service-account-impersonation] Google also says attached service accounts and service account keys involve only the service account identity in many audit paths, which means the initiating human or upstream workload can disappear from the audit trail.
- [inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] End-to-end attribution requires four distinct surfaces to be logged: the initiating principal, the machine identity that executed the action, the credential-exchange or impersonation event, and the downstream resource action under the resulting session.
- [inference; source: https://cloud.google.com/iam/docs/service-account-impersonation; https://cloud.google.com/iam/docs/best-practices-service-accounts; https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html] Shared service accounts, service account keys, and opaque attached identities break non-repudiation because downstream logs can no longer distinguish which human or upstream workload actually caused the action.

#### F. Enterprise platform synthesis

- [fact; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations] Microsoft Entra's pattern is explicit workload registration through applications, service principals, managed identities, and federated identity credentials, with exact issuer-subject matching and sign-in or risk telemetry for those identities.
- [fact; source: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html] AWS's pattern is explicit role assumption with temporary credentials, optional SourceIdentity for attribution, and optional session policies to narrow the resulting permissions, with IAM Roles Anywhere extending the same model to workloads outside AWS.
- [fact; source: https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-impersonation; https://cloud.google.com/iam/docs/best-practices-service-accounts] Google Cloud's pattern is to prefer Workload Identity Federation or attached identities over service account keys, use service account impersonation for controlled short-lived elevation, and limit blast radius through single-purpose service accounts and attribute-scoped principals.
- [inference; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] All three platforms converge on the same enterprise answer even though their nouns differ: separate non-human identities, short-lived credentials, explicit trust anchors or issuer bindings, scoped authorization, and auditable delegation or impersonation events.

### §3 Reasoning

- [fact; source: https://pages.nist.gov/800-63-3/sp800-63c.html] The NIST SP 800-63C evidence is narrow but important because it shows that subscriber federation and assertion exchange are established patterns, while also showing that the document's primary object is a subscriber rather than a workload.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview] Because NIST SP 800-207, SPIFFE/SPIRE, and the platform workload-identity documents all treat software actors as first-class subjects, the identity model for agents should start from workload identity rather than from human identity proofing.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] Because delegation preserves actor identity and impersonation collapses it, delegation is the stronger default for user-initiated work whenever accountability matters and should therefore be preferred unless a platform requires impersonation.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://cloud.google.com/iam/docs/best-practices-service-accounts; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html] Least privilege for non-human actors is not satisfied by assigning the agent a broad technical account and then relying on business process, because the access decision must be bounded inside the token, role, or service-account grant itself.
- [inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html; https://cloud.google.com/iam/docs/service-account-impersonation] Attribution only survives if enterprises create separate identities for separate actors and then log the exchange from one actor to the next, so identity design and audit design are inseparable.

### §4 Consistency Check

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693; https://cloud.google.com/iam/docs/service-account-impersonation] No direct contradiction was found between the standards and the platform documents: the main tension is that platforms still support impersonation even though delegation preserves accountability better.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] That tension is resolved by treating impersonation as a controlled mechanism for short-lived elevation or platform interoperability and by requiring compensating audit controls whenever delegation semantics cannot be preserved directly in the token.
- [fact; source: https://pages.nist.gov/800-63-3/sp800-63c.html; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview] The standards evidence also stays internally consistent if SP 800-63C is interpreted as an adjacent federation reference rather than as a workload-identity prescription.

### §5 Depth and Breadth Expansion

- [inference; source: https://cloud.google.com/iam/docs/workload-identity-federation; https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html] **Technical lens:** the same control pattern appears across platforms, namely explicit trust establishment, exact subject or certificate binding, and short-lived token exchange, which means enterprise policy should be written in platform-neutral terms and then translated into vendor-specific configuration.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] **Risk lens:** machine identity is a prerequisite control because permission amplification and permission-safe knowledge access both depend on whether the system can represent the actor precisely and narrow the access boundary at execution time.
- [inference; source: https://cloud.google.com/iam/docs/best-practices-service-accounts; https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview] **Operational lens:** single-purpose machine identities and explicit lifecycle ownership increase administrative overhead up front, but they reduce incident response ambiguity, privilege drift, and decommissioning risk later.
- [inference; source: https://cloud.google.com/iam/docs/best-practices-service-accounts; https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] **Behavioral lens:** default service accounts, shared technical accounts, and long-lived credentials persist mainly because they are convenient, which means governance has to make the secure path easier and more automatable than the unsafe one rather than merely forbidding bad patterns in policy text.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Enterprises need a first-class machine identity model for AI agents and low-code artefacts in which every consequential non-human actor has its own identity, user-initiated work uses bounded delegation where possible, autonomous work runs under the agent's own scoped identity, and credentials are short-lived by default.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 makes the core delegation rule explicit: delegation preserves both the subject and the acting party, while impersonation collapses the acting party into the subject within the token context.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/best-practices-service-accounts] That means an agent should not inherit a user's full permission estate by default, because least privilege for non-human actors must be enforced through intersected scope, session policy, or single-purpose service-account grants.
- [inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] Attribution survives only when the design records the initiator, the machine identity, the credential exchange, and the downstream action as linked but distinct events.

**Key findings:**

1. **High confidence.** [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation] An enterprise AI identity model should assign every consequential agent or low-code artefact its own machine identity, because the standards and vendor patterns all treat software workloads as first-class subjects rather than as invisible extensions of human users.
2. **High confidence.** [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] User-initiated agent actions are better governed through delegation semantics than impersonation, because RFC 8693 preserves both the original subject and the acting party, while AWS and Google both expose more useful audit chains when the acting identity remains distinguishable.
3. **High confidence.** [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final] Autonomous or scheduled agent work should run under the agent's own pre-authorized identity instead of under a retained user delegation token, because the user is no longer actively supervising the session and the agent therefore requires an independently bounded authorization decision.
4. **High confidence.** [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation] The effective permission set for a delegated agent should be the intersection of user rights, agent rights, and resource policy, not the union of those rights, because least privilege must be enforced inside the session or token rather than left to convention.
5. **High confidence.** [fact; source: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-impersonation] Enterprises should default to secretless or short-lived credentials such as managed identities, federated identities, assumed roles, and short-lived service account impersonation, because every platform now provides these mechanisms specifically to avoid long-lived credential risk.
6. **High confidence.** [inference; source: https://cloud.google.com/iam/docs/best-practices-service-accounts; https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] If persistent credentials remain unavoidable, they must be single-purpose, inventoried, vaulted, rotated, revocable, and owned by a clear workload lifecycle, because shared or long-lived machine credentials materially weaken both blast-radius control and non-repudiation.
7. **High confidence.** [inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] End-to-end attribution requires a linked audit chain that records the initiating principal, the machine identity, the credential exchange or role assumption, and the downstream resource action, because any missing hop makes forensic reconstruction incomplete.
8. **Medium confidence.** [inference; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Microsoft Entra, AWS IAM, and Google Cloud IAM converge on the same underlying model even though their implementation nouns differ, so a regulated enterprise can define one platform-neutral machine identity policy and translate it into vendor-specific controls.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Each consequential agent or low-code artefact needs its own machine identity. | https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation | high | All sources treat workloads or services as first-class identities. |
| [fact] Delegation preserves the actor while impersonation collapses it. | https://www.rfc-editor.org/rfc/rfc8693 | high | Directly defined in RFC 8693 section 1.1. |
| [inference] Autonomous work should run under the agent's own identity instead of a retained user token. | https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final | high | Derived from delegation semantics plus per-session authorization. |
| [inference] Effective delegated permissions should be an intersection, not a union. | https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation | high | Supported by least-privilege language and session-limiting mechanisms. |
| [fact] Secretless or short-lived credentials are the preferred vendor pattern. | https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-impersonation | high | All three platforms explicitly position these patterns as safer than long-lived secrets. |
| [inference] Persistent machine credentials require stronger lifecycle controls. | https://cloud.google.com/iam/docs/best-practices-service-accounts; https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk | high | Single-purpose design, disablement, leaked-credential response, and secret rotation all point to lifecycle ownership. |
| [inference] Attribution requires a linked initiator, machine, exchange, and action chain. | https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation | high | Each platform exposes part of the chain if distinct identities are used. |
| [inference] The three major cloud platforms converge on one platform-neutral model. | https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation | medium | The convergence is architectural, even though implementation details differ. |

**Assumptions:**

- [assumption; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://cloud.google.com/iam/docs/service-account-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html] Low-code artefacts that perform API calls, write records, or trigger workflows can be governed as software workloads for IAM purposes. **Justification:** the reviewed platform documents define workload identity by operational behavior, not by whether the actor was authored in pro-code or low-code tooling.

**Analysis:**

- [inference; source: https://pages.nist.gov/800-63-3/sp800-63c.html; https://csrc.nist.gov/pubs/sp/800/207/final] The evidence was weighted by direct applicability to non-human actors, which made NIST SP 800-207 more decisive than NIST SP 800-63C for workload identity even though both remain relevant standards.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://cloud.google.com/iam/docs/service-account-impersonation; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html] Delegation was favored over impersonation in the synthesis because the direct standard definition in RFC 8693 aligns better with the audit-preservation mechanisms exposed by AWS and Google than with identity-collapsing impersonation semantics alone.
- [inference; source: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Secretless and short-lived credential patterns were treated as higher-quality evidence than secret-management guidance because removing persistent credentials is a stronger control than rotating them after compromise.
- [inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html; https://cloud.google.com/iam/docs/service-account-impersonation] Competing interpretations about whether attached identities are sufficient for attribution were resolved against the attached-identity approach because the vendor documentation repeatedly shows that richer attribution exists only when delegation or impersonation events themselves are separately logged.

**Risks, gaps, uncertainties:**

- [inference; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations] Microsoft federation configuration changes can take several minutes to propagate, so immediate cutover assumptions are unsafe unless retry behavior and staging windows are designed explicitly.
- [inference; source: https://cloud.google.com/iam/docs/service-account-impersonation] Google notes that most audit logs include both identities for impersonation, which implies there are service-specific exceptions that can still weaken attribution if enterprises assume universal coverage.
- [inference; source: https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] Managed identities are not in scope for some Microsoft workload-risk detections, so enterprises may need compensating telemetry for those identities.
- [inference; source: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html] AWS SourceIdentity must be required in trust and permissions policy to be reliable, so attribution quality is partly a policy-deployment question rather than a platform default.

**Open questions:**

- When a low-code platform cannot preserve actor information inside downstream tokens, what minimum out-of-band provenance record is sufficient for non-repudiation?
- Which enterprise Software as a Service (SaaS) products preserve delegated actor claims end to end, and which collapse them to a service account at the integration boundary?
- What is the best platform-neutral pattern for human approval and re-authorization when an autonomous agent needs temporary elevation outside its baseline role?

### §7 Recursive Review

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Review outcome: the synthesis remains supported by the cited standards and platform documents, the main uncertainty areas are service-specific audit coverage and platform-specific implementation limits, and no finding depends on an inaccessible source.
- [fact; source: https://pages.nist.gov/800-63-3/sp800-63c.html; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html] Acronym audit completed in-line: National Institute of Standards and Technology (NIST), Special Publication (SP), Amazon Web Services (AWS), Request for Comments (RFC), Secure Production Identity Framework For Everyone (SPIFFE), SPIFFE Runtime Environment (SPIRE), Security Token Service (STS), JSON Web Token (JWT), and Application Programming Interface (API) are expanded on first use in the research output.
- [fact; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html; https://cloud.google.com/iam/docs/service-account-impersonation] Claim-label and source-binding review completed: all factual and inferential claims in the research output and Findings carry inline labels, and the Evidence Map mirrors the synthesis claims without introducing new unsupported conclusions.

---

## Findings

### Executive Summary

[inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Enterprises need a first-class machine identity model for AI agents and low-code artefacts in which every consequential non-human actor has its own identity, user-initiated work uses bounded delegation where possible, autonomous work runs under the agent's own scoped identity, and credentials are short-lived by default.

[fact; source: https://www.rfc-editor.org/rfc/rfc8693] The central standards distinction is that delegation preserves both the subject and the actor, while impersonation collapses the actor into the subject inside the token context.

[inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/best-practices-service-accounts] That distinction means an agent should not inherit a user's full permission estate by default, because least privilege for non-human actors must be enforced through intersected scope, session policy, or single-purpose service-account grants.

[inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] Attribution survives only when the design records the initiator, the machine identity, the credential exchange, and the downstream action as linked but distinct events.

### Key Findings

1. **High confidence.** [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation] An enterprise AI identity model should assign every consequential agent or low-code artefact its own machine identity, because the standards and vendor patterns all treat software workloads as first-class subjects rather than as invisible extensions of human users.
2. **High confidence.** [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] User-initiated agent actions are better governed through delegation semantics than impersonation, because RFC 8693 preserves both the original subject and the acting party, while AWS and Google both expose more useful audit chains when the acting identity remains distinguishable.
3. **High confidence.** [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final] Autonomous or scheduled agent work should run under the agent's own pre-authorized identity instead of under a retained user delegation token, because the user is no longer actively supervising the session and the agent therefore requires an independently bounded authorization decision.
4. **High confidence.** [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation] The effective permission set for a delegated agent should be the intersection of user rights, agent rights, and resource policy, not the union of those rights, because least privilege must be enforced inside the session or token rather than left to convention.
5. **High confidence.** [fact; source: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-impersonation] Enterprises should default to secretless or short-lived credentials such as managed identities, federated identities, assumed roles, and short-lived service account impersonation, because every platform now provides these mechanisms specifically to avoid long-lived credential risk.
6. **High confidence.** [inference; source: https://cloud.google.com/iam/docs/best-practices-service-accounts; https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] If persistent credentials remain unavoidable, they must be single-purpose, inventoried, vaulted, rotated, revocable, and owned by a clear workload lifecycle, because shared or long-lived machine credentials materially weaken both blast-radius control and non-repudiation.
7. **High confidence.** [inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation] End-to-end attribution requires a linked audit chain that records the initiating principal, the machine identity, the credential exchange or role assumption, and the downstream resource action, because any missing hop makes forensic reconstruction incomplete.
8. **Medium confidence.** [inference; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Microsoft Entra, AWS IAM, and Google Cloud IAM converge on the same underlying model even though their implementation nouns differ, so a regulated enterprise can define one platform-neutral machine identity policy and translate it into vendor-specific controls.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Each consequential agent or low-code artefact needs its own machine identity. | https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/; https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation | high | All sources treat workloads or services as first-class identities. |
| [fact] Delegation preserves the actor while impersonation collapses it. | https://www.rfc-editor.org/rfc/rfc8693 | high | Direct standard language from RFC 8693 section 1.1. |
| [inference] Autonomous work should run under the agent's own identity instead of a retained user token. | https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final | high | Derived from delegation semantics plus per-session authorization. |
| [inference] Effective delegated permissions should be an intersection, not a union. | https://csrc.nist.gov/pubs/sp/800/207/final; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html; https://cloud.google.com/iam/docs/workload-identity-federation | high | Supported by least-privilege language and session-limiting mechanisms. |
| [fact] Secretless or short-lived credentials are the preferred vendor pattern. | https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation; https://cloud.google.com/iam/docs/service-account-impersonation | high | All three platforms explicitly position these patterns as safer than long-lived secrets. |
| [inference] Persistent machine credentials require stronger lifecycle controls. | https://cloud.google.com/iam/docs/best-practices-service-accounts; https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk | high | Single-purpose design, disablement, leaked-credential response, and secret rotation all point to lifecycle ownership. |
| [inference] Attribution requires a linked initiator, machine, exchange, and action chain. | https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html; https://cloud.google.com/iam/docs/service-account-impersonation | high | Each platform exposes part of the chain if distinct identities are used. |
| [inference] The three major cloud platforms converge on one platform-neutral model. | https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation | medium | The convergence is architectural, even though implementation details differ. |

### Assumptions

- [assumption; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview; https://cloud.google.com/iam/docs/service-account-overview; https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html] **Assumption:** Low-code artefacts that perform API calls, write records, or trigger workflows can be governed as software workloads for IAM purposes. **Justification:** the reviewed platform documents define workload identity by operational behavior, not by whether the actor was authored in pro-code or low-code tooling.

### Analysis

[inference; source: https://pages.nist.gov/800-63-3/sp800-63c.html; https://csrc.nist.gov/pubs/sp/800/207/final] The evidence was weighted by direct applicability to non-human actors, which made NIST SP 800-207 more decisive than NIST SP 800-63C for workload identity even though both remain relevant standards.

[inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://cloud.google.com/iam/docs/service-account-impersonation; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html] Delegation was favored over impersonation in the synthesis because the direct standard definition in RFC 8693 aligns better with the audit-preservation mechanisms exposed by AWS and Google than with identity-collapsing impersonation semantics alone.

[inference; source: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview; https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html; https://cloud.google.com/iam/docs/workload-identity-federation] Secretless and short-lived credential patterns were treated as higher-quality evidence than secret-management guidance because removing persistent credentials is a stronger control than rotating them after compromise.

[inference; source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins; https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html; https://cloud.google.com/iam/docs/service-account-impersonation] Competing interpretations about whether attached identities are sufficient for attribution were resolved against the attached-identity approach because the vendor documentation repeatedly shows that richer attribution exists only when delegation or impersonation events themselves are separately logged.

### Risks, Gaps, and Uncertainties

- [inference; source: https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-considerations] Microsoft federation configuration changes can take several minutes to propagate, so immediate cutover assumptions are unsafe unless retry behavior and staging windows are designed explicitly.
- [inference; source: https://cloud.google.com/iam/docs/service-account-impersonation] Google notes that most audit logs include both identities for impersonation, which implies there are service-specific exceptions that can still weaken attribution if enterprises assume universal coverage.
- [inference; source: https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk] Managed identities are not in scope for some Microsoft workload-risk detections, so enterprises may need compensating telemetry for those identities.
- [inference; source: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html] AWS SourceIdentity must be required in trust and permissions policy to be reliable, so attribution quality is partly a policy-deployment question rather than a platform default.

### Open Questions

- When a low-code platform cannot preserve actor information inside downstream tokens, what minimum out-of-band provenance record is sufficient for non-repudiation?
- Which enterprise Software as a Service (SaaS) products preserve delegated actor claims end to end, and which collapse them to a service account at the integration boundary?
- What is the best platform-neutral pattern for human approval and re-authorization when an autonomous agent needs temporary elevation outside its baseline role?

---

## Output

- Type: knowledge
- Description: A machine identity, delegation, credential, and attribution model for enterprise AI agents and low-code artefacts, grounded in NIST, RFC 8693, and Microsoft, AWS, and Google Cloud identity controls.
- Links:
  - https://csrc.nist.gov/pubs/sp/800/207/final
  - https://www.rfc-editor.org/rfc/rfc8693
  - https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview
