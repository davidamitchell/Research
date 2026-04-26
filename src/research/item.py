"""Research item data model and file I/O."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path


@dataclass
class ResearchItem:
    """Represents a single research item loaded from a Markdown file."""

    path: Path
    title: str
    added: date | datetime
    status: str  # backlog | in-progress | reviewing | completed
    priority: str  # low | medium | high
    tags: list[str] = field(default_factory=list)
    blocks: list[str] = field(default_factory=list)
    output: list[str] = field(default_factory=list)

    @classmethod
    def from_file(cls, path: Path) -> ResearchItem:
        """Load a ResearchItem from a Markdown file with YAML front matter."""
        import re

        text = path.read_text(encoding="utf-8")
        # Extract YAML front matter between --- delimiters
        match = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
        if not match:
            raise ValueError(f"No YAML front matter found in {path}")

        import yaml  # type: ignore[import-untyped]

        meta = yaml.safe_load(match.group(1))

        # ``added`` may be stored as a date-only string, a Python date (parsed
        # by YAML), or a full ISO-8601 datetime string / Python datetime.
        # Normalise to whatever Python type PyYAML gives us; callers should
        # treat it as a ``date | datetime`` union.
        added_raw = meta.get("added", date.today())
        if isinstance(added_raw, str):
            # PyYAML returns strings only for unrecognised formats; try to
            # parse as datetime first, then date.
            try:
                added_raw = datetime.fromisoformat(added_raw)
            except ValueError:
                try:
                    added_raw = date.fromisoformat(added_raw)
                except ValueError:
                    added_raw = date.today()

        return cls(
            path=path,
            title=meta.get("title", path.stem),
            added=added_raw,
            status=meta.get("status", "backlog"),
            priority=meta.get("priority", "medium"),
            tags=meta.get("tags") or [],
            blocks=meta.get("blocks") or [],
            output=meta.get("output") or [],
        )

    def state_dir_name(self) -> str:
        """Return the directory name corresponding to this item's status."""
        mapping = {
            "backlog": "backlog",
            "in-progress": "in-progress",
            "reviewing": "in-progress",
            "completed": "completed",
        }
        return mapping.get(self.status, "backlog")
