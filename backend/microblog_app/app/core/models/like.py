"""Модель лайков"""
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from .tweet import Tweet


class Like(Base):
    """
    Модель лайков в твитах.

    Эта модель содержит связь между пользователями, который поставил лайк и твитами.

    Attributes:
        name (Mapped[str]): Имя пользователя
        user_id (Mapped[int]): ID пользователя, поставившего лайк.
        tweet_id (Mapped[int]): ID твита, под которым поставлен лайк.
        tweet (Mapped["Tweet"]): Связь с моделью Tweet.

    """

    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweets_tab.id"))

    tweet: Mapped["Tweet"] = relationship(back_populates="likes")

    def __repr__(self) -> str:
        return f"user_id: {self.user_id}, name: {self.name}"
