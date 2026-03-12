from crewai import Task

def testing_task(agent):

    return Task(
        description="""
        Use the generated test cases to validate the corrected code.

        Ensure:
        - logic correctness
        - edge cases handled
        - no runtime errors
        """,

        expected_output="""
        Testing report including:
        - passed test cases
        - failed test cases
        - recommended fixes if needed
        """,

        agent=agent
    )