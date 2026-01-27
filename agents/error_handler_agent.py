from crewai import Agent

def error_handler_agent():
    return Agent(
        role="Error Handler",
        goal="Detect and fix errors or logical issues in code to ensure the code is in less time complexity",
        backstory="A senior engineer skilled at debugging and improving code reliability who can ensure that the code is in less time complexity",
        verbose=True
    )
