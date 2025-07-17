import streamlit as st
import pandas as pd
from utils.reset_sesssion import reset_session
from utils.connection import get_db_connection
from backend.nl2sql_feature import nl_to_sql


# Create a function for user Deshboard if Logged in
def show_deshboard():
    #  ------------- Add Sidebar Information ----------
    st.sidebar.title("🔍 Explore SQL from Natural Language")
    st.sidebar.markdown(f"👤 **Logged in as:** `{st.session_state.username}`")
    st.sidebar.info("""
    You can:
    - Enter natural language queries
    - View generated SQL
    - Execute queries
    """)
    Logout, Feedback = st.sidebar.columns(2)
    
    with Logout:
        if st.button('Logout'):
            reset_session()
            
    with Feedback:
        if st.button('Feedback'):
            st.info('I will provide feedback later!')
            
    # ----------- Placeholder for NL2SQL Interface ----------
    st.markdown("💬 *Enter your natural language query below:*")
    query = st.text_input("Your question:")
    if st.button('Generate SQL'):
        if query.strip() == '':
            st.warning('Please enter your question.')
        else:
            sql = nl_to_sql(query, schema_tables)
            if sql == "Tables or columns not found":
                st.error('⚠️ The requested information is not available in your database schema.')
            elif sql == 'Irrelevant request: Cannot generate SQL for this.':
                st.error('⚠️ Your question is not related to database queries.')
            else:
                st.success("✅ SQL query generated:")
                st.code(sql, language='sql')
                st.session_state.generated_sql = sql
    
    # if 'generated_sql' in st.session_state and st.button('Run Query?'):
    #     run_query()


schema_tables = """
    Tables:
        - employees (id, name, address),
        - sales (id, amount, sale_date, employee_id)
        - departments (id, department_name, employee_id)
"""

# Option to run query in database if database exists
def run_query():
    sql = st.session_state['generated_sql']
    conn = get_db_connection()
    if conn:
        try:
            df = pd.read_sql_query(sql, conn)
            conn.close()
            
            if df.empty:
                st.info("SQL has been run successfully but no rows were returned!")
            else:
                st.dataframe(df)
        except Exception as e:
            st.error(f"An error has been occured to run the query !!!: {e}")
    else:
        st.error("Could not connect to the database!!!")