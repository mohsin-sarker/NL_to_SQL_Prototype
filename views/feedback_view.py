import streamlit as st
from backend.save_feedback import save_feedback_to_db

def feedback_view(username):
    st.subheader("🧠 NL2SQL Prototype – User Feedback Form")

    with st.form("feedback_form"):
        # User Background
        st.subheader("👤 User Background")
        role = st.text_input("What is your job title or role?")
        sql_db_experience = st.slider(
            "What is your experience with SQL and database usage? (0 = none, 10 = expert & daily use)",
            0, 10, 0
        )
        ai_tools_used = st.radio("Have you used natural language AI tools before (e.g., ChatGPT)?", ["Yes", "No"])

        # Usability
        st.subheader("🧩 Usability")
        ease_of_use = st.slider("How easy was it to use the system?", 0, 10, 0)
        response_time = st.slider("Was the system's response time acceptable?", 0, 10, 0)
        layout_intuitiveness = st.slider("Is the layout intuitive and easy to navigate?", 0, 10, 0)

        # Natural Language Querying
        st.subheader("💬 Natural Language Querying")
        query_expression = st.slider("Was it easy to express your query in natural language?", 0, 10, 0)
        intent_understanding = st.slider("Did the system understand your intent accurately?", 0, 10, 0)
        sql_match_intent = st.slider("Did the generated SQL match your intended question?", 0, 10, 0)
        sql_output_used = st.radio("Did you examine or use the SQL output provided?", ["Yes", "No"])

        # Accuracy of Results
        st.subheader("📊 Accuracy of Results")
        result_accuracy = st.slider("Were the results accurate and relevant?", 0, 10, 0)
        sql_readability = st.slider("Was the SQL readable and understandable to you?", 0, 10, 0)
        error_description = st.text_area("If results were incorrect, what went wrong?")

        # Learning & Insights
        st.subheader("📘 Learning & Insights")
        learning_help = st.slider("Did the SQL output help you learn or validate your understanding?", 0, 10, 0)
        insight_discovery = st.slider("Did the tool help you discover insights from the data?", 0, 10, 0)

        # Algorithm Performance
        st.subheader("⚙️ Algorithm Performance")
        algorithm_efficiency = st.slider("How efficient was the SQL generation process?", 0, 10, 0)
        alt_algorithms = st.radio("Would you like to see alternative NLP-to-SQL algorithms?", ["Yes", "No", "Maybe"])
        alt_algorithm_suggestions = st.text_area("If yes, which algorithms or approaches would you suggest?")

        # Analytics Capabilities
        st.subheader("📈 Analytics Capabilities")
        analytics_support = st.slider("How well did the system support analytics (e.g., filtering, grouping, summarizing)?", 0, 10, 0)
        analytics_usefulness = st.slider("Were the analytical outputs useful for decision-making?", 0, 10, 0)
        viz_quality = st.slider("Did the system provide meaningful visualizations or summaries?", 0, 10, 0)
        analytics_improvements = st.text_area("What analytics features would you like to see improved or added?")

        # Overall Experience
        st.subheader("🌟 Overall Experience")
        enjoyment = st.slider("Did you enjoy using the tool?", 0, 10, 0)
        reuse_intent = st.radio("Would you use this tool again in the future?", ["Yes", "No", "Maybe"])
        recommend_score = st.slider("Would you recommend this tool to others?", 0, 10, 0)

        # AI System Experience
        st.subheader("🤖 AI System Experience")
        aware_ai = st.radio("Were you aware that the system is powered by AI?", ["Yes", "No"])
        aware_ai_inaccuracy = st.slider("Were you aware that AI can sometimes generate incorrect results?", 0, 10, 0)
        ai_confidence = st.slider("How confident were you in the AI’s understanding of your query?", 0, 10, 0)
        trust_suggestions = st.text_area("What would increase your trust in AI-generated SQL or results?")

        # Final Thoughts
        st.subheader("💡 Final Thoughts")
        other_comments = st.text_area("Any other comments or suggestions?")

        submitted = st.form_submit_button("Submit Feedback")

        feedback_data = {
            "username": username,
            "role": role,
            "sql_db_experience": sql_db_experience,
            "ai_tools_used": ai_tools_used,
            "ease_of_use": ease_of_use,
            "response_time": response_time,
            "layout_intuitiveness": layout_intuitiveness,
            "query_expression": query_expression,
            "intent_understanding": intent_understanding,
            "sql_match_intent": sql_match_intent,
            "sql_output_used": sql_output_used,
            "result_accuracy": result_accuracy,
            "sql_readability": sql_readability,
            "error_description": error_description,
            "learning_help": learning_help,
            "insight_discovery": insight_discovery,
            "algorithm_efficiency": algorithm_efficiency,
            "alt_algorithms": alt_algorithms,
            "alt_algorithm_suggestions": alt_algorithm_suggestions,
            "analytics_support": analytics_support,
            "analytics_usefulness": analytics_usefulness,
            "viz_quality": viz_quality,
            "analytics_improvements": analytics_improvements,
            "enjoyment": enjoyment,
            "reuse_intent": reuse_intent,
            "recommend_score": recommend_score,
            "aware_ai": aware_ai,
            "aware_ai_inaccuracy": aware_ai_inaccuracy,
            "ai_confidence": ai_confidence,
            "trust_suggestions": trust_suggestions,
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

feedback_view('Mohsin')