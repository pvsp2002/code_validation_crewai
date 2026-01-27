from crewai import Task

def error_fix_task(agent):
    return Task(
        description="""
Review the provided code.
Identify and fix:
- Syntax errors
- Logical errors
- Bad practices

Return the corrected version of the code.
""",
        expected_output="Corrected and improved code.",
        agent=agent
    )
