# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScheduledActivity"]


class ScheduledActivity(BaseModel):
    description: str
    """The description of the notification"""

    scheduled_at: datetime
    """The timestamp when the scheduled activity will be sent"""

    title: str
    """The title of the notification"""

    executed_at: Optional[datetime] = None
    """The timestamp when the scheduled activity was executed"""

    type: Optional[Literal["scheduled_activity"]] = None
    """The type of notification"""
