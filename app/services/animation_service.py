import asyncio
import random

from telegram import Message

from app.utils.slot_constants import (
    SYMBOL_WEIGHTS,
)


class AnimationService:
    """
    Servicio de animaciones.
    """

    @staticmethod
    def generate_random_row() -> str:
        """
        Genera una fila aleatoria visual.
        """

        symbols = list(
            SYMBOL_WEIGHTS.keys()
        )

        weights = list(
            SYMBOL_WEIGHTS.values()
        )

        row = random.choices(
            symbols,
            weights=weights,
            k=3,
        )

        return " | ".join(row)

    @staticmethod
    async def play_spin_animation(
        message: Message,
    ) -> None:
        """
        Ejecuta animación fake
        con desaceleración progresiva.
        """

        delays = [
            0.1,
            0.15,
            0.25,
            0.4,
            0.6,
        ]

        for delay in delays:

            row = (
                AnimationService
                .generate_random_row()
            )

            text = (
                "━━━━━━━━━━━━━━\n"
                "🎰 GIRANDO... 🎰\n"
                "━━━━━━━━━━━━━━\n\n"
                f"{row}"
            )

            await message.edit_text(text)

            await asyncio.sleep(delay)