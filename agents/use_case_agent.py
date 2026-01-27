from crewai import Agent

def use_case_agent():
    return Agent(
        role="Use Case Designer",
        goal="Generate realistic and edge-case test scenarios for code",
        backstory="A QA expert who designs test cases to break and validate systems.",
        verbose=True
    )
