from crewai import Crew, Process

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


def create_crew(user_input: str):

    dev_agent = developer_agent()
    error_agent = error_handler_agent()
    use_case_agent_instance = use_case_agent()
    test_agent = testing_agent()
    review_agent = reviewer_agent()

    tasks = [
        develop_code_task(dev_agent, user_input),
        error_fix_task(error_agent),
        generate_use_cases_task(use_case_agent_instance),
        testing_task(test_agent),
        review_task(review_agent)
    ]

    crew = Crew(
        agents=[
            dev_agent,
            error_agent,
            use_case_agent_instance,
            test_agent,
            review_agent
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew