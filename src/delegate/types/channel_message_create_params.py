# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChannelMessageCreateParams"]


class ChannelMessageCreateParams(TypedDict, total=False):
    content: Required[str]
    """The message content"""

    message_metadata: Optional[Dict[str, object]]
    """Additional metadata for the message (reactions, files, etc.)"""

    message_type: str
    """The type of message (text, file, reaction, etc.)"""

    parent_message_id: Optional[str]
    """The parent message id if this is a reply"""
