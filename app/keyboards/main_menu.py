from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Keyboard principal del juego.
    """

    keyboard = [

        [
            InlineKeyboardButton(
                "🎰 SPIN",
                callback_data="spin",
            )
        ],

        [
            InlineKeyboardButton(
                "💰 BALANCE",
                callback_data="balance",
            ),

            InlineKeyboardButton(
                "📊 STATS",
                callback_data="stats",
            ),
        ],

        [
            InlineKeyboardButton(
                "❓ HELP",
                callback_data="help",
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)