from telegram import Update
from telegram.ext import ContextTypes

from app.database.session import get_db
from app.services.user_service import UserService
from app.keyboards.main_menu import (
    get_main_menu_keyboard,
)
from app.utils.telegram import (
    send_message,
)


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Maneja el comando /start.
    """

    telegram_user = update.effective_user

    # Obtener sesión DB
    db = next(get_db())

    # Obtener o crear usuario
    user, created = UserService.get_or_create_user(
        db=db,
        telegram_id=telegram_user.id,
        first_name=telegram_user.first_name,
        username=telegram_user.username,
    )

    if created:

        message = (
            f"🎰 ¡Bienvenido {user.first_name}!\n\n"
            f"Has recibido {user.balance} monedas iniciales.\n\n"
            "Usa /spin para jugar."
        )

    else:

        message = (
            f"🎰 ¡Bienvenido de nuevo {user.first_name}!\n\n"
            f"💰 Balance actual: {user.balance} monedas"
        )

        await send_message(update, message)