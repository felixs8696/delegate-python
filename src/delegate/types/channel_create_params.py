# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ChannelCreateParams"]


class ChannelCreateParams(TypedDict, total=False):
    channel_metadata: Optional[Dict[str, object]]
    """Additional metadata for the channel"""

    description: Optional[str]
    """The channel description"""

    is_group_chat: bool
    """Whether this is a group chat"""

    is_private: bool
    """Whether this channel is private"""

    name: Optional[str]
    """The channel name (required for regular channels, optional for group chats)"""
