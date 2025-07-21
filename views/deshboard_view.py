import streamlit as st
import pandas as pd
from utils.reset_sesssion import reset_session
from utils.connection import get_db_connection
from utils.schema_tables import get_db_schema
from backend.nl2sql_feature import nl_to_sql


# Create a function for user Deshboard if Logged in
def show_deshboard():
    # -------- Ensure generated_sql is initialized --------
    if "generated_sql" not in st.session_state:
        st.session_state.generated_sql = None
        
    #  ------------- Add Sidebar Information --------------
    st.sidebar.title("🔍 Explore SQL from Natural Language")
    st.sidebar.markdown(f"👤 **Logged in as:** `{st.session_state.username}`")
    st.sidebar.info("""
    You can:
    - Enter natural language queries
    - View generated SQL
    - Execute queries
    """)
    
    st.sidebar.markdown("-----------------")
          
    # ----------- Placeholder for NL2SQL Interface ----------
    st.markdown("💬 *Enter your natural language query below:*")
    query = st.text_input("Your question:")
    if st.button('Generate SQL'):
        if query.strip() == '':
            st.warning('Please enter your question.')
        else:
            sql = nl_to_sql(query, get_db_schema('company.db'))
            if sql == "Tables or columns not found":
                st.session_state.generated_sql = None
                st.error('⚠️ The requested information is not available in your database schema.')
            elif sql == 'Irrelevant request: Cannot generate SQL for this.':
                st.session_state.generated_sql = None
                st.error('⚠️ Your question is not related to database queries.')
            else:
                st.session_state.generated_sql = sql
                st.success("✅ SQL query generated:")
                st.code(sql, language='sql')

    
    # --------------- Trigger Query or Clear SQL -------------
    # Check any query triggered in the session state
    if 'query_triggered' not in st.session_state:
        st.session_state.query_triggered = False
        
    st.sidebar.subheader("Actions for Generated SQL:")
    query_col, clear_col = st.sidebar.columns(2)
    with query_col:
        if st.session_state.generated_sql:
            if st.button("▶️RUN QUERY?"):
                st.session_state.query_triggered = True
        else:
            st.caption("⚠️ Generate a SQL query first.")
    
    with clear_col:
        if st.button("❌ Clear SQL"):
            st.session_state.generated_sql = None

    if st.session_state.query_triggered:
        st.session_state.query_triggered = False
        execute_query()
    
    st.sidebar.markdown("-----------------") 
    # -------------- Logout & Feedback Option ----------
    Logout, Feedback = st.sidebar.columns(2)
    
    with Logout:
        if st.button('Logout'):
            reset_session()
            
    with Feedback:
        if st.button('Feedback'):
            st.info('I will provide feedback later!')
        


# --------------- Create Function to Query SQL -----------
def execute_query():
    sql = st.session_state['generated_sql']
    conn = get_db_connection('company.db')
    if conn:
        try:
            df = pd.read_sql_query(sql, conn)
            conn.close()
            
            if df.empty:
                st.info("SQL has been run successfully but no rows were returned!")
            else:
                st.subheader("📊 Query Result:")
                st.dataframe(df)
                visualize_query_result(df)
        except Exception as e:
            st.error(f"An error has been occured to run the query !!!: {e}")
    else:
        st.error("Could not connect to the database!!!")



# -------------- Visualize Query Result -----------------
def visualize_query_result(df):
    st.markdown("### 📈 Visualization")
    
    if df.empty:
        st.info("No data to visualize.")
        return

    if len(df.columns) >= 2:
        # Identify numeric and categorical columns
        num_cols = df.select_dtypes(include=['int', 'float']).columns
        if len(num_cols) >= 1:
            label_col = df.columns[0]
            value_col = num_cols[0]
            try:
                st.bar_chart(df[[label_col, value_col]].set_index(label_col))
            except Exception as e:
                st.warning(f"Couldn't generate chart: {e}")
        else:
            st.info("No numeric data available for charting.")
    else:
        st.info("Not enough data to generate a chart.")