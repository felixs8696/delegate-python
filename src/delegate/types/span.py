# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Span"]


class Span(BaseModel):
    id: str

    name: str

    start_time: datetime

    trace_id: str

    data: Union[Dict[str, object], List[Dict[str, object]], None] = None

    end_time: Optional[datetime] = None

    filters: Union[Dict[str, object], List[Dict[str, object]], None] = None

    input: Union[Dict[str, object], List[Dict[str, object]], None] = None

    output: Union[Dict[str, object], List[Dict[str, object]], None] = None

    parent_id: Optional[str] = None
