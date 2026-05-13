from telegram import Update
from telegram.ext import ContextTypes

from app.database.session import get_db

from app.keyboards.main_menu import (
    get_main_menu_keyboard,
)

from app.services.animation_service import (
    AnimationService,
)

from app.services.spin_service import (
    SpinService,
)

from app.services.user_service import (
    UserService,
)

from app.utils.messages import (
    USER_NOT_FOUND,
)

from app.utils.telegram import (
    send_message,
)


async def spin_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Ejecuta un spin de la tragaperras.
    """

    telegram_user = update.effective_user

    db = next(get_db())

    # Buscar usuario
    user = UserService.get_user_by_telegram_id(
        db=db,
        telegram_id=telegram_user.id,
    )

    # Usuario no encontrado
    if not user:

        await send_message(
            update,
            USER_NOT_FOUND,
            reply_markup=get_main_menu_keyboard(),
        )

        return

    # Crear mensaje inicial según origen
    if update.callback_query:

        spin_message = await (
            update.callback_query.message.reply_text(
                "🎰 Preparando tragaperras..."
            )
        )

    else:

        spin_message = await (
            update.message.reply_text(
                "🎰 Preparando tragaperras..."
            )
        )

    # Ejecutar animación
    await AnimationService.play_spin_animation(
        spin_message
    )

    # Procesar lógica real del spin
    result = SpinService.process_spin(
        db=db,
        user=user,
    )

    # Caso derrota/reset
    if not result["success"]:

        await spin_message.edit_text(
            result["message"],
            reply_markup=get_main_menu_keyboard(),
        )

        return

    # Símbolos visuales
    symbols_text = " | ".join(
        result["symbols"]
    )

    # Cabecera
    message = (
        "━━━━━━━━━━━━━━\n"
        "🎰 SLOT MACHINE 🎰\n"
        "━━━━━━━━━━━━━━\n\n"
        f"{symbols_text}\n\n"
    )

    # Premio o pérdida
    if result["reward"] > 0:

        message += (
            f"🎉 ¡Has ganado "
            f"{result['reward']} monedas!\n"
        )

    else:

        message += (
            "😢 No hubo premio.\n"
        )

    # Jackpot
    if result["jackpot"]:

        message += (
            "\n🏆 ¡HAS GANADO LA PARTIDA!\n"
            "Tu progreso ha sido reiniciado."
        )

    # Balance final
    message += (
        f"\n\n💰 Balance actual: "
        f"{result['balance']}"
    )

    # Editar mensaje final
    await spin_message.edit_text(
        message,
        reply_markup=get_main_menu_keyboard(),
    )