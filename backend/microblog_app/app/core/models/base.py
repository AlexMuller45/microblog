from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column)


class Base(DeclarativeBase):
    """
    Объявление класса Base для моделей SQLAlchemy.

    Этот класс обеспечивает общую основу для всех моделей SQLAlchemy в приложении.
    Он определяет атрибут __tablename__ и столбец id в качестве первичного ключа.

    Attributes:
        __tablename__ (str): Имя таблицы базы данных, связанной с моделью.
        id (int): Первичный ключ.

    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s_tab"

    id: Mapped[int] = mapped_column(primary_key=True)
