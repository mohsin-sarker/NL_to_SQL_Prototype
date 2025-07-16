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
        return True
    except Exception as e:
        print(f"Error has been happend during registration: {e}")
        return False
    finally:
        if conn:
            conn.close()
            

# Create funcation to let user login
def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result:
            hashed_pw = result[0]
            if verify_password(password, hashed_pw):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"Error has been happend during varify user: {e}")
        return False
    finally:
        if conn:
            conn.close()
            

# If users are registered, show all users
def show_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        conn.close()