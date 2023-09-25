from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tweets.crud import get_last_tweet_id
from core.models import Media


async def add_media(session: AsyncSession, file_name: str) -> int:
    last_tweet_id = await get_last_tweet_id(session=session)
    # TODO убрать привязку к твиту
    media = Media(file_name=file_name, tweet_id=last_tweet_id)
    session.add(media)
    await session.commit()
    await session.refresh(media)

    return media.id
