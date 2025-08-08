# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["ContextUpdateParams"]


class ContextUpdateParams(TypedDict, total=False):
    data: Optional[Dict[str, object]]

    draft: Optional[bool]
