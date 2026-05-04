"""
`ailayer remove` subcommands.

  ailayer remove instruction <label> [--tool SLUG] [--global | --project DIR]
  ailayer remove hook <name> [--tool SLUG] [--global | --project DIR]
  ailayer remove mcp <name> [--tool SLUG] [--global | --project DIR]
  ailayer remove skill <name> [--tool SLUG] [--global | --project DIR]
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from ailayer.console import err, ok, warn
from ailayer.tools import resolve_tools

remove_app = typer.Typer(help="Remove previously injected instructions, hooks, MCP servers, or skills.")

_TOOL_HELP = "Target tool: claude | codex | gemini | all"


def _resolve(tool_arg: str) -> list:
    try:
        return resolve_tools(tool_arg)
    except ValueError as exc:
        err(str(exc))
        raise typer.Exit(1)


def _scope(global_flag: bool, project: Optional[Path]):
    if project is not None:
        return False, project.resolve()
    return True, None


@remove_app.command("instruction")
def remove_instruction(
    label: str = typer.Argument(..., help="Label of the instruction block to remove"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global"),
    project: Optional[Path] = typer.Option(None, "--project", "-p"),
) -> None:
    """Remove a labelled instruction block."""
    global_scope, project_dir = _scope(global_flag, project)
    for adapter in _resolve(tool):
        removed = adapter.remove_instruction(label, global_scope=global_scope, project_dir=project_dir)
        if removed:
            ok(f"{adapter.name} — instruction '{label}' removed")
        else:
            warn(f"{adapter.name} — instruction '{label}' not found (skipped)")


@remove_app.command("hook")
def remove_hook(
    name: str = typer.Argument(..., help="Name of the hook to remove"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global"),
    project: Optional[Path] = typer.Option(None, "--project", "-p"),
) -> None:
    """Remove a registered hook."""
    global_scope, project_dir = _scope(global_flag, project)
    for adapter in _resolve(tool):
        removed = adapter.remove_hook(name, global_scope=global_scope, project_dir=project_dir)
        if removed:
            ok(f"{adapter.name} — hook '{name}' removed")
        else:
            warn(f"{adapter.name} — hook '{name}' not found (skipped)")


@remove_app.command("mcp")
def remove_mcp(
    name: str = typer.Argument(..., help="MCP server name to remove"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global"),
    project: Optional[Path] = typer.Option(None, "--project", "-p"),
) -> None:
    """Remove a registered MCP server."""
    global_scope, project_dir = _scope(global_flag, project)
    for adapter in _resolve(tool):
        removed = adapter.remove_mcp(name, global_scope=global_scope, project_dir=project_dir)
        if removed:
            ok(f"{adapter.name} — MCP server '{name}' removed")
        else:
            warn(f"{adapter.name} — MCP server '{name}' not found (skipped)")


@remove_app.command("skill")
def remove_skill(
    skill_name: str = typer.Argument(..., help="Skill name to remove"),
    tool: str = typer.Option("all", "--tool", "-t", help=_TOOL_HELP),
    global_flag: bool = typer.Option(True, "--global/--no-global"),
    project: Optional[Path] = typer.Option(None, "--project", "-p"),
) -> None:
    """Remove an installed skill."""
    global_scope, project_dir = _scope(global_flag, project)
    for adapter in _resolve(tool):
        removed = adapter.remove_skill(skill_name, global_scope=global_scope, project_dir=project_dir)
        if removed:
            ok(f"{adapter.name} — skill '{skill_name}' removed")
        else:
            warn(f"{adapter.name} — skill '{skill_name}' not found (skipped)")
