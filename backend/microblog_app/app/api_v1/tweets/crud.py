import json
from typing import Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from auth.secure import get_user_id
from core.models import Follow, Tweet

from .schemas import TweetCreate


async def get_tweet(session: AsyncSession, tweet_id: int) -> Tweet | None:
    return await session.get(Tweet, tweet_id)


async def get_last_tweet_id(session: AsyncSession) -> int:
    stmt = select(Tweet).order_by(Tweet.id.desc())
    result: Result = await session.execute(stmt)
    tweet = result.scalars().first()
    return tweet.id


async def get_tweets_for_user(session: AsyncSession) -> list[Tweet]:
    current_user_id = await get_user_id(session=session)
    subq = (
        select(Follow.follow_user_id)
        .where(Follow.user_id == current_user_id)
        .subquery()
    )
    stmt = select(Tweet).where(Tweet.author.in_(subq)).order_by(Tweet.views, Tweet.id)
    result: Result = await session.execute(stmt)
    tweets = result.scalars().all()
    return list(tweets)


async def create_tweet(session: AsyncSession, tweet_in: TweetCreate) -> JSONResponse:
    tweet = Tweet(**tweet_in.model_dump())
    session.add(tweet)
    await session.commit()
    await session.refresh(tweet)

    response_json: json = jsonable_encoder({"result": True, "tweet_id": tweet.id})
    return JSONResponse(content=response_json)


async def delete_tweet(session: AsyncSession, tweet: Tweet) -> JSONResponse:
    await session.delete(tweet)
    await session.commit()

    response_json: json = jsonable_encoder({"result": True})
    return JSONResponse(content=response_json)
