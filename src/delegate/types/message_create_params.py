# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .text_content_param import TextContentParam
from .reasoning_content_param import ReasoningContentParam
from .tool_request_content_param import ToolRequestContentParam
from .tool_response_content_param import ToolResponseContentParam

__all__ = ["MessageCreateParams", "Content"]


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


Content: TypeAlias = Union[TextContentParam, ToolRequestContentParam, ToolResponseContentParam, ReasoningContentParam]
