# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolResponseContent"]


class ToolResponseContent(BaseModel):
    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: object
    """The result of the tool."""

    name: str
    """The name of the tool that is being responded to."""

    tool_call_id: str
    """The ID of the tool call that is being responded to."""

    type: Optional[Literal["tool_response"]] = None
    """The type of the message, in this case `tool_response`."""
