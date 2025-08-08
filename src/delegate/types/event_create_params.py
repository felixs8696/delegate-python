# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .text_format import TextFormat
from .file_attachment_param import FileAttachmentParam

__all__ = [
    "EventCreateParams",
    "Content",
    "ContentTextContent",
    "ContentToolRequestContent",
    "ContentToolResponseContent",
    "ContentDataContent",
]


class EventCreateParams(TypedDict, total=False):
    content: Required[Content]
    """The event content"""

    objective_id: Required[str]
    """The objective id the event is for"""


class ContentTextContent(TypedDict, total=False):
    content: Required[str]
    """The contents of the text activity."""

    attachments: Optional[Iterable[FileAttachmentParam]]
    """Optional list of file attachments with structured metadata."""

    format: TextFormat
    """The format of the activity.

    This is used by the client to determine how to display it.
    """

    type: Literal["text"]
    """Text content type"""


class ContentToolRequestContent(TypedDict, total=False):
    tool_request: Required[Dict[str, object]]
    """The tool request content of the activity"""

    type: Literal["tool_request"]
    """Tool request content type"""


class ContentToolResponseContent(TypedDict, total=False):
    tool_response: Required[Dict[str, object]]
    """The tool response content of the activity"""

    type: Literal["tool_response"]
    """Tool response content type"""


class ContentDataContent(TypedDict, total=False):
    data: Required[Dict[str, object]]
    """The data content of the activity"""

    type: Literal["data"]
    """Data content type"""


Content: TypeAlias = Union[
    ContentTextContent, ContentToolRequestContent, ContentToolResponseContent, ContentDataContent
]
