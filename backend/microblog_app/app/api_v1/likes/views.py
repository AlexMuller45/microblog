"""Роуты для Like"""

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.likes.schemas import LikeAdd, LikeDelete
from core.models import Like, db_helper

from . import crud
from .dependencies import get_like_by_tweet_id

router = APIRouter(tags=["Likes"])


@router.post(
    "/{idx}/like",
    response_model=LikeAdd,
    status_code=status.HTTP_201_CREATED,
)
async def add_like(
    request: Request,
    idx: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Добавьте лайк к твиту.

    Args:
        request (Request): Объект запроса FastAPI.
        idx (int): Идентификатор твита как параметр пути.
        session (AsyncSession, optional): Асинхронный сеанс SQLAlchemy.

    Returns:
        {"result": True}

    """

    api_key: str = request.headers.get("api-key")
    return await crud.add_like(session=session, tweet_id=idx, api_key=api_key)


@router.delete(
    "/{idx}/like",
    response_model=LikeDelete,
    status_code=status.HTTP_200_OK,
)
async def delete_like(
    request: Request,
    like: Like = Depends(get_like_by_tweet_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Удаление лайка из твита.

     Args:
         request (Request): Объект запроса FastAPI.
         like (Like): Объект Like получен с использованием зависимости get_like_by_tweet_id.
         session (AsyncSession, optional): Асинхронный сеанс SQLAlchemy.

     Returns:
         {"result": True}

    """

    return await crud.delete_like(session=session, like=like)
