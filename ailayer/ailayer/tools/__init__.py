"""Tool adapter registry."""

from __future__ import annotations

from typing import Optional

from ailayer.tools.base import ToolAdapter
from ailayer.tools.claude_code import ClaudeCodeAdapter
from ailayer.tools.codex import CodexAdapter
from ailayer.tools.gemini import GeminiAdapter

_ALL_ADAPTERS: list[ToolAdapter] = [
    ClaudeCodeAdapter(),
    CodexAdapter(),
    GeminiAdapter(),
]

_BY_SLUG: dict[str, ToolAdapter] = {a.slug: a for a in _ALL_ADAPTERS}


def all_adapters() -> list[ToolAdapter]:
    return list(_ALL_ADAPTERS)


def get_adapter(slug: str) -> Optional[ToolAdapter]:
    return _BY_SLUG.get(slug.lower())


def resolve_tools(tool_arg: str) -> list[ToolAdapter]:
    """
    Resolve the --tool flag value to a list of adapters.
    'all' returns every adapter; otherwise return the named one.
    Raises ValueError for unknown slugs.
    """
    if tool_arg.lower() == "all":
        return list(_ALL_ADAPTERS)
    adapter = get_adapter(tool_arg)
    if adapter is None:
        valid = ", ".join(a.slug for a in _ALL_ADAPTERS)
        raise ValueError(f"Unknown tool '{tool_arg}'. Valid options: all, {valid}")
    return [adapter]
