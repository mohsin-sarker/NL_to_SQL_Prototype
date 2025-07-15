# This is the main content page for Prototype Applicaton NL2SQL
import streamlit as st

# --------------- Add Home Button ---------------
# Create a Home button at the top for refresh and go back to default page.
cols = st.columns([1, 8])
with cols[0]:
    if st.button('🏠 Home'):
        # Reset to default state
        st.session_state.logged_in = False
        st.session_state.show_register = False
        st.session_state.username = ''

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


# ---------- ADD SIDEBAR INFO ----------
st.sidebar.title('🧭 Prototype Info')
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
        first_name = st.text_input('Enter Your First Name:', key='firt_name')
        last_name = st.text_input('Enter Your Last Name:', key='last_name')
        username = st.text_input('New Username:', key='reg_user')
        password = st.text_input('New Password:', type='password', key='reg_pass')
        if st.button('Register'):
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
        username = st.text_input('Username', key='login_user')
        password = st.text_input('Password', type='password', key='login_pass')
        if st.button('Login'):
            st.session_state.logged_in = True
        if st.button('New Register'):
            st.session_state.show_register = True