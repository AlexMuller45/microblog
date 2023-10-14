"""Валидация данных для User"""

from typing import List
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """Базовая схему пользователя"""

    name: str
    api_key: str = Field(exclude=True)


class User(UserBase):
    """Схема пользователя с идентификатором"""

    id: int


class Followers(BaseModel):
    """Схема для списка подписчиков"""

    followers: List[User]


class Following(BaseModel):
    """Схема для списка подписок"""

    following: List[User]


class UserInfo(User):
    """Схема пользователь со списком подписчиков"""

    followers: List[User]


class UserData(BaseModel):
    """Схема ответа данных пользователя с подписчиками и подписками"""

    result: bool = True
    user: UserInfo
    following: List[User]


class UserResponse(BaseModel):
    """Базовая схема ответа"""

    result: bool = True


class FollowAdd(UserResponse):
    """Схема ответа для добавления подписки"""

    ...
