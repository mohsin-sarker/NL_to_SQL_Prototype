from datetime import datetime
from fpdf import FPDF
import streamlit as st
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

# Initialize AWS S3 Bucket name and directory
S3_BUCKET_NAME = "participant-consent-forms"

# Initialize an S3 Client
s3_client = boto3.client(
        's3',
        aws_access_key_id=st.secrets["aws"]["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=st.secrets["aws"]["AWS_SECRET_ACCESS_KEY"],
        region_name=st.secrets["aws"]["AWS_DEFAULT_REGION"]
    )

# Generate pdf
def generate_pdf(user):
    """
        Generates a SUMMARY PDF to act as a signed record of consent.
        The full terms are assumed to be displayed on the Streamlit page.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf = FPDF()
    pdf.add_page()
    
    # For the Title
    pdf.set_font("Arial", "B", size=16)
    pdf.cell(0, 10, "Perticipant's Consent Form", ln=True, align="C")
    pdf.ln(20)
    
    # Confirmation Text
    # This text confirms they agreed to the terms shown on the previous page.
    pdf.set_font("Arial", '', size=12)
    pdf.multi_cell(0, 7, (
        "This document confirms that the participant named below has reviewed the full consent information." 
        "Which is presented on the application page to read through and check digitally."
        "Participant has also voluntarily agreed to participate in the research study." 
        "That is under the specified terms."
    ))
    pdf.ln(15)
    
    # Signed Statement of Consent
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(0, 10, "Participant Details", ln=True, align='L')
    pdf.set_font("Arial", 'I', size=12)
    pdf.multi_cell(0, 10, (
        f"""
        Signed by: {user}
        Date: {current_time}
        """
    ))
    return pdf.output(dest="S").encode("latin-1")



# Generates a consent PDF and uploads it to Storage Bucket.
def upload_consent_form():
    try:
        user = st.session_state.user
        pdf_bytes = generate_pdf(user)
        filename = f"{user}_consent.pdf"
        
        # Upload to S3 Bucket
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=filename,
            Body=pdf_bytes,
            ContentType='application/pdf'
        )
        print(f"✅ Successfully uploaded consent form for {user}.")
        return True
    
    except (BotoCoreError, NoCredentialsError) as aws_error:
        st.error(f"❌ AWS Error: {aws_error}")
    except Exception as e:
        st.error(f"❌ Unexpected error uploading file: {e}")
    return False
