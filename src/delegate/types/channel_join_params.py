# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ChannelJoinParams"]


class ChannelJoinParams(TypedDict, total=False):
    role: Literal["member", "admin", "owner"]
    """The user's role in the channel (member, admin, owner)"""
