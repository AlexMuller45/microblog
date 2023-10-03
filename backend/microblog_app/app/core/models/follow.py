from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Follow(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))
    follow_user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))

    def __repr__(self) -> str:
        return f"id: {self.id}"
