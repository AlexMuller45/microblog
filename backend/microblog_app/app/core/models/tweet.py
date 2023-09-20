from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .user import User


class Tweet(Base):
    content: Mapped[str]
    author: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    attachments: Mapped[list[int]] = mapped_column(
        ARRAY(int),
    )

    def __repr__(self) -> str:
        return f"id: {self.id}, content: {self.content}, author: {self.author}"
