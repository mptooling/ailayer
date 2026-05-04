"""
OpenAI Codex CLI adapter.

The OpenAI Codex CLI (github.com/openai/codex) reads its project context from
AGENTS.md files and its user config from ~/.codex/config.yaml.

Config locations:
  Project instructions : <project>/AGENTS.md
  Global instructions  : ~/.codex/AGENTS.md  (custom convention, picked up via --instructions flag)
  Global config        : ~/.codex/config.yaml
  MCP servers          : ~/.codex/config.yaml  →  mcp_servers:
  Skills               : Injected as sections in AGENTS.md (no native slash-command system)
  Hooks                : ~/.codex/config.yaml  →  hooks:  (shell scripts run pre/post agent loop)

config.yaml schema (ailayer-supported subset):
  model: o3              # default model
  approval_mode: auto    # suggest | auto | full-auto
  hooks:
    pre_apply:           # list of shell commands run before file writes
      - name: lint
        command: "ruff check ."
    post_apply:          # list of shell commands run after file writes
      - name: test
        command: "pytest -x -q"
  mcp_servers:
    server_name:
      command: npx
      args: ["-y", "@pkg/server"]
      env:
        KEY: VAL
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import yaml  # PyYAML – listed as dependency

from ailayer.tools.base import ToolAdapter

_HOOK_EVENTS = {"pre_apply", "post_apply"}
_HOOK_EVENT_ALIASES = {
    "pre": "pre_apply",
    "pre-tool-use": "pre_apply",
    "pretoolusee": "pre_apply",
    "post": "post_apply",
    "post-tool-use": "post_apply",
    "posttooluse": "post_apply",
    "stop": "post_apply",  # map Stop → post_apply (closest equivalent)
}


def _normalise_event(event: str) -> str:
    return _HOOK_EVENT_ALIASES.get(event.lower(), event)


class CodexAdapter(ToolAdapter):

    @property
    def name(self) -> str:
        return "Codex CLI"

    @property
    def cli_name(self) -> str:
        return "codex"

    @property
    def slug(self) -> str:
        return "codex"

    # ── paths ────────────────────────────────────────────────────────────────

    def global_instruction_file(self) -> Path:
        return Path.home() / ".codex" / "AGENTS.md"

    def project_instruction_file(self, project_dir: Path) -> Path:
        return project_dir / "AGENTS.md"

    def global_settings_file(self) -> Path:
        return Path.home() / ".codex" / "config.yaml"

    def global_commands_dir(self) -> Optional[Path]:
        return None  # Codex CLI has no native slash command directory

    # ── YAML helpers ─────────────────────────────────────────────────────────

    def _read_yaml(self, path: Path) -> dict:
        if path.exists():
            try:
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                return data if isinstance(data, dict) else {}
            except yaml.YAMLError:
                return {}
        return {}

    def _write_yaml(self, path: Path, data: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.dump(data, default_flow_style=False, allow_unicode=True), encoding="utf-8")

    # ── instructions ─────────────────────────────────────────────────────────

    def _instruction_path(self, global_scope: bool, project_dir: Optional[Path]) -> Path:
        if global_scope:
            return self.global_instruction_file()
        return self.project_instruction_file(project_dir or Path.cwd())

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
        # Codex CLI hooks are global-only (config.yaml)
        path = self.global_settings_file()
        cfg = self._read_yaml(path)
        hooks_cfg = cfg.setdefault("hooks", {})
        event_key = _normalise_event(event)
        event_list: list = hooks_cfg.setdefault(event_key, [])

        for entry in event_list:
            if entry.get("name") == name:
                return False  # already registered

        event_list.append({"name": name, "command": command})
        self._write_yaml(path, cfg)
        return True

    def remove_hook(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self.global_settings_file()
        cfg = self._read_yaml(path)
        hooks_cfg = cfg.get("hooks", {})
        changed = False
        for event_key, event_list in hooks_cfg.items():
            new_list = [e for e in event_list if e.get("name") != name]
            if len(new_list) < len(event_list):
                changed = True
            hooks_cfg[event_key] = new_list
        if changed:
            self._write_yaml(path, cfg)
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
        path = self.global_settings_file()
        cfg = self._read_yaml(path)
        servers = cfg.setdefault("mcp_servers", {})
        if name in servers:
            return False
        entry: dict[str, Any] = {"command": command}
        if args:
            entry["args"] = args
        if env:
            entry["env"] = env
        servers[name] = entry
        self._write_yaml(path, cfg)
        return True

    def remove_mcp(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self.global_settings_file()
        cfg = self._read_yaml(path)
        servers = cfg.get("mcp_servers", {})
        if name not in servers:
            return False
        del servers[name]
        self._write_yaml(path, cfg)
        return True

    # ── skills ───────────────────────────────────────────────────────────────
    # Codex has no native slash-command system; we inject skills as labelled
    # sections in the AGENTS.md instruction file.

    def add_skill(self, name: str, content: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._instruction_path(global_scope, project_dir)
        return self._append_or_create_md(path, f"skill:{name}", content)

    def remove_skill(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._instruction_path(global_scope, project_dir)
        return self._remove_md_section(path, f"skill:{name}")

    # ── status ───────────────────────────────────────────────────────────────

    def status(self) -> dict[str, Any]:
        cfg = self._read_yaml(self.global_settings_file())
        hooks_cfg = cfg.get("hooks", {})
        hook_count = sum(len(v) for v in hooks_cfg.values() if isinstance(v, list))
        return {
            "installed": self.is_installed(),
            "global_instruction_exists": self.global_instruction_file().exists(),
            "global_settings_exists": self.global_settings_file().exists(),
            "hooks": hook_count,
            "mcp_servers": list(cfg.get("mcp_servers", {}).keys()),
            "global_skills": [],  # embedded in AGENTS.md, not enumerable separately
        }
