from crewai import Crew, Process, Task
from auto_coder.agents.coder import CoderAgent
from auto_coder.agents.reviewer import ReviewerAgent
from auto_coder.agents.planner import PlannerAgent
from auto_coder.tasks.coding_tasks import CodingTasks
from auto_coder.tasks.planning_tasks import PlanningTasks
from auto_coder.reflection.manager import ReflectionManager

class DevCrew:
    def __init__(self, llm=None, memory=False):
        self.coder = CoderAgent(llm=llm, memory=memory)
        self.reviewer = ReviewerAgent(llm=llm, memory=memory)
        self.planner = PlannerAgent(llm=llm)
        self.tasks = CodingTasks()
        self.planning_tasks = PlanningTasks()
        self.reflection = ReflectionManager()

    def run(self, problem_description):
        # Step 1: Generate Code
        task1 = self.tasks.code_generation_task(self.coder, problem_description)
        
        # Note: In a real sequential flow with CrewAI, we typically define all tasks upfront.
        # However, for a review, we might want to pass the output of task1 to task2.
        # CrewAI handles context passing automatically if tasks are in valid order.
        
        task2 = Task(
             description="Review the code generated in the previous task. identifying bugs or improvements.",
             expected_output="A detailed code review.",
             agent=self.reviewer
        )

        crew = Crew(
            agents=[self.coder, self.reviewer],
            tasks=[task1, task2],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return result

    def run_with_reflection(self, problem_description, max_retries=2):
        # Initial Run
        code_task = self.tasks.code_generation_task(self.coder, problem_description)
        review_task = self.tasks.code_review_task(self.reviewer, code_content="[Output of previous task]")
        # Note: In CrewAI, referencing previous task output explicitly in description is good practice,
        # but the sequential process automatically passes context.
        
        crew = Crew(
            agents=[self.coder, self.reviewer],
            tasks=[code_task, review_task],
            process=Process.sequential,
            verbose=True
        )
        
        review_result = crew.kickoff()
        
        # Simple heuristic: Check if review is positive. 
        # In a real system, we'd use a structured output or another LLM call to classify the review.
        # For this prototype, we'll assume if it contains "Issues:" or "Suggestions:" it might need work,
        # but let's just blindly do one iteration for demonstration or look for key phrases.
        
        # Better approach: The Reviewer should strictly output "APPROVED" if it's good.
        
        for i in range(max_retries):
            if "APPROVED" in str(review_result).upper():
                print("Code approved by reviewer.")
                # We need the code, but kickoff returns the review. 
                # We can access task output history, OR we can just ask the coder to output the final code again?
                # Or we can rely on the fact that the code is in the context.
                return review_result

            print(f"Refining code... Iteration {i+1}")
            fix_task = self.reflection.create_fix_task(self.coder, problem_description, review_result)
            new_review_task = self.tasks.code_review_task(self.reviewer, code_content="[Output of fix task]")
            
            refine_crew = Crew(
                agents=[self.coder, self.reviewer],
                tasks=[fix_task, new_review_task],
                process=Process.sequential,
                verbose=True
            )
            
            review_result = refine_crew.kickoff()
            
        return review_result

    def run_with_planning(self, problem_description, max_retries=2):
        # Step 1: Plan
        plan_task = self.planning_tasks.decompose_task(self.planner, problem_description)
        
        planning_crew = Crew(
            agents=[self.planner],
            tasks=[plan_task],
            verbose=True
        )
        
        plan_output = planning_crew.kickoff()
        print("Plan generated:\n", plan_output)
        
        # Step 2: Parse and Execute (Simplified)
        context_description = f"Follow this plan to solve the problem:\n{problem_description}\n\nPLAN:\n{plan_output}"
        
        return self.run_with_reflection(context_description, max_retries=max_retries)
