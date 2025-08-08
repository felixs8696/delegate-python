# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BatchUpdateParams", "Updates"]


class BatchUpdateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The channel id"""

    updates: Required[Dict[str, Updates]]
    """The updates to apply to messages.

    The key is the message id and the value is the update request.
    """


class Updates(TypedDict, total=False):
    content: Required[str]
    """The message content"""

    message_metadata: Optional[Dict[str, object]]
    """Additional metadata for the message (reactions, files, etc.)"""

    message_type: Optional[str]
    """The type of message (text, file, reaction, etc.)"""
