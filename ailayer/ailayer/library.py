"""
Read skills and tool metadata from the ai_skills_and_tools library on disk.

The library root is resolved in this priority order:
  1. AILAYER_LIBRARY env var
  2. ~/.ailayer/library_path (config file)
  3. Auto-detection: walk up from CWD looking for INDEX.md
  4. Same directory as this package's parent (dev convenience)
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from ailayer.console import warn


def _find_library_root() -> Optional[Path]:
    # 1. Env override
    env_val = os.environ.get("AILAYER_LIBRARY")
    if env_val:
        p = Path(env_val).expanduser().resolve()
        if p.is_dir():
            return p

    # 2. Config file
    cfg_path = Path.home() / ".ailayer" / "config"
    if cfg_path.exists():
        for line in cfg_path.read_text().splitlines():
            if line.startswith("library_path="):
                p = Path(line.split("=", 1)[1].strip()).expanduser().resolve()
                if p.is_dir():
                    return p

    # 3. Walk up from CWD
    current = Path.cwd()
    for _ in range(8):
        if (current / "INDEX.md").exists():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent

    # 4. Package-relative fallback (repo checkout)
    pkg_parent = Path(__file__).parent.parent.parent  # …/ailayer/../..
    if (pkg_parent / "INDEX.md").exists():
        return pkg_parent

    return None


LIBRARY_ROOT: Optional[Path] = _find_library_root()


def require_library() -> Path:
    if LIBRARY_ROOT is None:
        raise RuntimeError(
            "Could not locate the ai_skills_and_tools library.\n"
            "Set the AILAYER_LIBRARY environment variable to its path, e.g.:\n"
            "  export AILAYER_LIBRARY=~/ai_skills_and_tools"
        )
    return LIBRARY_ROOT


class Skill:
    """Represents one entry in the library."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.name = path.name  # directory name, e.g. "langchain"
        self._readme: Optional[str] = None

    @property
    def readme(self) -> str:
        if self._readme is None:
            readme_path = self.path / "README.md"
            self._readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
        return self._readme

    @property
    def summary(self) -> str:
        """Return the first non-header, non-empty line of the README as a one-liner."""
        for line in self.readme.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith(">") and line != "---":
                return line[:120]
        return "(no summary)"

    @property
    def category(self) -> str:
        """Detect category from README frontmatter '> Category: ...' line."""
        for line in self.readme.splitlines():
            line = line.strip()
            if line.startswith("> **Category:**"):
                return line.replace("> **Category:**", "").split("|")[0].strip()
        return "Uncategorised"

    def skill_prompt(self) -> str:
        """Return the content suitable for injecting as a slash-command prompt."""
        return self.readme

    def __repr__(self) -> str:
        return f"<Skill {self.name}>"


def list_skills() -> list[Skill]:
    """Return all skills (tool directories containing a README.md) from the library."""
    root = require_library()
    skills: list[Skill] = []
    for entry in sorted(root.iterdir()):
        if entry.is_dir() and (entry / "README.md").exists() and entry.name != "ailayer":
            skills.append(Skill(entry))
    return skills


def get_skill(name: str) -> Optional[Skill]:
    """Look up a skill by directory name (case-insensitive)."""
    root = require_library()
    target = name.lower().replace(" ", "-")
    for entry in root.iterdir():
        if entry.is_dir() and entry.name.lower() == target and (entry / "README.md").exists():
            return Skill(entry)
    return None
