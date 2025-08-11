from psycopg2 import sql
from utils.connection import get_database_connection

def save_feedback_to_db(feedback_data):
    """
    This function is to store users feedback for further analysis.
    Connect to the PostgreSQL DB.
    Create user_feedback table if not exists.
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
                submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                role TEXT,
                sql_db_experience INTEGER,
                ai_tools_used TEXT,
                ease_of_use INTEGER,
                response_time INTEGER,
                layout_intuitiveness INTEGER,
                query_expression INTEGER,
                intent_understanding INTEGER,
                sql_match_intent INTEGER,
                sql_output_used TEXT,
                result_accuracy INTEGER,
                sql_readability INTEGER,
                error_description TEXT,
                learning_help INTEGER,
                insight_discovery INTEGER,
                algorithm_efficiency INTEGER,
                alt_algorithms TEXT,
                alt_algorithm_suggestions TEXT,
                analytics_support INTEGER,
                analytics_usefulness INTEGER,
                viz_quality INTEGER,
                analytics_improvements TEXT,
                enjoyment INTEGER,
                reuse_intent TEXT,
                recommend_score INTEGER,
                aware_ai TEXT,
                aware_ai_inaccuracy INTEGER,
                ai_confidence INTEGER,
                trust_suggestions TEXT,
                other_comments TEXT
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