"""Модель пользователя"""
from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from .tweet import Tweet


class User(Base):
    """
    Модель представления пользователя.

    Эта модель представляет пользователя, у которого есть имя, ключ API, подписчики и твиты.

    Attributes:
        name (Mapped[str]): Имя пользователя.
        api_key (Mapped[str]): Ключ API, связанный с пользователем.
        followers (Mapped[list]): Пустое поле, для добавления подписчиков из БД.
        tweets (Mapped[List["Tweet"]]): Связь с твитами, пользователя.

    """

    name: Mapped[str]
    api_key: Mapped[str] = mapped_column(unique=True)
    followers: Mapped[list] = []

    tweets: Mapped[List["Tweet"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"user_id: {self.id}, name: {self.name}"
