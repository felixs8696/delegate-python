# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ApprovalRequestParam"]


class ApprovalRequestParam(TypedDict, total=False):
    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the notification was created"""

    description: Required[str]
    """The description of the notification"""

    title: Required[str]
    """The title of the notification"""

    addressed: bool
    """Whether the approval request has been addressed"""

    addressed_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the approval request was addressed"""

    approved: Optional[bool]
    """Whether the approval request has been approved"""

    type: Literal["approval_request"]
    """The type of notification"""
