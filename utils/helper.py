import streamlit as st
from backend.nl2sql_feature import nl_to_sql
from utils.schema_tables import get_db_schema


# Create a function to reset session_state
def reset_session():
    st.session_state.logged_in = False
    st.session_state.username = ''
    st.session_state.show_register = False


# Create a function to initialize session_state
def initialize_session_state():
    if 'generated_sql' not in st.session_state:
        st.session_state.generated_sql = None
    if 'user_query' not in st.session_state:
        st.session_state.user_query = ''
    if 'query_triggered' not in st.session_state:
        st.session_state.query_triggered = False
    if 'clear_triggered' not in st.session_state:
        st.session_state.clear_triggered = False


# Create function for sidebar information
def get_sidebar():
    st.sidebar.title("🔍 Explore SQL from Natural Language")
    st.sidebar.markdown(f"👤 **Logged in as:** `{st.session_state.username}`")
    st.sidebar.info("""
    You can:
    - Enter natural language queries
    - View generated SQL
    - Execute queries
    """)
    st.sidebar.markdown("------")
    
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
            st.session_state.user_query = ''
            st.session_state.clear_triggered = False
    
    st.sidebar.markdown("------")
    # Logout & Feedback Option
    Logout, Feedback = st.sidebar.columns(2) 
    with Logout:
        if st.button('Logout'):
            reset_session()
            
    with Feedback:
        if st.button('Feedback'):
            st.info('I will provide feedback later!')
    
    st.sidebar.markdown("------")
    

# Create function to get query input from users
def handle_generated_sql():
    st.markdown("💬 *Enter your natural language query below:*") 
    query = st.text_input("Your question:", value=st.session_state.user_query, key='user_query_input')
    st.session_state.user_query = query
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
                st.session_state.clear_triggered = True 