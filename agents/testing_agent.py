from crewai import Agent
from llm_config import get_llm

def testing_agent():
    return Agent(
        role="Tester",
        goal="Run tests and validate correctness of the generated code",
        backstory="Automation testing expert ensuring reliability of software.",
        llm=get_llm(),
        verbose=True
    )