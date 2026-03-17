# Session: clean-ai-slop-citations-speculation

**Date:** 2026-03-17
**Issue:** #[clean] — Apply three quality skills to `Research/completed/2026-03-02-ai-not-a-data-problem.md`

## What was done

Applied three quality skills to `Research/completed/2026-03-02-ai-not-a-data-problem.md`:

### 1. citation-discipline

Expanded all acronyms and initialisations on their first occurrence in the document:

- `HADR` → high availability and disaster recovery (HADR) — Scope section
- `STS` → Security Token Service (STS) — Scope section
- `DID` → decentralised identifiers (DID) — Scope section
- `RBNZ` → Reserve Bank of New Zealand (RBNZ) — Constraints section
- `DIA` → Department of Internal Affairs (DIA) — Constraints section
- `MBIE` → Ministry of Business, Innovation and Employment (MBIE) — Constraints section
- `BI` → business intelligence (BI) — Context section
- `ETL` → extract-transform-load (ETL) — Context section
- `APRA` → Australian Prudential Regulation Authority (APRA) — Context Prior research
- `SRE` → site reliability engineering (SRE) — Approach section
- `OCC` → Office of the Comptroller of the Currency (OCC) — Approach section
- `FCA` → Financial Conduct Authority (FCA) — Approach section
- `GDPR` → General Data Protection Regulation (GDPR) — Approach section
- `NIST` → National Institute of Standards and Technology (NIST) — Sources section
- `CDO/CDAO` → Chief Data Officer (CDO)/Chief Data and Analytics Officer (CDAO) — §1
- `RBAC` → role-based access control (RBAC) — §2 Investigation
- `RPO/RTO` → recovery point objective/recovery time objective (RPO/RTO) — §2
- `mTLS` → mutual TLS (mTLS) — §2
- `IAM` → identity and access management (IAM) — §2
- `IETF` → Internet Engineering Task Force (IETF) — §2
- `HBR` → Harvard Business Review (HBR) — §2
- `BCG` → Boston Consulting Group (BCG) — §2
- `CTO/CAIO` → Chief Technology Officer (CTO)/Chief Artificial Intelligence Officer (CAIO) — §2
- `OIDC` → OpenID Connect (OIDC) — §2
- `MLOps` → machine learning operations (MLOps) — §2
- `SMCR` → Senior Managers and Certification Regime (SMCR) — §2
- `CRO` → Chief Risk Officer (CRO) — §2
- `PRA` → Prudential Regulation Authority (PRA) — §2

### 2. speculation-control

Added `[inference]` labels to three speculative claims in §5 (Depth and Breadth Expansion) that were presented without labels:

- **Economic lens:** Causal claim that data-team-anchored organisations are disproportionately represented in the 74% failure category — labelled as inference derived from IBM CDO Study + BCG 10-20-70 data.
- **Behavioural lens:** Structural incentive analysis about data teams accumulating AI ownership — labelled as inference derived from IBM CDO Study and HBR CDO failure analysis; not directly measured.
- **Historical lens:** Analogical conclusion "AI follows the same arc" from the BI precedent — labelled as inference; no single authoritative study confirms the full AI transition trajectory.

### 3. remove-ai-slop

Rewrote the Analysis paragraph in `## Findings` that used a formulaic "First, the technical/architectural direction... Second, the organisational direction... Third, the evidence direction..." tri-part parallel structure. Replaced with direct prose that presents the same three evidence streams without the mechanical enumeration.

## Observations

The document was already in strong shape overall: the Research Skill Output used `[fact]`, `[inference]`, and `[assumption]` labels consistently, and the prose avoided most common AI slop patterns. The main issues were:
1. Many acronyms used before formal expansion (systematic across the whole document)
2. Three unlabelled inferences in §5 that required [inference] labels
3. One formulaic tri-part structure in the Findings/Analysis section
