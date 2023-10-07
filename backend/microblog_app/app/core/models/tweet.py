from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from .like import Like
    from .user import User


class Tweet(Base):
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))
    attachments: Mapped[List[str] | None] = mapped_column(ARRAY(String))
    views: Mapped[int]

    likes: Mapped[List["Like"] | None] = relationship(
        back_populates="tweet",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    author: Mapped["User"] = relationship(back_populates="tweets")

    def __repr__(self) -> str:
        return (
            f"id: {self.id}, "
            f"content: {self.content}, "
            f"author: {self.author}, "
            f"attachments: {self.attachments}, "
            f"likes: {self.likes}"
        )
