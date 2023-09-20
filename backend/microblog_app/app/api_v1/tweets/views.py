from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Tweet, TweetResponse
from . import crud
from core.models import db_helper


router = APIRouter(tags=["Tweets"])


@router.post("/", response_model=TweetResponse)
def add_tweet():
    ...


@router.delete("/{idx}")
def delete_tweet(idx: int):
    ...


@router.post("/{idx}/like")
def add_like(idx: int):
    ...


@router.delete("/{idx}/like")
def delete_like(idx: int):
    ...


@router.get("/", response_model=list[Tweet])
async def get_tweets(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_tweets_for_user(session=session)
