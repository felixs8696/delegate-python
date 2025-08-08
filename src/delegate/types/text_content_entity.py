# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .text_format import TextFormat
from .file_attachment import FileAttachment

__all__ = ["TextContentEntity"]


class TextContentEntity(BaseModel):
    content: str
    """The contents of the text activity."""

    attachments: Optional[List[FileAttachment]] = None
    """Optional list of file attachments with structured metadata."""

    format: Optional[TextFormat] = None
    """The format of the activity.

    This is used by the client to determine how to display it.
    """

    type: Optional[Literal["text"]] = None
    """Text content type"""
