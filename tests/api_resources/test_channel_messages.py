# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import (
    ChannelMessage,
    ChannelMessageListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        channel_message = client.channel_messages.create(
            content="content",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Delegate) -> None:
        channel_message = client.channel_messages.create(
            content="content",
            message_metadata={"foo": "bar"},
            message_type="message_type",
            parent_message_id="parent_message_id",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.channel_messages.with_raw_response.create(
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.channel_messages.with_streaming_response.create(
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        channel_message = client.channel_messages.retrieve(
            "message_id",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.channel_messages.with_raw_response.retrieve(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.channel_messages.with_streaming_response.retrieve(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.channel_messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Delegate) -> None:
        channel_message = client.channel_messages.update(
            message_id="message_id",
            content="content",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Delegate) -> None:
        channel_message = client.channel_messages.update(
            message_id="message_id",
            content="content",
            message_metadata={"foo": "bar"},
            message_type="message_type",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Delegate) -> None:
        response = client.channel_messages.with_raw_response.update(
            message_id="message_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Delegate) -> None:
        with client.channel_messages.with_streaming_response.update(
            message_id="message_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.channel_messages.with_raw_response.update(
                message_id="",
                content="content",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        channel_message = client.channel_messages.list(
            channel_id="channel_id",
        )
        assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Delegate) -> None:
        channel_message = client.channel_messages.list(
            channel_id="channel_id",
            limit=0,
            parent_message_id="parent_message_id",
        )
        assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.channel_messages.with_raw_response.list(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = response.parse()
        assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.channel_messages.with_streaming_response.list(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = response.parse()
            assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Delegate) -> None:
        channel_message = client.channel_messages.delete(
            "message_id",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Delegate) -> None:
        response = client.channel_messages.with_raw_response.delete(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Delegate) -> None:
        with client.channel_messages.with_streaming_response.delete(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.channel_messages.with_raw_response.delete(
                "",
            )


class TestAsyncChannelMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.create(
            content="content",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.create(
            content="content",
            message_metadata={"foo": "bar"},
            message_type="message_type",
            parent_message_id="parent_message_id",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.with_raw_response.create(
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = await response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.with_streaming_response.create(
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = await response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.retrieve(
            "message_id",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.with_raw_response.retrieve(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = await response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.with_streaming_response.retrieve(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = await response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.channel_messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.update(
            message_id="message_id",
            content="content",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.update(
            message_id="message_id",
            content="content",
            message_metadata={"foo": "bar"},
            message_type="message_type",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.with_raw_response.update(
            message_id="message_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = await response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.with_streaming_response.update(
            message_id="message_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = await response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.channel_messages.with_raw_response.update(
                message_id="",
                content="content",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.list(
            channel_id="channel_id",
        )
        assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.list(
            channel_id="channel_id",
            limit=0,
            parent_message_id="parent_message_id",
        )
        assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.with_raw_response.list(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = await response.parse()
        assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.with_streaming_response.list(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = await response.parse()
            assert_matches_type(ChannelMessageListResponse, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDelegate) -> None:
        channel_message = await async_client.channel_messages.delete(
            "message_id",
        )
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.with_raw_response.delete(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_message = await response.parse()
        assert_matches_type(ChannelMessage, channel_message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.with_streaming_response.delete(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_message = await response.parse()
            assert_matches_type(ChannelMessage, channel_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.channel_messages.with_raw_response.delete(
                "",
            )
