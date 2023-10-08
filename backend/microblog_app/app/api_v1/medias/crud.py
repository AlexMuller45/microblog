from typing import Type
from fastapi import Response
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tweets.crud import get_last_tweet_id
from core.models import Media


async def add_media(session: AsyncSession, file_name: str) -> int:
    media = Media(filename=file_name)
    session.add(media)
    await session.commit()
    await session.refresh(media)

    return media.id


async def get_media(session: AsyncSession, media_id: int) -> Media:
    stmt = select(Media).where(Media.id == media_id)
    result: Result = await session.execute(stmt)
    media: Media = result.scalar_one()
    return media
