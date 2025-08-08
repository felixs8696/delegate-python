# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChannelMessageUpdateParams"]


class ChannelMessageUpdateParams(TypedDict, total=False):
    content: Required[str]
    """The message content"""

    message_metadata: Optional[Dict[str, object]]
    """Additional metadata for the message (reactions, files, etc.)"""

    message_type: Optional[str]
    """The type of message (text, file, reaction, etc.)"""
