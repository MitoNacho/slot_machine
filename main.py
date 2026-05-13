from app.bot.telegram_bot import create_application

from app.database.init_db import init_db
from app.database.test_connection import (
    test_database_connection,
)

from app.utils.logger import setup_logger

import logging

logger = logging.getLogger(__name__)

def main() -> None:


    setup_logger()

    # Verificar conexión
    test_database_connection()

    # Crear bot
    application = create_application()

    logger.info(
        "🎰 Slot Machine Bot iniciado..."
    )
    application.run_polling()


if __name__ == "__main__":
    main()