"""
Create Read Update Delete для Media
"""

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Media


async def add_media(session: AsyncSession, file_name: str) -> int:
    """
    Создайте новую запись Media в базе данных.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        file_name (str): Имя файла.

    Returns:
        int: Идентификатор файла в БД.

    """

    media = Media(filename=file_name)
    session.add(media)
    await session.commit()
    await session.refresh(media)

    return media.id


async def get_media(session: AsyncSession, media_id: int) -> Media:
    """
    Получает запись Media по ее идентификатору.

    Args:
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.
        media_id (int): Идентификатор файла, для которого требуется получить данные из БД.

    Returns:
        Media

    """

    stmt = select(Media).where(Media.id == media_id)
    result: Result = await session.execute(stmt)
    media: Media = result.scalar_one()
    return media
