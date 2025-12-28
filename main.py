import os
import sys
from auto_coder.crews.dev_crew import DevCrew
from dotenv import load_dotenv

# Add src to pythonpath
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY in .env file")
        return

    print("Welcome to Auto-Coder with CrewAI")
    problem = input("Enter a coding problem: ")
    
    if not problem:
        problem = "Write a Python script that calculates the factorial of a number."

    crew = DevCrew()
    result = crew.run(problem)
    
    print("\n\n########################")
    print("Result:")
    print(result)

if __name__ == "__main__":
    main()
