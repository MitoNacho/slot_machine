from telegram import Update
from telegram.ext import ContextTypes
from app.utils.telegram import (
    send_message,
)
from app.keyboards.main_menu import (
    get_main_menu_keyboard,
)
async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Muestra los comandos disponibles.
    """

    help_message = (
    "📚 COMANDOS DISPONIBLES\n\n"
    "/start - Iniciar partida\n"
    "/spin - Tirar la tragaperras\n"
    "/balance - Ver monedas\n"
    "/stats - Ver estadísticas\n"
    "/help - Mostrar ayuda"
)
    await send_message(
    update,
    help_message,
    reply_markup=get_main_menu_keyboard(),
)