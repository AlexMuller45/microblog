from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Tweet, Follow, User
from .schemas import TweetBase


async def get_tweets_for_user(session: AsyncSession) -> list[Tweet]:

    subq = select(Follow.following).where(Follow.followers == current_user).subquery()
    stmt = select(Tweet).where(Tweet.author.in_(subq))
    result: Result = await session.execute(stmt)
    tweets = result.scalars().all()
    return list(tweets)


async def create_tweet(session: AsyncSession, tweet_in: TweetBase) -> Tweet:
    tweet = Tweet(**tweet_in.model_dump())
    session.add(tweet)
    await session.commit()
    await session.refresh(tweet)
    return tweet
