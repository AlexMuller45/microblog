import json

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from auth.secure import get_user_id
from core.models import Follow, Tweet

from .schemas import TweetCreate, TweetIn


async def get_tweet(session: AsyncSession, tweet_id: int) -> Tweet | None:
    return await session.get(Tweet, tweet_id)


async def get_last_tweet_id(session: AsyncSession) -> int:
    stmt = select(Tweet).order_by(Tweet.id.desc())
    result: Result = await session.execute(stmt)
    tweet = result.scalars().first()
    return tweet.id


async def get_tweets_for_user(session: AsyncSession, api_key: str) -> list[Tweet]:
    current_user_id = await get_user_id(session=session, api_key=api_key)
    subq = (
        select(Follow.follow_user_id)
        .where(Follow.user_id == current_user_id)
        .subquery()
    )
    stmt = (
        select(Tweet)
        .options(
            selectinload(Tweet.likes),
            joinedload(Tweet.user),
            selectinload(Tweet.medias),
        )
        .where(Tweet.author.in_(select(subq)))
        .order_by(Tweet.views, Tweet.id)
    )
    result: Result = await session.execute(stmt)
    tweets = result.scalars().all()
    return list(tweets)


async def create_tweet(
    session: AsyncSession,
    tweet_in: TweetIn,
    api_key: str,
) -> JSONResponse:
    current_user_id = await get_user_id(session=session, api_key=api_key)
    tweet = Tweet(
        content=tweet_in.tweet_data,
        attachments=tweet_in.tweet_media_ids,
        author=current_user_id,
        views=0,
    )

    session.add(tweet)
    await session.commit()
    await session.refresh(tweet)

    return JSONResponse(content={"result": True, "tweet_id": tweet.id})


async def delete_tweet(session: AsyncSession, tweet: Tweet) -> JSONResponse:
    await session.delete(tweet)
    await session.commit()

    response_json: json = jsonable_encoder({"result": True})
    return JSONResponse(content=response_json)
