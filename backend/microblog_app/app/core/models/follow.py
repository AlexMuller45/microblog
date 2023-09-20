from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import User

from .base import Base


class Follow(Base):
    followers: Mapped[int] = mapped_column(ForeignKey("users.id"))
    following: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"id: {self.id}"
