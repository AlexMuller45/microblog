from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.models.base import Base

if TYPE_CHECKING:
    from .tweet import Tweet


class Media(Base):
    filename: Mapped[str]
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweets_tab.id"))

    tweet: Mapped["Tweet"] = relationship(back_populates="medias")

    def __repr__(self) -> str:
        return f"id: {self.id}| file name: {self.filename}"
