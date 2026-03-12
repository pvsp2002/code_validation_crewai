from crewai import Agent
from llm_config import get_llm

def error_handler_agent():
    return Agent(
        role="Error Fixer",
        goal="Identify and fix bugs or runtime errors in generated code",
        backstory="A debugging specialist skilled at analyzing stack traces and fixing issues quickly.",
        llm=get_llm(),
        verbose=True
    )