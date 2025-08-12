# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import (
    Objective,
    ObjectiveListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjectives:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        objective = client.objectives.create(
            name="name",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.objectives.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.objectives.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        objective = client.objectives.retrieve(
            "objective_id",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.objectives.with_raw_response.retrieve(
            "objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.objectives.with_streaming_response.retrieve(
            "objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        objective = client.objectives.list()
        assert_matches_type(ObjectiveListResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Delegate) -> None:
        objective = client.objectives.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(ObjectiveListResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.objectives.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(ObjectiveListResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.objectives.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(ObjectiveListResponse, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Delegate) -> None:
        objective = client.objectives.delete(
            "objective_id",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Delegate) -> None:
        response = client.objectives.with_raw_response.delete(
            "objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Delegate) -> None:
        with client.objectives.with_streaming_response.delete(
            "objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Delegate) -> None:
        objective = client.objectives.cancel(
            objective_id="objective_id",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Delegate) -> None:
        objective = client.objectives.cancel(
            objective_id="objective_id",
            reason="reason",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Delegate) -> None:
        response = client.objectives.with_raw_response.cancel(
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Delegate) -> None:
        with client.objectives.with_streaming_response.cancel(
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.cancel(
                objective_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: Delegate) -> None:
        objective = client.objectives.stream_events(
            "objective_id",
        )
        assert_matches_type(object, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: Delegate) -> None:
        response = client.objectives.with_raw_response.stream_events(
            "objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(object, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: Delegate) -> None:
        with client.objectives.with_streaming_response.stream_events(
            "objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(object, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.stream_events(
                "",
            )


class TestAsyncObjectives:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.create(
            name="name",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.retrieve(
            "objective_id",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.with_raw_response.retrieve(
            "objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.with_streaming_response.retrieve(
            "objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.list()
        assert_matches_type(ObjectiveListResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(ObjectiveListResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(ObjectiveListResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(ObjectiveListResponse, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.delete(
            "objective_id",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.with_raw_response.delete(
            "objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.with_streaming_response.delete(
            "objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.cancel(
            objective_id="objective_id",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.cancel(
            objective_id="objective_id",
            reason="reason",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.with_raw_response.cancel(
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.with_streaming_response.cancel(
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.cancel(
                objective_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncDelegate) -> None:
        objective = await async_client.objectives.stream_events(
            "objective_id",
        )
        assert_matches_type(object, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncDelegate) -> None:
        response = await async_client.objectives.with_raw_response.stream_events(
            "objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(object, objective, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncDelegate) -> None:
        async with async_client.objectives.with_streaming_response.stream_events(
            "objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(object, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.stream_events(
                "",
            )
