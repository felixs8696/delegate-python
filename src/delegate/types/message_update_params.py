# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .text_content_param import TextContentParam
from .tool_request_content_param import ToolRequestContentParam
from .tool_response_content_param import ToolResponseContentParam

__all__ = ["MessageUpdateParams", "Content"]


class MessageUpdateParams(TypedDict, total=False):
    content: Required[Content]
    """The message content"""

    message_metadata: Optional[Dict[str, object]]
    """Additional metadata for the message (reactions, files, etc.)"""

    streaming_status: Optional[Literal["pending", "streaming", "completed", "failed"]]
    """Status of message streaming"""


Content: TypeAlias = Union[TextContentParam, ToolRequestContentParam, ToolResponseContentParam]
