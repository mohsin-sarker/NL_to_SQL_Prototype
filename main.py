# This is the main entrance for Prototype Applicaton: NL2SQL
import streamlit as st
from views.login_view import show_login
from views.register_view import show_register
from views.deshboard_view import show_deshboard
from utils.helper import reset_session
from utils.prototype_info import prototype_info
from utils.schema_tables import get_db_schema


# --------------- Add Home Button ---------------
# Create a Home button at the top for refresh and go back to default page.
nav, main = st.columns([1, 8])
with nav:
    if st.button('🏠 Home'):
        if not st.session_state.logged_in:
            # Reset to default state
            reset_session()
        else:
            st.session_state.logged_in = True

# Add markdown for Home button to keep it at the top.
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)


# -------------- Add Home Page Title -------------
st.title('Natural Language to SQL Analytics')


# ------------ Declare Session State --------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ''

if 'show_register' not in st.session_state:
    st.session_state.show_register = False


# ---------- Routing Content --------------
if st.session_state.logged_in:
    st.info("💬 *If Database is connected - Expend to View Schema Tables and Columns:*")
    with st.expander("📘 View Company's Available Tables and Columns"):
        st.code(get_db_schema('company.db'), language='sql')
    show_deshboard()
    
# ----------- Show Register/Login Tab -------------
else:
    prototype_info()
    if st.session_state.show_register:
        show_register()
    else:
        show_login()