"""Зависимости для Tweet"""

from typing import Annotated

from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from core.models import Tweet, db_helper

from . import crud


async def tweet_by_id(
    idx: Annotated[int, Path()],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Tweet:
    """
    Получение твита по ID

    Args:
        idx (Annotated[int, Path]): Идентификатор твита из пути.
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.

    Returns:
         Tweet: Экземпляр Tweet

    Raises:
        HTTPException: Если tweet не найден, вызывает HTTPException с кодом состояния 404.

    """

    tweet = await crud.get_tweet(session=session, tweet_id=idx)

    if tweet:
        return tweet

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Tweet id:{idx} not found",
    )
