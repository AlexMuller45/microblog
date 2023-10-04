from typing import List, Annotated

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import FollowAdd, UserData
from auth.secure import get_user_id
from core.models import Follow, User, db_helper

from . import crud
from .dependencies import (
    get_follow_by_user_id,
    get_follower,
    get_following,
    get_my_follower,
    get_my_following,
)

router = APIRouter(tags=["Users"])


@router.get(
    "/me",
    response_model=UserData,
    status_code=status.HTTP_200_OK,
)
async def get_me(
    request: Request,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    api_key: str = request.headers.get("api-key")
    user_id: int | None = await get_user_id(session=session, api_key=api_key)

    followers: List[User] = await get_my_follower(user_id=user_id, session=session)
    following: List[User] = await get_my_following(user_id=user_id, session=session)

    return await crud.get_user_data(
        idx=user_id,
        followers=followers,
        following=following,
        session=session,
    )


@router.post(
    "/{idx}/follow",
    response_model=FollowAdd,
    status_code=status.HTTP_201_CREATED,
)
async def add_follow(
    request: Request,
    idx: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    api_key: str = request.headers.get("api-key")
    return await crud.create_follow(
        session=session, follow_user_id=idx, api_key=api_key
    )


@router.delete(
    "/{idx}/follow",
    status_code=status.HTTP_200_OK,
)
async def delete_follow(
    request: Request,
    follow: Follow = Depends(get_follow_by_user_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_follow(session=session, follow=follow)


@router.get(
    "/{idx}",
    response_model=UserData,
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(
    idx: int,
    followers: List[User] = Depends(get_follower),
    following: List[User] = Depends(get_following),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_user_data(
        idx=idx,
        followers=followers,
        following=following,
        session=session,
    )
