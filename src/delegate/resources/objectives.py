# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import objective_list_params, objective_cancel_params, objective_create_params
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
from ..types.objective import Objective
from ..types.objective_list_response import ObjectiveListResponse

__all__ = ["ObjectivesResource", "AsyncObjectivesResource"]


class ObjectivesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return ObjectivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return ObjectivesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Create a new objective with parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/objectives",
            body=maybe_transform({"name": name}, objective_create_params.ObjectiveCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def retrieve(
        self,
        objective_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Get an objective by its unique ID with channel data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._get(
            f"/objectives/{objective_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def list(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectiveListResponse:
        """
        List all objectives with channel data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/objectives",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    objective_list_params.ObjectiveListParams,
                ),
            ),
            cast_to=ObjectiveListResponse,
        )

    def delete(
        self,
        objective_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Delete an objective by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._delete(
            f"/objectives/{objective_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def cancel(
        self,
        objective_id: str,
        *,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Cancel an objective by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._post(
            f"/objectives/{objective_id}:cancel",
            body=maybe_transform({"reason": reason}, objective_cancel_params.ObjectiveCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def stream_events(
        self,
        objective_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream events for an objective by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._get(
            f"/objectives/{objective_id}:stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncObjectivesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return AsyncObjectivesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Create a new objective with parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/objectives",
            body=await async_maybe_transform({"name": name}, objective_create_params.ObjectiveCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    async def retrieve(
        self,
        objective_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Get an objective by its unique ID with channel data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._get(
            f"/objectives/{objective_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    async def list(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectiveListResponse:
        """
        List all objectives with channel data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/objectives",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    objective_list_params.ObjectiveListParams,
                ),
            ),
            cast_to=ObjectiveListResponse,
        )

    async def delete(
        self,
        objective_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Delete an objective by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._delete(
            f"/objectives/{objective_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    async def cancel(
        self,
        objective_id: str,
        *,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Objective:
        """
        Cancel an objective by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._post(
            f"/objectives/{objective_id}:cancel",
            body=await async_maybe_transform({"reason": reason}, objective_cancel_params.ObjectiveCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    async def stream_events(
        self,
        objective_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream events for an objective by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._get(
            f"/objectives/{objective_id}:stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ObjectivesResourceWithRawResponse:
    def __init__(self, objectives: ObjectivesResource) -> None:
        self._objectives = objectives

        self.create = to_raw_response_wrapper(
            objectives.create,
        )
        self.retrieve = to_raw_response_wrapper(
            objectives.retrieve,
        )
        self.list = to_raw_response_wrapper(
            objectives.list,
        )
        self.delete = to_raw_response_wrapper(
            objectives.delete,
        )
        self.cancel = to_raw_response_wrapper(
            objectives.cancel,
        )
        self.stream_events = to_raw_response_wrapper(
            objectives.stream_events,
        )


class AsyncObjectivesResourceWithRawResponse:
    def __init__(self, objectives: AsyncObjectivesResource) -> None:
        self._objectives = objectives

        self.create = async_to_raw_response_wrapper(
            objectives.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            objectives.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            objectives.list,
        )
        self.delete = async_to_raw_response_wrapper(
            objectives.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            objectives.cancel,
        )
        self.stream_events = async_to_raw_response_wrapper(
            objectives.stream_events,
        )


class ObjectivesResourceWithStreamingResponse:
    def __init__(self, objectives: ObjectivesResource) -> None:
        self._objectives = objectives

        self.create = to_streamed_response_wrapper(
            objectives.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            objectives.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            objectives.list,
        )
        self.delete = to_streamed_response_wrapper(
            objectives.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            objectives.cancel,
        )
        self.stream_events = to_streamed_response_wrapper(
            objectives.stream_events,
        )


class AsyncObjectivesResourceWithStreamingResponse:
    def __init__(self, objectives: AsyncObjectivesResource) -> None:
        self._objectives = objectives

        self.create = async_to_streamed_response_wrapper(
            objectives.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            objectives.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            objectives.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            objectives.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            objectives.cancel,
        )
        self.stream_events = async_to_streamed_response_wrapper(
            objectives.stream_events,
        )
