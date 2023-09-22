from typing import List

from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base
from core.models import Tweet, Follow


class User(Base):
    name: Mapped[str]
    api_key: Mapped[str]

    tweets: Mapped[List["Tweet"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"user_id: {self.id}, name: {self.name}"
