from crewai import Task

def review_task(agent):
    return Task(
        description="""
Review the test execution results.
Provide:
- Validation score (0–100%)
- Key issues found
- Final approval decision
""",
        expected_output="""
A review report including:
- Validation score (%)
- Issues summary
- Approved or Not Approved
""",
        agent=agent
    )
