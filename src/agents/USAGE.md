# Agent Development Usage

This directory contains the core agent implementations using the fast-agent framework and SPARC methodology.

## Available Agents

- `core.py`: Basic agent example with structured output
- `workflows.py`: Chain workflow example with multiple agents
- `evaluator_optimizer.py`: Evaluator-optimizer pattern implementation
- `settings.py`: Application settings with Pydantic validation

## Developing New Agents

To create a new agent:

1. Create a new Python file in this directory
2. Define your Pydantic models for structured output
3. Create your agent with proper type hints and configuration
4. Add to the FastAgent instance with appropriate decorators
5. Write tests in the `tests/` directory

## Example: Basic Agent

```python
import asyncio
from pathlib import Path
from typing import Literal, TypedDict
from pydantic import BaseModel
from mcp_agent.core.fastagent import FastAgent
from mcp_agent.core.prompt import Prompt
from mcp_agent.core.request_params import RequestParams

fast = FastAgent("My Agent System")

class MyResult(BaseModel):
    """Type-safe analysis output."""
    summary: str
    confidence: float
    recommendations: list[str]

@fast.agent(
    name="my_agent",
    instruction=Path("./prompts/my_prompt.md"),
    servers=["filesystem"],
    model="anthropic.claude-sonnet-4-0",
    request_params=RequestParams(
        maxTokens=4096,
        temperature=0.7,
    ),
)
async def main() -> None:
    async with fast.run() as agent:
        result, message = await agent.my_agent.structured(
            [Prompt.user("Process this data")],
            MyResult
        )
        if result is not None:
            print(result.summary)

if __name__ == "__main__":
    asyncio.run(main())
```

## GitHub CLI Integration

Use GitHub CLI for agent development:

```bash
# Create a new agent PR
gh pr create --title "feat: Add new analysis agent" --body "Implements new agent for data analysis"

# Review agent code changes
gh pr list --label agent
gh pr checkout 123

# Track agent issues
gh issue create --title "Bug: Agent not handling edge case" --body "Agent fails when processing empty data"
```

## CodeRabbit Integration

CodeRabbit can assist in developing agents:

1. Generate agent code: "Create a router agent that routes tasks to specialized agents"
2. Improve type safety: "Add proper type hints to this agent implementation"
3. Optimize performance: "Improve the async performance of this agent workflow"
4. Review security: "Check for security issues in this agent implementation"
5. Generate documentation: "Add comprehensive docstrings to this agent class"