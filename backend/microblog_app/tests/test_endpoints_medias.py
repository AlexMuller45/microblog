import os

import aiofiles
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.microblog_app.tests.conftest import (
    test_session,
    ac,
)
from core.config import settings
from core.models import Media


class TestEndpointsMedias:
    endpoint: str = "/api/medias/"
    auth: dict[str] = {"api-key": "test"}
    media_dir = settings.media_path

    async def test_endpoint_get_media(self, ac: AsyncClient):
        os.makedirs(self.media_dir, exist_ok=True)
        async with aiofiles.open(
            os.path.join(self.media_dir, "test_image.jpg"), "w"
        ) as f:
            await f.write("test content")

        response = await ac.get(f"{self.endpoint}test_image.jpg", headers=self.auth)
        assert response.status_code == 200

        os.remove(os.path.join(self.media_dir, "test_image.jpg"))

    async def test_endpoint_add_media(
        self, ac: AsyncClient, test_session: AsyncSession
    ):
        files = {"file": ("temp_file.jpg", open("temp_file.jpg", "rb"))}

        response = await ac.post(self.endpoint, files=files)
        media_id = response.json()["media_id"]
        assert response.status_code == 201

        stmt = select(Media).where(Media.id == media_id)
        result = await test_session.execute(stmt)
        _media = result.scalar()
        print(_media)
        assert _media is not None

        file_path = f"{self.media_dir}/{settings.filename.format(media_id=media_id, file_name='temp_file.jpg')}"
        os.remove(file_path)
        await test_session.delete(_media)
        await test_session.commit()
