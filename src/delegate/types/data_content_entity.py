# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataContentEntity"]


class DataContentEntity(BaseModel):
    data: Dict[str, object]
    """The data content of the activity"""

    type: Optional[Literal["data"]] = None
    """Data content type"""
