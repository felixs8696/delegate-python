# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import ObjectiveActivity, ActivityListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActivities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        activity = client.activities.create(
            objective_id="objective_id",
            content={"content": "content"},
        )
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Delegate) -> None:
        activity = client.activities.create(
            objective_id="objective_id",
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
            streaming_status="IN_PROGRESS",
        )
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.activities.with_raw_response.create(
            objective_id="objective_id",
            content={"content": "content"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.activities.with_streaming_response.create(
            objective_id="objective_id",
            content={"content": "content"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ObjectiveActivity, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        activity = client.activities.retrieve(
            "activity_id",
        )
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.activities.with_raw_response.retrieve(
            "activity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.activities.with_streaming_response.retrieve(
            "activity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ObjectiveActivity, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `activity_id` but received ''"):
            client.activities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        activity = client.activities.list(
            objective_id="objective_id",
        )
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Delegate) -> None:
        activity = client.activities.list(
            objective_id="objective_id",
            limit=0,
        )
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.activities.with_raw_response.list(
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.activities.with_streaming_response.list(
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityListResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActivities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        activity = await async_client.activities.create(
            objective_id="objective_id",
            content={"content": "content"},
        )
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDelegate) -> None:
        activity = await async_client.activities.create(
            objective_id="objective_id",
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
            streaming_status="IN_PROGRESS",
        )
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.activities.with_raw_response.create(
            objective_id="objective_id",
            content={"content": "content"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.activities.with_streaming_response.create(
            objective_id="objective_id",
            content={"content": "content"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ObjectiveActivity, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        activity = await async_client.activities.retrieve(
            "activity_id",
        )
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.activities.with_raw_response.retrieve(
            "activity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ObjectiveActivity, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.activities.with_streaming_response.retrieve(
            "activity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ObjectiveActivity, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `activity_id` but received ''"):
            await async_client.activities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        activity = await async_client.activities.list(
            objective_id="objective_id",
        )
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDelegate) -> None:
        activity = await async_client.activities.list(
            objective_id="objective_id",
            limit=0,
        )
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.activities.with_raw_response.list(
            objective_id="objective_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.activities.with_streaming_response.list(
            objective_id="objective_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityListResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True
