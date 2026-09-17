from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    health_endpoint: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    monitoring_interval: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=5,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )