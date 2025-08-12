# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["State"]


class State(BaseModel):
    objective_id: str
    """ID of the objective this state belongs to. The objective_id is globally unique."""

    state: Dict[str, object]
    """The state object that contains arbitrary data"""

    id: Optional[str] = None
    """The objective state's unique id"""

    created_at: Optional[datetime] = None
    """The timestamp when the state was created"""

    updated_at: Optional[datetime] = None
    """The timestamp when the state was last updated"""
