from sqlalchemy import text

from app.database.database import engine 

import traceback

def test_database_connection() -> None:
    """
    Prueba la conexión con PostgreSQL.
    """

    try:
        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT 1")
            )

            print("✅ Conexión a PostgreSQL exitosa")

            for row in result:
                print(row)

    except Exception as error:
        print("❌ Error conectando a PostgreSQL")
        
        
        traceback.print_exc()