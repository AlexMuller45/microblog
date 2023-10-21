from httpx import AsyncClient
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User, Tweet
from .conftest import ac, test_session, tweet, user

ENDPOINT = "/api/tweets/"
AUTH = {"api-key": "test"}


class TestDB:
    async def test_add_user_in_db(self, user, test_session: AsyncSession):
        query = select(User).where(User.name == "Like_69")
        result: Result = await test_session.execute(query)
        data = result.scalar()
        assert data.name == "Like_69"

    async def test_add_tweet_in_db(self, tweet, test_session: AsyncSession):
        _tweet = await test_session.scalar(select(Tweet))

        assert isinstance(_tweet, Tweet)
        assert isinstance(_tweet.content, str)

    async def test_auth_tweet(self, ac: AsyncClient):
        response = await ac.get(ENDPOINT)
        assert response.status_code == 403

        data = response.json()
        assert data["result"] == False


class TestEndpointsTweet:
    async def test_endpoint_get_tweets(self, ac: AsyncClient):
        response = await ac.get(ENDPOINT, headers=AUTH)
        assert response.status_code == 200

        data = response.json()
        assert data["result"] == True
        assert isinstance(data["tweets"], list)

    async def test_endpoint_post_tweet(self, ac: AsyncClient):
        request_body = {
            "tweet_data": "Привет, мир! Я использую YouBot, умную модель языка от You.com"
        }
        response = await ac.post(ENDPOINT, json=request_body, headers=AUTH)

        assert response.status_code == 201

        data = response.json()
        assert data["result"] == True
        assert "tweet_id" in data

    async def test_endpoint_delete_tweet(
        tweet, test_session: AsyncSession, ac: AsyncClient
    ):
        _tweet = (
            await test_session.scalars(
                select(Tweet).where(Tweet.content == "test test to add tweet")
            )
        ).first()
        tweet_id = _tweet.id
        print(tweet_id)
        response = await ac.delete(f"{ENDPOINT}{tweet_id}", headers=AUTH)

        assert response.status_code == 200

        response_data = response.json()
        print()
        assert response_data["result"] == True
