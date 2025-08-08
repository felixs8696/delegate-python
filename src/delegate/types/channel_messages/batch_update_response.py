# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..channel_message import ChannelMessage

__all__ = ["BatchUpdateResponse"]

BatchUpdateResponse: TypeAlias = List[ChannelMessage]
