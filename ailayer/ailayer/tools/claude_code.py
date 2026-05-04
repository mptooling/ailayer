"""
Claude Code adapter.

Config locations:
  Global instructions : ~/.claude/CLAUDE.md
  Project instructions: <project>/CLAUDE.md
  Global settings     : ~/.claude/settings.json
  Project settings    : <project>/.claude/settings.json  (or settings.local.json)
  Global commands     : ~/.claude/commands/<name>.md
  Project commands    : <project>/.claude/commands/<name>.md

Hook format in settings.json:
  {
    "hooks": {
      "PreToolUse":  [{"matcher": "Bash", "hooks": [{"type": "command", "command": "..."}]}],
      "PostToolUse": [...],
      "Stop":        [...],
      "Notification":[...]
    }
  }

MCP format in settings.json:
  {
    "mcpServers": {
      "server_name": {
        "command": "npx",
        "args": ["-y", "@pkg/server"],
        "env": {"KEY": "VAL"}
      }
    }
  }
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Optional

from ailayer.tools.base import ToolAdapter

_HOOK_EVENTS = {"PreToolUse", "PostToolUse", "Stop", "Notification"}
_HOOK_EVENT_ALIASES = {
    "pre": "PreToolUse",
    "pre-tool-use": "PreToolUse",
    "post": "PostToolUse",
    "post-tool-use": "PostToolUse",
    "stop": "Stop",
    "notification": "Notification",
}


def _normalise_event(event: str) -> str:
    return _HOOK_EVENT_ALIASES.get(event.lower(), event)


class ClaudeCodeAdapter(ToolAdapter):

    @property
    def name(self) -> str:
        return "Claude Code"

    @property
    def cli_name(self) -> str:
        return "claude"

    @property
    def slug(self) -> str:
        return "claude"

    # ── paths ────────────────────────────────────────────────────────────────

    def global_instruction_file(self) -> Path:
        return Path.home() / ".claude" / "CLAUDE.md"

    def project_instruction_file(self, project_dir: Path) -> Path:
        return project_dir / "CLAUDE.md"

    def global_settings_file(self) -> Path:
        return Path.home() / ".claude" / "settings.json"

    def project_settings_file(self, project_dir: Path) -> Path:
        return project_dir / ".claude" / "settings.json"

    def global_commands_dir(self) -> Path:
        return Path.home() / ".claude" / "commands"

    def project_commands_dir(self, project_dir: Path) -> Path:
        return project_dir / ".claude" / "commands"

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

    def _settings_path(self, global_scope: bool, project_dir: Optional[Path]) -> Path:
        if global_scope:
            return self.global_settings_file()
        return self.project_settings_file(project_dir or Path.cwd())

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
        event = _normalise_event(event)
        path = self._settings_path(global_scope, project_dir)
        cfg = self._read_json(path)
        hooks_cfg = cfg.setdefault("hooks", {})
        event_list: list = hooks_cfg.setdefault(event, [])

        # Guard: don't duplicate by name tag
        for entry in event_list:
            for h in entry.get("hooks", []):
                if h.get("_ailayer_name") == name:
                    return False  # already registered

        hook_entry: dict[str, Any] = {
            "hooks": [{"type": "command", "command": command, "_ailayer_name": name}]
        }
        if matcher:
            hook_entry["matcher"] = matcher

        event_list.append(hook_entry)
        self._write_json(path, cfg)
        return True

    def remove_hook(self, name: str, *, global_scope: bool, project_dir: Optional[Path]) -> bool:
        path = self._settings_path(global_scope, project_dir)
        cfg = self._read_json(path)
        hooks_cfg = cfg.get("hooks", {})
        changed = False
        for event_key, event_list in hooks_cfg.items():
            new_list = []
            for entry in event_list:
                new_hooks = [h for h in entry.get("hooks", []) if h.get("_ailayer_name") != name]
                if len(new_hooks) < len(entry.get("hooks", [])):
                    changed = True
                if new_hooks:
                    entry = copy.deepcopy(entry)
                    entry["hooks"] = new_hooks
                    new_list.append(entry)
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
            return False  # already registered
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

    # ── skills (slash commands) ───────────────────────────────────────────────

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
        global_instruction = self.global_instruction_file()
        commands_dir = self.global_commands_dir()

        skills = []
        if commands_dir.exists():
            skills = [f.stem for f in sorted(commands_dir.glob("*.md"))]

        hook_count = sum(
            len(lst) for lst in cfg.get("hooks", {}).values()
        )
        mcp_count = len(cfg.get("mcpServers", {}))

        return {
            "installed": self.is_installed(),
            "global_instruction_exists": global_instruction.exists(),
            "global_settings_exists": self.global_settings_file().exists(),
            "hooks": hook_count,
            "mcp_servers": list(cfg.get("mcpServers", {}).keys()),
            "global_skills": skills,
        }
