import sqlite3
import sys
from pathlib import Path

from db.db import get_db_connection

DB_PATH = Path(__file__).parent / "database.db"


def retrieve_db_items():
    """ retrieve all items from and return as list. """
    if DB_PATH.exists():
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM FoodItems")

        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return rows


if __name__ == "__main__":
    print("DB_PATH:", DB_PATH.resolve())
    items = retrieve_db_items()
    print(type(items), items)