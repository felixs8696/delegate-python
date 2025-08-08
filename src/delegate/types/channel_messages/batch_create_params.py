# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..create_channel_message_param import CreateChannelMessageParam

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The channel id"""

    messages: Required[Iterable[CreateChannelMessageParam]]
    """The messages to create"""
