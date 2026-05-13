import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="slot_machine",
        user="postgres",
        password="19940228"
    )

    print("✅ PostgreSQL conectado")

    connection.close()

except Exception as error:
    print("❌ Error")
    print(repr(error))