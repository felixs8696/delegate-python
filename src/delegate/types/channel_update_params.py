# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ChannelUpdateParams"]


class ChannelUpdateParams(TypedDict, total=False):
    channel_metadata: Optional[Dict[str, object]]
    """Additional metadata for the channel"""

    description: Optional[str]
    """The channel description"""

    is_archived: Optional[bool]
    """Whether the channel is archived"""

    name: Optional[str]
    """The channel name"""
