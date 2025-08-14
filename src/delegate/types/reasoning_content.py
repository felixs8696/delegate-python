# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReasoningContent"]


class ReasoningContent(BaseModel):
    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: str
    """The reasoning content or chain-of-thought text"""

    reasoning_id: Optional[str] = None
    """The ID of the reasoning item"""

    summary: Optional[str] = None
    """A short reasoning summary"""

    type: Optional[Literal["reasoning"]] = None
    """The type of the message, in this case `reasoning`."""

    usage: Optional[Dict[str, object]] = None
    """Usage information for reasoning tokens"""
