import streamlit as st
from utils.reset_sesssion import reset_session


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
    st.text_input("Your question:")
    if st.button('Generate SQL'):
        pass
    