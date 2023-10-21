from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from .conftest import ac, test_session, user
from core.models import User


class TestEndpointsUsers:
    endpoint: str = "/api/users/"
    auth: dict[str] = {"api-key": "test"}

    async def test_endpoint_get_me(self, ac: AsyncClient):
        response = await ac.get(f"{self.endpoint}me", headers=self.auth)

        assert response.status_code == 200
        assert response.json()["result"] == True

    async def test_endpoint_get_user_by_id(self, ac: AsyncClient):
        response = await ac.get(f"{self.endpoint}2")

        assert response.status_code == 200
        assert response.json()["result"] == True
        assert response.json()["user"]["name"] == "test2"

    async def test_endpoint_add_follows(self, ac: AsyncClient):
        response = await ac.post(f"{self.endpoint}2/follow", headers=self.auth)

        assert response.status_code == 201
        assert response.json() == {"result": True}

    async def test_endpoint_delete_follow(self, ac: AsyncClient):
        response = await ac.delete(f"{self.endpoint}2/follow", headers=self.auth)

        assert response.status_code == 200
        assert response.json() == {"result": True}
