import random
import sqlite3
from datetime import datetime

from faker import Faker

DB_PATH = "dummy.db"
STATUSES = ("pending", "shipped", "completed")

fake = Faker()


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


def generate_order():
    return (
        f"ORD-{random.randint(1, 999999):06d}",
        fake.name(),
        fake.word().capitalize(),
        random.randint(1, 100),
        random.choice(STATUSES),
        datetime.now().isoformat(),
    )
