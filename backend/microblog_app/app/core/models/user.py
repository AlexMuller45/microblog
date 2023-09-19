from sqlalchemy.orm import Mapped

from core.models.base import Base


class User(Base):
    name: Mapped[str]

    def __repr__(self) -> str:
        return f"user_id: {self.id}, name: {self.name}"
