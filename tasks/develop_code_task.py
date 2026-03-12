from crewai import Task

def develop_code_task(agent, user_input):

    return Task(
        description=f"""
        Write Python code based on the following requirement:

        {user_input}

        The code should be clean, modular, and production ready.
        Add comments explaining the logic.
        """,

        expected_output="""
        Complete Python code implementing the requested functionality.
        The output should contain only the code with comments.
        """,

        agent=agent
    )