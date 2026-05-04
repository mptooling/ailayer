"""
`ailayer list` subcommands.

  ailayer list tools    — show all supported tools and whether they're installed
  ailayer list skills   — show all skills from the library
"""

from __future__ import annotations

import typer
from rich.table import Table

from ailayer.console import console, err
from ailayer.library import list_skills
from ailayer.tools import all_adapters

list_app = typer.Typer(help="List available tools or library skills.")


@list_app.command("tools")
def list_tools() -> None:
    """Show all supported agentic tools and their detection status."""
    table = Table(title="Supported Agentic Tools", show_header=True, header_style="bold cyan")
    table.add_column("Tool", style="bold")
    table.add_column("CLI Binary")
    table.add_column("Installed")
    table.add_column("Hooks support")
    table.add_column("MCP support")
    table.add_column("Skills / Commands")

    feature_map = {
        "claude": ("✓ PreToolUse, PostToolUse, Stop, Notification", "✓ mcpServers", "✓ ~/.claude/commands/"),
        "codex":  ("✓ pre_apply, post_apply", "✓ mcp_servers", "via AGENTS.md sections"),
        "gemini": ("✓ beforeCommand, afterCommand", "✓ mcpServers", "✓ ~/.gemini/commands/"),
    }

    for adapter in all_adapters():
        installed = "✅ yes" if adapter.is_installed() else "✗ not found"
        hooks, mcp, skills = feature_map.get(adapter.slug, ("-", "-", "-"))
        table.add_row(adapter.name, adapter.cli_name, installed, hooks, mcp, skills)

    console.print(table)


@list_app.command("skills")
def list_skills_cmd(
    category: str = typer.Option("", "--category", "-c", help="Filter by category keyword"),
) -> None:
    """Show all skills available in the ai_skills_and_tools library."""
    try:
        skills = list_skills()
    except RuntimeError as exc:
        err(str(exc))
        raise typer.Exit(1)

    if category:
        skills = [s for s in skills if category.lower() in s.category.lower()]

    if not skills:
        console.print("[muted]No skills found.[/muted]")
        return

    table = Table(title="Library Skills", show_header=True, header_style="bold cyan")
    table.add_column("Name", style="bold blue")
    table.add_column("Category")
    table.add_column("Summary", max_width=60)

    for skill in skills:
        table.add_row(skill.name, skill.category, skill.summary)

    console.print(table)
    console.print(f"\n[muted]{len(skills)} skill(s). Use [bold]ailayer add skill <name>[/bold] to install.[/muted]")
