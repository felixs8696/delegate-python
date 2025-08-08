# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolResponseContentEntity"]


class ToolResponseContentEntity(BaseModel):
    tool_response: Dict[str, object]
    """The tool response content of the activity"""

    type: Optional[Literal["tool_response"]] = None
    """Tool response content type"""
