# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["State"]


class State(BaseModel):
    id: str
    """The objective state's unique id"""

    created_at: datetime
    """The timestamp when the state was created"""

    objective_id: str

    state: Dict[str, object]

    updated_at: Optional[datetime] = None
    """The timestamp when the state was last updated"""
