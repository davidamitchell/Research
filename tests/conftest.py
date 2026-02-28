"""Shared pytest fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture
def research_dir(tmp_path):
    """Create a temporary Research directory structure."""
    for subdir in ("backlog", "in-progress", "completed"):
        (tmp_path / subdir).mkdir()
    return tmp_path
