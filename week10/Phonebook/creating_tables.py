import psycopg2
from config import load_config

def create_tables():
    config = load_config()

    commands = [
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS phone_numbers (
            contact_id INT REFERENCES contacts(id) ON DELETE CASCADE,
            phone_number VARCHAR(20) NOT NULL UNIQUE
        );
        """
    ]

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("Таблицы созданы ")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")

if __name__ == "__main__":
    create_tables()
