# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import channel_message_list_params, channel_message_create_params, channel_message_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.channel_message import ChannelMessage
from ...types.channel_message_list_response import ChannelMessageListResponse

__all__ = ["ChannelMessagesResource", "AsyncChannelMessagesResource"]


class ChannelMessagesResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChannelMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return ChannelMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return ChannelMessagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        message_metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message_type: str | NotGiven = NOT_GIVEN,
        parent_message_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Create a new message in a channel.

        Args:
          content: The message content

          message_metadata: Additional metadata for the message (reactions, files, etc.)

          message_type: The type of message (text, file, reaction, etc.)

          parent_message_id: The parent message id if this is a reply

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/channel-messages",
            body=maybe_transform(
                {
                    "content": content,
                    "message_metadata": message_metadata,
                    "message_type": message_type,
                    "parent_message_id": parent_message_id,
                },
                channel_message_create_params.ChannelMessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Get a message by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/channel-messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def update(
        self,
        message_id: str,
        *,
        content: str,
        message_metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Update a message in a channel.

        Args:
          content: The message content

          message_metadata: Additional metadata for the message (reactions, files, etc.)

          message_type: The type of message (text, file, reaction, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/channel-messages/{message_id}",
            body=maybe_transform(
                {
                    "content": content,
                    "message_metadata": message_metadata,
                    "message_type": message_type,
                },
                channel_message_update_params.ChannelMessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    def list(
        self,
        *,
        channel_id: str,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        parent_message_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessageListResponse:
        """
        List messages in a channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/channel-messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel_id": channel_id,
                        "limit": limit,
                        "parent_message_id": parent_message_id,
                    },
                    channel_message_list_params.ChannelMessageListParams,
                ),
            ),
            cast_to=ChannelMessageListResponse,
        )

    def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Delete a message (soft delete).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            f"/channel-messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )


class AsyncChannelMessagesResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChannelMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felixs8696/delegate-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felixs8696/delegate-python#with_streaming_response
        """
        return AsyncChannelMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        message_metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message_type: str | NotGiven = NOT_GIVEN,
        parent_message_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Create a new message in a channel.

        Args:
          content: The message content

          message_metadata: Additional metadata for the message (reactions, files, etc.)

          message_type: The type of message (text, file, reaction, etc.)

          parent_message_id: The parent message id if this is a reply

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/channel-messages",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "message_metadata": message_metadata,
                    "message_type": message_type,
                    "parent_message_id": parent_message_id,
                },
                channel_message_create_params.ChannelMessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Get a message by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/channel-messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    async def update(
        self,
        message_id: str,
        *,
        content: str,
        message_metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Update a message in a channel.

        Args:
          content: The message content

          message_metadata: Additional metadata for the message (reactions, files, etc.)

          message_type: The type of message (text, file, reaction, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/channel-messages/{message_id}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "message_metadata": message_metadata,
                    "message_type": message_type,
                },
                channel_message_update_params.ChannelMessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )

    async def list(
        self,
        *,
        channel_id: str,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        parent_message_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessageListResponse:
        """
        List messages in a channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/channel-messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel_id": channel_id,
                        "limit": limit,
                        "parent_message_id": parent_message_id,
                    },
                    channel_message_list_params.ChannelMessageListParams,
                ),
            ),
            cast_to=ChannelMessageListResponse,
        )

    async def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelMessage:
        """
        Delete a message (soft delete).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            f"/channel-messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelMessage,
        )


class ChannelMessagesResourceWithRawResponse:
    def __init__(self, channel_messages: ChannelMessagesResource) -> None:
        self._channel_messages = channel_messages

        self.create = to_raw_response_wrapper(
            channel_messages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            channel_messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            channel_messages.update,
        )
        self.list = to_raw_response_wrapper(
            channel_messages.list,
        )
        self.delete = to_raw_response_wrapper(
            channel_messages.delete,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._channel_messages.batch)


class AsyncChannelMessagesResourceWithRawResponse:
    def __init__(self, channel_messages: AsyncChannelMessagesResource) -> None:
        self._channel_messages = channel_messages

        self.create = async_to_raw_response_wrapper(
            channel_messages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            channel_messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            channel_messages.update,
        )
        self.list = async_to_raw_response_wrapper(
            channel_messages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            channel_messages.delete,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._channel_messages.batch)


class ChannelMessagesResourceWithStreamingResponse:
    def __init__(self, channel_messages: ChannelMessagesResource) -> None:
        self._channel_messages = channel_messages

        self.create = to_streamed_response_wrapper(
            channel_messages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            channel_messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            channel_messages.update,
        )
        self.list = to_streamed_response_wrapper(
            channel_messages.list,
        )
        self.delete = to_streamed_response_wrapper(
            channel_messages.delete,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._channel_messages.batch)


class AsyncChannelMessagesResourceWithStreamingResponse:
    def __init__(self, channel_messages: AsyncChannelMessagesResource) -> None:
        self._channel_messages = channel_messages

        self.create = async_to_streamed_response_wrapper(
            channel_messages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            channel_messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            channel_messages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            channel_messages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            channel_messages.delete,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._channel_messages.batch)
