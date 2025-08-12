# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .approval_request import ApprovalRequest
from .completed_activity import CompletedActivity
from .scheduled_activity import ScheduledActivity
from .intervention_request import InterventionRequest

__all__ = ["NotificationUpdateResponse", "Content"]

Content: TypeAlias = Annotated[
    Union[ScheduledActivity, CompletedActivity, ApprovalRequest, InterventionRequest],
    PropertyInfo(discriminator="type"),
]


class NotificationUpdateResponse(BaseModel):
    id: str
    """The notification's unique id"""

    content: Content
    """The content of the notification.

    This content is not OpenAI compatible. These are notifications meant to be
    displayed to the user.
    """

    objective_id: str
    """ID of the objective this notification belongs to"""

    created_at: Optional[datetime] = None
    """The timestamp when the notification was created"""

    is_read: Optional[bool] = None
    """Whether the notification has been read by the user"""

    read_at: Optional[datetime] = None
    """The timestamp when the notification was read"""

    updated_at: Optional[datetime] = None
    """The timestamp when the notification was last updated"""
