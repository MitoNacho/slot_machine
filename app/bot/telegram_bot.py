from telegram.ext import (
    Application,
    CommandHandler,
)
from app.config.settings import settings
from app.handlers.start_handler import start_command
from app.handlers.help_handler import help_command
from app.handlers.spin_handler import spin_command
from app.handlers.balance_handler import (balance_command,)
from app.handlers.stats_handler import (stats_command,)
from app.handlers.error_handler import (global_error_handler,)
from app.bot.commands import (get_bot_commands,)
from telegram.ext import CallbackQueryHandler
from app.handlers.callback_handler import (
    button_callback_handler,
)

async def setup_bot_commands(
    application: Application,
) -> None:
    """
    Registra comandos oficiales en Telegram.
    """

    await application.bot.set_my_commands(
        get_bot_commands()
    )


def create_application() -> Application:
    """
    Crea y configura la aplicación principal del bot.
    """

    application = Application.builder().token(
        settings.BOT_TOKEN
    ).build()
    
    application.post_init = setup_bot_commands


    # Registro de comandos
    application.add_handler(
        CommandHandler("start", start_command)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
    CommandHandler("spin", spin_command)
    )

    application.add_handler(
    CommandHandler(
        "balance",
        balance_command,
    )
)

    application.add_handler(
    CommandHandler(
        "stats",
        stats_command,
    )
)
    

    application.add_error_handler(
    global_error_handler
)


    application.add_handler(
    CallbackQueryHandler(
        button_callback_handler
    )
)
    return application