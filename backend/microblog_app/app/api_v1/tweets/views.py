from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from . import crud
from .dependencies import tweet_by_id
from .schemas import Tweet, TweetCreate, TweetDelete

router = APIRouter(tags=["Tweets"])


@router.get("/", response_model=list[Tweet])
async def get_tweets(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_tweets_for_user(session=session)


@router.post("/", response_model=TweetCreate)
async def add_tweet(
    tweet_in: TweetCreate, session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_tweet(session=session, tweet_in=tweet_in)


@router.delete("/{idx}", response_model=TweetDelete)
async def delete_tweet(
    tweet: Tweet = Depends(tweet_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.delete_tweet(session=session, tweet=tweet)


@router.post("/{idx}/like")
def add_like(idx: int):
    ...


@router.delete("/{idx}/like")
def delete_like(idx: int):
    ...
