"""
Abstract base class for agentic tool adapters.

Each supported tool (Claude Code, Codex, Gemini CLI) implements this interface
so the CLI commands stay tool-agnostic.
"""

from __future__ import annotations

import json
import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Optional


class ToolAdapter(ABC):
    """Base class for agentic tool configuration adapters."""

    # ── identity ────────────────────────────────────────────────────────────
    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable tool name, e.g. 'Claude Code'."""

    @property
    @abstractmethod
    def cli_name(self) -> str:
        """The executable name to detect, e.g. 'claude'."""

    @property
    @abstractmethod
    def slug(self) -> str:
        """Short identifier used in CLI flags, e.g. 'claude'."""

    # ── detection ───────────────────────────────────────────────────────────
    def is_installed(self) -> bool:
        return shutil.which(self.cli_name) is not None

    # ── paths ────────────────────────────────────────────────────────────────
    @abstractmethod
    def global_instruction_file(self) -> Path:
        """Path to the global instruction markdown file."""

    @abstractmethod
    def project_instruction_file(self, project_dir: Path) -> Path:
        """Path to the project-level instruction markdown file."""

    @abstractmethod
    def global_settings_file(self) -> Path:
        """Path to the global JSON/YAML settings file."""

    def project_settings_file(self, project_dir: Path) -> Optional[Path]:
        """Path to project-level settings file, or None if not supported."""
        return None

    @abstractmethod
    def global_commands_dir(self) -> Optional[Path]:
        """Directory for global slash commands / skills, or None if unsupported."""

    def project_commands_dir(self, project_dir: Path) -> Optional[Path]:
        """Directory for project-level slash commands, or None if unsupported."""
        return None

    # ── helpers ──────────────────────────────────────────────────────────────
    def _read_json(self, path: Path) -> dict:
        if path.exists():
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return {}
        return {}

    def _write_json(self, path: Path, data: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def _append_or_create_md(self, path: Path, heading: str, content: str) -> bool:
        """
        Append a named section to a markdown file.
        Returns True if the section was added, False if it already existed.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        marker = f"<!-- ailayer:{heading} -->"
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        if marker in existing:
            return False  # already present
        section = f"\n{marker}\n## {heading}\n\n{content}\n"
        with path.open("a", encoding="utf-8") as f:
            f.write(section)
        return True

    def _remove_md_section(self, path: Path, heading: str) -> bool:
        """Remove a previously injected section. Returns True if removed."""
        if not path.exists():
            return False
        marker = f"<!-- ailayer:{heading} -->"
        text = path.read_text(encoding="utf-8")
        if marker not in text:
            return False
        lines = text.splitlines(keepends=True)
        out, skip = [], False
        for line in lines:
            if marker in line:
                skip = True
            if skip and line.strip().startswith("## ") and marker not in line:
                skip = False
            if not skip:
                out.append(line)
        path.write_text("".join(out), encoding="utf-8")
        return True

    # ── abstract injection operations ────────────────────────────────────────
    @abstractmethod
    def add_instruction(self, content: str, label: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        """Inject a labelled instruction block. Returns True on success."""

    @abstractmethod
    def remove_instruction(self, label: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        """Remove a previously injected instruction block."""

    @abstractmethod
    def add_hook(
        self,
        name: str,
        command: str,
        event: str,
        matcher: Optional[str],
        *,
        global_scope: bool,
        project_dir: Optional[Path],
    ) -> bool:
        """Register a hook. Returns True on success."""

    @abstractmethod
    def remove_hook(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        """Remove a hook by name."""

    @abstractmethod
    def add_mcp(
        self,
        name: str,
        command: str,
        args: list[str],
        env: dict[str, str],
        *,
        global_scope: bool,
        project_dir: Optional[Path],
    ) -> bool:
        """Register an MCP server. Returns True on success."""

    @abstractmethod
    def remove_mcp(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        """Remove an MCP server entry."""

    @abstractmethod
    def add_skill(self, name: str, content: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        """Inject a skill (slash command or instruction section)."""

    @abstractmethod
    def remove_skill(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        """Remove a previously injected skill."""

    # ── status ───────────────────────────────────────────────────────────────
    @abstractmethod
    def status(self) -> dict[str, Any]:
        """Return a dict describing current config state for display."""
