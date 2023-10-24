"""Модель подписчиков и подписок"""

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Follow(Base):
    """
    Модель представления пользователей и их подписок.

    Эта модель представляет отношения в одну сторону - подписки, в другую сторону - подписчики.

    Attributes:
        user_id (Mapped[int]): Идентификатор пользователя
        follow_user_id (Mapped[int]): Идентификатор пользователя, на которого подписаны

    """

    user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))
    follow_user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))

    __table_args__ = (UniqueConstraint("user_id", "follow_user_id"),)

    def __repr__(self) -> str:
        return f"id: {self.id}"
