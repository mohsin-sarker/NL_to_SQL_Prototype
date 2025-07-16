import streamlit as st
from backend.auth import show_users


def prototype_info():
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


    # --------- For Showing All Users (Debuggin purpose) -------------
    if st.sidebar.button("Show All Registered Users (Debug)"):
        users = show_users()
        st.sidebar.write("### Registered Users")
        for user in users:
            st.sidebar.write(f"ID: {user[0]}, Name: {user[1]} {user[2]}, Username: {user[3]}")