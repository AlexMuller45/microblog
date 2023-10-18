import pytest

from httpx import AsyncClient
from sqlalchemy import insert, select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User, Tweet
from .conftest import ac, test_session

ENDPOINT = "/api/tweets/"
AUTH = {"api-key": "test"}


async def test_get_tweets(ac: AsyncClient):
    response = await ac.get(ENDPOINT, headers=AUTH)
    assert response.status_code == 200

    data = response.json()
    assert data["result"] == True
    assert isinstance(data["tweets"], list)


async def test_add_user(test_session: AsyncSession):
    user: User = User(name="Test", api_key="test")

    test_session.add(user)
    await test_session.commit()

    query = select(User)
    result: Result = await test_session.execute(query)
    data = result.scalar_one_or_none()
    assert data.name == "Test"


async def test_post_tweet(ac: AsyncClient):
    request_body = {
        "tweet_data": "Привет, мир! Я использую YouBot, умную модель языка от You.com"
    }
    response = await ac.post(ENDPOINT, json=request_body, headers=AUTH)

    assert response.status_code == 201

    data = response.json()
    assert data["result"] == True
    assert "tweet_id" in data


async def test_add_tweet(test_session: AsyncSession):
    content: str = "test test to add tweet"
    data = await test_session.scalars(select(User))
    user = data.first()

    tweet = Tweet(
        content=content,
        attachments=None,
        author_id=user.id,
        views=0,
    )

    test_session.add(tweet)
    await test_session.commit()

    tweet = await test_session.scalar(select(Tweet))

    assert isinstance(tweet, Tweet)
    assert tweet.content == content


async def test_delete_tweet(test_session: AsyncSession, ac: AsyncClient):
    tweet = await test_session.scalar(select(Tweet))

    response = await ac.delete(ENDPOINT + f"/{tweet.id}", headers=AUTH)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["result"] == True
