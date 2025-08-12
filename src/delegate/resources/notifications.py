# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import notification_list_params, notification_create_params, notification_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.notification_list_response import NotificationListResponse
from ..types.notification_create_response import NotificationCreateResponse
from ..types.notification_delete_response import NotificationDeleteResponse
from ..types.notification_update_response import NotificationUpdateResponse
from ..types.notification_retrieve_response import NotificationRetrieveResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: notification_create_params.Content,
        objective_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationCreateResponse:
        """
        Create a new notification for an objective.

        Args:
          content: The notification content

          objective_id: The objective ID this notification belongs to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/notifications",
            body=maybe_transform(
                {
                    "content": content,
                    "objective_id": objective_id,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
        )

    def retrieve(
        self,
        notification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationRetrieveResponse:
        """
        Get a notification by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._get(
            f"/notifications/{notification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationRetrieveResponse,
        )

    def update(
        self,
        notification_id: str,
        *,
        content: notification_update_params.Content,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationUpdateResponse:
        """
        Update a notification's content.

        Args:
          content: The updated notification content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._put(
            f"/notifications/{notification_id}",
            body=maybe_transform({"content": content}, notification_update_params.NotificationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdateResponse,
        )

    def list(
        self,
        *,
        objective_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationListResponse:
        """
        List notifications for an objective.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "objective_id": objective_id,
                        "limit": limit,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    def delete(
        self,
        notification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationDeleteResponse:
        """
        Delete a notification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._delete(
            f"/notifications/{notification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationDeleteResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: notification_create_params.Content,
        objective_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationCreateResponse:
        """
        Create a new notification for an objective.

        Args:
          content: The notification content

          objective_id: The objective ID this notification belongs to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/notifications",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "objective_id": objective_id,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
        )

    async def retrieve(
        self,
        notification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationRetrieveResponse:
        """
        Get a notification by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._get(
            f"/notifications/{notification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationRetrieveResponse,
        )

    async def update(
        self,
        notification_id: str,
        *,
        content: notification_update_params.Content,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationUpdateResponse:
        """
        Update a notification's content.

        Args:
          content: The updated notification content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._put(
            f"/notifications/{notification_id}",
            body=await async_maybe_transform({"content": content}, notification_update_params.NotificationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdateResponse,
        )

    async def list(
        self,
        *,
        objective_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationListResponse:
        """
        List notifications for an objective.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "objective_id": objective_id,
                        "limit": limit,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    async def delete(
        self,
        notification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationDeleteResponse:
        """
        Delete a notification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._delete(
            f"/notifications/{notification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationDeleteResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            notifications.update,
        )
        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.delete = to_raw_response_wrapper(
            notifications.delete,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            notifications.update,
        )
        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notifications.delete,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            notifications.update,
        )
        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.delete = to_streamed_response_wrapper(
            notifications.delete,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            notifications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notifications.delete,
        )
