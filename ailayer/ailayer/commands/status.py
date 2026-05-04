"""
`ailayer status` — show current configuration state for all supported tools.
"""

from __future__ import annotations

import typer
from rich.panel import Panel
from rich.table import Table
from rich import box

from ailayer.console import console
from ailayer.tools import all_adapters

status_app = typer.Typer(help="Show configuration state for all agentic tools.")


@status_app.callback(invoke_without_command=True)
def status_cmd(ctx: typer.Context) -> None:
    """Display current hook, MCP, and skill state for all supported tools."""
    if ctx.invoked_subcommand is not None:
        return

    for adapter in all_adapters():
        s = adapter.status()
        installed_str = "[green]✅ installed[/green]" if s["installed"] else "[red]✗ not found[/red]"
        instr_str = "[green]✓[/green]" if s["global_instruction_exists"] else "[muted]—[/muted]"
        cfg_str = "[green]✓[/green]" if s["global_settings_exists"] else "[muted]—[/muted]"

        table = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))
        table.add_column("Key", style="dim", width=22)
        table.add_column("Value")

        table.add_row("Binary", installed_str)
        table.add_row("Global instruction file", instr_str)
        table.add_row("Global settings file", cfg_str)
        table.add_row("Hooks registered", str(s["hooks"]))

        mcp_val = ", ".join(s["mcp_servers"]) if s["mcp_servers"] else "[muted]none[/muted]"
        table.add_row("MCP servers", mcp_val)

        skills_val = ", ".join(s["global_skills"]) if s["global_skills"] else "[muted]none[/muted]"
        table.add_row("Global skills", skills_val)

        console.print(Panel(table, title=f"[bold magenta]{adapter.name}[/bold magenta]", expand=False))
