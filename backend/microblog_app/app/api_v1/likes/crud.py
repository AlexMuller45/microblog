import json

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from auth.secure import get_user
from core.models import Like


async def add_like(session: AsyncSession, tweet_id: int) -> JSONResponse:
    current_user = await get_user(session=session)

    like = Like(
        name=current_user.name,
        user_id=current_user.id,
        tweet_id=tweet_id,
    )

    session.add(like)
    await session.commit()

    return JSONResponse(content=jsonable_encoder({"result": True}))


async def delete_like(session: AsyncSession, like: Like) -> JSONResponse:
    await session.delete(like)
    await session.commit()

    return JSONResponse(content=jsonable_encoder({"result": True}))
