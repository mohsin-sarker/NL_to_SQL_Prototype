import streamlit as st
import time
from utils.generate_pdf import upload_consent_form
from views.feedback_view import feedback_view


def show_consent_page():
    st.header("User Consent for Prototype Application")
    for info in participant_info:
        st.subheader(f"{info['title']}")
        st.markdown(f"{info['body']}")
        
    st.subheader("📝 Statement of Consent to be Signed Digitally")
    st.markdown("""
        Thank you for participating in our feedback study.
        By continuing, you agree to let us collect and use your answers for research and product improvement purposes. 
        We will not share your personal data externally.

        Please confirm you consent to proceed.
    """)
    check_box = st.checkbox("By checking in the box means you are giving your consent")
    if check_box:
        if st.button("Agree and Continue"):
            success = upload_consent_form()
            if success:
                st.success("Thank you for your consent!")
                st.balloons()
                time.sleep(3)
                st.session_state.page = "questionnaire"
                st.rerun()
                
            else:
                st.error("A problem occurred while saving your consent. Please ensure you are logged in and try again.")
                
    else:
        st.info("Please check the box to agree and continue!")
    
    if st.button("Go Back"):
        st.session_state.page = "dashboard"
        st.rerun()


participant_info = [
    {
        "title": "Introduction and Purpose",
        "body": "I am participating in a research study to evaluate a new prototype application. I understand that my feedback will be used for academic analysis to improve the application's design and usability."
    },
    {
        "title": "Procedures and Confidentiality",
        "body": "I understand that I will interact with the application and that my responses and usage patterns will be collected. All data will be anonymized to protect my privacy and will be stored securely."
    },
    {
        "title": "Voluntary Participation",
        "body": "My participation is voluntary. I understand that I can withdraw from the study at any time, for any reason, without penalty."
    },
]




def show_questionnaire_page():
    username = st.session_state.user
    if feedback_view(username):
        st.success("Thank you for your feedback!")
        st.balloons()
        time.sleep(3)
        st.session_state.page = 'thankyou'
        st.rerun()
        
        



def show_thankyou_page():
    st.subheader("🎉 Thank You!")
    st.markdown("We appreciate your time. Your feedback helps us improve the app.")

    if st.button("⬅️ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()