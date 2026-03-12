from crewai import Task

def error_fix_task(agent):

    return Task(
        description="""
        Review the previously generated code.

        Identify:
        - syntax errors
        - runtime errors
        - logical bugs

        Fix the code and provide the corrected version.
        """,

        expected_output="""
        A corrected version of the Python code with all bugs fixed.
        Include explanations for the fixes.
        """,

        agent=agent
    )