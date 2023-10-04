from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column, sessionmaker)


class Base(DeclarativeBase):
    pass
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s_tab"

    id: Mapped[int] = mapped_column(primary_key=True)
