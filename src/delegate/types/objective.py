# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Objective", "Channel"]


class Channel(BaseModel):
    id: Optional[str] = None
    """The channel's unique id"""

    channel_metadata: Optional[Dict[str, object]] = None
    """Additional metadata for the channel"""

    created_at: Optional[datetime] = None
    """The timestamp when the channel was created"""

    description: Optional[str] = None
    """The channel description"""

    is_archived: Optional[bool] = None
    """Whether the channel is archived"""

    is_group_chat: Optional[bool] = None
    """Whether this is a group chat"""

    is_objective_channel: Optional[bool] = None
    """Whether this channel is a special reserved channel for objectives"""

    is_private: Optional[bool] = None
    """Whether this channel is private"""

    name: Optional[str] = None
    """The channel name (required for regular channels, optional for group chats)"""

    updated_at: Optional[datetime] = None
    """The timestamp when the channel was last updated"""


class Objective(BaseModel):
    id: str

    channel: Optional[Channel] = None
    """Represents a channel in the system (can be a regular channel or group chat)."""

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    objective_channel_id: Optional[str] = None

    status: Optional[Literal["CANCELED", "COMPLETED", "FAILED", "RUNNING", "TERMINATED", "TIMED_OUT"]] = None

    status_reason: Optional[str] = None

    updated_at: Optional[datetime] = None
