"""
Create Read Update Delete для User
"""

import json
from typing import List

from fastapi import HTTPException
from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from auth.secure import get_user_id
from core.models import Follow, User


async def get_follow(
    session: AsyncSession, user_id: int, follow_user_id: int
) -> Follow | None:
    """
    Получение экземпляра Follow по пользователю и его подписке

    Args:
        session (AsyncSession): Объект асинхронного сеанса.
        user_id (int): Идентификатор пользователя.
        follow_user_id (int): Идентификатор подписки.

    Returns:
        Follow | None: Экземпляр Follow, или None.

    """

    stmt: Select = (
        select(Follow)
        .where(Follow.user_id == user_id)
        .where(Follow.follow_user_id == follow_user_id)
    )
    follow: Follow | None = await session.scalar(stmt)

    return follow


def hide_api_key(data: list[User]) -> List[User]:
    """
    Скрытие API-ключей в списке пользователей.

    Args:
        data (list[User]): Список пользователей.

    Returns:
        List[User]: Список пользователей со скрытыми API-ключами.

    """

    for item in data:
        item.api_key = "*" * 12
    return data


async def get_following(session: AsyncSession, user_id: int) -> List[User]:
    """
    Получение подписок для пользователя.

    Args:
        session (AsyncSession): Объект асинхронного сеанса.
        user_id (int): Идентификатор пользователя.

    Returns:
        List[User]: Список подписок.

    """

    subq = select(Follow.follow_user_id).where(Follow.user_id == user_id).subquery()
    stmt: Select = select(User).where(User.id.in_(select(subq))).order_by(User.id)
    result: Result = await session.execute(stmt)
    following = list(result.scalars().all())
    return hide_api_key(following)


async def get_followers(session: AsyncSession, user_id: int) -> List[User]:
    """
    Получение списка подписчиков на пользователя.

    Args:
        session (AsyncSession): The asynchronous session object.
        user_id (int): TID пользователя.

    Returns:
        List[User]: Список подписчиков.

    """

    subq = select(Follow.user_id).where(Follow.follow_user_id == user_id).subquery()
    stmt: Select = select(User).where(User.id.in_(select(subq))).order_by(User.id)
    result: Result = await session.execute(stmt)
    followers = list(result.scalars().all())
    return hide_api_key(followers)


async def create_follow(
    session: AsyncSession, follow_user_id: int, api_key: str
) -> dict[str, bool]:
    """
    Добавление подписке пользователю.

    Args:
        session (AsyncSession): Объект асинхронного сеанса.
        follow_user_id (int): Идентификатор подписки.
        api_key (str): API-ключ текущего пользователя.

    Returns:
        dict[str, bool]: {"result": True}

    """

    current_user_id = await get_user_id(session=session, api_key=api_key)

    follow = Follow(user_id=current_user_id, follow_user_id=follow_user_id)

    session.add(follow)
    await session.commit()

    return {"result": True}


async def delete_follow(session: AsyncSession, follow: Follow) -> dict[str, bool]:
    """
    Удаление подписки

    Args:
        session (AsyncSession): Объект асинхронного сеанса.
        follow (Follow): Экземпляр Follow/

    Returns:
        dict[str, bool]: {"result": True}

    """

    await session.delete(follow)
    await session.commit()

    return {"result": True}


async def get_user(session: AsyncSession, user_id: int) -> User:
    """
    Получение экземпляра User по ID.

    Args:
        session (AsyncSession): Объект асинхронного сеанса.
        user_id (int): Идентификатор пользователя.

    Returns:
        User: Экземпляр User

    Raises:
        HTTPException: Если пользователь не найден.

    """

    user: User | None = await session.get(User, user_id)

    if user:
        return user

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail="User not found",
    )


async def get_user_data(
    idx: int,
    followers: List[User],
    following: List[User],
    session: AsyncSession,
) -> dict[str, bool]:
    """
    Получите данные о пользователе, включая его подписчиков и подписок.

    Args:
        idx (int): Идентификатор пользователя.
        followers (List[User]): Список подписчиков.
        following (List[User]): Список подписок.
        session (AsyncSession): Объект асинхронного сеанса.

    Returns:
        dict: Данные, содержащие пользователя, подписчиков и подписок.

    """

    user: User = await get_user(session=session, user_id=idx)

    user.api_key = "*" * 12
    user.followers = followers

    return {
        "result": True,
        "user": user,
        "following": following,
    }
