# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InterventionRequestParam"]


class InterventionRequestParam(TypedDict, total=False):
    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the notification was created"""

    description: Required[str]
    """The description of the notification"""

    title: Required[str]
    """The title of the notification"""

    addressed: bool
    """Whether the intervention request has been addressed"""

    addressed_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the intervention request was addressed"""

    type: Literal["intervention_request"]
    """The type of notification"""
