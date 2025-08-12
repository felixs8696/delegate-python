# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    channel_id: Required[str]

    limit: Optional[int]

    parent_message_id: Optional[str]
