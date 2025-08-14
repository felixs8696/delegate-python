# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .approval_request_param import ApprovalRequestParam
from .completed_activity_param import CompletedActivityParam
from .scheduled_activity_param import ScheduledActivityParam
from .intervention_request_param import InterventionRequestParam

__all__ = ["NotificationUpdateParams", "Content"]


class NotificationUpdateParams(TypedDict, total=False):
    content: Required[Content]
    """The updated notification content"""


Content: TypeAlias = Union[
    ScheduledActivityParam, CompletedActivityParam, ApprovalRequestParam, InterventionRequestParam
]
