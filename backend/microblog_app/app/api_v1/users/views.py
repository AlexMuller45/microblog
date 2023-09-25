from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from api_v1.users.schemas import FollowAdd, FollowDelete, UserData
from auth.secure import get_user
from core.models import User, db_helper, Follow
from .dependencies import (
    get_follow_by_user_id,
    get_user_by_id,
    get_follower,
    get_following,
)

router = APIRouter(tags=["Users"])


@router.post("/{idx}/follow", response_model=FollowAdd)
async def add_follow(
    idx: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_follow(session=session, follow_user_id=idx)


@router.delete("/{idx}/follow", response_model=FollowDelete)
async def delete_follow(
    follow: Follow = Depends(get_follow_by_user_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await crud.delete_follow(session=session, follow=follow)


@router.get("/me")
def get_me(
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: User = Depends(get_user),
):
    ...


@router.get("/{idx}", response_model=UserData)
async def get_user_by_id(
    user: User = Depends(get_user_by_id),
    followers: List[User] = Depends(get_follower),
    following: List[User] = Depends(get_following),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    crud.get_user_data(
        session=session, user=user, followers=followers, following=following
    )
