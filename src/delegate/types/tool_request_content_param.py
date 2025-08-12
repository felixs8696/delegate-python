# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolRequestContentParam"]


class ToolRequestContentParam(TypedDict, total=False):
    arguments: Required[Dict[str, object]]
    """The arguments to the tool."""

    author: Required[Literal["system", "user", "assistant"]]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    name: Required[str]
    """The name of the tool that is being requested."""

    tool_call_id: Required[str]
    """The ID of the tool call that is being requested."""

    type: Literal["tool_request"]
    """The type of the message, in this case `tool_request`."""
