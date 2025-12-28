from crewai import Agent

class HypothesisAgent(Agent):
    def __init__(self, llm=None):
        super().__init__(
            role='Innovation Lead / Researcher',
            goal='Generate multiple innovative hypotheses and approaches to solve a problem.',
            backstory=(
                "You are a creative thinker who looks at problems from different angles. "
                "You propose diverse coding strategies, architectural patterns, and libraries "
                "to solve the user's request, considering pros and cons for each."
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm
        )
