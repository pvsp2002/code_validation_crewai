from crewai import Agent

def developer_agent():
    return Agent(
        role="Developer",
        goal="Develop correct and efficient code of any language based on user requirements with less time complexity",
        backstory="An experienced any-language developer who writes clean, readable, and maintainable code with less time complexity.",
        verbose=True
    )
