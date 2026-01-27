from crewai import Task

def generate_use_cases_task(agent):
    return Task(
        description="""
Generate test scenarios for the corrected code.
Include:
- Normal cases
- Edge cases
- Failure cases
""",
        expected_output="A structured list of test cases.",
        agent=agent
    )
