# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompletedActivity"]


class CompletedActivity(BaseModel):
    completed_at: datetime
    """The timestamp when the activity was completed"""

    description: str
    """The description of the notification"""

    title: str
    """The title of the notification"""

    type: Optional[Literal["completed_activity"]] = None
    """The type of notification"""
