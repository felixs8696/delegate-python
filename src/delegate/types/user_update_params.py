# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    display_name: Optional[str]
    """The user's display name"""

    email: Optional[str]
    """The user's email address"""

    is_active: Optional[bool]
    """Whether the user is active"""

    username: Optional[str]
    """The user's unique username"""
