from crewai import Agent
from llm_config import get_llm

def use_case_agent():
    return Agent(
        role="Use Case Generator",
        goal="Generate realistic test cases for validating generated code",
        backstory="Quality analyst who creates edge-case scenarios.",
        llm=get_llm(),
        verbose=True
    )