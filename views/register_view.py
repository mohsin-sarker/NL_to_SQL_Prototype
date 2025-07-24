import streamlit as st
from backend.auth import register
import time 


# Create a function to let unregisterd user to register
def show_register_view():
    register_tab, = st.tabs(['📝 Register Here!'])
    
    with register_tab:
        st.title('Register')
        first_name = st.text_input('Enter Your First Name:', key='first_name')
        last_name = st.text_input('Enter Your Last Name:', key='last_name')
        username = st.text_input('Create a Username:', key='username')
        password = st.text_input('Create a Password:', type='password', key='reg_pass')
        if st.button('Register'):
            if not (first_name and last_name and username and password):
                st.warning("🚫 All fields are required.")
            else:
                user_object = register(first_name, last_name, username, password)
                if user_object:
                    st.success('You have been successfully registered! Please Login')
                    st.balloons()
                    time.sleep(3)
                    st.session_state.show_register = False
                    st.session_state.reg_success = True
                    st.rerun()      
                else:
                    st.error(f'⚠️ Registration failed')
            
        if st.button('Back to Login'):
            st.session_state.show_register = False
            st.rerun()
        