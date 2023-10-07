from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from .tweet import Tweet


class User(Base):
    name: Mapped[str]
    api_key: Mapped[str] = mapped_column(unique=True)
    followers: Mapped[list] = []

    tweets: Mapped[List["Tweet"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"user_id: {self.id}, name: {self.name}"
