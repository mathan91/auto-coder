from crewai import Crew, Agent, Task, Process

class PromptChain:
    def __init__(self, agents, tasks):
        self.crew = Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

    def run(self):
        return self.crew.kickoff()
    
    @staticmethod
    def create_simple_chain(llm, prompts):
        """Creates a simple chain of agents executing prompts sequentially."""
        agents = []
        tasks = []
        
        for i, prompt in enumerate(prompts):
            agent = Agent(role=f"Agent {i}", goal="Execute prompt", backstory="Generic agent", llm=llm, allow_delegation=False)
            task = Task(description=prompt, expected_output="Result", agent=agent)
            agents.append(agent)
            tasks.append(task)
            
        return PromptChain(agents, tasks)
