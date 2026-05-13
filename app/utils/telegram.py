from telegram import Update


async def send_message(
    update: Update,
    text: str,
    **kwargs,
) -> None:
    """
    Envía mensajes compatible con:
    - comandos
    - callbacks
    """

    if update.message:

        await update.message.reply_text(
            text,
            **kwargs,
        )

    elif update.callback_query:

        await update.callback_query.message.reply_text(
            text,
            **kwargs,
        )