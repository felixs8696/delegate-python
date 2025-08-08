# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..channel_membership import ChannelMembership

__all__ = ["MemberListResponse"]

MemberListResponse: TypeAlias = List[ChannelMembership]
