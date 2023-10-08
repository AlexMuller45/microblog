"""Валидация данных для Like"""

from pydantic import BaseModel


class LikeResponse(BaseModel):
    """Базовая схема"""

    result: bool = True


class LikeAdd(LikeResponse):
    """Схема ответа для добавления лайка"""

    ...


class LikeDelete(LikeResponse):
    """Схема ответа для удаления лайка"""

    ...


class Like(BaseModel):
    """Схема ответа лайка"""

    user_id: int
    name: str
