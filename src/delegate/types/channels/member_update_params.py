# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    channel_id: Required[str]

    role: Required[Literal["member", "admin", "owner"]]
    """The user's new role in the channel (member, admin, owner)"""
