from utils.connection import get_db_connection


# Create a funcaiton that returns users schema tables and colums.
def get_db_schema(db_name: str) -> str:
    """
    Reads tables and columns from SQLite database and builds a schema string.
    """
    conn = get_db_connection(db_name)
    cursor = conn.cursor()
    
    table_schema = ["Tables:"]
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()
    
    for table_tuple in tables:
        table_name = table_tuple[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        column_info = cursor.fetchall()
        columns = [col[1] for col in column_info]
        table_schema.append(f"- {table_name} ({', '.join(columns)})")
    conn.close()
    return "\n".join(table_schema)
