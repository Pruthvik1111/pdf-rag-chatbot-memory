import sqlite3

DB_NAME = "memory.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(role, message):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history(role, message)
        VALUES (?, ?)
        """,
        (role, message)
    )

    conn.commit()
    conn.close()


def load_memory():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, message
        FROM chat_history
        ORDER BY id
    """)

    history = cursor.fetchall()

    conn.close()

    return history