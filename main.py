import sqlite3

DB_PATH = "dummy.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_no TEXT,
            customer_name TEXT,
            product_name TEXT,
            quantity INTEGER,
            status TEXT,
            created_at TEXT
        )
        """
    )
    conn.commit()
    conn.close()
