# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolRequestContentEntity"]


class ToolRequestContentEntity(BaseModel):
    tool_request: Dict[str, object]
    """The tool request content of the activity"""

    type: Optional[Literal["tool_request"]] = None
    """Tool request content type"""
