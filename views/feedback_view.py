import streamlit as st
from backend.save_feedback import save_feedback_to_db

def feedback_view(username):
    st.subheader("🧠 NL2SQL Prototype – User Feedback Form")

    with st.form("feedback_form"):
        # SECTION 1: ABOUT YOU
        st.subheader("👤 User Background")
        role = st.text_input("What is your job title or role?")
        sql_experience = st.selectbox("Do you have experience with SQL?", ["None", "Beginner", "Intermediate", "Expert"])
        db_usage = st.selectbox("How often do you work with databases?", ["Never", "Occasionally", "Frequently", "Daily"])
        ai_familiarity = st.radio("Have you used natural language AI tools before (e.g., ChatGPT)?", ["Yes", "No"])

        # SECTION 2: SYSTEM USABILITY
        st.subheader("🧩 Usability")
        ui_ease = st.slider("How easy was it to use the system?", 1, 5)
        system_response_time = st.slider("Was the system's response time acceptable?", 1, 5)
        layout_friendliness = st.slider("Is the layout intuitive and easy to navigate?", 1, 5)

        # SECTION 3: QUERYING WITH NATURAL LANGUAGE
        st.subheader("💬 Natural Language Querying")
        nl_query_ease = st.slider("Was it easy to express your query in natural language?", 1, 5)
        nl_understood = st.slider("Did the system understand your intent?", 1, 5)
        sql_match_intent = st.slider("Did the generated SQL match your intended question?", 1, 5)
        used_sql_output = st.radio("Did you examine or use the SQL output provided?", ["Yes", "No"])

        # SECTION 4: ACCURACY & RESULTS
        st.subheader("📊 Accuracy of Results")
        output_accuracy = st.slider("Were the results accurate and relevant?", 1, 5)
        sql_understandability = st.slider("Was the SQL readable and understandable to you?", 1, 5)
        query_failures = st.text_area("If results were incorrect, what went wrong?")

        # SECTION 5: LEARNING & INSIGHTS
        st.subheader("📘 Learning & Insights")
        learn_from_sql = st.slider("Did the SQL output help you learn or validate your understanding?", 1, 5)
        insights_gained = st.slider("Did the tool help you discover insights from the data?", 1, 5)

        # SECTION 6: OVERALL EXPERIENCE
        st.subheader("🌟 Overall Experience")
        enjoyment = st.slider("Did you enjoy using the tool?", 1, 5)
        reuse = st.radio("Would you use this tool again in the future?", ["Yes", "No", "Maybe"])
        recommendation = st.slider("Would you recommend this tool to others?", 1, 5)

        # SECTION 7: AI SYSTEM EXPERIENCE
        st.subheader("🤖 AI System Experience")
        aware_of_ai = st.radio("Were you aware that the system is powered by AI?", ["Yes", "No"])
        ai_limitations = st.slider("Were you aware that AI can sometimes generate incorrect results?", 1, 5)
        ai_confidence = st.slider("How confident were you in the AI’s understanding of your query?", 1, 5)
        trust_feedback = st.text_area("What would increase your trust in AI-generated SQL or results?")

        # SECTION 8: FINAL COMMENTS
        st.subheader("💡 Final Thoughts")
        feature_requests = st.text_area("What features would you like to see added?")
        other_comments = st.text_area("Any other comments or suggestions?")

        submitted = st.form_submit_button("Submit Feedback")

        feedback_data = {
            "username": username,
            "role": role,
            "sql_experience": sql_experience,
            "db_usage": db_usage,
            "ai_familiarity": ai_familiarity,
            "ui_ease": ui_ease,
            "system_response_time": system_response_time,
            "layout_friendliness": layout_friendliness,
            "nl_query_ease": nl_query_ease,
            "nl_understood": nl_understood,
            "sql_match_intent": sql_match_intent,
            "used_sql_output": used_sql_output,
            "output_accuracy": output_accuracy,
            "sql_understandability": sql_understandability,
            "query_failures": query_failures,
            "learn_from_sql": learn_from_sql,
            "insights_gained": insights_gained,
            "enjoyment": enjoyment,
            "reuse": reuse,
            "recommendation": recommendation,
            "aware_of_ai": aware_of_ai,
            "ai_limitations": ai_limitations,
            "ai_confidence": ai_confidence,
            "trust_feedback": trust_feedback,
            "feature_requests": feature_requests,
            "other_comments": other_comments
        }

        if submitted:
            success = save_feedback_to_db(feedback_data)
            if success:
                st.success("✅ Thank you! Your feedback has been submitted.")
                return True
            else:
                st.error("❌ Something went wrong or you may have already submitted. Please try again later.")
                return False
