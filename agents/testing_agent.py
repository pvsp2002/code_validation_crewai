from crewai import Agent

def testing_agent():
    return Agent(
        role="Testing Engineer",
        goal="Execute test scenarios and validate code behavior",
        backstory="An automation engineer focused on correctness and coverage.",
        verbose=True
    )
