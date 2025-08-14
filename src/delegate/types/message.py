# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_content import TextContent
from .reasoning_content import ReasoningContent
from .tool_request_content import ToolRequestContent
from .tool_response_content import ToolResponseContent

__all__ = ["Message", "Content"]

Content: TypeAlias = Annotated[
    Union[TextContent, ToolRequestContent, ToolResponseContent, ReasoningContent], PropertyInfo(discriminator="type")
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
