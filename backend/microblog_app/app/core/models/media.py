"""Модель для хранения данных загруженных файлов"""

from sqlalchemy.orm import Mapped

from core.models.base import Base


class Media(Base):
    """
    Модель для хранения данных загруженных файловых.

    Эта модель содержит ID и имя файла.

    Attributes:
        filename (Mapped[str]): Имя загруженного файла.

    """

    filename: Mapped[str]

    def __repr__(self) -> str:
        return f"id: {self.id}| file name: {self.filename}"
