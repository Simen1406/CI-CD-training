import sqlite3
import sys
from pathlib import Path

from db.db import get_db_connection, get_db_path


def retrieve_db_items():
    """ retrieve all items from and return as list. """
    if get_db_path().exists():
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM FoodItems")

        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return rows

def insert_db_items():
    """Creates new row for db."""

    # Check if DB exists and has items
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM FoodItems")
    count = cursor.fetchone()[0]
    next_id = count + 1

        #if no items, insert some initial data for testing
    print("Inserting initial items into DB...")
    cursor.execute("INSERT INTO FoodItems (name, category, price) VALUES (?, ?, ?)",
        ("salmon", "fish", 35)
    )
    conn.commit()

    # Fetch the newly inserted row
    inserted_id = cursor.lastrowid
    print(f"Inserted item with id {inserted_id}.")
        
    conn.close()
    return {"id": inserted_id, "name": "salmon", "category": "fish", "price": 35}


if __name__ == "__main__":
    #print("DB_PATH:", DB_PATH.resolve())
    items = retrieve_db_items()
    new_row = insert_db_items()
    print(type(items), items)