import streamlit as st
from backend.auth import login_user

# Create function to show a login view for user to be logged-in
def show_login():
    login_tab, = st.tabs(['🔑 Login'])
    
    with login_tab:
        st.title('Login')
        username = st.text_input('Username', key='login_user')
        password = st.text_input('Password', type='password', key='login_pass')
        
        if st.button('Login'):
            user_first_name = login_user(username, password)
            if user_first_name:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f'Welcome {user_first_name}')
                st.rerun()
            else:
                st.error("❌ Invalid credentials.")
                
        if st.button('New Register'):
            st.session_state.show_register = True
            st.rerun()