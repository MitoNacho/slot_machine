from telegram import BotCommand


def get_bot_commands() -> list[BotCommand]:
    """
    Lista oficial de comandos del bot.
    """

    return [
        BotCommand(
            command="start",
            description="Iniciar partida",
        ),
        BotCommand(
            command="spin",
            description="Tirar la tragaperras",
        ),
        BotCommand(
            command="balance",
            description="Ver balance",
        ),
        BotCommand(
            command="stats",
            description="Ver estadísticas",
        ),
        BotCommand(
            command="help",
            description="Mostrar ayuda",
        ),
    ]