import streamlit as st
from backend.auth import login
import time

# Create function to show a login view for user to be logged-in if authenticated successful.
def show_login_view():
    login_tab, = st.tabs(['🔑 Login'])
    
    with login_tab:
        st.title('Login')
        username = st.text_input('Username', key='login_user')
        password = st.text_input('Password', type='password', key='login_pass')
        
        if st.button('Login'):
            user_first_name = login(username, password)
            if user_first_name:
                st.session_state.user = user_first_name
                st.session_state.logged_in = True
                st.success(f'Welcome {user_first_name}')
                st.balloons()
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ Login failed: Invalid username or password.")
                
        if st.button('New Register'):
            st.session_state.show_register = True
            st.rerun()