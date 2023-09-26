import json
from typing import List, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

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


async def get_following(session: AsyncSession, user_id: int) -> List[User] | None:
    subq = select(Follow.follow_user_id).where(Follow.user_id == user_id).subquery()
    stmt = select(User).where(User.id.in_(subq)).order_by(User.id)
    result: Result = await session.execute(stmt)
    following = result.scalars().all()
    return list(following)


async def get_followers(session: AsyncSession, user_id: int) -> List[User] | None:
    subq = select(Follow.user_id).where(Follow.follow_user_id == user_id).subquery()
    stmt = select(User).where(User.id.in_(subq)).order_by(User.id)
    result: Result = await session.execute(stmt)
    followers = result.scalars().all()
    return list(followers)


async def create_follow(session: AsyncSession, follow_user_id: int) -> JSONResponse:
    current_user_id = await get_user_id(session)
    follow = Follow(user_id=current_user_id, follow_user_id=follow_user_id)

    session.add(follow)
    await session.commit()

    return JSONResponse(content={"result": True})


async def delete_follow(session: AsyncSession, follow: Follow) -> JSONResponse:
    await session.delete(follow)
    await session.commit()

    return JSONResponse(content={"result": True})


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


def get_user_data(
    user: User,
    followers: List[User],
    following: List[User],
) -> JSONResponse:
    response_data: json = {"result": True}
    response_data["user"].update(jsonable_encoder(user))
    response_data["user"]["followers"].update(jsonable_encoder(followers))
    response_data["following"].update(jsonable_encoder(following))

    return JSONResponse(content=response_data)
