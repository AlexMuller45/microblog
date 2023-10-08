"""
Create Read Update Delete для Tweet
"""

from typing import Any, Dict, List

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from auth.secure import get_user_id
from core.models import Follow, Tweet

from .schemas import TweetBase, TweetIn
from .servises import get_attachments, hide_api_key_tweet


async def get_tweet(session: AsyncSession, tweet_id: int) -> Tweet | None:
    """
    Получите твит по его идентификатору.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        tweet_id (int): Идентификатор твита.

    Returns:
        Tweet | None: Объект Tweet, если он найден, в противном случае — None.

    """

    return await session.get(Tweet, tweet_id)


async def get_last_tweet_id(session: AsyncSession) -> int:
    """
    Получение ID последнего твита.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.

    Returns:
        int: ID последнего твита.

    """

    stmt = select(Tweet).order_by(Tweet.id.desc())
    result: Result = await session.execute(stmt)
    tweet = result.scalars().first()
    return tweet.id


async def get_tweets_for_user(session: AsyncSession, api_key: str) -> list[Tweet]:
    """
    Получение списка твитов для пользователя (по подпискам),
    увеличение счетчика просмотров на 1 для всех полученных твитов.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        api_key (str): API-ключ пользователя.

    Returns:
        list[Tweet]: Список твитов для пользователя.

    """

    current_user_id: int = await get_user_id(session=session, api_key=api_key)
    subq = (
        select(Follow.follow_user_id)
        .where(Follow.user_id == current_user_id)
        .subquery()
    )
    stmt = (
        select(Tweet)
        .options(
            selectinload(Tweet.likes),
            joinedload(Tweet.author),
        )
        .where(Tweet.author_id.in_(select(subq)))
        .order_by(Tweet.views, Tweet.id)
    )

    result: Result = await session.execute(stmt)
    tweets: list[Tweet] = list(result.scalars())

    for tweet in tweets:
        tweet.views += 1

    await session.commit()

    return tweets


async def create_tweet(
    session: AsyncSession,
    tweet_in: TweetIn,
    api_key: str,
) -> dict[str, bool]:
    """
    Создание нового твита.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        tweet_in (TweetIn): Входные данные для твита, проверенные по схеме.
        api_key (str): API-ключ пользователя.

    Returns:
        dict[str, bool]: {"result": True, "tweet_id": tweet.id}

    """

    current_user_id = await get_user_id(session=session, api_key=api_key)
    attachments = await get_attachments(session=session, data=tweet_in.tweet_media_ids)

    tweet = Tweet(
        content=tweet_in.tweet_data,
        attachments=attachments,
        author_id=current_user_id,
        views=0,
    )

    session.add(tweet)
    await session.commit()
    await session.refresh(tweet)

    return {"result": True, "tweet_id": tweet.id}


async def delete_tweet(session: AsyncSession, tweet: Tweet) -> dict[str, bool]:
    """
    Удаление твита.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        tweet (Tweet): Экземпляр Tweet

    Returns:
        dict[str, bool]: {"result": True}

    """

    await session.delete(tweet)
    await session.commit()

    return {"result": True}
