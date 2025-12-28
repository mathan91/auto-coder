from crewai import Task

class CodingTasks:
    def code_generation_task(self, agent, description):
        return Task(
            description=f"Write code to solve the following problem:\n{description}\n\nEnsure the code is complete, correct, and follows best practices.",
            expected_output="A complete Python code solution.",
            agent=agent
        )

    def code_review_task(self, agent, code_content):
        return Task(
            description=f"Review the following code:\n{code_content}\n\nCheck for bugs, security issues, and style violations. Provide a detailed report.",
            expected_output="A review report listing issues and suggestions.",
            agent=agent
        )
