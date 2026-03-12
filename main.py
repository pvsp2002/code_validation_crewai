from crew import create_crew

if __name__ == "__main__":
    user_input = input("Enter coding requirement: ")

    crew = create_crew(user_input)

    result = crew.kickoff()

    print("\nFINAL RESULT:\n")
    print(result)