from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.balance_handler import (
    balance_command,
)

from app.handlers.help_handler import (
    help_command,
)

from app.handlers.spin_handler import (
    spin_command,
)

from app.handlers.stats_handler import (
    stats_command,
)


async def button_callback_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Maneja botones inline.
    """

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "spin":

        await spin_command(update, context)

    elif data == "balance":

        await balance_command(update, context)

    elif data == "stats":

        await stats_command(update, context)

    elif data == "help":

        await help_command(update, context)