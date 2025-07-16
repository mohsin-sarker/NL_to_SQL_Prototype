import sqlite3

"""Create a users.db database

This document will create a users.db dataabse to store registered users data..
Create users table.
"""

# Create Connection to users.db database in the same directory
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create new tables into users database and drop if they exists
cursor.execute("DROP TABLE IF EXISTS users")


# Create users table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

conn.commit()
conn.close()

print("✅ Users database seeded.")