from crewai import Agent

def developer_agent():
    return Agent(
        role="Developer",
        goal="Develop correct and efficient code of any language based on user requirements",
        backstory="An experienced any-language developer who writes clean, readable, and maintainable code.",
        verbose=True
    )
