"""
Create Read Update Delete для Like
"""

from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.secure import get_user, get_user_id
from core.models import Like


async def add_like(
    session: AsyncSession, tweet_id: int, api_key: str
) -> dict[str, bool]:
    """
    Добавьте лайк к твиту.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        tweet_id (int): ID твита, которому нужно поставить лайк.
        api_key (str): API-ключ для аутентификации.

    Returns:
        dict[str, bool]

    """

    current_user = await get_user(session=session, api_key=api_key)

    like = Like(
        name=current_user.name,
        user_id=current_user.id,
        tweet_id=tweet_id,
    )

    session.add(like)
    await session.commit()

    return {"result": True}


async def get_like_by_tweet_id(session: AsyncSession, tweet_id, api_key: str) -> Like:
    """
    Получите лайк по идентификатору твита.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        tweet_id: ID твита, которому поставлен лайк.
        api_key (str): API-ключ для аутентификации.

    Returns:
        Like: объект Like, соответствующий идентификатору твита и аутентифицированному пользователю.

    """

    current_user_id = await get_user_id(session=session, api_key=api_key)

    stmt: Select = (
        select(Like)
        .where(Like.tweet_id == tweet_id)
        .where(Like.user_id == current_user_id)
    )
    result: Result = await session.execute(stmt)
    like: Like = result.scalar_one_or_none()

    return like


async def delete_like(session: AsyncSession, like: Like) -> dict[str, bool]:
    """
    Удаление лайка

     Args:
         session (AsyncSession): Асинхронный сеанс SQLAlchemy.
         like (Like): Объект Like для удаления.

     Returns:
         dict[str, bool]

    """

    await session.delete(like)
    await session.commit()

    return {"result": True}
