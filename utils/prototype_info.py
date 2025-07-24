import streamlit as st


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
 