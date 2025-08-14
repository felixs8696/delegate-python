# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_content import TextContent
from .tool_request_content import ToolRequestContent
from .tool_response_content import ToolResponseContent

__all__ = ["Event", "Content", "ContentReasoningContent"]


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
    Union[TextContent, ToolRequestContent, ToolResponseContent, ContentReasoningContent, None],
    PropertyInfo(discriminator="type"),
]


class Event(BaseModel):
    objective_id: str
    """ID of the objective this event belongs to"""

    id: Optional[str] = None
    """The event's unique id"""

    content: Optional[Content] = None
    """Event payload content, matching activity content schema"""

    created_at: Optional[datetime] = None
    """The timestamp when the event was created"""

    sequence_id: Optional[int] = None
    """Auto-incrementing sequence ID for reliable ordering"""
