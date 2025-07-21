import streamlit as st
import pandas as pd
from utils.connection import get_db_connection
from utils.helper import (
                    get_sidebar,
                    handle_generated_sql,
                    initialize_session_state
                )


# Create a function for user Deshboard if Logged in
def show_deshboard():
    #Initialize Session State
    initialize_session_state()
    
    # Clear user input if clear_triggered
    if st.session_state.clear_triggered:
        st.session_state.user_query = ''
        st.session_state.clear_triggered = False  
         
    #Placeholder for NL2SQL in Main Interface
    handle_generated_sql()
    
    #  Add Sidebar Information
    get_sidebar()

    # Execute Query
    if st.session_state.query_triggered:
        st.session_state.query_triggered = False
        execute_query()
 

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