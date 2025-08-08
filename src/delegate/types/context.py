# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["Context", "Data"]


class Data(BaseModel):
    communication_frequency: Optional[str] = None
    """hourly|daily|weekly|as_needed"""

    deadline: Optional[str] = None
    """ISO 8601 date-time"""

    escalation_conditions: Optional[List[str]] = None

    escalation_sensitivity: Optional[str] = None
    """low|medium|high|critical"""

    high_level_plan: Optional[str] = None

    key_stakeholders: Optional[List[str]] = None

    name: Optional[str] = None

    objective: Optional[str] = None


class Context(BaseModel):
    id: str

    data: Data

    draft: bool

    schema_version: Dict[str, object]

    objective_id: Optional[str] = None
