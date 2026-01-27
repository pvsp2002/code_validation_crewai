from crewai import Task

def develop_code_task(agent, user_input):
    return Task(
        description=f"""
Write a code based on the following user requirement:

{user_input}

The code should be functional, readable, and well-structured.
""",
        expected_output="A complete code solution.",
        agent=agent
    )
