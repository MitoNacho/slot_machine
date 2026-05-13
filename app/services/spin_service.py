import random

from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.slot_constants import (
    REWARDS,
    SPIN_COST,
    SYMBOL_WEIGHTS,
    WIN_BALANCE,
    INITIAL_BALANCE,
)


class SpinService:
    """
    Servicio principal de la tragaperras.
    """

    @staticmethod
    def generate_spin() -> list[str]:
        """
        Genera símbolos usando probabilidades balanceadas.
        """

        symbols = list(
            SYMBOL_WEIGHTS.keys()
        )

        weights = list(
            SYMBOL_WEIGHTS.values()
        )

        return random.choices(
            symbols,
            weights=weights,
            k=3,
        )

    @staticmethod
    def calculate_reward(
        symbols: list[str],
    ) -> int:
        """
        Calcula la recompensa del spin.
        """

        return REWARDS.get(tuple(symbols), 0)

    @staticmethod
    def process_spin(
        db: Session,
        user: User,
    ) -> dict:
        """
        Procesa un spin completo.
        """

        # Verificar balance
        if user.balance < SPIN_COST:

            user.balance = INITIAL_BALANCE

            db.commit()

            return {
                "success": False,
                "message": (
                    "💀 Te has quedado sin monedas.\n"
                    "La partida ha sido reiniciada.\n\n"
                    f"💰 Nuevo balance: {INITIAL_BALANCE}"
                )
            }

        # Cobrar spin
        user.balance -= SPIN_COST

        # Generar símbolos
        symbols = SpinService.generate_spin()

        # Calcular premio
        reward = SpinService.calculate_reward(
            symbols
        )

        # Actualizar balance
        user.balance += reward

        # Actualizar estadísticas
        user.total_spins += 1

        if reward > 0:
            user.total_wins += 1
        else:
            user.total_losses += 1

        # Verificar victoria
        jackpot = False

        if user.balance >= WIN_BALANCE:

            jackpot = True

            user.balance = INITIAL_BALANCE

        # Guardar cambios
        db.commit()

        return {
            "success": True,
            "symbols": symbols,
            "reward": reward,
            "balance": user.balance,
            "jackpot": jackpot,
        }