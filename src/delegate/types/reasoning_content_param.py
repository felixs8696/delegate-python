# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReasoningContentParam"]


class ReasoningContentParam(TypedDict, total=False):
    author: Required[Literal["system", "user", "assistant"]]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: Required[str]
    """The reasoning content or chain-of-thought text"""

    reasoning_id: Optional[str]
    """The ID of the reasoning item"""

    summary: Optional[str]
    """A short reasoning summary"""

    type: Literal["reasoning"]
    """The type of the message, in this case `reasoning`."""

    usage: Optional[Dict[str, object]]
    """Usage information for reasoning tokens"""
