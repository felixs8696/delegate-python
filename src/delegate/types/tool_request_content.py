# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolRequestContent"]


class ToolRequestContent(BaseModel):
    arguments: Dict[str, object]
    """The arguments to the tool."""

    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    name: str
    """The name of the tool that is being requested."""

    tool_call_id: str
    """The ID of the tool call that is being requested."""

    type: Optional[Literal["tool_request"]] = None
    """The type of the message, in this case `tool_request`."""
