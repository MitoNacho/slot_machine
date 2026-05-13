from sqlalchemy.orm import Session

from app.models.user import User


class UserService:
    """
    Servicio encargado de la lógica de usuarios.
    """

    @staticmethod
    def get_user_by_telegram_id(
        db: Session,
        telegram_id: int,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.telegram_id == telegram_id)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        telegram_id: int,
        first_name: str,
        username: str | None = None,
    ) -> User:

        user = User(
            telegram_id=telegram_id,
            first_name=first_name,
            username=username,
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def get_or_create_user(
        db: Session,
        telegram_id: int,
        first_name: str,
        username: str | None = None,
    ) -> tuple[User, bool]:

        user = UserService.get_user_by_telegram_id(
            db=db,
            telegram_id=telegram_id,
        )

        if user:
            return user, False

        new_user = UserService.create_user(
            db=db,
            telegram_id=telegram_id,
            first_name=first_name,
            username=username,
        )

        return new_user, True

    @staticmethod
    def calculate_win_rate(
        user: User,
    ) -> float:
        """
        Calcula porcentaje de victorias.
        """

        if user.total_spins == 0:
            return 0.0

        return round(
            (user.total_wins / user.total_spins) * 100,
            2,
        )