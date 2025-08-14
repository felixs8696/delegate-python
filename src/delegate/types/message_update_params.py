# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .text_content_param import TextContentParam
from .tool_request_content_param import ToolRequestContentParam
from .tool_response_content_param import ToolResponseContentParam

__all__ = ["MessageUpdateParams", "Content", "ContentReasoningContent"]


class MessageUpdateParams(TypedDict, total=False):
    content: Required[Content]
    """The message content"""

    message_metadata: Optional[Dict[str, object]]
    """Additional metadata for the message (reactions, files, etc.)"""

    streaming_status: Optional[Literal["pending", "streaming", "completed", "failed"]]
    """Status of message streaming"""


class ContentReasoningContent(TypedDict, total=False):
    author: Required[Literal["system", "user", "assistant"]]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: Required[str]
    """The reasoning content or chain-of-thought text"""

    reasoning_id: Optional[str]
    """The ID of the reasoning item"""

    summary: Optional[str]
    """A short reasoning summary"""

    type: Literal["reasoning"]
    """The type of the message, in this case `reasoning`."""

    usage: Optional[Dict[str, object]]
    """Usage information for reasoning tokens"""


Content: TypeAlias = Union[TextContentParam, ToolRequestContentParam, ToolResponseContentParam, ContentReasoningContent]
