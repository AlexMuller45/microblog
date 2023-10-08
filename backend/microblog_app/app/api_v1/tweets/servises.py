from typing import List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.medias import crud
from core.config import settings
from core.models import Tweet, Media, db_helper


async def get_media_path(
    media_id: int,
    session: AsyncSession,
) -> str:
    media: Media = await crud.get_media(session=session, media_id=media_id)
    media_file_name: str = settings.filename.format(
        media_id=media_id, in_file_name=media.filename
    )
    return f"/app/media/{media_file_name}"


async def get_attachments(
    session: AsyncSession, data: List[int] | None
) -> List[str] | None:
    links = []
    if data:
        for item in data:
            link: str = await get_media_path(session=session, media_id=item)
            links.append(link)
        return links
    return


def hide_api_key_tweet(data: list[Tweet]) -> List[Tweet]:
    for item in data:
        item.author.api_key = "*" * 12
    return data
