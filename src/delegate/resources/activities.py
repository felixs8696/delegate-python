# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import activity_list_params
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
from ..types.objective_activity import ObjectiveActivity
from ..types.activity_list_response import ActivityListResponse

__all__ = ["ActivitiesResource", "AsyncActivitiesResource"]


class ActivitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return ActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return ActivitiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        activity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectiveActivity:
        """
        Get Activity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not activity_id:
            raise ValueError(f"Expected a non-empty value for `activity_id` but received {activity_id!r}")
        return self._get(
            f"/activities/{activity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveActivity,
        )

    def list(
        self,
        *,
        objective_id: str,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityListResponse:
        """
        List Activities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/activities",
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
                    activity_list_params.ActivityListParams,
                ),
            ),
            cast_to=ActivityListResponse,
        )


class AsyncActivitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return AsyncActivitiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        activity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectiveActivity:
        """
        Get Activity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not activity_id:
            raise ValueError(f"Expected a non-empty value for `activity_id` but received {activity_id!r}")
        return await self._get(
            f"/activities/{activity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveActivity,
        )

    async def list(
        self,
        *,
        objective_id: str,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityListResponse:
        """
        List Activities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/activities",
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
                    activity_list_params.ActivityListParams,
                ),
            ),
            cast_to=ActivityListResponse,
        )


class ActivitiesResourceWithRawResponse:
    def __init__(self, activities: ActivitiesResource) -> None:
        self._activities = activities

        self.retrieve = to_raw_response_wrapper(
            activities.retrieve,
        )
        self.list = to_raw_response_wrapper(
            activities.list,
        )


class AsyncActivitiesResourceWithRawResponse:
    def __init__(self, activities: AsyncActivitiesResource) -> None:
        self._activities = activities

        self.retrieve = async_to_raw_response_wrapper(
            activities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            activities.list,
        )


class ActivitiesResourceWithStreamingResponse:
    def __init__(self, activities: ActivitiesResource) -> None:
        self._activities = activities

        self.retrieve = to_streamed_response_wrapper(
            activities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            activities.list,
        )


class AsyncActivitiesResourceWithStreamingResponse:
    def __init__(self, activities: AsyncActivitiesResource) -> None:
        self._activities = activities

        self.retrieve = async_to_streamed_response_wrapper(
            activities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            activities.list,
        )
