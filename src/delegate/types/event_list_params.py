# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    objective_id: Required[str]
    """The objective ID to filter events by"""

    last_processed_event_id: Optional[str]
    """Optional event ID to get events after this ID"""

    limit: Optional[int]
    """Optional limit on number of results"""
