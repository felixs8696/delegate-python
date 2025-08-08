# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .data_content_entity import DataContentEntity
from .text_content_entity import TextContentEntity
from .tool_request_content_entity import ToolRequestContentEntity
from .tool_response_content_entity import ToolResponseContentEntity

__all__ = ["ObjectiveActivity", "Content"]

Content: TypeAlias = Union[TextContentEntity, ToolRequestContentEntity, ToolResponseContentEntity, DataContentEntity]


class ObjectiveActivity(BaseModel):
    content: Content
    """The content of the activity.

    This content is not OpenAI compatible. These are activities meant to be
    displayed to the user.
    """

    objective_id: str
    """ID of the objective this activity belongs to"""

    id: Optional[str] = None
    """The objective activity's unique id"""

    created_at: Optional[datetime] = None
    """The timestamp when the activity was created"""

    streaming_status: Optional[Literal["IN_PROGRESS", "DONE"]] = None

    updated_at: Optional[datetime] = None
    """The timestamp when the activity was last updated"""
