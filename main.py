# This is the main entrance for Prototype Applicaton: NL2SQL
import streamlit as st
from views.login_view import show_login
from views.register_view import show_register
from views.deshboard_view import show_deshboard
from utils.reset_sesssion import reset_session
from utils.prototype_info import prototype_info


# --------------- Add Home Button ---------------
# Create a Home button at the top for refresh and go back to default page.
nav, main = st.columns([1, 8])
with nav:
    if st.button('🏠 Home'):
        # Reset to default state
        reset_session()

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
    show_deshboard()
# ----------- Show Register/Login Tab -------------
else:
    prototype_info()
    if st.session_state.show_register:
        show_register()
    else:
        show_login()