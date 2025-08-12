# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InterventionRequest"]


class InterventionRequest(BaseModel):
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
