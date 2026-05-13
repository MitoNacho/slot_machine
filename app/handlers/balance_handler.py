from telegram import Update
from telegram.ext import ContextTypes

from app.database.session import get_db
from app.services.user_service import UserService
from app.utils.slot_constants import (
    WIN_BALANCE,
)
from app.utils.messages import (
    USER_NOT_FOUND,
)

from app.utils.telegram import (
    send_message,
)
from app.keyboards.main_menu import (
    get_main_menu_keyboard,
)

async def balance_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Muestra el balance actual del usuario.
    """

    telegram_user = update.effective_user

    db = next(get_db())

    user = UserService.get_user_by_telegram_id(
        db=db,
        telegram_id=telegram_user.id,
    )

    if not user:

        await update.message.reply_text(
            USER_NOT_FOUND
        )

        return

    progress = round(
        (user.balance / WIN_BALANCE) * 100,
        1,
    )

    message = (
        "💰 BALANCE ACTUAL\n\n"
        f"Monedas: {user.balance}\n"
        f"Objetivo: {WIN_BALANCE}\n"
        f"Progreso: {progress}%"
    )

    await send_message(
    update,
    message,
    reply_markup=get_main_menu_keyboard(),
)