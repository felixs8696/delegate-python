# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    objective_id: Required[str]

    limit: int
