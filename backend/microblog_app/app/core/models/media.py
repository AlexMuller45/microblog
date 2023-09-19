from sqlalchemy.orm import Mapped

from core.models.base import Base


class Media(Base):
    filename: Mapped[str]

    def __repr__(self) -> str:
        return f"id: {self.id}| file name: {self.filename}"
