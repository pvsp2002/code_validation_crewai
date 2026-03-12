from crewai import Agent
from llm_config import get_llm

def reviewer_agent():
    return Agent(
        role="Code Reviewer",
        goal="Review generated code for correctness, readability and performance",
        backstory="Senior software engineer responsible for validating code quality.",
        llm=get_llm(),
        verbose=True
    )