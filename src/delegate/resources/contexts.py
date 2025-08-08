# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import context_chat_params, context_update_params
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
from ..types.context import Context
from ..types.context_chat_response import ContextChatResponse
from ..types.context_list_response import ContextListResponse
from ..types.context_create_response import ContextCreateResponse

__all__ = ["ContextsResource", "AsyncContextsResource"]


class ContextsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return ContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return ContextsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextCreateResponse:
        """Create Context"""
        return self._post(
            "/contexts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextCreateResponse,
        )

    def retrieve(
        self,
        context_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Context:
        """
        Get Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return self._get(
            f"/contexts/{context_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    def update(
        self,
        context_id: str,
        *,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        draft: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Context:
        """
        Update Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return self._patch(
            f"/contexts/{context_id}",
            body=maybe_transform(
                {
                    "data": data,
                    "draft": draft,
                },
                context_update_params.ContextUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextListResponse:
        """List Contexts"""
        return self._get(
            "/contexts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextListResponse,
        )

    def delete(
        self,
        context_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return self._delete(
            f"/contexts/{context_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def chat(
        self,
        context_id: str,
        *,
        content: str,
        context: Optional[context_chat_params.Context] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextChatResponse:
        """
        Chat Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return self._post(
            f"/contexts/{context_id}:chat",
            body=maybe_transform(
                {
                    "content": content,
                    "context": context,
                },
                context_chat_params.ContextChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextChatResponse,
        )


class AsyncContextsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return AsyncContextsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextCreateResponse:
        """Create Context"""
        return await self._post(
            "/contexts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextCreateResponse,
        )

    async def retrieve(
        self,
        context_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Context:
        """
        Get Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return await self._get(
            f"/contexts/{context_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    async def update(
        self,
        context_id: str,
        *,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        draft: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Context:
        """
        Update Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return await self._patch(
            f"/contexts/{context_id}",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "draft": draft,
                },
                context_update_params.ContextUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Context,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextListResponse:
        """List Contexts"""
        return await self._get(
            "/contexts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextListResponse,
        )

    async def delete(
        self,
        context_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return await self._delete(
            f"/contexts/{context_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def chat(
        self,
        context_id: str,
        *,
        content: str,
        context: Optional[context_chat_params.Context] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextChatResponse:
        """
        Chat Context

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_id:
            raise ValueError(f"Expected a non-empty value for `context_id` but received {context_id!r}")
        return await self._post(
            f"/contexts/{context_id}:chat",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "context": context,
                },
                context_chat_params.ContextChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextChatResponse,
        )


class ContextsResourceWithRawResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contexts.update,
        )
        self.list = to_raw_response_wrapper(
            contexts.list,
        )
        self.delete = to_raw_response_wrapper(
            contexts.delete,
        )
        self.chat = to_raw_response_wrapper(
            contexts.chat,
        )


class AsyncContextsResourceWithRawResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contexts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contexts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contexts.delete,
        )
        self.chat = async_to_raw_response_wrapper(
            contexts.chat,
        )


class ContextsResourceWithStreamingResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contexts.update,
        )
        self.list = to_streamed_response_wrapper(
            contexts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contexts.delete,
        )
        self.chat = to_streamed_response_wrapper(
            contexts.chat,
        )


class AsyncContextsResourceWithStreamingResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contexts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contexts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contexts.delete,
        )
        self.chat = async_to_streamed_response_wrapper(
            contexts.chat,
        )
