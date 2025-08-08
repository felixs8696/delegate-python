# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ObjectiveCreateParams"]


class ObjectiveCreateParams(TypedDict, total=False):
    context_id: Optional[str]

    name: Optional[str]
