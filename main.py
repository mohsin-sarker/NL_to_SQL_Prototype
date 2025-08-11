import streamlit as st 
from views.login_view import show_login_view
from views.register_view import show_register_view
from views.deshboard_view import show_deshboard
from utils.helper import update_session_state, get_home_button
from utils.prototype_info import prototype_info
from utils.schema_tables import get_db_schema
from views.pages import (
                        show_consent_page,
                        show_questionnaire_page,
                        show_thankyou_page
                    )

# -------------- Updates Session State ---------
# Update session state for logged_in user, pages and regitration view
update_session_state()

# --------------- Add Home Button ---------------
# Create a Home button at the top for refresh and go back to default page.
get_home_button()


# Add markdown for Home button to keep it at the top.
st.markdown("""
    <style>
        .block-container {
            padding-top: 3rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)


# -------------- Add Home Page Title -------------
st.title('Natural Language to SQL Analytics')

# ---------- Routing Content --------------------- 
if st.session_state.logged_in:
    if st.session_state.page == 'dashboard':
        st.info("💬 *If Database is connected - Expend to View Schema Tables and Columns:*")
        with st.expander("📘 View Company's Available Tables and Columns"):
            st.code(get_db_schema('company.db'), language='sql')
        show_deshboard()
        
    elif st.session_state.page == 'consent':
        show_consent_page()
    
    elif st.session_state.page == 'questionnaire':
        show_questionnaire_page()
        
    elif st.session_state.page == 'thankyou':
        show_thankyou_page()
    
# ----------- Show Register/Login Tab -------------
else:
    prototype_info()
    if st.session_state.show_register:
        show_register_view()
    else:
        show_login_view()