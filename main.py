import argparse
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


def reset_table():
    conn = get_connection()
    conn.execute("DROP TABLE IF EXISTS orders")
    conn.commit()
    conn.close()
    init_db()


def generate_order():
    return (
        f"ORD-{random.randint(1, 999999):06d}",
        fake.name(),
        fake.word().capitalize(),
        random.randint(1, 100),
        random.choice(STATUSES),
        datetime.now().isoformat(),
    )


def insert_orders(n):
    orders = [generate_order() for _ in range(n)]
    conn = get_connection()
    conn.executemany(
        """
        INSERT INTO orders (order_no, customer_name, product_name, quantity, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        orders,
    )
    conn.commit()
    conn.close()


def parse_args():
    parser = argparse.ArgumentParser(description="Generate dummy orders")
    parser.add_argument("--count", type=int, default=10, help="number of orders to generate")
    parser.add_argument("--reset", action="store_true", help="wipe and recreate the orders table first")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.reset:
        reset_table()
    else:
        init_db()
    insert_orders(args.count)
