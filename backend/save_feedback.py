from utils.connection import get_db_connection

def save_feedback(data):
    """
    This is function is storing feedback locally. I will update this function later.
    """
    
    conn = get_db_connection('feedback.db')
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                username TEXT,
                question_1 TEXT,
                question_2 INTEGER,
                question_3 TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
    """)    
    cursor.execute('''
        INSERT INTO feedback (username, question_1, question_2, question_3)
        VALUES (?, ?, ?, ?)
    ''', (data["username"], data["question_1"], data["question_2"], data["question_3"]))
    conn.commit()
    conn.close()