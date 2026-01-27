from crewai import Agent

def reviewer_agent():
    return Agent(
        role="Code Reviewer",
        goal="Review test results and provide a validation score in percentage",
        backstory="A lead reviewer responsible for final quality approval.",
        verbose=True
    )
