import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    """
    Configuración global del proyecto.
    """

    BOT_TOKEN: str = os.getenv(
        "BOT_TOKEN",
        "",
    )

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "",
    )

    # Compatibilidad Railway + SQLAlchemy
    if DATABASE_URL.startswith(
        "postgresql://"
    ):

        DATABASE_URL = DATABASE_URL.replace(
            "postgresql://",
            "postgresql+psycopg2://",
            1,
        )


settings = Settings()