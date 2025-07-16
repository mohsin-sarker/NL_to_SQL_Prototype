import streamlit as st

# Create a function to reset session_state
def reset_session():
    st.session_state.logged_in = False
    st.session_state.username = ''
    st.session_state.show_register = False