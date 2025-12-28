from crewai import Task

class ReflectionManager:
    def create_fix_task(self, agent, original_problem, review_feedback):
        return Task(
            description=f"""
            The previous code submission was reviewed and issues were found.
            
            Original Problem: {original_problem}
            
            Review Feedback:
            {review_feedback}
            
            Please rewrite the code to address the feedback and solve the original problem.
            Ensure the code is complete and correct.
            """,
            expected_output="The corrected Python code.",
            agent=agent
        )
