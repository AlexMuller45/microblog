from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Follow(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))
    follow_user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))

    __table_args__ = (UniqueConstraint("user_id", "follow_user_id"),)

    def __repr__(self) -> str:
        return f"id: {self.id}"
