"""Валидация данных для Media"""

from pydantic import BaseModel


class MediaAdd(BaseModel):
    """Схема ответа для добавления файла"""

    result: bool = True
    media_id: int
