# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from delegate import Delegate, AsyncDelegate
from tests.utils import assert_matches_type
from delegate.types import (
    Channel,
    ChannelMembership,
    ChannelListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Delegate) -> None:
        channel = client.channels.create()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Delegate) -> None:
        channel = client.channels.create(
            channel_metadata={"foo": "bar"},
            description="description",
            is_group_chat=True,
            is_private=True,
            name="name",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Delegate) -> None:
        channel = client.channels.retrieve(
            "channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.retrieve(
            "channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.retrieve(
            "channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Delegate) -> None:
        channel = client.channels.update(
            channel_id="channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Delegate) -> None:
        channel = client.channels.update(
            channel_id="channel_id",
            channel_metadata={"foo": "bar"},
            description="description",
            is_archived=True,
            name="name",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.update(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.update(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.update(
                channel_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Delegate) -> None:
        channel = client.channels.list()
        assert_matches_type(ChannelListResponse, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Delegate) -> None:
        channel = client.channels.list(
            is_group_chat=True,
            is_private=True,
            limit=0,
        )
        assert_matches_type(ChannelListResponse, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelListResponse, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelListResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Delegate) -> None:
        channel = client.channels.delete(
            "channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.delete(
            "channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.delete(
            "channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_join(self, client: Delegate) -> None:
        channel = client.channels.join(
            channel_id="channel_id",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_join_with_all_params(self, client: Delegate) -> None:
        channel = client.channels.join(
            channel_id="channel_id",
            role="role",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_join(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.join(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_join(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.join(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelMembership, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_join(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.join(
                channel_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_leave(self, client: Delegate) -> None:
        channel = client.channels.leave(
            channel_id="channel_id",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_leave_with_all_params(self, client: Delegate) -> None:
        channel = client.channels.leave(
            channel_id="channel_id",
            reason="reason",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_leave(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.leave(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_leave(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.leave(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(ChannelMembership, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_leave(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.with_raw_response.leave(
                channel_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_name(self, client: Delegate) -> None:
        channel = client.channels.retrieve_by_name(
            "channel_name",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_name(self, client: Delegate) -> None:
        response = client.channels.with_raw_response.retrieve_by_name(
            "channel_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: Delegate) -> None:
        with client.channels.with_streaming_response.retrieve_by_name(
            "channel_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_name(self, client: Delegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_name` but received ''"):
            client.channels.with_raw_response.retrieve_by_name(
                "",
            )


class TestAsyncChannels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.create()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.create(
            channel_metadata={"foo": "bar"},
            description="description",
            is_group_chat=True,
            is_private=True,
            name="name",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.retrieve(
            "channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.retrieve(
            "channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.retrieve(
            "channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.update(
            channel_id="channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.update(
            channel_id="channel_id",
            channel_metadata={"foo": "bar"},
            description="description",
            is_archived=True,
            name="name",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.update(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.update(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.update(
                channel_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.list()
        assert_matches_type(ChannelListResponse, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.list(
            is_group_chat=True,
            is_private=True,
            limit=0,
        )
        assert_matches_type(ChannelListResponse, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelListResponse, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelListResponse, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.delete(
            "channel_id",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.delete(
            "channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.delete(
            "channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_join(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.join(
            channel_id="channel_id",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_join_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.join(
            channel_id="channel_id",
            role="role",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_join(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.join(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.join(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelMembership, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_join(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.join(
                channel_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_leave(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.leave(
            channel_id="channel_id",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_leave_with_all_params(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.leave(
            channel_id="channel_id",
            reason="reason",
        )
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.leave(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(ChannelMembership, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.leave(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(ChannelMembership, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_leave(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.with_raw_response.leave(
                channel_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncDelegate) -> None:
        channel = await async_client.channels.retrieve_by_name(
            "channel_name",
        )
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncDelegate) -> None:
        response = await async_client.channels.with_raw_response.retrieve_by_name(
            "channel_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel = await response.parse()
        assert_matches_type(Channel, channel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncDelegate) -> None:
        async with async_client.channels.with_streaming_response.retrieve_by_name(
            "channel_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel = await response.parse()
            assert_matches_type(Channel, channel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_name(self, async_client: AsyncDelegate) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_name` but received ''"):
            await async_client.channels.with_raw_response.retrieve_by_name(
                "",
            )
