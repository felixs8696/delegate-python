# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ChannelListParams"]


class ChannelListParams(TypedDict, total=False):
    is_group_chat: Optional[bool]

    is_private: Optional[bool]

    limit: Optional[int]
