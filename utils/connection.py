import sqlite3
import os
import psycopg2
import streamlit as st


# # Get the current directory of this script and initialize the database path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Create and return a connection to SQLite database.
def get_db_connection(db_name="users.db"):
    try:
        db_path = os.path.join(base_dir, "database", db_name)
        conn = sqlite3.connect(db_path, check_same_thread=False)
        return conn
    except sqlite3.Error as e:
        print(f"An Error has been happend to connect to the database!: {e}")
        return None


# Get Connection to PostgreSQL database for users and user_feedback
def get_database_connection():
    """Establishes a connection to the AWS RDS database."""
    try:
        conn = psycopg2.connect(
            host=st.secrets["DB_HOST"],
            port=st.secrets["DB_PORT"],
            dbname=st.secrets["DB_NAME"],
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"]
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
