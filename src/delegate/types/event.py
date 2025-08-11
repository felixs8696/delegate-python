# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .text_content_entity import TextContentEntity
from .tool_request_content_entity import ToolRequestContentEntity
from .tool_response_content_entity import ToolResponseContentEntity

__all__ = ["Event", "Content"]

Content: TypeAlias = Annotated[
    Union[TextContentEntity, ToolRequestContentEntity, ToolResponseContentEntity, None],
    PropertyInfo(discriminator="type"),
]


class Event(BaseModel):
    objective_id: str
    """ID of the objective this event belongs to"""

    id: Optional[str] = None
    """The event's unique id"""

    content: Optional[Content] = None
    """Event payload content, matching activity content schema"""

    created_at: Optional[datetime] = None
    """The timestamp when the event was created"""

    sequence_id: Optional[int] = None
    """Auto-incrementing sequence ID for reliable ordering"""
