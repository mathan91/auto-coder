from crewai import Task

class HypothesisTasks:
    def generate_hypotheses(self, agent, problem_description):
        return Task(
            description=f"""
            Analyze the following problem and propose 3 distinct technical approaches (hypotheses) to solve it.
            
            Problem: {problem_description}
            
            For each approach, list:
            1. Overview
            2. Key Libraries/Technologies
            3. Pros and Cons
            
            Finally, recommend one approach.
            """,
            expected_output="A report detailing 3 technical approaches and a final recommendation.",
            agent=agent
        )
