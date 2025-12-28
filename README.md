# Auto-Coder SDK (CrewAI)

A powerful agentic coding tool built with [CrewAI](https://crewai.io) that automates software development tasks. It features multi-agent collaboration, reflection, planning, and hypothesis generation.

## Features

- 🤖 **Core Agents**: `Coder` and `Reviewer` agents for robust code generation.
- 🔄 **Reflection**: Automated feedback loops where the Reviewer critiques and the Coder fixes issues.
- 🗺️ **Planning**: Decomposes complex problems into actionable coding tasks.
- 💡 **Hypothesis Generation**: Proposes multiple technical approaches before implementation.
- 🧠 **Memory & Learning**: Supports context retention and DPO-ready feedback logging.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd auto-coder
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   ```

3. **Configure Environment**:
   Create a `.env` file with your OpenAI API Key:
   ```bash
   cp .env.example .env
   # Edit .env and set OPENAI_API_KEY
   ```

## Usage

### CLI (Command Line Interface)

The tool provides a direct `auto-coder` command:

**1. Generate Code**
Directly solve a coding problem:
```bash
auto-coder generate "Create a Python script for a Snake game using pygame"
```

**2. Plan & Code**
For complex tasks, generate a plan first:
```bash
auto-coder plan "Build a REST API with Flask and SQLite"
```

**3. Ideate / Hypothesis**
Brainstorm approaches for a problem:
```bash
auto-coder ideate "How to scale a WebSocket server to 1M users?"
```

### Python SDK

You can also use the agents programmatically:

```python
from auto_coder.crews.dev_crew import DevCrew

crew = DevCrew()

# Run with reflection loop
result = crew.run_with_reflection("Create a factorial function")
print(result)
```

## Project Structure

- `src/auto_coder/agents`: Agent definitions (Coder, Reviewer, Planner, Hypothesis).
- `src/auto_coder/tasks`: Task definitions.
- `src/auto_coder/crews`: Pre-assembled agent crews.
- `src/auto_coder/reflection`: Feedback loop logic.
- `src/auto_coder/sophisticated`: Advanced context tools.

## License
MIT
