import logging

from telegram import Update
from telegram.ext import ContextTypes


logger = logging.getLogger(__name__)


async def global_error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Manejo global de errores del bot.
    """

    logger.error(
        "Excepción capturada:",
        exc_info=context.error,
    )

    # Intentar responder al usuario
    if isinstance(update, Update):

        try:

            await update.message.reply_text(
                "❌ Ha ocurrido un error interno."
            )

        except Exception:

            logger.exception(
                "Error enviando mensaje de error"
            )