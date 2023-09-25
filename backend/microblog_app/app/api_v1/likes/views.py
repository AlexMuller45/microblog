from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from api_v1.likes.schemas import LikeAdd, LikeDelete
from core.models import db_helper, Like
from .dependencies import get_like_by_tweet_id

router = APIRouter(tags=["Likes"])


@router.post("/{idx}/like", response_model=LikeAdd)
async def add_like(
    idx: int,
    session: AsyncSession = Depends((db_helper.session_dependency())),
):
    return await crud.add_like(session=session, tweet_id=idx)


@router.delete("/{idx}/like", response_model=LikeDelete)
async def delete_like(
    like: Like = Depends(get_like_by_tweet_id),
    session: AsyncSession = Depends(db_helper.session_dependency()),
):
    await crud.delete_like(session=session, like=like)
    return JSONResponse(content=jsonable_encoder({"result": True}))
