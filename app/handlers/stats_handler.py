from telegram import Update
from telegram.ext import ContextTypes

from app.database.session import get_db
from app.services.user_service import UserService
from app.utils.messages import (
    USER_NOT_FOUND,
)
from app.utils.telegram import (
    send_message,
)
from app.keyboards.main_menu import (
    get_main_menu_keyboard,
)

async def stats_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Muestra estadísticas del jugador.
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

    win_rate = UserService.calculate_win_rate(
        user
    )

    message = (
        "📊 ESTADÍSTICAS\n\n"
        f"🎰 Spins totales: {user.total_spins}\n"
        f"🏆 Victorias: {user.total_wins}\n"
        f"💀 Derrotas: {user.total_losses}\n"
        f"📈 Win rate: {win_rate}%\n"
        f"💰 Balance actual: {user.balance}"
    )

    await send_message(
    update,
    message,
    reply_markup=get_main_menu_keyboard(),
)