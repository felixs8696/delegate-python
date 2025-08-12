# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .text_content_param import TextContentParam

__all__ = ["EventCreateParams", "Content", "ContentToolRequestContent", "ContentToolResponseContent"]


class EventCreateParams(TypedDict, total=False):
    content: Required[Content]
    """The event content"""

    objective_id: Required[str]
    """The objective id the event is for"""


class ContentToolRequestContent(TypedDict, total=False):
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


class ContentToolResponseContent(TypedDict, total=False):
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


Content: TypeAlias = Union[TextContentParam, ContentToolRequestContent, ContentToolResponseContent]
