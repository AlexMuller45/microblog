from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from .follow import Follow


class User(Base):
    name: Mapped[str]
    api_key: Mapped[str]
    followers: Mapped[list] = []

    def __repr__(self) -> str:
        return f"user_id: {self.id}, name: {self.name}"
