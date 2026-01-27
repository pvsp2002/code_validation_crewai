import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from crew import create_crew


st.set_page_config(
    page_title="CrewAI Code Validator",
    layout="wide"
)

st.title("🧠 CrewAI – Python Code Validation System")

st.markdown(
    """
    Enter your Python requirement below.
    The system will:
    1. Generate code
    2. Fix errors
    3. Create test cases
    4. Test them
    5. Review and validate the result
    """
)

user_input = st.text_area(
    "Python Requirement",
    height=200,
    placeholder="Example: Write a Python function to check if a number is prime"
)

if st.button("Run Validation 🚀"):
    if not user_input.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Running CrewAI agents..."):
            crew = create_crew(user_input)
            result = crew.kickoff()

        st.success("Validation Completed!")

        st.subheader("📄 Final Output")
        st.write(result)
