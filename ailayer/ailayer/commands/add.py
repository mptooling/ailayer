"""
`ailayer add` subcommands.

  ailayer add instruction <label> [--content TEXT | --file PATH] [--tool SLUG] [--global | --project DIR]
  ailayer add hook <name> --event EVENT --command CMD [--matcher MATCHER] [--tool SLUG] [--global | --project DIR]
  ailayer add mcp <name> --cmd CMD [--args ARGS] [--env KEY=VAL] [--tool SLUG] [--global | --project DIR]
  ailayer add skill <library-name> [--tool SLUG] [--global | --project DIR]
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

import typer

from ailayer.console import console, err, info, ok, warn
from ailayer.library import get_skill
from ailayer.tools import resolve_tools

add_app = typer.Typer(help="Inject instructions, hooks, MCP servers, or skills into an agentic tool.")

# ── shared option factory ────────────────────────────────────────────────────

_TOOL_HELP = "Target tool: claude | codex | gemini | all  (default: all)"
_GLOBAL_HELP = "Apply globally (~/.tool config). Default when no --project is given."
_PROJECT_HELP = "Apply to a specific project directory."


def _resolve(tool_arg: str) -> list:
    try:
        return resolve_tools(tool_arg)
    except ValueError as exc:
        err(str(exc))
        raise typer.Exit(1)


def _scope(global_flag: bool, project: Optional[Path]):
    """Return (global_scope, project_dir)."""
    if project is not None:
        return False, project.resolve()
    return True, None  # default to global


# ── add instruction ──────────────────────────────────────────────────────────

@add_app.command("instruction")
def add_instruction(
    label: str = typer.Argument(..., help="Unique label for the instruction block, e.g. 'python-style-guide'"),
    content: Optional[str] = typer.Option(None, "--content", "-c", help="Instruction text (inline)"),
    file: Optional[Path] = typer.Option(None, "--file", "-f", help="Read instruction text from a file"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global", help=_GLOBAL_HELP),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help=_PROJECT_HELP),
) -> None:
    """Inject a labelled instruction block into the tool's markdown context file."""
    if content is None and file is None:
        err("Provide --content TEXT or --file PATH.")
        raise typer.Exit(1)
    if file is not None:
        if not file.exists():
            err(f"File not found: {file}")
            raise typer.Exit(1)
        content = file.read_text(encoding="utf-8")

    global_scope, project_dir = _scope(global_flag, project)
    adapters = _resolve(tool)

    for adapter in adapters:
        added = adapter.add_instruction(content, label, global_scope=global_scope, project_dir=project_dir)
        if added:
            ok(f"[tool]{adapter.name}[/tool] — instruction '{label}' added")
        else:
            warn(f"[tool]{adapter.name}[/tool] — instruction '{label}' already present (skipped)")


# ── add hook ─────────────────────────────────────────────────────────────────

@add_app.command("hook")
def add_hook(
    name: str = typer.Argument(..., help="Unique hook name, e.g. 'lint-before-write'"),
    event: str = typer.Option(..., "--event", "-e", help="Hook event: pre | post | stop | notification"),
    command: str = typer.Option(..., "--command", "-c", help="Shell command to execute"),
    matcher: Optional[str] = typer.Option(None, "--matcher", "-m", help="Tool matcher (Claude Code only), e.g. 'Bash'"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global", help=_GLOBAL_HELP),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help=_PROJECT_HELP),
) -> None:
    """Register a pre/post hook command in the tool's config."""
    global_scope, project_dir = _scope(global_flag, project)
    adapters = _resolve(tool)

    for adapter in adapters:
        added = adapter.add_hook(
            name, command, event, matcher,
            global_scope=global_scope, project_dir=project_dir
        )
        if added:
            ok(f"[tool]{adapter.name}[/tool] — hook '{name}' ({event}) added")
        else:
            warn(f"[tool]{adapter.name}[/tool] — hook '{name}' already registered (skipped)")


# ── add mcp ──────────────────────────────────────────────────────────────────

@add_app.command("mcp")
def add_mcp(
    name: str = typer.Argument(..., help="MCP server identifier, e.g. 'filesystem'"),
    cmd: str = typer.Option(..., "--cmd", help="Executable to run, e.g. 'npx'"),
    args: Optional[str] = typer.Option(None, "--args", "-a", help="Comma-separated args, e.g. '-y,@pkg/server'"),
    env: Optional[List[str]] = typer.Option(None, "--env", help="Environment variable KEY=VAL (repeatable)"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global", help=_GLOBAL_HELP),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help=_PROJECT_HELP),
) -> None:
    """Register an MCP server in the tool's config."""
    args_list = [a.strip() for a in args.split(",")] if args else []
    env_dict: dict[str, str] = {}
    for kv in (env or []):
        if "=" not in kv:
            err(f"Invalid --env value '{kv}'. Use KEY=VAL format.")
            raise typer.Exit(1)
        k, v = kv.split("=", 1)
        env_dict[k.strip()] = v.strip()

    global_scope, project_dir = _scope(global_flag, project)
    adapters = _resolve(tool)

    for adapter in adapters:
        added = adapter.add_mcp(
            name, cmd, args_list, env_dict,
            global_scope=global_scope, project_dir=project_dir
        )
        if added:
            ok(f"[tool]{adapter.name}[/tool] — MCP server '{name}' added")
        else:
            warn(f"[tool]{adapter.name}[/tool] — MCP server '{name}' already registered (skipped)")


# ── add skill ────────────────────────────────────────────────────────────────

@add_app.command("skill")
def add_skill(
    skill_name: str = typer.Argument(..., help="Skill name from the library, e.g. 'langchain'"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global", help=_GLOBAL_HELP),
    project: Optional[Path] = typer.Option(None, "--project", "-p", help=_PROJECT_HELP),
) -> None:
    """Inject a skill from the ai_skills_and_tools library into the tool's skill/command system."""
    skill = get_skill(skill_name)
    if skill is None:
        err(f"Skill '{skill_name}' not found in the library.")
        info("Run [bold]ailayer list skills[/bold] to see available skills.")
        raise typer.Exit(1)

    info(f"Found skill: [skill]{skill.name}[/skill] ({skill.category})")
    global_scope, project_dir = _scope(global_flag, project)
    adapters = _resolve(tool)

    for adapter in adapters:
        added = adapter.add_skill(
            skill.name, skill.skill_prompt(),
            global_scope=global_scope, project_dir=project_dir
        )
        if added:
            ok(f"[tool]{adapter.name}[/tool] — skill '{skill.name}' installed")
        else:
            warn(f"[tool]{adapter.name}[/tool] — skill '{skill.name}' already installed (skipped)")
