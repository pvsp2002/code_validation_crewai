from crewai import Task

def testing_task(agent):
    return Task(
        description="""
Execute the generated test cases against the code.
Document:
- Passed tests
- Failed tests
- Errors encountered
""",
        expected_output="Detailed test execution results.",
        agent=agent
    )
