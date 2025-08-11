# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    email: str
    """The user's email address"""

    username: str
    """The user's unique username"""

    id: Optional[str] = None
    """The user's unique id"""

    created_at: Optional[datetime] = None
    """The timestamp when the user was created"""

    display_name: Optional[str] = None
    """The user's display name"""

    is_active: Optional[bool] = None
    """Whether the user is active"""

    is_delegate: Optional[bool] = None
    """Whether this user is a delegate service account"""

    updated_at: Optional[datetime] = None
    """The timestamp when the user was last updated"""
