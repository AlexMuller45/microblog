from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.models.base import Base
from core.models import Tweet


class Media(Base):
    filename: Mapped[str]
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweets_tab.id"))

    tweet: Mapped["Tweet"] = relationship(back_populates="medias")

    def __repr__(self) -> str:
        return f"id: {self.id}| file name: {self.filename}"
