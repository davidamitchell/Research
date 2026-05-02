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
    assert claims[0]["text"].startswith("Brooks (1975)")
    assert "communication effort scales" in claims[0]["text"]
    assert "confidence" not in claims[0]["text"].lower()
    assert claims[1]["text"].startswith("Brooks does not identify 5")


def test_format1_strips_parenthetical_confidence() -> None:
    findings = """\
### Key Findings

1. **Static extraction provides the highest-confidence declared edges.** (high confidence)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0]["text"] == "Static extraction provides the highest-confidence declared edges"


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
    assert claims[0]["text"] == (
        "The best empirical evidence indicates citizen development sprawl begins as a workaround"
    )
    assert claims[0]["sources"] == ["https://example.com/paper1.pdf"]
    assert claims[1]["text"] == "Governance architectures do not suppress automation demand"
    assert claims[1]["sources"] == ["https://example.com"]


def test_format2_colon_variant() -> None:
    """**High confidence:** variant (colon instead of period) is also stripped."""
    findings = """\
### Key Findings

1. **High confidence:** [fact; source: https://example.com] Shadow IT research identifies IT slowness as the recurring condition.
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert (
        claims[0]["text"] == "Shadow IT research identifies IT slowness as the recurring condition"
    )
    assert claims[0]["sources"] == ["https://example.com"]


def test_format2_multi_url_source_bracket() -> None:
    """Multi-URL source brackets are stripped; all URLs are captured."""
    findings = """\
### Key Findings

1. **High confidence.** [fact; source: https://a.com; https://b.com; https://c.com] The claim text survives intact.
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0]["text"] == "The claim text survives intact"
    assert claims[0]["sources"] == ["https://a.com", "https://b.com", "https://c.com"]


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
    assert claims[0]["text"] == "OPA is a well-supported default PDP runtime"
    assert claims[0]["sources"] == ["https://opentelemetry.io/docs/"]
    assert (
        claims[1]["text"] == "The reference architecture should separate canonical policy authoring"
    )
    assert claims[1]["sources"] == ["https://example.com"]


def test_format3_multiple_source_urls() -> None:
    findings = """\
### Key Findings

1. [inference; source: https://a.com; https://b.com; https://c.com; https://d.com] **High confidence:** Claim text here.
"""
    claims = extract_key_claims(findings)
    assert claims[0]["text"] == "Claim text here"
    assert claims[0]["sources"] == [
        "https://a.com",
        "https://b.com",
        "https://c.com",
        "https://d.com",
    ]


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
    assert any("Systems debt" in c["text"] or "Costs" in c["text"] for c in claims)


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


def test_no_source_bracket_produces_empty_sources() -> None:
    """Format 1 bullets with no source bracket produce an empty sources list."""
    findings = """\
### Key Findings

1. **Plain claim with no source reference.** (high confidence)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0]["sources"] == []


# ---------------------------------------------------------------------------
# Format 4 — suffix style: **Claim text.** ([inference]; confidence; source: URL)
# ---------------------------------------------------------------------------


def test_format4_suffix_extracts_sources_from_parens() -> None:
    """Format 4 suffix citations extract source URLs from the trailing parenthetical."""
    findings = """\
### Key Findings

1. **Bounded automation outperforms end-to-end autonomy for reliable coding tasks.** ([inference]; medium confidence; source: https://example.com/paper1; https://example.com/paper2)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0]["sources"] == [
        "https://example.com/paper1",
        "https://example.com/paper2",
    ]


def test_format4_suffix_strips_annotation_from_claim_text() -> None:
    """Format 4 suffix citations strip the trailing parenthetical from the claim text."""
    findings = """\
### Key Findings

1. **Bounded automation outperforms end-to-end autonomy for reliable coding tasks.** ([inference]; medium confidence; source: https://example.com/paper1)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0]["text"] == (
        "Bounded automation outperforms end-to-end autonomy for reliable coding tasks"
    )
    assert "confidence" not in claims[0]["text"].lower()
    assert "source" not in claims[0]["text"].lower()
    assert "inference" not in claims[0]["text"].lower()


def test_format4_high_confidence_variant() -> None:
    """Format 4 works with high confidence label."""
    findings = """\
### Key Findings

1. **Test-first development reduces defect rates in well-studied projects.** ([fact]; high confidence; source: https://example.com/study)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 1
    assert claims[0]["text"] == (
        "Test-first development reduces defect rates in well-studied projects"
    )
    assert claims[0]["sources"] == ["https://example.com/study"]


def test_format4_multiple_items() -> None:
    """Format 4 handles multiple numbered Key Findings."""
    findings = """\
### Key Findings

1. **First claim about coding agents.** ([inference]; medium confidence; source: https://a.com; https://b.com)
2. **Second claim about oversight.** ([inference]; high confidence; source: https://c.com)
"""
    claims = extract_key_claims(findings)
    assert len(claims) == 2
    assert "First claim" in claims[0]["text"]
    assert claims[0]["sources"] == ["https://a.com", "https://b.com"]
    assert "Second claim" in claims[1]["text"]
    assert claims[1]["sources"] == ["https://c.com"]
