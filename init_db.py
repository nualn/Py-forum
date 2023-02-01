from os import getenv
import sqlalchemy as sa
from dotenv import load_dotenv

from werkzeug.security import generate_password_hash

def init_db(database_conn):
    database_conn.execute("""
        DROP SCHEMA IF EXISTS public CASCADE;
        CREATE SCHEMA public;
    """)
    file = open("schema.sql")
    sql = file.read()
    database_conn.execute(sql)

if __name__ == "__main__":
    load_dotenv()

    db_url = getenv("DATABASE_URL")
    engine = sa.create_engine(db_url)
    conn = engine.connect()

    print("Initializing database...")
    init_db(conn)
    print("Database initialized.")

    conn.close()

