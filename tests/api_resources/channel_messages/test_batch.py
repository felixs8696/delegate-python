# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types.channel_messages import (
    BatchCreateResponse,
    BatchUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        batch = client.channel_messages.batch.create(
            channel_id="channel_id",
            messages=[{"content": "content"}],
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.channel_messages.batch.with_raw_response.create(
            channel_id="channel_id",
            messages=[{"content": "content"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.channel_messages.batch.with_streaming_response.create(
            channel_id="channel_id",
            messages=[{"content": "content"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Delegate) -> None:
        batch = client.channel_messages.batch.update(
            channel_id="channel_id",
            updates={"foo": {"content": "content"}},
        )
        assert_matches_type(BatchUpdateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Delegate) -> None:
        response = client.channel_messages.batch.with_raw_response.update(
            channel_id="channel_id",
            updates={"foo": {"content": "content"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchUpdateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Delegate) -> None:
        with client.channel_messages.batch.with_streaming_response.update(
            channel_id="channel_id",
            updates={"foo": {"content": "content"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchUpdateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        batch = await async_client.channel_messages.batch.create(
            channel_id="channel_id",
            messages=[{"content": "content"}],
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.batch.with_raw_response.create(
            channel_id="channel_id",
            messages=[{"content": "content"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.batch.with_streaming_response.create(
            channel_id="channel_id",
            messages=[{"content": "content"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDelegate) -> None:
        batch = await async_client.channel_messages.batch.update(
            channel_id="channel_id",
            updates={"foo": {"content": "content"}},
        )
        assert_matches_type(BatchUpdateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channel_messages.batch.with_raw_response.update(
            channel_id="channel_id",
            updates={"foo": {"content": "content"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchUpdateResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDelegate) -> None:
        async with async_client.channel_messages.batch.with_streaming_response.update(
            channel_id="channel_id",
            updates={"foo": {"content": "content"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchUpdateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
