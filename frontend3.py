import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

import streamlit as st
from dotenv import load_dotenv
from crew import create_crew

load_dotenv()

st.set_page_config(
    page_title="CrewAI Code Validator",
    layout="wide"
)

st.title("🧠 CrewAI – Code Validation System")

user_input = st.text_area(
    "Python Requirement",
    height=150,
    placeholder="Example: Write a Python program to compute factorial of a number"
)

if st.button("Run Validation 🚀"):
    if not user_input.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Running backend validation pipeline..."):
            crew = create_crew(user_input)
            result = crew.kickoff()

        st.success("Validation Completed")

        # -------------------------
        # Extract task outputs
        # -------------------------
        dev_output = result.tasks_output[0].raw
        corrected_output = result.tasks_output[1].raw
        test_cases = result.tasks_output[2].raw
        test_results = result.tasks_output[3].raw
        final_score = result.raw

        # -------------------------
        # UI Rendering
        # -------------------------

        st.subheader("🧑‍💻 Generated Code")
        st.code(dev_output, language="python")

        st.subheader("✏️ Corrections & Updated Code")
        st.markdown(corrected_output)

        st.subheader("🧪 Test Cases")
        st.markdown(test_cases)

        st.subheader("🧾 Test Execution Results")
        st.markdown(test_results)

        st.subheader("📊 Final Validation Score")
        st.markdown(final_score)
