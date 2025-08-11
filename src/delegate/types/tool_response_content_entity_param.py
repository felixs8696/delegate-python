# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolResponseContentEntityParam"]


class ToolResponseContentEntityParam(TypedDict, total=False):
    author: Required[Literal["system", "user", "assistant"]]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: Required[object]
    """The result of the tool."""

    name: Required[str]
    """The name of the tool that is being responded to."""

    tool_call_id: Required[str]
    """The ID of the tool call that is being responded to."""

    type: Literal["tool_response"]
    """The type of the message, in this case `tool_response`."""
