# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import (
    Context,
    ContextChatResponse,
    ContextListResponse,
    ContextCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContexts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        context = client.contexts.create()
        assert_matches_type(ContextCreateResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.contexts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextCreateResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.contexts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextCreateResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        context = client.contexts.retrieve(
            "context_id",
        )
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.contexts.with_raw_response.retrieve(
            "context_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.contexts.with_streaming_response.retrieve(
            "context_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(Context, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            client.contexts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Delegate) -> None:
        context = client.contexts.update(
            context_id="context_id",
        )
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Delegate) -> None:
        context = client.contexts.update(
            context_id="context_id",
            data={"foo": "bar"},
            draft=True,
        )
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Delegate) -> None:
        response = client.contexts.with_raw_response.update(
            context_id="context_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Delegate) -> None:
        with client.contexts.with_streaming_response.update(
            context_id="context_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(Context, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            client.contexts.with_raw_response.update(
                context_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        context = client.contexts.list()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.contexts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.contexts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextListResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Delegate) -> None:
        context = client.contexts.delete(
            "context_id",
        )
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Delegate) -> None:
        response = client.contexts.with_raw_response.delete(
            "context_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Delegate) -> None:
        with client.contexts.with_streaming_response.delete(
            "context_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(object, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            client.contexts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_chat(self, client: Delegate) -> None:
        context = client.contexts.chat(
            context_id="context_id",
            content="content",
        )
        assert_matches_type(ContextChatResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_chat_with_all_params(self, client: Delegate) -> None:
        context = client.contexts.chat(
            context_id="context_id",
            content="content",
            context={
                "local_time": "local_time",
                "location": {
                    "city": "city",
                    "country": "country",
                    "latitude": 0,
                    "longitude": 0,
                },
                "timestamp": "timestamp",
                "timezone": "timezone",
            },
        )
        assert_matches_type(ContextChatResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_chat(self, client: Delegate) -> None:
        response = client.contexts.with_raw_response.chat(
            context_id="context_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextChatResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_chat(self, client: Delegate) -> None:
        with client.contexts.with_streaming_response.chat(
            context_id="context_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextChatResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_chat(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            client.contexts.with_raw_response.chat(
                context_id="",
                content="content",
            )


class TestAsyncContexts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.create()
        assert_matches_type(ContextCreateResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.contexts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextCreateResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.contexts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextCreateResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.retrieve(
            "context_id",
        )
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.contexts.with_raw_response.retrieve(
            "context_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.contexts.with_streaming_response.retrieve(
            "context_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(Context, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            await async_client.contexts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.update(
            context_id="context_id",
        )
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.update(
            context_id="context_id",
            data={"foo": "bar"},
            draft=True,
        )
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDelegate) -> None:
        response = await async_client.contexts.with_raw_response.update(
            context_id="context_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(Context, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDelegate) -> None:
        async with async_client.contexts.with_streaming_response.update(
            context_id="context_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(Context, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            await async_client.contexts.with_raw_response.update(
                context_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.list()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.contexts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.contexts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextListResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.delete(
            "context_id",
        )
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDelegate) -> None:
        response = await async_client.contexts.with_raw_response.delete(
            "context_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(object, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDelegate) -> None:
        async with async_client.contexts.with_streaming_response.delete(
            "context_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(object, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            await async_client.contexts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_chat(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.chat(
            context_id="context_id",
            content="content",
        )
        assert_matches_type(ContextChatResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncDelegate) -> None:
        context = await async_client.contexts.chat(
            context_id="context_id",
            content="content",
            context={
                "local_time": "local_time",
                "location": {
                    "city": "city",
                    "country": "country",
                    "latitude": 0,
                    "longitude": 0,
                },
                "timestamp": "timestamp",
                "timezone": "timezone",
            },
        )
        assert_matches_type(ContextChatResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncDelegate) -> None:
        response = await async_client.contexts.with_raw_response.chat(
            context_id="context_id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextChatResponse, context, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncDelegate) -> None:
        async with async_client.contexts.with_streaming_response.chat(
            context_id="context_id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextChatResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_chat(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_id` but received ''"):
            await async_client.contexts.with_raw_response.chat(
                context_id="",
                content="content",
            )
