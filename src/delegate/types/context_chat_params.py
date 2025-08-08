# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContextChatParams", "Context", "ContextLocation"]


class ContextChatParams(TypedDict, total=False):
    content: Required[str]

    context: Optional[Context]


class ContextLocation(TypedDict, total=False):
    city: Optional[str]

    country: Optional[str]

    latitude: Optional[float]

    longitude: Optional[float]


class Context(TypedDict, total=False):
    local_time: Optional[str]

    location: Optional[ContextLocation]

    timestamp: Optional[str]

    timezone: Optional[str]
