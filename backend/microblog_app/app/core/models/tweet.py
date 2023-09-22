from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from .user import User
    from .like import Like
    from .media import Media


class Tweet(Base):
    content: Mapped[str]
    author: Mapped[int] = mapped_column(
        ForeignKey("users_tab.id"),
    )
    attachments: Mapped[List[str] | None] = mapped_column(ARRAY(String))
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
