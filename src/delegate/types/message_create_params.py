# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "MessageCreateParams",
    "Content",
    "ContentTextContentEntity",
    "ContentToolRequestContentEntity",
    "ContentToolResponseContentEntity",
]


class MessageCreateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The channel this message belongs to"""

    content: Required[Content]
    """The message content"""

    message_metadata: Optional[Dict[str, object]]
    """Additional metadata for the message (reactions, files, etc.)"""

    parent_message_id: Optional[str]
    """The parent message id if this is a reply"""

    streaming_status: Optional[Literal["pending", "streaming", "completed", "failed"]]
    """Status of message streaming"""


class ContentTextContentEntity(TypedDict, total=False):
    author: Required[Literal["system", "user", "assistant"]]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: Required[str]
    """The contents of the text message."""

    type: Literal["text"]
    """The type of the message, in this case `text`."""


class ContentToolRequestContentEntity(TypedDict, total=False):
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


class ContentToolResponseContentEntity(TypedDict, total=False):
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


Content: TypeAlias = Union[ContentTextContentEntity, ContentToolRequestContentEntity, ContentToolResponseContentEntity]
