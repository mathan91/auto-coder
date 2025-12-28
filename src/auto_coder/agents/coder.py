from crewai import Agent

class CoderAgent(Agent):
    def __init__(self, llm=None, memory=False):
        super().__init__(
            role='Senior Software Engineer',
            goal='Write clean, efficient, and error-free code to solve the given task.',
            backstory=(
                "You are an experienced software engineer with a mastery of Python and other languages. "
                "You write code that is not only functional but also follows best practices and design patterns. "
                "You pay close attention to requirements and edge cases."
            ),
            allow_delegation=False,
            verbose=True,
            memory=memory,
            llm=llm
        )
