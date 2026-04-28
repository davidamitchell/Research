"""Tests for key-claims extraction in scripts/extract_metadata.py."""

from __future__ import annotations

import sys
from pathlib import Path

# Make scripts/ importable
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from extract_metadata import extract_key_claims

# ---------------------------------------------------------------------------
# Format 1 — older style: **Claim text.** (confidence level)
# ---------------------------------------------------------------------------


def test_format1_extracts_claim_text() -> None:
    """Format 1 bullets return the bolded claim, not the confidence label."""
    findings = """\
### Key Findings

1. **Brooks (1975), Chapter 2, establishes that communication effort scales as n(n-1)/2.** (high confidence)
2. **Brooks does not identify 5 as the optimal team size.** (medium confidence)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 2
    assert claims[0].startswith("Brooks (1975)")
    assert "communication effort scales" in claims[0]
    assert "confidence" not in claims[0].lower()
    assert claims[1].startswith("Brooks does not identify 5")


def test_format1_strips_parenthetical_confidence() -> None:
    findings = """\
### Key Findings

1. **Static extraction provides the highest-confidence declared edges.** (high confidence)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0] == "Static extraction provides the highest-confidence declared edges"


# ---------------------------------------------------------------------------
# Format 2 — mid-era style: **High confidence.** [source] Claim text
# ---------------------------------------------------------------------------


def test_format2_extracts_claim_not_confidence_label() -> None:
    """Format 2 bullets return the claim text after the source bracket."""
    findings = """\
### Key Findings

1. **High confidence.** [inference; source: https://example.com/paper1.pdf] The best empirical evidence indicates citizen development sprawl begins as a workaround.
2. **Medium confidence.** [inference; source: https://example.com] Governance architectures do not suppress automation demand.
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 2
    assert claims[0] == (
        "The best empirical evidence indicates citizen development sprawl begins as a workaround"
    )
    assert claims[1] == "Governance architectures do not suppress automation demand"


def test_format2_colon_variant() -> None:
    """**High confidence:** variant (colon instead of period) is also stripped."""
    findings = """\
### Key Findings

1. **High confidence:** [fact; source: https://example.com] Shadow IT research identifies IT slowness as the recurring condition.
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0] == "Shadow IT research identifies IT slowness as the recurring condition"


def test_format2_multi_url_source_bracket() -> None:
    """Multi-URL source brackets are stripped in full."""
    findings = """\
### Key Findings

1. **High confidence.** [fact; source: https://a.com; https://b.com; https://c.com] The claim text survives intact.
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0] == "The claim text survives intact"


# ---------------------------------------------------------------------------
# Format 3 — current style: [source] **confidence:** Claim text
# ---------------------------------------------------------------------------


def test_format3_extracts_claim_text() -> None:
    """Format 3 bullets (source bracket first) are matched and extracted."""
    findings = """\
### Key Findings

1. [inference; source: https://opentelemetry.io/docs/] **Medium confidence:** OPA is a well-supported default PDP runtime.
2. [fact; source: https://example.com] **High confidence:** The reference architecture should separate canonical policy authoring.
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 2
    assert claims[0] == "OPA is a well-supported default PDP runtime"
    assert claims[1] == "The reference architecture should separate canonical policy authoring"


def test_format3_multiple_source_urls() -> None:
    findings = """\
### Key Findings

1. [inference; source: https://a.com; https://b.com; https://c.com; https://d.com] **High confidence:** Claim text here.
"""
    claims = extract_key_claims(findings)
    assert claims == ["Claim text here"]


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------


def test_no_key_findings_section_falls_back() -> None:
    """When ### Key Findings is absent, fallback extracts from Executive Summary bullets."""
    findings = """\
### Executive Summary

* [inference] Systems debt is the root cause of citizen development sprawl.
* [fact] Costs from poor data quality are already material.
"""
    claims = extract_key_claims(findings)
    assert isinstance(claims, list)
    # Fallback should pull both bullet sentences
    assert len(claims) >= 1
    assert any("Systems debt" in c or "Costs" in c for c in claims)


def test_empty_findings_returns_empty_list() -> None:
    assert extract_key_claims("") == []


def test_max_eight_claims() -> None:
    """No more than 8 claims are returned."""
    bullets = "\n".join(
        f"1. [fact; source: https://example.com] **High confidence:** Claim number {i}."
        for i in range(15)
    )
    findings = f"### Key Findings\n\n{bullets}\n"
    claims = extract_key_claims(findings)
    assert len(claims) <= 8
