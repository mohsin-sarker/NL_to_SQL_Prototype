from utils.connection import get_database_connection
from utils.hashing import hash_password, verify_password
import streamlit as st


# Create function to register users.
def register(fname, lname, username, password):
    # Get db connection client
    conn = get_database_connection()
    if conn is None:
        print("❌ No DB connection.")
        st.info("❌ No DB connection.")
        return None
    cursor = conn.cursor()
    
    try:
        # Create a hashed password
        hashed_pw = hash_password(password)
        cursor.execute(
            """
            INSERT INTO users(first_name, last_name, username, password_hash)
            VALUES (%s, %s, %s, %s)
            """, (fname, lname, username, hashed_pw))
        
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Error has been happend during registration: {e}")
        return False
    
    finally:
        if conn:
            conn.close()
        


# Create function to authenticate users to login
def login(username, password):
    # Get db connection client
    conn = get_database_connection()
    if conn is None:
        print("❌ No DB connection.")
        st.info("❌ No DB connection.")
        return None
    cursor = conn.cursor()
    
    try:
        sql = "SELECT first_name, password_hash FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        if user:
            first_name, hashed_pw = user
            if verify_password(password, hashed_pw):
                return first_name
    
    except Exception as e:
        print(f"Ops! there is a login error: {e}")

    finally:
        if conn:
            conn.close()
    


# # If user is registered and logged in, get user details.
# def show_user_details():
#     """
#     Fetches and displays the details for a single, specified user.
#     """
#     try:
#         user = supabase_client.auth.get_user().user
#         if user:
#             return {
#                 "user_ID": user.id,
#                 "email": user.email,
#                 "first_name": user.user_metadata.get("first_name"),
#                 "last_name": user.user_metadata.get("last_name"),
#                 "created_at": user.created_at
#             }
#         else:
#             print("No user is currently logged in.")
#             return None
        
#     except Exception as e:
#         print(f"An error occurred while fetching user details: {e}")
#         return None
        