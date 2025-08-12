# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import (
    Message,
    MessageListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        message = client.messages.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Delegate) -> None:
        message = client.messages.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
            message_metadata={"foo": "bar"},
            parent_message_id="parent_message_id",
            streaming_status="pending",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.messages.with_raw_response.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.messages.with_streaming_response.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        message = client.messages.retrieve(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.messages.with_raw_response.retrieve(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.messages.with_streaming_response.retrieve(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Delegate) -> None:
        message = client.messages.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Delegate) -> None:
        message = client.messages.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
            message_metadata={"foo": "bar"},
            streaming_status="pending",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Delegate) -> None:
        response = client.messages.with_raw_response.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Delegate) -> None:
        with client.messages.with_streaming_response.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.update(
                message_id="",
                content={
                    "author": "system",
                    "content": "content",
                    "type": "text",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        message = client.messages.list(
            channel_id="channel_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Delegate) -> None:
        message = client.messages.list(
            channel_id="channel_id",
            limit=0,
            parent_message_id="parent_message_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.messages.with_raw_response.list(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.messages.with_streaming_response.list(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Delegate) -> None:
        message = client.messages.delete(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Delegate) -> None:
        response = client.messages.with_raw_response.delete(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Delegate) -> None:
        with client.messages.with_streaming_response.delete(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.delete(
                "",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
            message_metadata={"foo": "bar"},
            parent_message_id="parent_message_id",
            streaming_status="pending",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.messages.with_raw_response.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.messages.with_streaming_response.create(
            channel_id="channel_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.retrieve(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
            message_metadata={"foo": "bar"},
            streaming_status="pending",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDelegate) -> None:
        response = await async_client.messages.with_raw_response.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDelegate) -> None:
        async with async_client.messages.with_streaming_response.update(
            message_id="message_id",
            content={
                "author": "system",
                "content": "content",
                "type": "text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.update(
                message_id="",
                content={
                    "author": "system",
                    "content": "content",
                    "type": "text",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.list(
            channel_id="channel_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.list(
            channel_id="channel_id",
            limit=0,
            parent_message_id="parent_message_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.messages.with_raw_response.list(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.messages.with_streaming_response.list(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDelegate) -> None:
        message = await async_client.messages.delete(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDelegate) -> None:
        response = await async_client.messages.with_raw_response.delete(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDelegate) -> None:
        async with async_client.messages.with_streaming_response.delete(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.delete(
                "",
            )
