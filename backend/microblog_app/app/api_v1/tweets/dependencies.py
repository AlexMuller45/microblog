from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from core.models import db_helper, Tweet
from . import crud


async def tweet_by_id(
    tweet_id: Annotated[int, Path()],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Tweet:
    tweet = await crud.get_tweet(session=session, tweet_id=tweet_id)

    if tweet:
        return tweet

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Tweet id:{tweet_id} not found",
    )
