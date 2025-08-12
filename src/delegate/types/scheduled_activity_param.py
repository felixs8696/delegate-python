# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScheduledActivityParam"]


class ScheduledActivityParam(TypedDict, total=False):
    description: Required[str]
    """The description of the notification"""

    scheduled_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the scheduled activity will be sent"""

    title: Required[str]
    """The title of the notification"""

    executed_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the scheduled activity was executed"""

    type: Literal["scheduled_activity"]
    """The type of notification"""
