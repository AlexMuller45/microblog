import pytest

from httpx import AsyncClient
from pytest_httpx import HTTPXMock

from .conftest import ac


endpoint = "/api/tweets/"
AUTH = {"api-key": "test"}


async def test_get_tweets(ac: AsyncClient, httpx_mock: HTTPXMock):
    httpx_mock.add_response(headers={"api-key": "test"})

    response = await ac.get(endpoint)
    assert response.status_code == 200


def test_post_tweet():
    pass


def test_delete_tweet():
    pass
