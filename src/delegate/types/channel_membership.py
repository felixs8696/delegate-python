# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChannelMembership"]


class ChannelMembership(BaseModel):
    channel_id: str
    """The channel's id"""

    member_id: str
    """The member's id"""

    id: Optional[str] = None
    """The membership's unique id"""

    joined_at: Optional[datetime] = None
    """The timestamp when the user joined"""

    left_at: Optional[datetime] = None
    """The timestamp when the user left (if applicable)"""

    role: Optional[Literal["member", "admin", "owner"]] = None
    """The user's role in the channel (member, admin, owner)"""

    updated_at: Optional[datetime] = None
    """The timestamp when the membership was last updated"""
