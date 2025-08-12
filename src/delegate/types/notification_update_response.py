# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "NotificationUpdateResponse",
    "Content",
    "ContentScheduledActivity",
    "ContentCompletedActivity",
    "ContentApprovalRequest",
    "ContentInterventionRequest",
]


class ContentScheduledActivity(BaseModel):
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


class ContentCompletedActivity(BaseModel):
    completed_at: datetime
    """The timestamp when the activity was completed"""

    description: str
    """The description of the notification"""

    title: str
    """The title of the notification"""

    type: Optional[Literal["completed_activity"]] = None
    """The type of notification"""


class ContentApprovalRequest(BaseModel):
    created_at: datetime
    """The timestamp when the notification was created"""

    description: str
    """The description of the notification"""

    title: str
    """The title of the notification"""

    addressed: Optional[bool] = None
    """Whether the approval request has been addressed"""

    addressed_at: Optional[datetime] = None
    """The timestamp when the approval request was addressed"""

    approved: Optional[bool] = None
    """Whether the approval request has been approved"""

    type: Optional[Literal["approval_request"]] = None
    """The type of notification"""


class ContentInterventionRequest(BaseModel):
    created_at: datetime
    """The timestamp when the notification was created"""

    description: str
    """The description of the notification"""

    title: str
    """The title of the notification"""

    addressed: Optional[bool] = None
    """Whether the intervention request has been addressed"""

    addressed_at: Optional[datetime] = None
    """The timestamp when the intervention request was addressed"""

    type: Optional[Literal["intervention_request"]] = None
    """The type of notification"""


Content: TypeAlias = Annotated[
    Union[ContentScheduledActivity, ContentCompletedActivity, ContentApprovalRequest, ContentInterventionRequest],
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
