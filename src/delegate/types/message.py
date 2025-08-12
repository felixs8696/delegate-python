# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Message",
    "Content",
    "ContentTextContentEntity",
    "ContentToolRequestContentEntity",
    "ContentToolResponseContentEntity",
]


class ContentTextContentEntity(BaseModel):
    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: str
    """The contents of the text message."""

    type: Optional[Literal["text"]] = None
    """The type of the message, in this case `text`."""


class ContentToolRequestContentEntity(BaseModel):
    arguments: Dict[str, object]
    """The arguments to the tool."""

    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    name: str
    """The name of the tool that is being requested."""

    tool_call_id: str
    """The ID of the tool call that is being requested."""

    type: Optional[Literal["tool_request"]] = None
    """The type of the message, in this case `tool_request`."""


class ContentToolResponseContentEntity(BaseModel):
    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: object
    """The result of the tool."""

    name: str
    """The name of the tool that is being responded to."""

    tool_call_id: str
    """The ID of the tool call that is being responded to."""

    type: Optional[Literal["tool_response"]] = None
    """The type of the message, in this case `tool_response`."""


Content: TypeAlias = Annotated[
    Union[ContentTextContentEntity, ContentToolRequestContentEntity, ContentToolResponseContentEntity],
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
