from app.database.base import Base
from app.database.database import engine

# Importar modelos
from app.models import User


def init_db() -> None:
    """
    Crea todas las tablas en la base de datos.
    """

    Base.metadata.create_all(bind=engine)

    print("✅ Tablas creadas correctamente")