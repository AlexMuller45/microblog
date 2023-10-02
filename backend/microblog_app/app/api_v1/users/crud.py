import json
from typing import List, Dict, Any, Type, Union

from fastapi.encoders import jsonable_encoder
from fastapi import Response
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from auth.secure import get_user_id
from core.models import Follow, User


async def get_follow(
    session: AsyncSession, user_id: int, follow_user_id: int
) -> Follow | None:
    stmt = (
        select(Follow)
        .where(Follow.user_id == user_id)
        .where(Follow.follow_user_id == follow_user_id)
    )
    follow: Follow | None = await session.scalar(stmt)

    return follow


async def get_following(session: AsyncSession, user_id: int) -> List[User]:
    subq = select(Follow.follow_user_id).where(Follow.user_id == user_id).subquery()
    stmt = select(User).where(User.id.in_(subq)).order_by(User.id)
    result: Result = await session.execute(stmt)
    following = result.scalars().all()
    return following


async def get_followers(session: AsyncSession, user_id: int) -> List[User]:
    subq = select(Follow.user_id).where(Follow.follow_user_id == user_id).subquery()
    stmt = select(User).where(User.id.in_(subq)).order_by(User.id)
    result: Result = await session.execute(stmt)
    followers = result.scalars().all()
    return followers


async def create_follow(session: AsyncSession, follow_user_id: int) -> dict[str, bool]:
    current_user_id = await get_user_id(session)
    follow = Follow(user_id=current_user_id, follow_user_id=follow_user_id)

    session.add(follow)
    await session.commit()

    return {"result": True}


async def delete_follow(session: AsyncSession, follow: Follow) -> dict[str, bool]:
    await session.delete(follow)
    await session.commit()

    return {"result": True}


async def get_user(session: AsyncSession, user_id: int) -> User | JSONResponse:
    user: User | None = await session.get(User, user_id)

    if user:
        return user

    return JSONResponse(
        content={
            "result": False,
            "error_type": "HTTP_404_NOT_FOUND",
            "error_message": "User not found",
        },
        status_code=404,
    )


async def get_user_data(
    idx: int,
    followers: List[User],
    following: List[User],
    session: AsyncSession,
) -> JSONResponse | dict[str, bool | str]:
    user: User = await get_user(session=session, user_id=idx)

    users_dict = jsonable_encoder(user)
    users_dict["followers"] = jsonable_encoder(followers)

    response_data = {
        "result": True,
        "user": users_dict,
        "following": jsonable_encoder(following),
    }

    return JSONResponse(content=response_data)
