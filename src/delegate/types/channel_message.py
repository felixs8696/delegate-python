# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ChannelMessage"]


class ChannelMessage(BaseModel):
    author_id: str
    """The user who sent the message"""

    channel_id: str
    """The channel this message belongs to"""

    content: str
    """The message content"""

    id: Optional[str] = None
    """The message's unique id"""

    created_at: Optional[datetime] = None
    """The timestamp when the message was created"""

    is_deleted: Optional[bool] = None
    """Whether the message has been deleted"""

    message_metadata: Optional[Dict[str, object]] = None
    """Additional metadata for the message (reactions, files, etc.)"""

    message_type: Optional[str] = None
    """The type of message (text, file, reaction, etc.)"""

    parent_message_id: Optional[str] = None
    """The parent message id if this is a reply"""

    updated_at: Optional[datetime] = None
    """The timestamp when the message was last updated"""
