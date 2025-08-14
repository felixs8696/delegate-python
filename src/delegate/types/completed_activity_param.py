# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompletedActivityParam"]


class CompletedActivityParam(TypedDict, total=False):
    completed_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the activity was completed"""

    description: Required[str]
    """The description of the notification"""

    title: Required[str]
    """The title of the notification"""

    type: Literal["completed_activity"]
    """The type of notification"""
