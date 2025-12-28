from crewai import Agent

class PlannerAgent(Agent):
    def __init__(self, llm=None):
        super().__init__(
            role='Software Architect / Project Manager',
            goal='Break down complex software requirements into smaller, actionable coding tasks.',
            backstory=(
                "You are a seasoned software architect. You understand how to structure a project "
                "and how to divide work into manageable chunks for developers. "
                "You anticipate dependencies and potential bottlenecks."
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm
        )
