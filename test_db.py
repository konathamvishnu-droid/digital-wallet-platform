
from sqlalchemy import text

from app.db.session import engine


def test_database_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database connection successful!")


if __name__ == "__main__":
    test_database_connection()
