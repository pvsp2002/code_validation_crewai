from crewai import Task

def review_task(agent):

    return Task(
        description="""
        Perform a final code review on the tested code.

        Evaluate:
        - readability
        - best practices
        - performance
        - maintainability
        """,

        expected_output="""
        Final reviewed version of the code with improvement suggestions.
        """,

        agent=agent
    )