from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from ..likes.views import router as likes_router
from . import crud
from .dependencies import tweet_by_id
from .schemas import Tweet, TweetCreate, TweetIn

router = APIRouter(tags=["Tweets"])
router.include_router(router=likes_router)


@router.get("/", response_model=list[Tweet], status_code=status.HTTP_200_OK)
async def get_tweets(
    request: Request,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    api_key: str = request.headers.get("api-key")
    return await crud.get_tweets_for_user(session=session, api_key=api_key)


@router.post("/", response_model=TweetCreate, status_code=status.HTTP_201_CREATED)
async def add_tweet(
    request: Request,
    tweet_in: TweetIn,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    api_key: str = request.headers.get("api-key")
    return await crud.create_tweet(
        session=session,
        tweet_in=tweet_in,
        api_key=api_key,
    )


@router.delete(
    "/{idx}",
    status_code=status.HTTP_200_OK,
)
async def delete_tweet(
    tweet: Tweet = Depends(tweet_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_tweet(session=session, tweet=tweet)
