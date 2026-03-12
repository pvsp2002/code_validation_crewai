from crewai import Task

def generate_use_cases_task(agent):

    return Task(
        description="""
        Generate comprehensive test cases for the given code.

        Include:
        - normal cases
        - edge cases
        - invalid inputs
        """,

        expected_output="""
        A structured list of test cases with inputs and expected outputs.
        """,

        agent=agent
    )