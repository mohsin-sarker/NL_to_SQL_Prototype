from psycopg2 import sql
from utils.connection import get_database_connection

def save_feedback_to_db(feedback_data):
    """
    This function is to store users feedback for further analysis.
    Connect to your PostgreSQL DB.
    Create table if not exists.
    Prepare the INSERT query dynamically.
    """
    
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        
        # Create user_feedback table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_feedback (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE,
                role TEXT,
                sql_experience TEXT,
                db_usage TEXT,
                ai_familiarity TEXT,
                ui_ease INTEGER,
                system_response_time INTEGER,
                layout_friendliness INTEGER,
                nl_query_ease INTEGER,
                nl_understood INTEGER,
                sql_match_intent INTEGER,
                used_sql_output TEXT,
                output_accuracy INTEGER,
                sql_understandability INTEGER,
                query_failures TEXT,
                learn_from_sql INTEGER,
                insights_gained INTEGER,
                enjoyment INTEGER,
                reuse TEXT,
                recommendation INTEGER,
                aware_of_ai TEXT,
                ai_limitations INTEGER,
                ai_confidence INTEGER,
                trust_feedback TEXT,
                feature_requests TEXT,
                other_comments TEXT,
                submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        
        # Prepare the insert query dynamically
        columns = feedback_data.keys()
        values = [feedback_data[col] for col in columns]
        
        # Insert into user_feedback table
        insert_data = sql.SQL("INSERT INTO user_feedback ({}) VALUES ({})").format(
            sql.SQL(',').join(map(sql.Identifier, columns)),
            sql.SQL(',').join(sql.Placeholder() * len(columns))
        )
        cursor.execute(insert_data, values)
        conn.commit()
        conn.close()
        return True
        
    except Exception as e:
        print(f'DB error: {e}')
        return False