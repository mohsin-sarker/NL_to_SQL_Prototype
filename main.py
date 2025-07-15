# Main.py is the entry point of Prototype Applicaton NL2SQL
import streamlit as st


st.title('Natural Language to SQL Analytics')


# ---------- ADD SIDEBAR INFO ----------
st.sidebar.title("🧭 Prototype Info")
st.sidebar.markdown("""
**Welcome!**

- This is a research prototype for translating **natural language into SQL**.
- Please **register first** if you don't have an account.
- After logging in, you can:
    - Generate SQL queries.
    - Save and run queries.
    - Provide feedback.

🟢 **Your data is used for academic analysis only.**
""")

# ------------ Declare Session State --------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ''

if 'show_register' not in st.session_state:
    st.session_state.show_register = False
    
# ----------- Show Register Tab -------------
if st.session_state.show_register:
    register_tab, = st.tabs(['📝 Register Here!'])
    with register_tab:
        st.title('Register')
        username = st.text_input("New Username", key="reg_user")
        password = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register"):
            # Need backend function code to store user registration into database
            # If users are successfully registered
            st.success('You have been successfully registered! Please Login')
            st.session_state.show_register = False
            
        if st.button('Back to Login'):
            st.session_state.show_register = False


# ----------- Show Login Tab ---------------
elif not st.session_state.logged_in:
    login_tab, = st.tabs(['🔑 Login'])
    with login_tab:
        st.title('Login')
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button('Login'):
            st.session_state.logged_in = True
        if st.button('New Register'):
            st.session_state.show_register = True