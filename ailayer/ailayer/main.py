"""
ailayer — AI tool configuration layer CLI.

Inject skills, hooks, MCP servers, and instruction files into agentic coding tools
(Claude Code, Codex CLI, Gemini CLI) from your ai_skills_and_tools library.

Usage:
  ailayer status
  ailayer list tools
  ailayer list skills
  ailayer add skill langchain --tool claude
  ailayer add hook lint --event pre --command "ruff check ." --tool all
  ailayer add mcp filesystem --cmd npx --args "-y,@modelcontextprotocol/server-filesystem" --tool claude
  ailayer add instruction my-style --file ./style-guide.md --tool all
  ailayer remove skill langchain --tool claude
"""

from __future__ import annotations

import typer
from rich.console import Console

from ailayer.commands.add import add_app
from ailayer.commands.list import list_app
from ailayer.commands.remove import remove_app
from ailayer.commands.status import status_app

__version__ = "0.1.0-alpha"

app = typer.Typer(
    name="ailayer",
    help="Inject skills, hooks, MCP servers, and instructions into agentic coding tools.",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)

app.add_typer(add_app, name="add")
app.add_typer(remove_app, name="remove")
app.add_typer(list_app, name="list")
app.add_typer(status_app, name="status")


@app.callback()
def main_callback(
    version: bool = typer.Option(False, "--version", "-v", help="Print version and exit", is_eager=True),
) -> None:
    if version:
        Console().print(f"ailayer {__version__}")
        raise typer.Exit()


def main() -> None:
    app()


if __name__ == "__main__":
    main()
