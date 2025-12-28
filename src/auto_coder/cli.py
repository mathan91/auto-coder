import click
import os
import sys
from dotenv import load_dotenv

# Ensure we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from auto_coder.crews.dev_crew import DevCrew
from auto_coder.agents.hypothesis import HypothesisAgent
from auto_coder.tasks.hypothesis_tasks import HypothesisTasks
from crewai import Crew

load_dotenv()

@click.group()
def cli():
    """Auto-Coder CLI Tool."""
    pass

@cli.command()
@click.argument('prompt')
def generate(prompt):
    """Generate code based on a prompt."""
    click.echo(f"Generatng code for: {prompt}")
    crew = DevCrew()
    result = crew.run_with_reflection(prompt)
    click.echo("\n\nResult:\n")
    click.echo(result)

@cli.command()
@click.argument('prompt')
def plan(prompt):
    """Plan and generate code based on a prompt."""
    click.echo(f"Planning and generating code for: {prompt}")
    crew = DevCrew()
    result = crew.run_with_planning(prompt)
    click.echo("\n\nResult:\n")
    click.echo(result)

@cli.command()
@click.argument('prompt')
def ideate(prompt):
    """Generate hypotheses for a problem."""
    click.echo(f"Generating hypotheses for: {prompt}")
    agent = HypothesisAgent()
    tasks = HypothesisTasks()
    task = tasks.generate_hypotheses(agent, prompt)
    crew = Crew(agents=[agent], tasks=[task], verbose=True)
    result = crew.kickoff()
    click.echo("\n\nHypotheses:\n")
    click.echo(result)

if __name__ == '__main__':
    cli()
