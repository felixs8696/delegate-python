# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .text_content_param import TextContentParam
from .tool_request_content_param import ToolRequestContentParam
from .tool_response_content_param import ToolResponseContentParam

__all__ = ["EventCreateParams", "Content"]


class EventCreateParams(TypedDict, total=False):
    content: Required[Content]
    """The event content"""

    objective_id: Required[str]
    """The objective id the event is for"""


Content: TypeAlias = Union[TextContentParam, ToolRequestContentParam, ToolResponseContentParam]
