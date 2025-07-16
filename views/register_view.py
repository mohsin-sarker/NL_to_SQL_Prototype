import streamlit as st
from backend.auth import register_user
import time 


# Create a function to let unregisterd user to register
def show_register():
    register_tab, = st.tabs(['📝 Register Here!'])
    
    with register_tab:
        st.title('Register')
        first_name = st.text_input('Enter Your First Name:', key='first_name')
        last_name = st.text_input('Enter Your Last Name:', key='last_name')
        username = st.text_input('New Username:', key='reg_user')
        password = st.text_input('New Password:', type='password', key='reg_pass')
        
        if st.button('Register'):
            if register_user(first_name, last_name, username, password):
                st.success('You have been successfully registered! Please Login')
                time.sleep(3)
                st.session_state.show_register = False
                st.session_state.reg_success = False
                st.rerun()      
            else:
                st.error('⚠️ Username already exists.')
            
        if st.button('Back to Login'):
            st.session_state.show_register = False
            st.rerun()
        