"""
Gemini CLI adapter (google-gemini/gemini-cli).

Config locations:
  Project instructions : <project>/GEMINI.md
  Global instructions  : ~/.gemini/GEMINI.md
  Global settings      : ~/.gemini/settings.json
  MCP servers          : ~/.gemini/settings.json  →  mcpServers:
  Skills               : ~/.gemini/commands/<name>.md (global)
                         <project>/.gemini/commands/<name>.md (project)
  Hooks                : ~/.gemini/settings.json  →  hooks:

settings.json schema (ailayer-supported subset):
  {
    "theme": "Default",
    "selectedAuthType": "oauth-personal",
    "mcpServers": {
      "server_name": {
        "command": "npx",
        "args": ["-y", "@pkg/server"],
        "env": { "KEY": "VAL" }
      }
    },
    "hooks": {
      "beforeCommand": [{ "_ailayer_name": "lint", "command": "ruff check ." }],
      "afterCommand":  [{ "_ailayer_name": "test", "command": "pytest -x -q" }]
    }
  }
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Optional

from ailayer.tools.base import ToolAdapter

_HOOK_EVENT_ALIASES = {
    "pre": "beforeCommand",
    "pre-tool-use": "beforeCommand",
    "pretooluse": "beforeCommand",
    "post": "afterCommand",
    "post-tool-use": "afterCommand",
    "posttooluse": "afterCommand",
    "stop": "afterCommand",
    "notification": "afterCommand",
}


def _normalise_event(event: str) -> str:
    return _HOOK_EVENT_ALIASES.get(event.lower(), event)


class GeminiAdapter(ToolAdapter):

    @property
    def name(self) -> str:
        return "Gemini CLI"

    @property
    def cli_name(self) -> str:
        return "gemini"

    @property
    def slug(self) -> str:
        return "gemini"

    # ── paths ────────────────────────────────────────────────────────────────

    def global_instruction_file(self) -> Path:
        return Path.home() / ".gemini" / "GEMINI.md"

    def project_instruction_file(self, project_dir: Path) -> Path:
        return project_dir / "GEMINI.md"

    def global_settings_file(self) -> Path:
        return Path.home() / ".gemini" / "settings.json"

    def project_settings_file(self, project_dir: Path) -> Path:
        return project_dir / ".gemini" / "settings.json"

    def global_commands_dir(self) -> Path:
        return Path.home() / ".gemini" / "commands"

    def project_commands_dir(self, project_dir: Path) -> Path:
        return project_dir / ".gemini" / "commands"

    # ── instructions ─────────────────────────────────────────────────────────

    def _instruction_path(self, global_scope: bool, project_dir: Optional[Path]) -> Path:
        if global_scope:
            return self.global_instruction_file()
        return self.project_instruction_file(project_dir or Path.cwd())

    def _settings_path(self, global_scope: bool, project_dir: Optional[Path]) -> Path:
        if global_scope:
            return self.global_settings_file()
        return self.project_settings_file(project_dir or Path.cwd())

    def add_instruction(self, content: str, label: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._instruction_path(global_scope, project_dir)
        return self._append_or_create_md(path, label, content)

    def remove_instruction(self, label: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._instruction_path(global_scope, project_dir)
        return self._remove_md_section(path, label)

    # ── hooks ────────────────────────────────────────────────────────────────

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
        path = self._settings_path(global_scope, project_dir)
        cfg = self._read_json(path)
        hooks_cfg = cfg.setdefault("hooks", {})
        event_key = _normalise_event(event)
        event_list: list = hooks_cfg.setdefault(event_key, [])

        for entry in event_list:
            if entry.get("_ailayer_name") == name:
                return False

        event_list.append({"_ailayer_name": name, "command": command})
        self._write_json(path, cfg)
        return True

    def remove_hook(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._settings_path(global_scope, project_dir)
        cfg = self._read_json(path)
        hooks_cfg = cfg.get("hooks", {})
        changed = False
        for event_key, event_list in hooks_cfg.items():
            new_list = [e for e in event_list if e.get("_ailayer_name") != name]
            if len(new_list) < len(event_list):
                changed = True
            hooks_cfg[event_key] = new_list
        if changed:
            self._write_json(path, cfg)
        return changed

    # ── MCP servers ──────────────────────────────────────────────────────────

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
        path = self._settings_path(global_scope, project_dir)
        cfg = self._read_json(path)
        servers = cfg.setdefault("mcpServers", {})
        if name in servers:
            return False
        entry: dict[str, Any] = {"command": command}
        if args:
            entry["args"] = args
        if env:
            entry["env"] = env
        servers[name] = entry
        self._write_json(path, cfg)
        return True

    def remove_mcp(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._settings_path(global_scope, project_dir)
        cfg = self._read_json(path)
        servers = cfg.get("mcpServers", {})
        if name not in servers:
            return False
        del servers[name]
        self._write_json(path, cfg)
        return True

    # ── skills ───────────────────────────────────────────────────────────────

    def _commands_dir(self, global_scope: bool, project_dir: Optional[Path]) -> Path:
        if global_scope:
            return self.global_commands_dir()
        return self.project_commands_dir(project_dir or Path.cwd())

    def add_skill(self, name: str, content: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        cmd_dir = self._commands_dir(global_scope, project_dir)
        skill_file = cmd_dir / f"{name}.md"
        if skill_file.exists():
            return False
        skill_file.parent.mkdir(parents=True, exist_ok=True)
        skill_file.write_text(content, encoding="utf-8")
        return True

    def remove_skill(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        cmd_dir = self._commands_dir(global_scope, project_dir)
        skill_file = cmd_dir / f"{name}.md"
        if not skill_file.exists():
            return False
        skill_file.unlink()
        return True

    # ── status ───────────────────────────────────────────────────────────────

    def status(self) -> dict[str, Any]:
        cfg = self._read_json(self.global_settings_file())
        commands_dir = self.global_commands_dir()
        skills = []
        if commands_dir.exists():
            skills = [f.stem for f in sorted(commands_dir.glob("*.md"))]
        hooks_cfg = cfg.get("hooks", {})
        hook_count = sum(len(v) for v in hooks_cfg.values() if isinstance(v, list))
        return {
            "installed": self.is_installed(),
            "global_instruction_exists": self.global_instruction_file().exists(),
            "global_settings_exists": self.global_settings_file().exists(),
            "hooks": hook_count,
            "mcp_servers": list(cfg.get("mcpServers", {}).keys()),
            "global_skills": skills,
        }
