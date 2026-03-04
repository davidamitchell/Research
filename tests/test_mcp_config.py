"""Tests proving both MCP config files are valid and consistently configured.

STRUCTURAL TESTS (sections 1-5 below)
--------------------------------------
These tests verify the *config files* only — they do NOT verify that any server
actually works at runtime. Specifically they check:
1. Both config files parse as valid JSON.
2. Neither file contains the removed `brave_search` server.
3. The Tavily entry references the correct env var (`TAVILY_API_KEY`).
4. Both files declare the same set of server keys (in sync check).
5. Smoke test: load each file end-to-end (parse → validate → assert server list).

INTEGRATION TEST (section 6)
------------------------------
test_tavily_live_search — makes a real HTTP call to the Tavily API using
`TAVILY_API_KEY` to prove the key is valid and the service responds.  Skipped
when `TAVILY_API_KEY` is not in the environment.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import httpx
import pytest

REPO_ROOT = Path(__file__).parent.parent
COPILOT_MCP = REPO_ROOT / ".github" / "mcp.json"
CLAUDE_MCP = REPO_ROOT / ".mcp.json"

EXPECTED_SERVERS = {
    "fetch",
    "sequential_thinking",
    "time",
    "memory",
    "git",
    "filesystem",
    "arxiv",
    "github",
    "tavily",
}


# ---------------------------------------------------------------------------
# File existence
# ---------------------------------------------------------------------------


def test_copilot_mcp_file_exists() -> None:
    assert COPILOT_MCP.exists(), f"MCP config not found: {COPILOT_MCP}"


def test_claude_mcp_file_exists() -> None:
    assert CLAUDE_MCP.exists(), f"MCP config not found: {CLAUDE_MCP}"


# ---------------------------------------------------------------------------
# Valid JSON
# ---------------------------------------------------------------------------


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_copilot_mcp_is_valid_json() -> None:
    data = _load_json(COPILOT_MCP)
    assert isinstance(data, dict)


def test_claude_mcp_is_valid_json() -> None:
    data = _load_json(CLAUDE_MCP)
    assert isinstance(data, dict)


# ---------------------------------------------------------------------------
# brave_search removed
# ---------------------------------------------------------------------------


def test_copilot_mcp_does_not_contain_brave_search() -> None:
    data = _load_json(COPILOT_MCP)
    assert "brave_search" not in data["mcpServers"], (
        ".github/mcp.json must not contain brave_search (W-0032: removed — no BRAVE_API_KEY)"
    )


def test_claude_mcp_does_not_contain_brave_search() -> None:
    data = _load_json(CLAUDE_MCP)
    assert "brave_search" not in data["mcpServers"], (
        ".mcp.json must not contain brave_search (W-0032: removed — no BRAVE_API_KEY)"
    )


def test_copilot_mcp_text_does_not_reference_brave_api_key() -> None:
    content = COPILOT_MCP.read_text(encoding="utf-8")
    assert "BRAVE_API_KEY" not in content, ".github/mcp.json must not reference BRAVE_API_KEY"


def test_claude_mcp_text_does_not_reference_brave_api_key() -> None:
    content = CLAUDE_MCP.read_text(encoding="utf-8")
    assert "BRAVE_API_KEY" not in content, ".mcp.json must not reference BRAVE_API_KEY"


# ---------------------------------------------------------------------------
# Tavily env var is correct
# ---------------------------------------------------------------------------


def test_copilot_mcp_tavily_uses_correct_env_var() -> None:
    data = _load_json(COPILOT_MCP)
    tavily = data["mcpServers"]["tavily"]
    assert "TAVILY_API_KEY" in tavily.get("env", {}), (
        "tavily entry in .github/mcp.json must declare TAVILY_API_KEY env var"
    )


def test_claude_mcp_tavily_uses_correct_env_var() -> None:
    data = _load_json(CLAUDE_MCP)
    tavily = data["mcpServers"]["tavily"]
    assert "TAVILY_API_KEY" in tavily.get("env", {}), (
        "tavily entry in .mcp.json must declare TAVILY_API_KEY env var"
    )


# ---------------------------------------------------------------------------
# Both files declare the same server set (in-sync check)
# ---------------------------------------------------------------------------


def test_both_mcp_files_have_same_server_keys() -> None:
    copilot_servers = set(_load_json(COPILOT_MCP)["mcpServers"].keys())
    claude_servers = set(_load_json(CLAUDE_MCP)["mcpServers"].keys())
    assert copilot_servers == claude_servers, (
        f".github/mcp.json and .mcp.json server keys are out of sync.\n"
        f"  .github/mcp.json only: {copilot_servers - claude_servers}\n"
        f"  .mcp.json only: {claude_servers - copilot_servers}"
    )


# ---------------------------------------------------------------------------
# Smoke test: load end-to-end and assert expected server list
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("config_path", [COPILOT_MCP, CLAUDE_MCP], ids=["copilot", "claude"])
def test_mcp_config_smoke_expected_server_list(config_path: Path) -> None:
    """End-to-end: parse → validate structure → assert exact server set."""
    data = _load_json(config_path)

    # Top-level key must be mcpServers
    assert "mcpServers" in data, f"{config_path.name} must have a top-level 'mcpServers' key"

    servers = data["mcpServers"]
    assert isinstance(servers, dict), "'mcpServers' must be an object"

    actual = set(servers.keys())
    missing = EXPECTED_SERVERS - actual
    extra = actual - EXPECTED_SERVERS

    assert not missing, f"{config_path.name} is missing expected servers: {missing}"
    assert not extra, f"{config_path.name} has unexpected servers: {extra}"


@pytest.mark.parametrize("config_path", [COPILOT_MCP, CLAUDE_MCP], ids=["copilot", "claude"])
def test_mcp_config_each_server_has_command(config_path: Path) -> None:
    """Every server entry must declare a command (or 'command' key for Claude, 'command'/'type' for Copilot)."""
    data = _load_json(config_path)
    for name, entry in data["mcpServers"].items():
        assert "command" in entry, (
            f"Server '{name}' in {config_path.name} is missing required 'command' key"
        )


# ---------------------------------------------------------------------------
# Live integration test: verify TAVILY_API_KEY is valid and service responds
# NOTE: structural tests above do NOT verify the service works — this one does.
# ---------------------------------------------------------------------------

_TAVILY_KEY = os.getenv("TAVILY_API_KEY", "")


@pytest.mark.skipif(not _TAVILY_KEY, reason="TAVILY_API_KEY not set — skipping live API call")
def test_tavily_live_search() -> None:
    """Make a real HTTP call to the Tavily API to prove the key is valid and the service works."""
    response = httpx.post(
        "https://api.tavily.com/search",
        json={"api_key": _TAVILY_KEY, "query": "test", "max_results": 1},
        timeout=30.0,
    )
    assert response.status_code == 200, (
        f"Tavily API returned HTTP {response.status_code}: {response.text[:200]}"
    )
    body = response.json()
    assert "results" in body, f"Tavily response missing 'results' key: {list(body.keys())}"
    assert isinstance(body["results"], list), "'results' must be a list"
