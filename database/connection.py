import sqlite3

# Initial function to create database and notes tables
def db_init():
    conn = sqlite3.connect("database/app.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('pending', 'done', 'canceled')),
        created_at TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime'))
        )
    """)

    conn.commit()
    conn.close()

    # run in terminal: python -c "from database.connection import db_init; db_init()"

def get_db():   # Helper function to get connection with database
    return sqlite3.connect("database/app.db")