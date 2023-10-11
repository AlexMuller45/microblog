"""Дополнительные функции обработки и подготовки данных для Tweet"""

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.medias import crud
from core.config import settings
from core.models import Media, Tweet


async def get_media_path(
    media_id: int,
    session: AsyncSession,
) -> str:
    """
    Генерация ссылки на  файлы

    Args:
        media_id (int): Идентификатор файла.
        session (AsyncSession): Объект асинхронного сеанса.

    Returns:
        str: ссылка на файл.

    """

    media: Media = await crud.get_media(session=session, media_id=media_id)
    media_file_name: str = settings.filename.format(
        media_id=media_id, in_file_name=media.filename
    )
    return f"/api/medias/{media_file_name}"


async def get_attachments(
    session: AsyncSession, data: List[int] | None
) -> List[str] | None:
    """
    Генерация списка ссылок на файлы из списка ID файлов

    Args:
        session (AsyncSession): Объект асинхронного сеанса.
        data (List[int] | None): Список идентификаторов файлов.

    Returns:
        List[str] | None: Список ссылок на файлы или None, если файлов нет.

    """

    links = []
    if data:
        for item in data:
            link: str = await get_media_path(session=session, media_id=item)
            links.append(link)
        return links
    return


def hide_api_key_tweet(data: list[Tweet]) -> List[Tweet]:
    """
    Скрытие API-ключей в списке твитов.

    Args:
        data (list[Tweet]): Список твитов.

    Returns:
        List[Tweet]: Список твитов со скрытыми API-ключами.

    """

    for item in data:
        item.author.api_key = "*" * 12
    return data
