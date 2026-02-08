import sqlite3
import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "database.db"
print("DB_PATH:", DB_PATH.resolve())


def init_db() -> None:
    """Initialize  sqlite db with schema."""
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FoodItems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
                   )
                   """)
    
    conn.commit()
    conn.close()

def create_db_items():
    """Creates some initial rows if db is empty."""

    # Check if DB exists and has items
    init_db()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM FoodItems")
    count = cursor.fetchone()[0]

    if count == 0:
        #if no items, insert some initial data for testing
        print("Inserting initial items into DB...")
        cursor.executemany("INSERT INTO FoodItems (name, category, price) VALUES (?, ?, ?)",
            [
            ("milk", "dairy", 35),
            ("pepperoni", "meat", 37),
            ("Salad", "vegetable", 25),
            ("Ice Cream", "sweets", 63)
            ]
        )
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM FoodItems")
        count = cursor.fetchone()[0]
        print(f"Inserted {count} items into DB.")
        
        conn.close()
        return count

def get_db_connection():
    """Get a connection to the sqlite db."""
    if not DB_PATH.exists():
        print("Database not found, initializing...")
        init_db()
    return sqlite3.connect(DB_PATH)


#create_db_items()
#get_db_connection()