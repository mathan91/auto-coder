from crewai import Task

class PlanningTasks:
    def decompose_task(self, agent, problem_description):
        return Task(
            description=f"""
            Analyze the following request and break it down into a list of specific coding subtasks.
            
            Request: {problem_description}
            
            Return ONLY a list of tasks in the following format:
            1. [Task Name]: [Brief Description]
            2. [Task Name]: [Brief Description]
            ...
            
            Ensure the tasks are in logical order of dependency.
            """,
            expected_output="A numbered list of actionable coding tasks.",
            agent=agent
        )
