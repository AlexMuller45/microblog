from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from core.models import User, Like, Media


class Tweet(Base):
    content: Mapped[str]
    author: Mapped[int] = mapped_column(
        ForeignKey("users_tab.id"),
    )
    attachments: Mapped[list[int]] = mapped_column(ARRAY(int))
    views: Mapped[int]

    likes: Mapped[List["Like"]] = relationship(
        back_populates="tweet",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    user: Mapped["User"] = relationship(back_populates="tweets")
    medias: Mapped[List["Media"]] = relationship(back_populates="tweet")

    def __repr__(self) -> str:
        return f"id: {self.id}, content: {self.content}, author: {self.author}"
