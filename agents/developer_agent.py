from crewai import Agent
from llm_config import get_llm

def developer_agent():
    return Agent(
        role="Developer",
        goal="Develop correct and efficient code based on user requirements",
        backstory="An experienced developer who writes clean, readable, and optimized code.",
        llm=get_llm(),
        verbose=True
    )