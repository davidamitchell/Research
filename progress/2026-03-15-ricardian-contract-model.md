# 2026-03-15 — Research Loop (ricardian-contract-model)

**Completed:**

Research item:
- `Research/completed/2026-03-14-ricardian-contract-model.md` — completed; the Ricardian Contract, developed by Ian Grigg in 1995–1996 for the Ricardo payment system and formally published in 2004, is a design pattern binding human-readable legal prose to machine-readable fields in a single cryptographically signed document whose hash serves as the instrument identifier. It is orthogonal to (not competing with) Ethereum-style smart contracts: Ricardian Contracts handle semantics and legal meaning; smart contracts handle execution. EOSIO is the most significant institutional adopter (mandatory for all deployed smart contracts); the Accord Project (Linux Foundation) is the most active current open standards ecosystem. Real-world asset (RWA) tokenisation — Mattereum, LTO Network — is the primary active commercial deployment domain.

Sources consulted:
- https://iang.org/papers/ricardian_contract.html (Ian Grigg's canonical 2004 definition paper)
- https://iang.org/papers/intersection_ricardian_smart.html (Grigg's 2015 analysis of Ricardian vs. smart contracts as orthogonal)
- https://accordproject.org (Accord Project — most active current open-source ecosystem)
- https://github.com/EOSIO/ricardian-template-toolkit (EOSIO's Ricardian Template Toolkit — major adopter)
- https://mattereum.com/2024/07/01/mattereum-and-plume-network-partner-to-revolutionize-tokenized-gold/ (production RWA deployment)
- https://astraea.law/insights/smart-contract-legal-enforceability-code-isnt-law (adoption barriers analysis)
- https://arxiv.org/html/2505.15051v1 (2025 EOS blockchain architecture survey confirming Ricardian Contract mandate)
- https://arxiv.org/html/2510.20007v1 (2025 zk-agreements paper extending Accord Project with zero-knowledge proofs)
- https://bitsonblocks.net/2016/11/22/in-a-nutshell-ian-griggs-ricardian-contracts-and-digital-assets-prehistory/ (Grigg interview confirming naming from Ricardo system)
- https://corpgov.law.harvard.edu/2018/05/26/an-introduction-to-smart-contracts-and-their-potential-and-inherent-limitations/ (Harvard Law definition cross-check)

## Mini-Retro

1. **Did the process work?** Yes. The evidence base was sufficient to answer all six sub-questions fully. Primary sources (Grigg's papers, official project documentation) were accessible; EOSIO adoption was confirmed by three independent sources including a 2025 peer-reviewed paper. Review workflow passed on first submission.

2. **What slowed down or went wrong?** The Grigg 1996 original documentation at iang.org/ricardo was partially inaccessible; this is flagged in the "identified but not consulted" section. No other material access issues.

3. **What single change would prevent this next time?** Nothing significant to change. The parallel search approach (multiple Tavily queries in one turn) worked efficiently. The acronym audit and AI-slop check embedded in §7 caught no violations.

4. **Is this a pattern?** The dual skill requirement as an adoption barrier is a recurring pattern in tools that bridge two professional domains (legal + technical here; strategy + engineering in prior items). This is now documented in Thread 4 of learnings.md.
