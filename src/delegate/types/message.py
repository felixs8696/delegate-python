# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_content import TextContent
from .tool_request_content import ToolRequestContent
from .tool_response_content import ToolResponseContent

__all__ = ["Message", "Content", "ContentReasoningContent"]


class ContentReasoningContent(BaseModel):
    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: str
    """The reasoning content or chain-of-thought text"""

    reasoning_id: Optional[str] = None
    """The ID of the reasoning item"""

    summary: Optional[str] = None
    """A short reasoning summary"""

    type: Optional[Literal["reasoning"]] = None
    """The type of the message, in this case `reasoning`."""

    usage: Optional[Dict[str, object]] = None
    """Usage information for reasoning tokens"""


Content: TypeAlias = Annotated[
    Union[TextContent, ToolRequestContent, ToolResponseContent, ContentReasoningContent],
    PropertyInfo(discriminator="type"),
]


class Message(BaseModel):
    author_id: str
    """The user who sent the message"""

    channel_id: str
    """The channel this message belongs to"""

    content: Content
    """The message content"""

    id: Optional[str] = None
    """The message's unique id"""

    created_at: Optional[datetime] = None
    """The timestamp when the message was created"""

    is_deleted: Optional[bool] = None
    """Whether the message has been deleted"""

    message_metadata: Optional[Dict[str, object]] = None
    """Additional metadata for the message (reactions, files, etc.)"""

    parent_message_id: Optional[str] = None
    """The parent message id if this is a reply"""

    streaming_status: Optional[Literal["pending", "streaming", "completed", "failed"]] = None
    """Status of message streaming"""

    updated_at: Optional[datetime] = None
    """The timestamp when the message was last updated"""
