from typing import Annotated, List

from fastapi import Depends, Path, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from auth.secure import get_user_id
from core.models import Follow, User, db_helper

from . import crud


async def get_follow_by_user_id(
    request: Request,
    idx: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Follow:
    api_key: str = request.headers.get("api-key")
    current_user_id = await get_user_id(session=session, api_key=api_key)
    follow = await crud.get_follow(
        session=session, user_id=current_user_id, follow_user_id=idx
    )
    if follow:
        return follow

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"The subscription #ID[{idx}] is not found",
    )


async def get_user_by_id(
    idx: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User | JSONResponse:
    user = await crud.get_user(session=session, user_id=idx)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"The user #ID[{idx}] is not found",
    )


async def get_follower(
    idx: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> List[User]:
    followers = await crud.get_followers(session=session, user_id=idx)
    if followers:
        return followers
    return []


async def get_following(
    idx: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> List[User]:
    following = await crud.get_following(session=session, user_id=idx)
    if following:
        return following
    return []


async def get_my_follower(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
) -> List[User]:
    followers = await crud.get_followers(session=session, user_id=user_id)
    if followers:
        return followers
    return []


async def get_my_following(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
) -> List[User]:
    following = await crud.get_following(session=session, user_id=user_id)
    if following:
        return following
    return []
