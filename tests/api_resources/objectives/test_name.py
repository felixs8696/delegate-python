# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import Objective

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        name = client.objectives.name.retrieve(
            "objective_name",
        )
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.objectives.name.with_raw_response.retrieve(
            "objective_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.objectives.name.with_streaming_response.retrieve(
            "objective_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(Objective, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_name` but received ''"):
            client.objectives.name.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Delegate) -> None:
        name = client.objectives.name.delete(
            "objective_name",
        )
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Delegate) -> None:
        response = client.objectives.name.with_raw_response.delete(
            "objective_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Delegate) -> None:
        with client.objectives.name.with_streaming_response.delete(
            "objective_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(Objective, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_name` but received ''"):
            client.objectives.name.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_events(self, client: Delegate) -> None:
        name = client.objectives.name.stream_events(
            "objective_name",
        )
        assert_matches_type(object, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_events(self, client: Delegate) -> None:
        response = client.objectives.name.with_raw_response.stream_events(
            "objective_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(object, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_events(self, client: Delegate) -> None:
        with client.objectives.name.with_streaming_response.stream_events(
            "objective_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(object, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_events(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_name` but received ''"):
            client.objectives.name.with_raw_response.stream_events(
                "",
            )


class TestAsyncName:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        name = await async_client.objectives.name.retrieve(
            "objective_name",
        )
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.name.with_raw_response.retrieve(
            "objective_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.name.with_streaming_response.retrieve(
            "objective_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(Objective, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_name` but received ''"):
            await async_client.objectives.name.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDelegate) -> None:
        name = await async_client.objectives.name.delete(
            "objective_name",
        )
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.name.with_raw_response.delete(
            "objective_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(Objective, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.name.with_streaming_response.delete(
            "objective_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(Objective, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_name` but received ''"):
            await async_client.objectives.name.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncDelegate) -> None:
        name = await async_client.objectives.name.stream_events(
            "objective_name",
        )
        assert_matches_type(object, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.name.with_raw_response.stream_events(
            "objective_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(object, name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.name.with_streaming_response.stream_events(
            "objective_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(object, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_name` but received ''"):
            await async_client.objectives.name.with_raw_response.stream_events(
                "",
            )
