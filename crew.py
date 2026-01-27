from crewai import Crew

from agents.developer_agent import developer_agent
from agents.error_handler_agent import error_handler_agent
from agents.use_case_agent import use_case_agent
from agents.testing_agent import testing_agent
from agents.reviewer_agent import reviewer_agent

from tasks.develop_code_task import develop_code_task
from tasks.error_fix_task import error_fix_task
from tasks.generate_use_cases_task import generate_use_cases_task
from tasks.testing_task import testing_task
from tasks.review_task import review_task


def create_crew(user_input: str) -> Crew:
    """
    Creates and returns a CrewAI crew that:
    1. Develops code of desired language
    2. Fixes errors
    3. Generates test scenarios
    4. Tests the scenarios
    5. Reviews and validates the result
    """

    # Initialize agents
    dev_agent = developer_agent()
    error_agent = error_handler_agent()
    use_case_agent_instance = use_case_agent()
    test_agent = testing_agent()
    review_agent = reviewer_agent()

    # Define tasks in execution order
    tasks = [
        develop_code_task(dev_agent, user_input),
        error_fix_task(error_agent),
        generate_use_cases_task(use_case_agent_instance),
        testing_task(test_agent),
        review_task(review_agent)
    ]

    # Create crew
    crew = Crew(
        agents=[
            dev_agent,
            error_agent,
            use_case_agent_instance,
            test_agent,
            review_agent
        ],
        tasks=tasks,
        verbose=True
    )

    return crew
