import sqlite3
import os


# Get the current directory of this script and initialize the database path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "database", "users.db")

# Create and return a connection to SQLite database.
def get_db_connection():
    try:
        conn = sqlite3.connect(db_path, check_same_thread=False)
        return conn
    except sqlite3.Error as e:
        print(f"An Error has been happend to connect to the database!: {e}")
        return None
