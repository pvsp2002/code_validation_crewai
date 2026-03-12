import streamlit as st
import time
from crew import create_crew

# Page configuration
st.set_page_config(
    page_title="CrewAI Code Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 CrewAI Multi-Agent Code Generator")
st.write("Enter a coding requirement and let the AI crew generate, test, and review the code.")

# Sidebar
st.sidebar.header("Settings")
show_time = st.sidebar.checkbox("Show Execution Time", value=True)

# User Input
user_input = st.text_area(
    "Enter your coding requirement:",
    placeholder="Example: Write a Python function to check if a number is prime.",
    height=150
)

run_button = st.button("🚀 Run CrewAI")

if run_button:

    if not user_input.strip():
        st.warning("Please enter a requirement.")
        st.stop()

    st.info("Running AI Crew...")

    start_time = time.time()

    try:
        crew = create_crew(user_input)

        with st.spinner("Agents are working..."):
            result = crew.kickoff()

        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        st.success("Crew execution completed!")

        st.subheader("📄 Final Output")
        st.code(result, language="python")

        if show_time:
            st.sidebar.success(f"Execution Time: {total_time} seconds")

    except Exception as e:
        st.error("Error occurred during execution.")
        st.exception(e)