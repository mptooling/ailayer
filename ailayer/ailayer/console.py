"""Shared Rich console and output helpers."""

from rich.console import Console
from rich.theme import Theme

THEME = Theme(
    {
        "success": "bold green",
        "error": "bold red",
        "warning": "bold yellow",
        "info": "bold cyan",
        "muted": "dim",
        "tool": "bold magenta",
        "skill": "bold blue",
    }
)

console = Console(theme=THEME)


def ok(msg: str) -> None:
    console.print(f"[success]✓[/success] {msg}")


def err(msg: str) -> None:
    console.print(f"[error]✗[/error] {msg}")


def warn(msg: str) -> None:
    console.print(f"[warning]⚠[/warning] {msg}")


def info(msg: str) -> None:
    console.print(f"[info]→[/info] {msg}")
