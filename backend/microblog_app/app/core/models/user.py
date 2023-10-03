from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


class User(Base):
    name: Mapped[str]
    api_key: Mapped[str] = mapped_column(unique=True)
    followers: Mapped[list] = []

    def __repr__(self) -> str:
        return f"user_id: {self.id}, name: {self.name}"
