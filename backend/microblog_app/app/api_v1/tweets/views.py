"""Роуты для Tweet"""

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from ..likes.views import router as likes_router
from . import crud
from .dependencies import tweet_by_id
from .schemas import Tweet, TweetCreate, TweetIn, TweetDelete

router = APIRouter(tags=["Tweets"])
router.include_router(router=likes_router)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Tweet,
    response_model_exclude={"api_key"},
)
async def get_tweets(
    request: Request,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Получение всех твитов для пользователя

    Args:
        request (Request): Объект запроса.
        session (AsyncSession): Объект асинхронного сеанса.

    Returns:
        dict: {"result": True, "tweets": [список твитов]}

    """

    api_key: str = request.headers.get("api-key")
    response_data = await crud.get_tweets_for_user(session=session, api_key=api_key)

    return {"result": True, "tweets": response_data}


@router.post("/", response_model=TweetCreate, status_code=status.HTTP_201_CREATED)
async def add_tweet(
    request: Request,
    tweet_in: TweetIn,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Создание нового твита

    Args:
        request (Request): Объект запроса.
        tweet_in (TweetIn): Входные данные твита, проверенные по схеме.
        session (AsyncSession): Объект асинхронного сеанса.

    Returns:
        dict: {"result": True, "tweet_id": идентификатор твита}

    """

    api_key: str = request.headers.get("api-key")
    return await crud.create_tweet(
        session=session,
        tweet_in=tweet_in,
        api_key=api_key,
    )


@router.delete(
    "/{idx}",
    response_model=TweetDelete,
    status_code=status.HTTP_200_OK,
)
async def delete_tweet(
    tweet: Tweet = Depends(tweet_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Удаление твита.

    Args:
        tweet (Tweet): Экземпляр Tweet.
        session (AsyncSession): Объект асинхронного сеанса.

    Returns:
        dict: {"result": True}

    """

    return await crud.delete_tweet(session=session, tweet=tweet)
