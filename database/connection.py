import sqlite3

def db_init():
    conn = sqlite3.connect("database/app.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('pending', 'done', 'canceled')),
        created_at TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime'))
        )
    """)

    conn.commit()
    conn.close()

    # run in terminal: python -c "from database.db import init_db; init_db()"

def get_db():
    return sqlite3.connect("database/app.db")