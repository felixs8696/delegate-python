# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TextContent"]


class TextContent(BaseModel):
    author: Literal["system", "user", "assistant"]
    """
    The role of the messages author, in this case `system`, `user`, `assistant`, or
    `tool`.
    """

    content: str
    """The contents of the text message."""

    type: Optional[Literal["text"]] = None
    """The type of the message, in this case `text`."""
