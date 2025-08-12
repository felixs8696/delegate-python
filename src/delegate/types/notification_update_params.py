# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "NotificationUpdateParams",
    "Content",
    "ContentScheduledActivity",
    "ContentCompletedActivity",
    "ContentApprovalRequest",
    "ContentInterventionRequest",
]


class NotificationUpdateParams(TypedDict, total=False):
    content: Required[Content]
    """The updated notification content"""


class ContentScheduledActivity(TypedDict, total=False):
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


class ContentCompletedActivity(TypedDict, total=False):
    completed_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the activity was completed"""

    description: Required[str]
    """The description of the notification"""

    title: Required[str]
    """The title of the notification"""

    type: Literal["completed_activity"]
    """The type of notification"""


class ContentApprovalRequest(TypedDict, total=False):
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


class ContentInterventionRequest(TypedDict, total=False):
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


Content: TypeAlias = Union[
    ContentScheduledActivity, ContentCompletedActivity, ContentApprovalRequest, ContentInterventionRequest
]
