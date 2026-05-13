from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base
from app.utils.slot_constants import INITIAL_BALANCE

class User(Base):
    """
    Modelo principal de usuario.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    balance: Mapped[int] = mapped_column(
        Integer,
        default=INITIAL_BALANCE,
        nullable=False,
    )

    total_spins: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_wins: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_losses: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )