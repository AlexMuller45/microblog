from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tweets.crud import get_last_tweet_id
from core.models import Media


async def add_media(session: AsyncSession, file_name: str) -> int:
    media = Media(filename=file_name)
    session.add(media)
    await session.commit()
    await session.refresh(media)

    return media.id
