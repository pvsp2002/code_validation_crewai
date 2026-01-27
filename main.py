from dotenv import load_dotenv
load_dotenv()
from crew import create_crew


def main():
    print("=== CrewAI Code Validation System ===\n")

    user_input = input("Enter your requirement:\n> ")

    crew = create_crew(user_input)

    print("\n--- Crew Execution Started ---\n")
    result = crew.kickoff()

    print("\n--- FINAL OUTPUT ---\n")
    print(result)


if __name__ == "__main__":
    main()
