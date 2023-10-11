"""Роуты для User"""

from typing import Annotated, List

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import FollowAdd, UserData, UserResponse
from auth.secure import check_user, get_user_id
from core.models import Follow, User, db_helper

from . import crud
from .dependencies import (get_follow_by_user_id, get_follower, get_following,
                           get_my_follower, get_my_following)

router = APIRouter(tags=["Users"])


@router.get(
    "/me",
    response_model=UserData,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(check_user)],
)
async def get_me(
    request: Request,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Получение данных для текущего аутентифицированного пользователя.

    Args:
        request (Request): Объект запроса FastAPI.
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.

    Returns:
        UserData: Пользовательские данные для текущего аутентифицированного пользователя.

    """

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
    dependencies=[Depends(check_user)],
)
async def add_follow(
    request: Request,
    idx: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Добавление подписки к текущему аутентифицированному пользователю.

    Args:
        request (Request): Объект запроса FastAPI.
        idx(int): ID пользователя на которого добавляется подписка.
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.

    Returns:
        dict[str, bool]: {"result": True}

    """

    api_key: str = request.headers.get("api-key")
    return await crud.create_follow(
        session=session, follow_user_id=idx, api_key=api_key
    )


@router.delete(
    "/{idx}/follow",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(check_user)],
)
async def delete_follow(
    request: Request,
    follow: Follow = Depends(get_follow_by_user_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Удаление подписки у текущему аутентифицированному пользователя.

    Args:
        request (Request): Объект запроса FastAPI.
        follow(Follow): Экземпляр Follow, который удаляется
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.

    Returns:
        dict[str, bool]: {"result": True}

    """
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
    """
    Получение данных для пользователя с указанным идентификатором.

    Args:
        idx (int): Идентификатор пользователя, которого требуется получить.
        followers (List[User]): Список подписчиков. Для получения используется зависимость get_follower.
        following (List[User]): Список подписок пользователя. Для получения используется зависимость get_following.
        session (AsyncSession): Объект SQLAlchemy AsyncSession.

    Returns:
        UserData: Данные пользователя с указанным идентификатором.

    """

    return await crud.get_user_data(
        idx=idx,
        followers=followers,
        following=following,
        session=session,
    )
