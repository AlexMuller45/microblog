from typing import Annotated

from fastapi import Depends, Path, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Like, db_helper
from . import crud


async def get_like_by_tweet_id(
    request: Request,
    idx: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Like:
    api_key: str = request.headers.get("api-key")

    like: Like = await crud.get_like_by_tweet_id(
        session=session, tweet_id=idx, api_key=api_key
    )

    if like:
        return like

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The like is not found",
    )
