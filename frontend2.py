import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

import io
import sys
from contextlib import redirect_stdout

import streamlit as st
from dotenv import load_dotenv
from crew import create_crew

load_dotenv()

st.set_page_config(
    page_title="CrewAI Code Validator",
    layout="wide"
)

st.title("🧠 CrewAI – Python Code Validation System")

st.markdown(
    """
    Enter a Python requirement below.
    The system will:
    - Generate code
    - Fix errors
    - Create test cases
    - Execute tests
    - Review and validate the result
    """
)

user_input = st.text_area(
    "Python Requirement",
    height=180,
    placeholder="Example: Write a Python function to compute factorial of a number"
)

if st.button("Run Validation 🚀"):
    if not user_input.strip():
        st.warning("Please enter a requirement.")
    else:
        output_buffer = io.StringIO()

        with st.spinner("Running CrewAI agents..."):
            with redirect_stdout(output_buffer):
                crew = create_crew(user_input)
                result = crew.kickoff()

        terminal_output = output_buffer.getvalue()

        st.success("Validation Completed!")

        # Terminal-like output
        with st.expander("🖥️ Full Crew Execution Log", expanded=True):
            st.code(terminal_output, language="text")

        st.divider()

        # Clean final output
        st.subheader("✅ Final Validation Report")
        st.markdown(result.raw)
