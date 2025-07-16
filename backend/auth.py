from utils.connection import get_db_connection
from utils.hashing import hash_password, verify_password


# Create function to register users
def register_user(fname, lname, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        hashed_pw = hash_password(password)
        cursor.execute(
            """
            INSERT INTO users(first_name, last_name, username, password)
            VALUES (?, ?, ?, ?)
            """, (fname, lname, username, hashed_pw)
        )
        conn.commit()
    except Exception as e:
        print(f"Error has been happend during registration: {e}")
    finally:
        if conn:
            conn.close()