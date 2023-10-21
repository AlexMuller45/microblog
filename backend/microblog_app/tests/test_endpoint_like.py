from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from backend.microblog_app.tests.conftest import (
    get_tweet_id,
    test_session,
    get_tweet_id_through_like,
)


class TestEndpointsLike:
    endpoint: str = "/api/tweets/"
    auth: dict[str] = {"api-key": "test"}

    async def test_endpoint_add_like(self, ac: AsyncClient, test_session: AsyncSession):
        tweet_id: int = await get_tweet_id(test_session)
        print("* " * 5, tweet_id)
        response = await ac.post(f"{self.endpoint}{tweet_id}/like", headers=self.auth)
        assert response.status_code == 201

        data = response.json()
        assert data["result"] == True

    async def test_endpoint_delete_like(
        self, ac: AsyncClient, test_session: AsyncSession
    ):
        tweet_id = await get_tweet_id_through_like(test_session)
        print("*  " * 5, tweet_id)
        response = await ac.delete(f"{self.endpoint}{tweet_id}/like", headers=self.auth)
        assert response.status_code == 200
        assert response.json() == {"result": True}
