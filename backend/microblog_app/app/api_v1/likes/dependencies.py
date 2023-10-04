import json
from typing import Annotated

from fastapi import Depends, Path
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from auth.secure import get_user_id
from core.models import Like, db_helper

from . import crud


async def get_like_by_tweet_id(
    tweet_id: Annotated[int, Path()],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    current_user_id = await get_user_id(session=session)
    stmt = (
        select(Like)
        .where(Like.tweet_id == tweet_id)
        .where(Like.user_id == current_user_id)
    )
    result: Result = await session.execute(stmt)

    like = result.scalars().one()

    if like:
        return like

    response_json: json = jsonable_encoder(
        {
            "result": False,
            "error_type": "HTTP_404_NOT_FOUND",
            "error_message": "The like is not found",
        }
    )
    return JSONResponse(content=response_json)
