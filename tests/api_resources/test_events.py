# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import Event, EventListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        event = client.events.create(
            content={"content": "content"},
            objective_id="objective_id",
        )
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Delegate) -> None:
        event = client.events.create(
            content={
                "content": "content",
                "attachments": [
                    {
                        "file_id": "file_id",
                        "name": "name",
                        "size": 0,
                        "type": "type",
                    }
                ],
                "format": "markdown",
                "type": "text",
            },
            objective_id="objective_id",
        )
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.events.with_raw_response.create(
            content={"content": "content"},
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.events.with_streaming_response.create(
            content={"content": "content"},
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        event = client.events.retrieve(
            "event_id",
        )
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.events.with_raw_response.retrieve(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.events.with_streaming_response.retrieve(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.events.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        event = client.events.list(
            objective_id="objective_id",
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Delegate) -> None:
        event = client.events.list(
            objective_id="objective_id",
            last_processed_event_id="last_processed_event_id",
            limit=1,
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.events.with_raw_response.list(
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventListResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.events.with_streaming_response.list(
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventListResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        event = await async_client.events.create(
            content={"content": "content"},
            objective_id="objective_id",
        )
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDelegate) -> None:
        event = await async_client.events.create(
            content={
                "content": "content",
                "attachments": [
                    {
                        "file_id": "file_id",
                        "name": "name",
                        "size": 0,
                        "type": "type",
                    }
                ],
                "format": "markdown",
                "type": "text",
            },
            objective_id="objective_id",
        )
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.events.with_raw_response.create(
            content={"content": "content"},
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.events.with_streaming_response.create(
            content={"content": "content"},
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        event = await async_client.events.retrieve(
            "event_id",
        )
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.events.with_raw_response.retrieve(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.events.with_streaming_response.retrieve(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.events.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        event = await async_client.events.list(
            objective_id="objective_id",
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDelegate) -> None:
        event = await async_client.events.list(
            objective_id="objective_id",
            last_processed_event_id="last_processed_event_id",
            limit=1,
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.events.with_raw_response.list(
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventListResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.events.with_streaming_response.list(
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventListResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
