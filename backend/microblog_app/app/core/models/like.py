from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from core.models import Tweet


class Like(Base):
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))
    tweet_id: Mapped[int] = mapped_column(ForeignKey("users_tab.id"))

    tweet: Mapped["Tweet"] = relationship(back_populates="likes")

    def __repr__(self) -> str:
        return f"user_id: {self.user_id}, name: {self.name}"
